import pytest
from httpx import ASGITransport, AsyncClient

from crate_backend.db.session import get_session
from crate_backend.main import app
from crate_backend.models.catalog import Album

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
