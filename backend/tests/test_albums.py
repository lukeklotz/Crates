import uuid

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import func, select

from crate_backend.db.session import get_session
from crate_backend.main import app
from crate_backend.models.catalog import Album
from crate_backend.models.event import Event
from crate_backend.models.popularity import PopularitySignal
from crate_backend.models.user import User

pytestmark = pytest.mark.asyncio


@pytest.fixture
def client(db_session):
    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session
    transport = ASGITransport(app=app)
    try:
        yield AsyncClient(transport=transport, base_url="http://test")
    finally:
        app.dependency_overrides.pop(get_session, None)


async def _seed(db_session, *albums: Album) -> None:
    db_session.add_all(albums)
    await db_session.commit()


async def test_search_matches_title(client, db_session):
    await _seed(
        db_session,
        Album(title="Zzyzx Quietude", artist_name="Test Fixture Artist", release_year=2005),
        Album(title="Kid A", artist_name="Radiohead", release_year=2000),
    )
    async with client as ac:
        response = await ac.get("/albums/search", params={"q": "zzyzx quietude"})

    assert response.status_code == 200
    results = response.json()
    assert len(results) == 1
    assert results[0]["title"] == "Zzyzx Quietude"
    assert results[0]["artist_name"] == "Test Fixture Artist"


async def test_search_matches_artist(client, db_session):
    await _seed(
        db_session,
        Album(title="First Fixture Record", artist_name="Zzyzx Fixture Band", release_year=1997),
        Album(title="Second Fixture Record", artist_name="Zzyzx Fixture Band", release_year=2007),
        Album(title="Unrelated Record", artist_name="Someone Else", release_year=2005),
    )
    async with client as ac:
        response = await ac.get("/albums/search", params={"q": "zzyzx fixture band"})

    assert response.status_code == 200
    titles = {result["title"] for result in response.json()}
    assert titles == {"First Fixture Record", "Second Fixture Record"}


async def test_search_returns_empty_list_for_blank_query(client, db_session):
    await _seed(db_session, Album(title="Zzyzx Quietude", artist_name="Test Fixture Artist"))

    async with client as ac:
        response = await ac.get("/albums/search", params={"q": "   "})

    assert response.status_code == 200
    assert response.json() == []


async def test_search_returns_no_results_for_unmatched_query(client, db_session):
    await _seed(db_session, Album(title="Zzyzx Quietude", artist_name="Test Fixture Artist"))

    async with client as ac:
        response = await ac.get("/albums/search", params={"q": "nonexistent record zzyzx"})

    assert response.status_code == 200
    assert response.json() == []


_SANDBOX_USER = "sandbox-user@example.com"


async def _register_and_login(ac) -> None:
    await ac.post(
        "/auth/register", json={"email": _SANDBOX_USER, "password": "correct horse battery staple"}
    )
    response = await ac.post(
        "/auth/login", data={"username": _SANDBOX_USER, "password": "correct horse battery staple"}
    )
    assert response.status_code == 204


async def _kid_a(db_session) -> Album:
    album = Album(title="Kid A", artist_name="Radiohead")
    await _seed(db_session, album)
    return album


async def _signal(db_session, album_id) -> PopularitySignal | None:
    return await db_session.scalar(
        select(PopularitySignal)
        .where(PopularitySignal.album_id == album_id)
        .execution_options(populate_existing=True)
    )


async def _sandbox_events(db_session, album_id) -> list[Event]:
    rows = await db_session.scalars(
        select(Event).where(
            Event.event_type == "album_added_to_sandbox",
            Event.payload["album_id"].astext == str(album_id),
        )
    )
    return list(rows)


async def test_add_to_sandbox_requires_auth(client, db_session):
    album = await _kid_a(db_session)

    async with client as ac:
        response = await ac.post(f"/albums/{album.id}/add-to-sandbox")

    assert response.status_code == 401
    assert await _signal(db_session, album.id) is None
    assert await _sandbox_events(db_session, album.id) == []


async def test_add_to_sandbox_404s_for_unknown_album(client, db_session):
    unknown_id = uuid.uuid4()
    signals_before = await db_session.scalar(select(func.count()).select_from(PopularitySignal))

    async with client as ac:
        await _register_and_login(ac)
        response = await ac.post(f"/albums/{unknown_id}/add-to-sandbox")

    assert response.status_code == 404
    signals_after = await db_session.scalar(select(func.count()).select_from(PopularitySignal))
    assert signals_after == signals_before
    assert await _sandbox_events(db_session, unknown_id) == []


async def test_add_to_sandbox_increments_counter_and_emits_event(client, db_session):
    album = await _kid_a(db_session)

    async with client as ac:
        await _register_and_login(ac)
        response = await ac.post(f"/albums/{album.id}/add-to-sandbox")

    assert response.status_code == 204
    assert (await _signal(db_session, album.id)).sandbox_add_count == 1
    user = await db_session.scalar(select(User).where(User.email == _SANDBOX_USER))
    [event] = await _sandbox_events(db_session, album.id)
    assert event.user_id == user.id


async def test_add_to_sandbox_increments_existing_counter(client, db_session):
    album = await _kid_a(db_session)
    db_session.add(PopularitySignal(album_id=album.id, sandbox_add_count=4))
    await db_session.commit()

    async with client as ac:
        await _register_and_login(ac)
        await ac.post(f"/albums/{album.id}/add-to-sandbox")
        await ac.post(f"/albums/{album.id}/add-to-sandbox")

    assert (await _signal(db_session, album.id)).sandbox_add_count == 6
    assert len(await _sandbox_events(db_session, album.id)) == 2


async def test_add_to_sandbox_does_not_change_album_popularity(client, db_session):
    album = await _kid_a(db_session)

    async with client as ac:
        await _register_and_login(ac)
        await ac.post(f"/albums/{album.id}/add-to-sandbox")

    await db_session.refresh(album)
    assert album.popularity is None
