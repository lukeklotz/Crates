"""Recomputes Album.popularity as each matched album's percentile rank of
Last.fm listeners. Percentile rank is only meaningful against the whole
current distribution, so this runs as a batch step, not per request."""

import bisect

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal


def _percentile_rank(sorted_values: list[int], value: int) -> float:
    """0.0 for the least-listened album, 1.0 for the most; ties share their
    average rank. A lone album scores 1.0."""
    if len(sorted_values) == 1:
        return 1.0
    lo = bisect.bisect_left(sorted_values, value)
    hi = bisect.bisect_right(sorted_values, value)
    return (lo + hi - 1) / 2 / (len(sorted_values) - 1)


async def recompute_popularity_scores(session: AsyncSession) -> int:
    """Score every album with a verified Last.fm match; albums without one
    are left untouched. Returns the number of albums scored."""
    rows = (
        await session.execute(
            select(PopularitySignal.album_id, PopularitySignal.lastfm_listeners).where(
                PopularitySignal.lastfm_listeners.is_not(None)
            )
        )
    ).all()
    if not rows:
        return 0

    sorted_values = sorted(listeners for _, listeners in rows)
    await session.execute(
        update(Album),
        [
            {"id": album_id, "popularity": _percentile_rank(sorted_values, listeners)}
            for album_id, listeners in rows
        ],
    )
    return len(rows)
