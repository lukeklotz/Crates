from datetime import UTC, datetime

import pytest

from crate_backend.models.album_text import AlbumText
from crate_backend.models.catalog import Album
from crate_backend.scripts import backfill_wikipedia_text
from crate_backend.scripts.backfill_wikipedia_text import CoverageRow, summarize_coverage
from crate_backend.wikipedia import client as wikipedia_client


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


class _Settings:
    wikimedia_contact_email = "someone@example.test"


class _Row:
    def __init__(self, fetched: bool):
        self.fetched_at = datetime.now(UTC) if fetched else None


@pytest.fixture
def script(monkeypatch, db_session):
    """The script wired to the test session with Wikimedia faked. The dev DB
    may hold real linked albums, so tests assert on their own albums'
    membership, never on exact counts. Test Wikidata ids start with Q9000."""
    monkeypatch.setattr(
        backfill_wikipedia_text, "async_session_factory", _SessionFactory(db_session)
    )
    monkeypatch.setattr(backfill_wikipedia_text, "get_settings", lambda: _Settings())
    state = {
        "synced": [],
        "sleeps": [],
        "resolved_batches": [],
        "unresolvable": set(),
        "titles_seen": {},
    }

    async def fake_sleep(seconds):
        state["sleeps"].append(seconds)

    async def fake_resolve(client, qids):
        state["resolved_batches"].append(list(qids))
        return {q: f"Title {q}" for q in qids if q not in state["unresolvable"]}

    async def fake_sync(session, client, album, enwiki_titles):
        state["synced"].append(album.id)
        state["titles_seen"][album.id] = enwiki_titles.get(album.wikidata_id)
        return _Row(fetched=True)

    async def fake_print_coverage(session):
        state["reported"] = True

    monkeypatch.setattr(backfill_wikipedia_text, "_sleep", fake_sleep)
    monkeypatch.setattr(backfill_wikipedia_text, "resolve_enwiki_titles", fake_resolve)
    monkeypatch.setattr(backfill_wikipedia_text, "sync_album_text", fake_sync)
    monkeypatch.setattr(backfill_wikipedia_text, "print_coverage", fake_print_coverage)
    return state


async def _album(db_session, **fields) -> Album:
    album = Album(**{"title": "Wiki Backfill Fixture", "artist_name": "Test Artist", **fields})
    db_session.add(album)
    await db_session.flush()
    return album


async def test_fetches_unattempted_and_failed_albums_and_skips_done_ones(script, db_session):
    never_tried = await _album(db_session, wikidata_id="Q900000001")
    failed_before = await _album(db_session, wikipedia_title="Failed_Before")
    done = await _album(db_session, wikidata_id="Q900000002")
    db_session.add_all(
        [
            AlbumText(album_id=failed_before.id, source="wikipedia", fetched_at=None),
            AlbumText(album_id=done.id, source="wikipedia", fetched_at=datetime.now(UTC)),
        ]
    )
    await db_session.flush()

    await backfill_wikipedia_text.backfill()

    assert never_tried.id in script["synced"]
    assert failed_before.id in script["synced"]
    assert done.id not in script["synced"]


async def test_skips_albums_with_no_links(script, db_session):
    unlinked = await _album(db_session)

    await backfill_wikipedia_text.backfill()

    assert unlinked.id not in script["synced"]


async def test_resolved_titles_are_passed_to_sync(script, db_session):
    album = await _album(db_session, wikidata_id="Q900000003")

    await backfill_wikipedia_text.backfill()

    assert script["titles_seen"][album.id] == "Title Q900000003"


async def test_wikidata_ids_are_resolved_in_batches_of_fifty(script, db_session):
    await _album(db_session, wikidata_id="Q900000004")

    await backfill_wikipedia_text.backfill()

    assert script["resolved_batches"]
    assert all(
        len(batch) <= wikipedia_client.MAX_WIKIDATA_IDS_PER_REQUEST
        for batch in script["resolved_batches"]
    )
    assert any("Q900000004" in batch for batch in script["resolved_batches"])


async def test_unresolved_albums_are_skipped_without_counting_as_failures(script, db_session):
    limit = backfill_wikipedia_text.MAX_CONSECUTIVE_FAILURES
    unresolved = [
        await _album(db_session, wikidata_id=f"Q9000001{i:02d}") for i in range(limit + 2)
    ]
    script["unresolvable"] = {album.wikidata_id for album in unresolved}

    await backfill_wikipedia_text.backfill()

    assert not {album.id for album in unresolved} & set(script["synced"])
    assert script.get("reported") is True


async def test_paces_requests(script, db_session):
    await _album(db_session, wikidata_id="Q900000005")

    await backfill_wikipedia_text.backfill(request_interval_seconds=2.5)

    assert set(script["sleeps"]) == {2.5}
    assert len(script["sleeps"]) == len(script["synced"]) + len(script["resolved_batches"])


async def test_default_pacing_matches_the_client(script, db_session):
    await _album(db_session, wikidata_id="Q900000006")

    await backfill_wikipedia_text.backfill()

    assert set(script["sleeps"]) == {wikipedia_client.REQUEST_INTERVAL_SECONDS}


async def test_refuses_to_run_without_a_contact_email(script, db_session, monkeypatch):
    class _NoContact:
        wikimedia_contact_email = ""

    monkeypatch.setattr(backfill_wikipedia_text, "get_settings", lambda: _NoContact())
    await _album(db_session, wikidata_id="Q900000007")

    with pytest.raises(SystemExit):
        await backfill_wikipedia_text.backfill()
    assert script["synced"] == []


async def test_aborts_after_consecutive_failed_fetches(script, db_session, monkeypatch):
    limit = backfill_wikipedia_text.MAX_CONSECUTIVE_FAILURES
    for i in range(limit):
        await _album(db_session, wikipedia_title=f"Failing_{i}")

    async def always_failing(session, client, album, enwiki_titles):
        script["synced"].append(album.id)
        return _Row(fetched=False)

    monkeypatch.setattr(backfill_wikipedia_text, "sync_album_text", always_failing)

    with pytest.raises(SystemExit):
        await backfill_wikipedia_text.backfill()
    assert len(script["synced"]) == limit
    assert "reported" not in script


async def test_a_success_resets_the_failure_streak(script, db_session, monkeypatch):
    limit = backfill_wikipedia_text.MAX_CONSECUTIVE_FAILURES
    for i in range(limit + 5):
        await _album(db_session, wikipedia_title=f"Flaky_{i}")

    async def mostly_failing(session, client, album, enwiki_titles):
        script["synced"].append(album.id)
        return _Row(fetched=len(script["synced"]) % limit == 0)

    monkeypatch.setattr(backfill_wikipedia_text, "sync_album_text", mostly_failing)

    await backfill_wikipedia_text.backfill()

    assert script.get("reported") is True


async def test_aborts_when_wikidata_keeps_failing(script, db_session, monkeypatch):
    limit = backfill_wikipedia_text.MAX_CONSECUTIVE_FAILURES
    for i in range(limit * wikipedia_client.MAX_WIKIDATA_IDS_PER_REQUEST):
        await _album(db_session, wikidata_id=f"Q90001{i:04d}")

    async def wikidata_down(client, qids):
        script["resolved_batches"].append(list(qids))
        return {}

    monkeypatch.setattr(backfill_wikipedia_text, "resolve_enwiki_titles", wikidata_down)

    with pytest.raises(SystemExit):
        await backfill_wikipedia_text.backfill()
    assert len(script["resolved_batches"]) == limit
    assert script["synced"] == []


# --- summarize_coverage (pure) ------------------------------------------------


def test_summarize_coverage_buckets_by_popularity_percentile():
    rows = summarize_coverage(
        [
            (0.9, True, True),
            (0.75, True, False),
            (0.6, False, False),
            (0.3, True, True),
            (0.1, False, False),
            (0.0, True, False),
            (None, True, True),
        ]
    )
    assert rows == [
        CoverageRow("All", 7, 5, 3),
        CoverageRow("Top 25%", 2, 2, 1),
        CoverageRow("50–75%", 1, 0, 0),
        CoverageRow("25–50%", 1, 1, 1),
        CoverageRow("Bottom 25%", 2, 1, 0),
        CoverageRow("No popularity", 1, 1, 1),
    ]


def test_summarize_coverage_of_nothing_is_all_zero():
    rows = summarize_coverage([])
    assert rows[0] == CoverageRow("All", 0, 0, 0)
    assert all(row.albums == 0 for row in rows)
