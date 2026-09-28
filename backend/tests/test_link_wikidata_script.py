from pathlib import Path

import pytest

from crate_backend.models.catalog import Album
from crate_backend.scripts import link_wikidata

pytestmark = pytest.mark.asyncio


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


def _relation(rel_type: str, url: str) -> dict:
    return {"type": rel_type, "target-type": "url", "url": {"id": "x", "resource": url}}


_RELEASE_GROUPS = [
    {
        "id": "test-wiki-both",
        "relations": [
            _relation("wikidata", "https://www.wikidata.org/wiki/Q900000001"),
            _relation("wikipedia", "https://en.wikipedia.org/wiki/Test_Album"),
        ],
    },
    {
        "id": "test-wiki-german-only",
        "relations": [_relation("wikipedia", "https://de.wikipedia.org/wiki/Test_Album")],
    },
    {"id": "test-wiki-stale", "relations": []},
    {
        "id": "test-wiki-not-in-catalog",
        "relations": [_relation("wikidata", "https://www.wikidata.org/wiki/Q900000009")],
    },
]


@pytest.fixture
def script(monkeypatch, db_session):
    monkeypatch.setattr(link_wikidata, "async_session_factory", _SessionFactory(db_session))
    streamed: list[tuple[Path, str]] = []

    def fake_stream(archive_path: Path, member_name: str):
        streamed.append((archive_path, member_name))
        return iter(_RELEASE_GROUPS)

    monkeypatch.setattr(link_wikidata, "stream_jsonl_from_tar", fake_stream)
    return streamed


async def _album(db_session, mbid: str, **fields) -> Album:
    album = Album(title="Link Fixture", musicbrainz_release_group_id=mbid, **fields)
    db_session.add(album)
    await db_session.flush()
    return album


async def test_reads_the_release_group_dump(script, db_session):
    await link_wikidata.link_albums(Path("/dumps"))

    assert script == [(Path("/dumps/release-group.tar.xz"), "mbdump/release-group")]


async def test_stores_wikidata_id_and_english_title(script, db_session):
    album = await _album(db_session, "test-wiki-both")

    await link_wikidata.link_albums(Path("/unused"))

    await db_session.refresh(album)
    assert album.wikidata_id == "Q900000001"
    assert album.wikipedia_title == "Test_Album"


async def test_non_english_only_album_gets_no_links(script, db_session):
    album = await _album(db_session, "test-wiki-german-only")

    await link_wikidata.link_albums(Path("/unused"))

    await db_session.refresh(album)
    assert album.wikidata_id is None
    assert album.wikipedia_title is None


async def test_rerun_clears_links_removed_from_the_dump(script, db_session):
    album = await _album(
        db_session, "test-wiki-stale", wikidata_id="Q900000002", wikipedia_title="Old_Title"
    )

    await link_wikidata.link_albums(Path("/unused"))

    await db_session.refresh(album)
    assert album.wikidata_id is None
    assert album.wikipedia_title is None


async def test_catalog_album_absent_from_the_dump_is_cleared(script, db_session):
    album = await _album(db_session, "test-wiki-gone", wikidata_id="Q900000003")

    await link_wikidata.link_albums(Path("/unused"))

    await db_session.refresh(album)
    assert album.wikidata_id is None


async def test_albums_without_a_musicbrainz_id_are_left_alone(script, db_session):
    album = Album(title="iTunes Stand-in", wikidata_id="Q900000004")
    db_session.add(album)
    await db_session.flush()

    await link_wikidata.link_albums(Path("/unused"))

    await db_session.refresh(album)
    assert album.wikidata_id == "Q900000004"
