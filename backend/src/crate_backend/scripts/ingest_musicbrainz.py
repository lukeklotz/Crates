"""Import MusicBrainz JSON Data Dumps into Crate's album catalog (Phase 2).

Design: docs/superpowers/specs/2026-09-20-musicbrainz-ingestion-design.md

Run with: uv run python -m crate_backend.scripts.ingest_musicbrainz [--skip-cover-art | --cover-art-only]
"""

import argparse
import asyncio
from pathlib import Path

import httpx
from sqlalchemy import select

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.models.catalog import Album
from crate_backend.musicbrainz.cover_art import iter_cover_art
from crate_backend.musicbrainz.dump_reader import read_dump_metadata, stream_jsonl_from_tar
from crate_backend.musicbrainz.extract import (
    artist_ids_in_credits,
    filter_and_rank_release_groups,
    resolve_artists,
)
from crate_backend.musicbrainz.ingest import upsert_album, upsert_artist_relationships

_PROGRESS_EVERY = 1000
_COVER_ART_COMMIT_EVERY = 100


def _percent(part: int, whole: int) -> str:
    return f"{100 * part / whole:.1f}%" if whole else "n/a"


async def ingest_dumps(dump_dir: Path, target_size: int) -> None:
    release_group_archive = dump_dir / "release-group.tar.xz"
    artist_archive = dump_dir / "artist.tar.xz"
    for archive in (release_group_archive, artist_archive):
        print(f"{archive.name}: {read_dump_metadata(archive)}")

    print("Filtering release groups (streams the whole dump; takes several minutes)...")
    candidates = filter_and_rank_release_groups(
        stream_jsonl_from_tar(release_group_archive, "mbdump/release-group"), target_size
    )
    print(f"Selected {len(candidates)} candidate albums.")

    wanted_ids = artist_ids_in_credits(candidates)
    print(f"Resolving {len(wanted_ids)} credited artists...")
    artists = resolve_artists(stream_jsonl_from_tar(artist_archive, "mbdump/artist"), wanted_ids)
    print(f"Resolved {len(artists)} of {len(wanted_ids)} credited artists.")

    async with async_session_factory() as session:
        for index, candidate in enumerate(candidates, start=1):
            await upsert_album(session, candidate)
            if index % _PROGRESS_EVERY == 0:
                print(f"  upserted {index}/{len(candidates)} albums")
        for artist in artists.values():
            await upsert_artist_relationships(session, artist)
        await session.commit()

    total = len(candidates)
    print(
        f"Ingested {total} albums. Coverage: "
        f"genre {_percent(sum(1 for c in candidates if c.genres), total)}, "
        f"tag {_percent(sum(1 for c in candidates if c.tags), total)}, "
        f"resolved artists with a relationship "
        f"{_percent(sum(1 for a in artists.values() if a.relationships), len(artists))}."
    )


async def fetch_missing_cover_art() -> None:
    """Check Cover Art Archive for every MusicBrainz album without a
    cover_art_url, committing as it goes so an interrupted run keeps its
    progress. Albums with no art stay null and are re-checked next run."""
    async with async_session_factory() as session:
        albums = (
            await session.scalars(
                select(Album).where(
                    Album.musicbrainz_release_group_id.is_not(None),
                    Album.cover_art_url.is_(None),
                )
            )
        ).all()
        by_mbid = {album.musicbrainz_release_group_id: album for album in albums}
        print(f"Checking cover art for {len(by_mbid)} albums (about 1 per second)...")

        found = 0
        async with httpx.AsyncClient(timeout=10.0) as client:
            async for index, (mbid, url) in _enumerate(iter_cover_art(client, list(by_mbid))):
                if url is not None:
                    by_mbid[mbid].cover_art_url = url
                    found += 1
                if index % _COVER_ART_COMMIT_EVERY == 0:
                    await session.commit()
                    print(f"  checked {index}/{len(by_mbid)}, found {found}")
        await session.commit()
    print(f"Found cover art for {found} of {len(by_mbid)} albums.")


async def _enumerate(iterator):
    index = 0
    async for item in iterator:
        index += 1
        yield index, item


def main() -> None:
    parser = argparse.ArgumentParser(description="Import MusicBrainz dumps into Crate.")
    stage = parser.add_mutually_exclusive_group()
    stage.add_argument(
        "--skip-cover-art", action="store_true", help="Only ingest the dumps."
    )
    stage.add_argument(
        "--cover-art-only",
        action="store_true",
        help="Skip the dumps; only fetch cover art for albums that don't have it yet.",
    )
    args = parser.parse_args()
    settings = get_settings()

    async def _run() -> None:
        if not args.cover_art_only:
            await ingest_dumps(
                Path(settings.musicbrainz_dump_dir), settings.musicbrainz_target_catalog_size
            )
        if not args.skip_cover_art:
            await fetch_missing_cover_art()

    asyncio.run(_run())


if __name__ == "__main__":
    main()
