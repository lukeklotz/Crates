import uuid

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import select

from crate_backend.db.session import get_session
from crate_backend.main import app
from crate_backend.models.catalog import Album, AlbumTag, Tag

pytestmark = pytest.mark.asyncio


@pytest.fixture
async def client(db_session):
    """An open client (an httpx client can't be reopened, and some tests
    post twice)."""

    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session
    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            yield ac
    finally:
        app.dependency_overrides.pop(get_session, None)


async def _album(db_session, title: str, *tag_names: str, **fields) -> Album:
    album = Album(title=title, artist_name="Fixture Artist", **fields)
    db_session.add(album)
    await db_session.flush()
    for name in tag_names:
        tag = Tag(name=f"zzfixture-api-{name}")
        db_session.add(tag)
        await db_session.flush()
        db_session.add(AlbumTag(album_id=album.id, tag_id=tag.id))
    await db_session.flush()
    return album


async def _link(db_session, album: Album, *tag_names: str) -> None:
    """Give `album` tags that already exist (created by _album)."""
    for name in tag_names:
        tag = await db_session.scalar(select(Tag).where(Tag.name == f"zzfixture-api-{name}"))
        db_session.add(AlbumTag(album_id=album.id, tag_id=tag.id))
    await db_session.flush()


async def _post(client, **body):
    return await client.post("/recommendations", json=body)


async def test_returns_ranked_albums_with_shared_terms(client, db_session):
    seed = await _album(db_session, "Seed", "a", "b")
    match = await _album(db_session, "Match", release_year=1999, cover_art_url="https://x.test/c")
    await _link(db_session, match, "a", "b")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.status_code == 200
    body = response.json()
    assert body["reason"] is None
    assert body["results"] == [
        {
            "id": str(match.id),
            "title": "Match",
            "artist_name": "Fixture Artist",
            "release_year": 1999,
            "cover_art_url": "https://x.test/c",
            "score": pytest.approx(1.0),
            "shared_terms": ["zzfixture-api-a", "zzfixture-api-b"],
        }
    ]


async def test_limit_is_respected(client, db_session):
    seed = await _album(db_session, "Seed", "a")
    for i in range(4):
        await _link(db_session, await _album(db_session, f"Candidate {i}"), "a")

    response = await _post(client, album_ids=[str(seed.id)], limit=2)

    assert len(response.json()["results"]) == 2


async def test_duplicate_seed_ids_are_collapsed(client, db_session):
    seed = await _album(db_session, "Seed", "a", "b")
    await _link(db_session, await _album(db_session, "Partial"), "a")

    once = (await _post(client, album_ids=[str(seed.id)])).json()
    twice = (await _post(client, album_ids=[str(seed.id), str(seed.id)])).json()

    assert twice == once
    assert twice["results"][0]["score"] == pytest.approx(1 / 2)


async def test_unknown_album_ids_are_404_and_listed(client, db_session):
    seed = await _album(db_session, "Seed", "a")
    missing = str(uuid.uuid4())

    response = await _post(client, album_ids=[str(seed.id), missing])

    assert response.status_code == 404
    assert response.json()["detail"]["missing"] == [missing]


@pytest.mark.parametrize(
    "body",
    [
        {"album_ids": []},
        {"album_ids": [str(uuid.uuid4()) for _ in range(51)]},
        {"album_ids": ["not-a-uuid"]},
        {"album_ids": [str(uuid.uuid4())], "limit": 0},
        {"album_ids": [str(uuid.uuid4())], "limit": 51},
    ],
)
async def test_invalid_input_is_422(client, body):
    response = await _post(client, **body)

    assert response.status_code == 422


async def test_seeds_without_terms_explain_the_empty_result(client, db_session):
    seed = await _album(db_session, "Untagged Seed")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.status_code == 200
    assert response.json() == {"results": [], "reason": "seeds_have_no_terms"}


async def test_tagged_seed_with_no_matches_has_no_reason(client, db_session):
    seed = await _album(db_session, "Lonely Seed", "lonely")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.json() == {"results": [], "reason": None}
