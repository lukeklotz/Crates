"""Pick the next batch of albums to add to the catalog from the scene pool.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md

Run with: uv run python -m crate_backend.scripts.select_catalog_batch --name batch-1 --target 25000 [--force]

Reads settings.scene_pool_path (written by profile_catalog_pool), the
current catalog and catalog/scenes.toml. Writes catalog/batches/<name>.jsonl
(one line per album) and <name>.md (a summary to read before ingesting).
Nothing is written to the database; ingest the batch with
ingest_musicbrainz --batch.
"""

import argparse
import asyncio
import dataclasses
import subprocess
from collections import Counter
from pathlib import Path

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.scenes.batches import batch_line, read_batch_ids, write_batch
from crate_backend.scenes.catalog import load_catalog_albums
from crate_backend.scenes.config import SceneConfig, load_scene_config
from crate_backend.scenes.pool import PoolAlbum, read_pool
from crate_backend.scenes.select import SLICES, BatchResult, select_batch

__all__ = ["main", "read_batch_ids", "select"]

_TOP_ARTISTS = 10


def _scenes_version(catalog_dir: Path) -> str:
    try:
        root = Path(
            subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                cwd=catalog_dir, capture_output=True, text=True, check=True,
            ).stdout.strip()
        )
        relative = (catalog_dir / "scenes.toml").resolve().relative_to(root)
        commit = subprocess.run(
            ["git", "log", "-1", "--format=%h", "--", str(relative)],
            cwd=root, capture_output=True, text=True, check=True,
        ).stdout.strip()
        changed = subprocess.run(
            ["git", "diff", "--quiet", "HEAD", "--", str(relative)], cwd=root
        ).returncode
    except (OSError, ValueError, subprocess.CalledProcessError):
        return "unknown"
    if not commit:
        return "uncommitted"
    return f"{commit} (with uncommitted changes)" if changed else commit


def render_summary(
    name: str,
    target: int,
    result: BatchResult,
    albums: dict[str, PoolAlbum],
    config: SceneConfig,
    scenes_version: str,
) -> str:
    by_scene_slice = Counter((p.scene, p.slice) for p in result.picks)
    by_scene = Counter(p.scene for p in result.picks)
    lines = [
        f"# Catalog batch {name}",
        "",
        f"Target: {target:,}. Picked: {len(result.picks):,}. scenes.toml: {scenes_version}.",
        "",
        "## Scenes",
        "",
        "| Scene | Budget | Picked | " + " | ".join(s.capitalize() for s in SLICES) + " | Shortfall |",
        "|---" * (4 + len(SLICES)) + "|",
    ]
    for scene in config.scenes:
        sid = scene.id
        slices = " | ".join(f"{by_scene_slice[(sid, s)]:,}" for s in SLICES)
        lines.append(
            f"| {sid} | {result.budgets.get(sid, 0):,} | {by_scene[sid]:,} | {slices} | "
            f"{result.shortfalls.get(sid, 0):,} |"
        )
    artists = Counter(albums[p.musicbrainz_id].artist_name for p in result.picks)
    decades = Counter(
        f"{albums[p.musicbrainz_id].year // 10 * 10}s" for p in result.picks
    )
    lines += [
        "",
        "## Artists with the most picks",
        "",
        "| Artist | Albums |",
        "|---|---|",
        *(f"| {a.replace('|', chr(92) + '|')} | {n} |" for a, n in artists.most_common(_TOP_ARTISTS)),
        "",
        "## Picks per decade",
        "",
        "| Decade | Albums |",
        "|---|---|",
        *(f"| {d} | {n:,} |" for d, n in sorted(decades.items())),
        "",
    ]
    return "\n".join(lines)


async def select(
    name: str,
    target: int,
    *,
    force: bool,
    catalog_dir: Path | None = None,
    pool_path: Path | None = None,
) -> Path:
    settings = get_settings()
    catalog_dir = catalog_dir or Path(settings.catalog_dir)
    pool_path = pool_path or Path(settings.scene_pool_path)
    batch_path = catalog_dir / "batches" / f"{name}.jsonl"
    if batch_path.exists() and not force:
        raise SystemExit(f"{batch_path} exists; pass --force to replace it.")
    if not pool_path.exists():
        raise SystemExit(f"No scene pool at {pool_path}; run profile_catalog_pool first.")

    config = load_scene_config()
    # Only matched albums matter, and their raw records aren't needed here.
    albums = {
        a.musicbrainz_id: dataclasses.replace(a, record={})
        for a in read_pool(pool_path, config)
        if a.match is not None
    }
    async with async_session_factory() as session:
        catalog = await load_catalog_albums(session, config)
    print(f"{len(albums):,} in-scene pool albums; catalog has {len(catalog):,} albums.")

    result = select_batch(albums.values(), catalog, config, target)
    write_batch((batch_line(p, albums[p.musicbrainz_id]) for p in result.picks), batch_path)
    summary = render_summary(name, target, result, albums, config, _scenes_version(catalog_dir))
    batch_path.with_suffix(".md").write_text(summary)
    print(summary)
    print(f"Wrote {batch_path}")
    return batch_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Pick the next catalog batch from the scene pool.")
    parser.add_argument("--name", required=True, help="batch name, e.g. batch-1")
    parser.add_argument("--target", type=int, required=True, help="albums to add")
    parser.add_argument("--force", action="store_true", help="replace an existing batch file")
    args = parser.parse_args()
    if args.target <= 0:
        parser.error("--target must be positive")
    asyncio.run(select(args.name, args.target, force=args.force))


if __name__ == "__main__":
    main()
