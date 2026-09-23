from pathlib import Path

import pytest
from sqlalchemy import select

from crate_backend.models.artist_relationship import ArtistRelationship
from crate_backend.models.catalog import Album, Artist
from crate_backend.scripts import ingest_musicbrainz

pytestmark = pytest.mark.asyncio

_RELEASE_GROUPS = [
    {
        "id": "test-rg-1",
        "title": "Test Album",
        "primary-type": "Album",
        "secondary-types": [],
        "first-release-date": "1959-08-17",
        "genres": [{"id": "test-genre-1", "name": "test-jazz", "count": 5}],
        "tags": [{"name": "test-modal", "count": 2}],
        "artist-credit": [
            {"name": "Test Artist", "artist": {"id": "test-artist-1", "name": "Test Artist"}}
        ],
    },
    {
        "id": "test-rg-single",
        "title": "Filtered Out",
        "primary-type": "Single",
        "secondary-types": [],
        "genres": [{"id": "test-genre-1", "name": "test-jazz", "count": 5}],
        "tags": [],
        "artist-credit": [],
    },
]

_ARTISTS = [
    {
        "id": "test-artist-1",
        "name": "Test Artist",
        "relations": [
            {
                "type": "collaboration",
                "direction": "forward",
                "artist": {"id": "test-artist-2", "name": "Test Collaborator"},
            }
        ],
    }
]


class _SessionFactory:
    """Stands in for async_session_factory: `async with factory() as s`
    yields the rollback-wrapped test session instead of a real one."""

    def __init__(self, session):
        self._session = session

    def __call__(self):
        return self

    async def __aenter__(self):
        return self._session

    async def __aexit__(self, *exc_info):
        return False


@pytest.fixture
def script(monkeypatch, db_session):
    monkeypatch.setattr(ingest_musicbrainz, "async_session_factory", _SessionFactory(db_session))
    monkeypatch.setattr(
        ingest_musicbrainz, "read_dump_metadata", lambda archive: {"SCHEMA_SEQUENCE": "test"}
    )

    def fake_stream(archive_path: Path, member_name: str):
        return iter(_RELEASE_GROUPS if member_name == "mbdump/release-group" else _ARTISTS)

    monkeypatch.setattr(ingest_musicbrainz, "stream_jsonl_from_tar", fake_stream)
    return ingest_musicbrainz


async def test_ingest_dumps_writes_albums_and_relationships(script, db_session):
    await script.ingest_dumps(dump_dir=Path("/unused"), target_size=10)

    album = await db_session.scalar(
        select(Album).where(Album.musicbrainz_release_group_id == "test-rg-1")
    )
    assert album.title == "Test Album"
    assert await db_session.scalar(
        select(Album).where(Album.musicbrainz_release_group_id == "test-rg-single")
    ) is None

    artist = await db_session.scalar(select(Artist).where(Artist.musicbrainz_id == "test-artist-1"))
    edges = (await db_session.scalars(
        select(ArtistRelationship).where(ArtistRelationship.artist_id == artist.id)
    )).all()
    assert [e.relationship_type for e in edges] == ["collaboration"]


async def test_fetch_missing_cover_art_saves_found_urls(script, db_session, monkeypatch):
    album = Album(title="Test Album", musicbrainz_release_group_id="test-rg-art")
    db_session.add(album)
    await db_session.flush()

    async def fake_iter(client, mbids):
        for mbid in mbids:
            yield mbid, (f"https://example.test/{mbid}" if mbid == "test-rg-art" else None)

    monkeypatch.setattr(script, "iter_cover_art", fake_iter)
    await script.fetch_missing_cover_art()

    await db_session.refresh(album)
    assert album.cover_art_url == "https://example.test/test-rg-art"
