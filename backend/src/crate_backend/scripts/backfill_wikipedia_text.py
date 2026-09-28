"""Fetch English Wikipedia article text for catalog albums linked to
Wikidata or Wikipedia (Phase 4, Milestone 1). Run link_wikidata first.

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md

Run with: uv run python -m crate_backend.scripts.backfill_wikipedia_text [--report-only]

Safe to re-run: albums with a definitive answer (fetched_at set) are
skipped, so an interrupted run resumes where it stopped.
"""

import argparse
import asyncio
from collections.abc import Iterable
from typing import NamedTuple

import httpx
from sqlalchemy import and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album
from crate_backend.wikipedia.client import (
    MAX_WIKIDATA_IDS_PER_REQUEST,
    REQUEST_INTERVAL_SECONDS,
    resolve_enwiki_titles,
    user_agent,
)
from crate_backend.wikipedia.ingest import sync_album_text

_PROGRESS_EVERY = 500
_COMMIT_EVERY = 50
# Each failed request already spent ~30s retrying; this many in a row means
# Wikimedia is down or blocking us, so stop instead of hammering it.
MAX_CONSECUTIVE_FAILURES = 10

# Module-level so tests can replace waiting without patching asyncio globally.
_sleep = asyncio.sleep

_LINKED = or_(Album.wikidata_id.is_not(None), Album.wikipedia_title.is_not(None))


class CoverageRow(NamedTuple):
    label: str
    albums: int
    linked: int
    with_text: int


_QUARTILES = (("Top 25%", 0.75), ("50–75%", 0.5), ("25–50%", 0.25), ("Bottom 25%", 0.0))


def _bucket(popularity: float | None) -> str:
    if popularity is None:
        return "No popularity"
    return next(label for label, floor in _QUARTILES if popularity >= floor)


def summarize_coverage(albums: Iterable[tuple[float | None, bool, bool]]) -> list[CoverageRow]:
    """Count albums, linked albums and albums with stored text, overall and
    per popularity quartile. Input tuples are (popularity, linked, has_text)."""
    labels = ["All", *(label for label, _ in _QUARTILES), "No popularity"]
    counts = {label: [0, 0, 0] for label in labels}
    for popularity, linked, has_text in albums:
        for label in ("All", _bucket(popularity)):
            counts[label][0] += 1
            counts[label][1] += int(linked)
            counts[label][2] += int(has_text)
    return [CoverageRow(label, *counts[label]) for label in labels]


def _percent(part: int, whole: int) -> str:
    return f"{100 * part / whole:.0f}%" if whole else "n/a"


async def print_coverage(session: AsyncSession) -> None:
    rows = (
        await session.execute(
            select(Album.popularity, _LINKED, AlbumText.text.is_not(None))
            .outerjoin(
                AlbumText,
                and_(AlbumText.album_id == Album.id, AlbumText.source == WIKIPEDIA_SOURCE),
            )
            .where(Album.musicbrainz_release_group_id.is_not(None))
        )
    ).all()
    print(f"{'Popularity':<14}{'Albums':>8}{'Linked':>14}{'With text':>14}")
    for row in summarize_coverage((pop, bool(linked), bool(text)) for pop, linked, text in rows):
        print(
            f"{row.label:<14}{row.albums:>8}"
            f"{row.linked:>8} ({_percent(row.linked, row.albums):>4})"
            f"{row.with_text:>8} ({_percent(row.with_text, row.albums):>4})"
        )


async def _pending_albums(session: AsyncSession) -> list[Album]:
    done = select(AlbumText.album_id).where(
        AlbumText.source == WIKIPEDIA_SOURCE, AlbumText.fetched_at.is_not(None)
    )
    return list(
        (
            await session.scalars(
                select(Album).where(_LINKED, Album.id.not_in(done)).order_by(Album.id)
            )
        ).all()
    )


async def _resolve_all(
    client: httpx.AsyncClient, qids: list[str], request_interval_seconds: float
) -> dict[str, str | None]:
    titles: dict[str, str | None] = {}
    failure_streak = 0
    for start in range(0, len(qids), MAX_WIKIDATA_IDS_PER_REQUEST):
        answered = await resolve_enwiki_titles(
            client, qids[start : start + MAX_WIKIDATA_IDS_PER_REQUEST]
        )
        titles.update(answered)
        failure_streak = 0 if answered else failure_streak + 1
        if failure_streak >= MAX_CONSECUTIVE_FAILURES:
            raise SystemExit(
                f"{failure_streak} Wikidata requests in a row failed; Wikidata looks "
                "unavailable. Nothing was fetched yet; re-run later."
            )
        await _sleep(request_interval_seconds)
    return titles


async def backfill(request_interval_seconds: float = REQUEST_INTERVAL_SECONDS) -> None:
    contact = get_settings().wikimedia_contact_email
    if not contact:
        raise SystemExit(
            "CRATE_WIKIMEDIA_CONTACT_EMAIL is not set; add it to backend/.env "
            "(Wikimedia requires a contact address in the User-Agent)."
        )

    async with async_session_factory() as session:
        albums = await _pending_albums(session)
        qids = sorted({album.wikidata_id for album in albums if album.wikidata_id})
        print(f"Resolving {len(qids)} Wikidata ids for {len(albums)} albums...")

        headers = {"User-Agent": user_agent(contact)}
        async with httpx.AsyncClient(timeout=30, headers=headers) as client:
            titles = await _resolve_all(client, qids, request_interval_seconds)
            ready = [a for a in albums if not a.wikidata_id or a.wikidata_id in titles]
            print(f"Fetching articles for {len(ready)} albums (about 4 per second)...")

            failure_streak = 0
            for index, album in enumerate(ready, start=1):
                row = await sync_album_text(session, client, album, titles)
                if row.fetched_at is None:
                    failure_streak += 1
                    if failure_streak >= MAX_CONSECUTIVE_FAILURES:
                        await session.commit()
                        raise SystemExit(
                            f"{failure_streak} article fetches in a row failed; Wikipedia "
                            "looks unavailable. Progress is saved; re-run later to resume."
                        )
                else:
                    failure_streak = 0
                if index % _COMMIT_EVERY == 0:
                    await session.commit()
                if index % _PROGRESS_EVERY == 0:
                    print(f"  fetched {index}/{len(ready)}")
                await _sleep(request_interval_seconds)
        await session.commit()

        skipped = len(albums) - len(ready)
        if skipped:
            print(f"Skipped {skipped} albums whose Wikidata lookup failed; re-run to retry.")
        await print_coverage(session)


async def report() -> None:
    async with async_session_factory() as session:
        await print_coverage(session)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Wikipedia text for catalog albums.")
    parser.add_argument(
        "--report-only", action="store_true", help="Only print coverage; fetch nothing."
    )
    args = parser.parse_args()
    asyncio.run(report() if args.report_only else backfill())


if __name__ == "__main__":
    main()
