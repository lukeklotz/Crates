"""Path reach: do recommendations for an album in one scene stay in that
scene or step to the next scene along a path? An ungraded check, run
before and after each catalog batch on the same frozen seeds.

Scene membership comes from tags, so tag-based variants are favoured. Read
the report as coverage, not quality; the graded answer keys measure quality.

Run with: uv run python -m crate_backend.evaluation.path_reach --label baseline-25k
          [--variants overlap,tfidf-tags] [--per-scene 10] [--refresh-seeds]

Seeds (the top catalog albums by tag evidence in each scene on a path, one
per artist) are frozen in eval/path-reach-seeds.json on the first run and
reused afterwards, so later batches are measured on the same seeds.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

import argparse
import asyncio
import json
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from crate_backend.db.session import async_session_factory
from crate_backend.evaluation.store import Seed, eval_dir, popularity_quartile
from crate_backend.evaluation.variants import ModelNotBuilt, parse_variant_names, run_variants
from crate_backend.scenes.catalog import CatalogAlbum, load_catalog_albums
from crate_backend.scenes.config import SceneConfig, load_scene_config

REACH_K = 10
SEEDS_FILE = "path-reach-seeds.json"


@dataclass(frozen=True)
class ReachRow:
    variant: str
    scene: str
    seeds: int
    # Mean share of each seed's top REACH_K by where the album sits.
    same_scene: float
    neighbor_scene: float
    no_scene: float
    # Mean distinct artists in the top REACH_K.
    artists: float


def _path_scenes(config: SceneConfig) -> list[str]:
    seen: list[str] = []
    for path in config.paths:
        for scene in path.scenes:
            if scene not in seen:
                seen.append(scene)
    return seen


def pick_path_seeds(
    catalog: list[CatalogAlbum], config: SceneConfig, per_scene: int
) -> dict[str, list[uuid.UUID]]:
    """Each path scene's strongest catalog albums by tag evidence, at most one
    per artist, ties broken by album id."""
    ranked = sorted(
        (a for a in catalog if a.match is not None),
        key=lambda a: (-a.match.evidence, str(a.album_id)),
    )
    seeds: dict[str, list[uuid.UUID]] = {scene: [] for scene in _path_scenes(config)}
    artists: dict[str, set[str]] = {scene: set() for scene in seeds}
    for album in ranked:
        scene = album.match.home
        if scene not in seeds or len(seeds[scene]) >= per_scene:
            continue
        artist = album.primary_artist_id or album.artist_name or str(album.album_id)
        if artist in artists[scene]:
            continue
        artists[scene].add(artist)
        seeds[scene].append(album.album_id)
    return seeds


def reach_rows(
    runs: dict[str, dict[uuid.UUID, list[uuid.UUID]]],
    seed_scenes: dict[uuid.UUID, str],
    catalog_index: dict[uuid.UUID, CatalogAlbum],
    config: SceneConfig,
) -> list[ReachRow]:
    rows = []
    scenes = [s for s in _path_scenes(config) if s in set(seed_scenes.values())]
    for variant, by_seed in runs.items():
        for scene in scenes:
            neighbors = config.neighbors(scene)
            shares: list[tuple[float, float, float, int]] = []
            for seed_id, seed_scene in seed_scenes.items():
                if seed_scene != scene:
                    continue
                ranked = by_seed.get(seed_id, [])[:REACH_K]
                if not ranked:
                    shares.append((0.0, 0.0, 0.0, 0))
                    continue
                homes = [
                    album.match.home if (album := catalog_index.get(i)) and album.match else None
                    for i in ranked
                ]
                artists = {
                    (catalog_index[i].primary_artist_id or catalog_index[i].artist_name or str(i))
                    if i in catalog_index
                    else str(i)
                    for i in ranked
                }
                shares.append(
                    (
                        sum(h == scene for h in homes) / len(ranked),
                        sum(h in neighbors for h in homes) / len(ranked),
                        sum(h is None for h in homes) / len(ranked),
                        len(artists),
                    )
                )
            n = len(shares)
            rows.append(
                ReachRow(
                    variant=variant,
                    scene=scene,
                    seeds=n,
                    same_scene=sum(s[0] for s in shares) / n if n else 0.0,
                    neighbor_scene=sum(s[1] for s in shares) / n if n else 0.0,
                    no_scene=sum(s[2] for s in shares) / n if n else 0.0,
                    artists=sum(s[3] for s in shares) / n if n else 0.0,
                )
            )
    return rows


def render_reach(rows: list[ReachRow], *, label: str) -> str:
    lines = [
        f"# Path reach: {label}",
        "",
        "Scene membership comes from tags, so tag-based variants are favoured; read this as "
        "coverage, not quality.",
        "",
        f"Shares of each seed's top {REACH_K}: in the seed's own scene, in a scene next to it "
        "on a path, or in no scene. The rest are in other scenes. Artists = mean distinct "
        f"artists in the top {REACH_K}.",
        "",
        "| Variant | Scene | Seeds | Same scene | Neighbor scene | No scene | Artists |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row.variant} | {row.scene} | {row.seeds} | {row.same_scene:.0%} | "
            f"{row.neighbor_scene:.0%} | {row.no_scene:.0%} | {row.artists:.1f} |"
        )
    lines.append("")
    return "\n".join(lines)


async def write_path_reach(
    label: str,
    *,
    variant_names: str | None = None,
    per_scene: int = 10,
    refresh_seeds: bool = False,
    eval_folder: Path | None = None,
) -> Path:
    folder = eval_folder or eval_dir()
    variants = parse_variant_names(variant_names)
    config = load_scene_config()
    seeds_path = folder / SEEDS_FILE
    async with async_session_factory() as session:
        catalog = await load_catalog_albums(session, config)
        index = {a.album_id: a for a in catalog}
        if seeds_path.exists() and not refresh_seeds:
            frozen = {
                scene: [uuid.UUID(i) for i in ids]
                for scene, ids in json.loads(seeds_path.read_text()).items()
            }
        else:
            frozen = pick_path_seeds(catalog, config, per_scene)
            seeds_path.parent.mkdir(parents=True, exist_ok=True)
            seeds_path.write_text(
                json.dumps({s: [str(i) for i in ids] for s, ids in frozen.items()}, indent=2) + "\n"
            )
        seed_scenes = {
            album_id: scene for scene, ids in frozen.items() for album_id in ids if album_id in index
        }
        seeds = [
            Seed(
                album_id=album_id,
                title=index[album_id].title,
                artist_name=index[album_id].artist_name,
                popularity_quartile=(
                    popularity_quartile(index[album_id].popularity)
                    if index[album_id].popularity is not None
                    else "unknown"
                ),
            )
            for album_id in seed_scenes
        ]
        runs = await run_variants(variants, session, seeds, REACH_K)
    report = render_reach(reach_rows(runs, seed_scenes, index, config), label=label)
    today = datetime.now().astimezone().date().isoformat()
    path = folder / "results" / f"path-reach-{today}-{label}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report)
    print(report)
    print(f"Wrote {path}")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Report path reach on frozen scene seeds.")
    parser.add_argument("--label", required=True, help="e.g. baseline-25k or after-batch-1")
    parser.add_argument(
        "--variants", default=None, help="comma-separated; default: the five core variants"
    )
    parser.add_argument("--per-scene", type=int, default=10, help="seeds per scene")
    parser.add_argument(
        "--refresh-seeds", action="store_true", help="re-pick and re-freeze the seeds"
    )
    args = parser.parse_args()
    try:
        asyncio.run(
            write_path_reach(
                args.label,
                variant_names=args.variants,
                per_scene=args.per_scene,
                refresh_seeds=args.refresh_seeds,
            )
        )
    except (ModelNotBuilt, ValueError, FileNotFoundError) as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()
