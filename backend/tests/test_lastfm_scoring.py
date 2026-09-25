import pytest
from sqlalchemy import delete

from crate_backend.lastfm.scoring import recompute_popularity_scores
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal

pytestmark = pytest.mark.asyncio


@pytest.fixture(autouse=True)
async def only_test_signals(db_session):
    """The dev DB may hold real backfilled signals, which would shift every
    percentile. Clear them inside the test's rolled-back transaction."""
    await db_session.execute(delete(PopularitySignal))


async def _album_with_signal(db_session, listeners: int | None) -> Album:
    album = Album(title=f"Album {listeners}", artist_name="Test Artist")
    db_session.add(album)
    await db_session.flush()
    db_session.add(PopularitySignal(album_id=album.id, lastfm_listeners=listeners))
    await db_session.flush()
    return album


async def _scores(db_session, *albums: Album) -> list[float | None]:
    for album in albums:
        await db_session.refresh(album)
    return [album.popularity for album in albums]


async def test_returns_zero_when_no_albums_have_listeners(db_session):
    await _album_with_signal(db_session, None)

    assert await recompute_popularity_scores(db_session) == 0


async def test_ranks_from_zero_to_one(db_session):
    low = await _album_with_signal(db_session, 100)
    mid = await _album_with_signal(db_session, 500)
    high = await _album_with_signal(db_session, 100_000)

    scored = await recompute_popularity_scores(db_session)

    assert scored == 3
    assert await _scores(db_session, low, mid, high) == [0.0, 0.5, 1.0]


async def test_tied_listener_counts_get_the_same_score(db_session):
    first = await _album_with_signal(db_session, 500)
    second = await _album_with_signal(db_session, 500)
    await _album_with_signal(db_session, 100_000)

    await recompute_popularity_scores(db_session)

    first_score, second_score = await _scores(db_session, first, second)
    assert first_score == second_score == 0.25


async def test_unmatched_album_popularity_stays_null(db_session):
    unmatched = await _album_with_signal(db_session, None)
    await _album_with_signal(db_session, 500)

    await recompute_popularity_scores(db_session)

    assert await _scores(db_session, unmatched) == [None]


async def test_single_matched_album_scores_at_one(db_session):
    only = await _album_with_signal(db_session, 500)

    assert await recompute_popularity_scores(db_session) == 1
    assert await _scores(db_session, only) == [1.0]
