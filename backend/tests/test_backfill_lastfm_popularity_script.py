from datetime import UTC, datetime

import pytest

from crate_backend.lastfm import client as lastfm_client
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal
from crate_backend.scripts import backfill_lastfm_popularity

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


@pytest.fixture
def script(monkeypatch, db_session):
    """The script wired to the test session, with Last.fm sync and scoring
    faked. The dev DB may hold the real catalog, so tests assert on their
    own albums' membership rather than exact lists."""
    monkeypatch.setattr(
        backfill_lastfm_popularity, "async_session_factory", _SessionFactory(db_session)
    )
    state = {"synced": [], "sleeps": [], "recomputed": False}

    async def fake_sleep(seconds):
        state["sleeps"].append(seconds)

    async def fake_sync(session, client, api_key, album):
        state["synced"].append(album.id)

    async def fake_recompute(session):
        state["recomputed"] = True
        return 0

    monkeypatch.setattr(backfill_lastfm_popularity, "_sleep", fake_sleep)
    monkeypatch.setattr(backfill_lastfm_popularity, "sync_album_popularity", fake_sync)
    monkeypatch.setattr(backfill_lastfm_popularity, "recompute_popularity_scores", fake_recompute)
    return state


async def _album(db_session, **fields) -> Album:
    album = Album(**{"title": "Backfill Fixture", "artist_name": "Test Artist", **fields})
    db_session.add(album)
    await db_session.flush()
    return album


async def test_syncs_unattempted_albums_and_skips_attempted_ones(script, db_session):
    never_tried = await _album(db_session)
    failed_before = await _album(db_session)
    already_tried = await _album(db_session)
    db_session.add_all(
        [
            PopularitySignal(album_id=failed_before.id, lastfm_fetched_at=None),
            PopularitySignal(album_id=already_tried.id, lastfm_fetched_at=datetime.now(UTC)),
        ]
    )
    await db_session.flush()

    await backfill_lastfm_popularity.backfill()

    assert never_tried.id in script["synced"]
    assert failed_before.id in script["synced"]
    assert already_tried.id not in script["synced"]


async def test_skips_albums_without_an_artist_name(script, db_session):
    nameless = await _album(db_session, artist_name=None)

    await backfill_lastfm_popularity.backfill()

    assert nameless.id not in script["synced"]


async def test_recomputes_scores_after_syncing(script, db_session):
    await _album(db_session)

    await backfill_lastfm_popularity.backfill()

    assert script["recomputed"] is True


async def test_paces_one_sleep_per_album(script, db_session):
    await _album(db_session)

    await backfill_lastfm_popularity.backfill(request_interval_seconds=2.5)

    assert len(script["sleeps"]) == len(script["synced"])
    assert set(script["sleeps"]) == {2.5}


async def test_default_pacing_matches_the_client(script, db_session):
    await _album(db_session)

    await backfill_lastfm_popularity.backfill()

    assert set(script["sleeps"]) == {lastfm_client.REQUEST_INTERVAL_SECONDS}


async def test_refuses_to_run_without_an_api_key(script, db_session, monkeypatch):
    class _NoKey:
        lastfm_api_key = ""

    monkeypatch.setattr(backfill_lastfm_popularity, "get_settings", lambda: _NoKey())
    await _album(db_session)

    with pytest.raises(SystemExit):
        await backfill_lastfm_popularity.backfill()
    assert script["synced"] == []
