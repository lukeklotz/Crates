import httpx
import pytest
from sqlalchemy import select

from crate_backend.lastfm import ingest
from crate_backend.lastfm.client import AlbumInfoResult, FetchOutcome
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal

pytestmark = pytest.mark.asyncio

_KID_A = AlbumInfoResult(FetchOutcome.FOUND, listeners=500, artist="Radiohead", title="Kid A")


@pytest.fixture
def fetch_returns(monkeypatch):
    """Make ingest's Last.fm lookup return `result`; records each call."""
    calls: list[tuple] = []

    def install(result: AlbumInfoResult) -> list[tuple]:
        async def fake_fetch(client, api_key, artist_name, album_title):
            calls.append((artist_name, album_title))
            return result

        monkeypatch.setattr(ingest, "fetch_album_info", fake_fetch)
        return calls

    return install


async def _album(db_session, **overrides) -> Album:
    fields = {"title": "Kid A", "artist_name": "Radiohead"}
    fields.update(overrides)
    album = Album(**fields)
    db_session.add(album)
    await db_session.flush()
    return album


async def _signals(db_session, album_id) -> list[PopularitySignal]:
    rows = await db_session.scalars(
        select(PopularitySignal).where(PopularitySignal.album_id == album_id)
    )
    return list(rows)


async def _sync(db_session, album):
    return await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)


async def test_skips_album_with_no_artist_name(db_session, fetch_returns):
    calls = fetch_returns(_KID_A)
    album = await _album(db_session, artist_name=None)

    assert await _sync(db_session, album) is None
    assert calls == []
    assert await _signals(db_session, album.id) == []


async def test_verified_match_stores_listeners_and_fetched_at(db_session, fetch_returns):
    calls = fetch_returns(_KID_A)
    album = await _album(db_session)

    signal = await _sync(db_session, album)

    assert calls == [("Radiohead", "Kid A")]
    assert signal.lastfm_listeners == 500
    assert signal.lastfm_matched_artist == "Radiohead"
    assert signal.lastfm_matched_title == "Kid A"
    assert signal.lastfm_fetched_at is not None


async def test_mismatch_sets_fetched_at_but_leaves_listeners_null(db_session, fetch_returns):
    fetch_returns(
        AlbumInfoResult(FetchOutcome.FOUND, listeners=500, artist="Someone Else", title="Other")
    )
    album = await _album(db_session)

    signal = await _sync(db_session, album)

    assert signal.lastfm_listeners is None
    assert signal.lastfm_matched_artist is None
    assert signal.lastfm_fetched_at is not None


async def test_not_found_sets_fetched_at_and_leaves_listeners_null(db_session, fetch_returns):
    fetch_returns(AlbumInfoResult(FetchOutcome.NOT_FOUND))
    album = await _album(db_session)

    signal = await _sync(db_session, album)

    assert signal.lastfm_listeners is None
    assert signal.lastfm_fetched_at is not None


async def test_failed_outcome_leaves_fetched_at_unset_for_retry(db_session, fetch_returns):
    fetch_returns(AlbumInfoResult(FetchOutcome.FAILED))
    album = await _album(db_session)

    signal = await _sync(db_session, album)

    assert signal.lastfm_fetched_at is None
    assert signal.lastfm_listeners is None


async def test_is_idempotent_on_rerun(db_session, fetch_returns):
    fetch_returns(_KID_A)
    album = await _album(db_session)

    await _sync(db_session, album)
    await _sync(db_session, album)

    rows = await _signals(db_session, album.id)
    assert len(rows) == 1
    assert rows[0].lastfm_listeners == 500


async def test_does_not_touch_sandbox_add_count(db_session, fetch_returns):
    fetch_returns(_KID_A)
    album = await _album(db_session)
    db_session.add(PopularitySignal(album_id=album.id, sandbox_add_count=3))
    await db_session.flush()

    signal = await _sync(db_session, album)

    assert signal.sandbox_add_count == 3
