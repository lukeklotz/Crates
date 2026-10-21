"""Profile the MusicBrainz release-group dump by catalog scene and write the
scene pool file the batch selector reads.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md

Run with: uv run python -m crate_backend.scripts.profile_catalog_pool [--from-pool]

The dump pass streams the whole release-group dump (about 10 minutes) and
writes settings.scene_pool_path plus catalog/reports/profile-<snapshot>.md.
After editing catalog/scenes.toml, re-run with --from-pool: it re-profiles
from the pool file in a minute or two without reading the dump.
"""

import argparse
import asyncio
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from sqlalchemy import func, select

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.models.catalog import Album
from crate_backend.musicbrainz.dump_reader import read_dump_metadata, stream_jsonl_from_tar
from crate_backend.scenes.config import SceneConfig, load_scene_config
from crate_backend.scenes.pool import read_raw_pool, to_pool_album, write_pool
from crate_backend.scenes.profile import ProfileCounts, render_profile

_PROGRESS_EVERY = 500_000


async def _catalog_ids() -> set[str]:
    async with async_session_factory() as session:
        rows = await session.scalars(
            select(Album.musicbrainz_release_group_id).where(
                Album.musicbrainz_release_group_id.is_not(None)
            )
        )
        return set(rows.all())


async def _catalog_size() -> int:
    async with async_session_factory() as session:
        return await session.scalar(select(func.count()).select_from(Album)) or 0


def _snapshot_file(pool_path: Path) -> Path:
    return pool_path.with_name(pool_path.name + ".timestamp")


def _snapshot_date(timestamp: str) -> str:
    return timestamp[:10] if timestamp else "unknown"


def _counted(
    records: Iterator[dict[str, Any]],
    counts: ProfileCounts,
    config: SceneConfig,
    catalog_ids: set[str],
) -> Iterator[dict[str, Any]]:
    """Count every record and yield the ones that belong in the pool."""
    for index, record in enumerate(records, start=1):
        album = to_pool_album(record, config)
        counts.add_release_group(record, album, record.get("id") in catalog_ids)
        if album is not None:
            yield record
        if index % _PROGRESS_EVERY == 0:
            print(f"  read {index:,} release groups")


def _write_report(counts: ProfileCounts, config: SceneConfig, snapshot: str, size: int,
                  report_dir: Path) -> Path:
    report_dir.mkdir(parents=True, exist_ok=True)
    path = report_dir / f"profile-{snapshot}.md"
    path.write_text(render_profile(counts, config, snapshot=snapshot, catalog_size=size))
    return path


async def profile_dump(dump_dir: Path, pool_path: Path, report_dir: Path) -> Path:
    archive = dump_dir / "release-group.tar.xz"
    metadata = read_dump_metadata(archive)
    print(f"{archive.name}: {metadata}")
    config = load_scene_config()
    catalog_ids = await _catalog_ids()
    counts = ProfileCounts(config.settings)
    print("Profiling release groups (streams the whole dump; takes several minutes)...")
    records = stream_jsonl_from_tar(archive, "mbdump/release-group")
    written = write_pool(_counted(records, counts, config, catalog_ids), pool_path)
    timestamp = metadata.get("TIMESTAMP", "")
    _snapshot_file(pool_path).write_text(timestamp)
    print(f"Wrote {written:,} pool records to {pool_path}")
    path = _write_report(counts, config, _snapshot_date(timestamp), await _catalog_size(), report_dir)
    print(f"Wrote {path}")
    return path


async def profile_pool(pool_path: Path, report_dir: Path) -> Path:
    config = load_scene_config()
    catalog_ids = await _catalog_ids()
    counts = ProfileCounts(config.settings)
    for _ in _counted(read_raw_pool(pool_path), counts, config, catalog_ids):
        pass
    snapshot_file = _snapshot_file(pool_path)
    timestamp = snapshot_file.read_text() if snapshot_file.exists() else ""
    path = _write_report(counts, config, _snapshot_date(timestamp), await _catalog_size(), report_dir)
    print(f"Wrote {path}")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Profile the dump by scene; write the pool.")
    parser.add_argument(
        "--from-pool", action="store_true", help="re-profile the existing pool file only"
    )
    args = parser.parse_args()
    settings = get_settings()
    pool_path = Path(settings.scene_pool_path)
    report_dir = Path(settings.catalog_dir) / "reports"
    if args.from_pool:
        if not pool_path.exists():
            raise SystemExit(f"No pool at {pool_path}; run without --from-pool first.")
        asyncio.run(profile_pool(pool_path, report_dir))
    else:
        asyncio.run(profile_dump(Path(settings.musicbrainz_dump_dir), pool_path, report_dir))


if __name__ == "__main__":
    main()
