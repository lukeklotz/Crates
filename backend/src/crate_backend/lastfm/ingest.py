"""Idempotent sync of one album's PopularitySignal row against Last.fm,
keyed by album_id so re-runs update in place."""

import uuid
from datetime import UTC, datetime

import httpx
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.lastfm.client import FetchOutcome, fetch_album_info
from crate_backend.lastfm.match import verify_match
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal


async def get_or_create_signal(session: AsyncSession, album_id: uuid.UUID) -> PopularitySignal:
    signal = await session.scalar(
        select(PopularitySignal).where(PopularitySignal.album_id == album_id)
    )
    if signal is None:
        signal = PopularitySignal(album_id=album_id, sandbox_add_count=0)
        session.add(signal)
        await session.flush()
    return signal


async def sync_album_popularity(
    session: AsyncSession, client: httpx.AsyncClient, api_key: str, album: Album
) -> PopularitySignal | None:
    """Look up `album` on Last.fm and record the verified listener count.

    Returns None, with no request and no row, when the album has no
    artist_name to search with.
    """
    if not album.artist_name:
        return None

    signal = await get_or_create_signal(session, album.id)
    result = await fetch_album_info(client, api_key, album.artist_name, album.title)
    if result.outcome is FetchOutcome.FAILED:
        return signal

    signal.lastfm_fetched_at = datetime.now(UTC)
    if result.outcome is FetchOutcome.FOUND and verify_match(
        album.artist_name, album.title, result.artist, result.title
    ):
        signal.lastfm_listeners = result.listeners
        signal.lastfm_matched_artist = result.artist[:255]
        signal.lastfm_matched_title = result.title[:500]
    await session.flush()
    return signal
