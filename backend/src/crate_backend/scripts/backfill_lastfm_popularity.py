"""Backfill Last.fm popularity signals for the catalog, then recompute
Album.popularity (Phase 3 prerequisite).

Design: docs/superpowers/specs/2026-09-24-lastfm-popularity-signal-design.md

Run with: uv run python -m crate_backend.scripts.backfill_lastfm_popularity

Safe to re-run: albums with a completed attempt (lastfm_fetched_at set) are
skipped, so an interrupted run resumes where it stopped.
"""

import asyncio

import httpx
from sqlalchemy import select

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.lastfm.client import REQUEST_INTERVAL_SECONDS, LastfmKeyRejected
from crate_backend.lastfm.ingest import sync_album_popularity
from crate_backend.lastfm.scoring import recompute_popularity_scores
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal

_PROGRESS_EVERY = 500
_COMMIT_EVERY = 50
# Each failed lookup already spent ~30s retrying; this many in a row means
# Last.fm is down or blocking us, so stop instead of hammering it for days.
MAX_CONSECUTIVE_FAILURES = 10

# Module-level so tests can replace waiting without patching asyncio globally.
_sleep = asyncio.sleep


async def backfill(request_interval_seconds: float = REQUEST_INTERVAL_SECONDS) -> None:
    api_key = get_settings().lastfm_api_key
    if not api_key:
        raise SystemExit("CRATE_LASTFM_API_KEY is not set; add it to backend/.env.")

    async with async_session_factory() as session:
        albums = (
            await session.scalars(
                select(Album)
                .outerjoin(PopularitySignal, PopularitySignal.album_id == Album.id)
                .where(
                    Album.artist_name.is_not(None),
                    PopularitySignal.lastfm_fetched_at.is_(None),
                )
            )
        ).all()
        total = len(albums)
        print(f"Looking up {total} albums on Last.fm...")

        failure_streak = 0
        async with httpx.AsyncClient(timeout=30) as client:
            for index, album in enumerate(albums, start=1):
                try:
                    signal = await sync_album_popularity(session, client, api_key, album)
                except LastfmKeyRejected as exc:
                    await session.commit()
                    raise SystemExit(f"Last.fm rejected the API key ({exc}); stopping.") from exc
                if signal is not None and signal.lastfm_fetched_at is None:
                    failure_streak += 1
                    if failure_streak >= MAX_CONSECUTIVE_FAILURES:
                        await session.commit()
                        raise SystemExit(
                            f"{failure_streak} lookups in a row failed; Last.fm looks "
                            "unavailable. Progress is saved; re-run later to resume."
                        )
                else:
                    failure_streak = 0
                if index % _COMMIT_EVERY == 0:
                    await session.commit()
                if index % _PROGRESS_EVERY == 0:
                    print(f"  checked {index}/{total}")
                await _sleep(request_interval_seconds)
        await session.commit()

        scored = await recompute_popularity_scores(session)
        await session.commit()
    print(f"Recomputed popularity for {scored} matched albums.")


def main() -> None:
    asyncio.run(backfill())


if __name__ == "__main__":
    main()
