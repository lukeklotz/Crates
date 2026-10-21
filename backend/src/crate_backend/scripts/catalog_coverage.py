"""Report how well the catalog covers each scene and path edge.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md

Run with: uv run python -m crate_backend.scripts.catalog_coverage --label baseline-25k

Reads the catalog, the scene pool (for entry points and live status, which
the albums table doesn't store) and catalog/batches/*.jsonl, and writes
catalog/reports/coverage-<date>-<label>.md.
"""

import argparse
import asyncio
import heapq
from datetime import datetime
from pathlib import Path

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.scenes.batches import batch_memberships
from crate_backend.scenes.catalog import load_catalog_albums
from crate_backend.scenes.config import load_scene_config
from crate_backend.scenes.coverage import (
    ENTRY_POINT_DEPTH,
    edge_coverage,
    render_coverage,
    scene_coverage,
)
from crate_backend.scenes.pool import read_pool


async def write_coverage(
    label: str, *, catalog_dir: Path | None = None, pool_path: Path | None = None
) -> Path:
    settings = get_settings()
    catalog_dir = catalog_dir or Path(settings.catalog_dir)
    pool_path = pool_path or Path(settings.scene_pool_path)
    config = load_scene_config()

    # Each scene's strongest pool albums, kept as a bounded heap per scene.
    tops: dict[str, list[tuple[float, str]]] = {s.id: [] for s in config.scenes}
    live_ids: set[str] = set()
    if pool_path.exists():
        for album in read_pool(pool_path, config):
            if album.is_live:
                live_ids.add(album.musicbrainz_id)
            if album.match is None:
                continue
            heap = tops[album.match.home]
            entry = (album.match.evidence, album.musicbrainz_id)
            if len(heap) < ENTRY_POINT_DEPTH:
                heapq.heappush(heap, entry)
            else:
                heapq.heappushpop(heap, entry)
    else:
        print(f"No scene pool at {pool_path}: entry points and live counts will be empty.")
    pool_top = {scene: {mbid for _, mbid in heap} for scene, heap in tops.items()}

    async with async_session_factory() as session:
        catalog = await load_catalog_albums(session, config)
    scenes = scene_coverage(
        catalog, pool_top, live_ids, batch_memberships(catalog_dir / "batches"), config
    )
    report = render_coverage(
        scenes,
        edge_coverage(catalog, config),
        total=len(catalog),
        in_no_scene=sum(a.match is None for a in catalog),
        label=label,
    )
    today = datetime.now().astimezone().date().isoformat()
    path = catalog_dir / "reports" / f"coverage-{today}-{label}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report)
    print(report)
    print(f"Wrote {path}")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Report catalog coverage by scene and path edge.")
    parser.add_argument("--label", required=True, help="e.g. baseline-25k or after-batch-1")
    args = parser.parse_args()
    asyncio.run(write_coverage(args.label))


if __name__ == "__main__":
    main()
