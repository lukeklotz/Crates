"""How well the catalog covers each scene and each path edge, compared
across batches.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass

from crate_backend.evaluation.store import QUARTILES, popularity_quartile
from crate_backend.scenes.catalog import CatalogAlbum
from crate_backend.scenes.config import SceneConfig
from crate_backend.scenes.select import is_deep_cut

# Entry-point coverage: the share of a scene's strongest pool albums (by
# evidence) that are in the catalog.
ENTRY_POINT_DEPTH = 100
ORIGINAL = "original"
UNKNOWN = "unknown"


@dataclass(frozen=True)
class SceneCoverage:
    scene: str
    albums: int
    live: int
    # Batch name -> albums it added to this scene; "original" = no batch file.
    by_batch: dict[str, int]
    artists: int
    max_per_artist: int
    entry_point_coverage: float
    deep_cuts: int
    with_text: float
    quartiles: dict[str, int]


@dataclass(frozen=True)
class EdgeCoverage:
    path: str
    a: str
    b: str
    # Catalog albums at home in one end that connect to the other, both ways.
    connectors: int


def _batch_of(mbid: str | None, batches: dict[str, set[str]]) -> str:
    for name, ids in batches.items():
        if mbid in ids:
            return name
    return ORIGINAL


def scene_coverage(
    catalog: Iterable[CatalogAlbum],
    pool_top: dict[str, set[str]],
    live_ids: set[str],
    batches: dict[str, set[str]],
    config: SceneConfig,
) -> list[SceneCoverage]:
    members: dict[str, list[CatalogAlbum]] = {s.id: [] for s in config.scenes}
    for album in catalog:
        if album.match is not None:
            members[album.match.home].append(album)
    rows = []
    for scene in config.scenes:
        albums = members[scene.id]
        in_catalog = {a.musicbrainz_id for a in albums}
        top = pool_top.get(scene.id, set())
        artists = Counter(a.primary_artist_id or a.artist_name or str(a.album_id) for a in albums)
        rows.append(
            SceneCoverage(
                scene=scene.id,
                albums=len(albums),
                live=sum(a.musicbrainz_id in live_ids for a in albums),
                by_batch=dict(Counter(_batch_of(a.musicbrainz_id, batches) for a in albums)),
                artists=len(artists),
                max_per_artist=max(artists.values(), default=0),
                entry_point_coverage=len(top & in_catalog) / len(top) if top else 0.0,
                deep_cuts=sum(is_deep_cut(a, config.settings) for a in albums),
                with_text=sum(a.has_text for a in albums) / len(albums) if albums else 0.0,
                quartiles=dict(
                    Counter(
                        UNKNOWN if a.popularity is None else popularity_quartile(a.popularity)
                        for a in albums
                    )
                ),
            )
        )
    return rows


def edge_coverage(catalog: Iterable[CatalogAlbum], config: SceneConfig) -> list[EdgeCoverage]:
    links = Counter(
        (album.match.home, other)
        for album in catalog
        if album.match is not None
        for other in album.match.connects_to
    )
    return [
        EdgeCoverage(path.name, a, b, links[(a, b)] + links[(b, a)])
        for path in config.paths
        for a, b in zip(path.scenes, path.scenes[1:])
    ]


def render_coverage(
    scenes: list[SceneCoverage],
    edges: list[EdgeCoverage],
    *,
    total: int,
    in_no_scene: int,
    label: str,
) -> str:
    batch_names = sorted({name for row in scenes for name in row.by_batch} - {ORIGINAL})
    batch_columns = [ORIGINAL, *batch_names]
    quartile_columns = [*QUARTILES, UNKNOWN]
    lines = [
        f"# Catalog coverage: {label}",
        "",
        f"Catalog albums: {total:,}. In no scene: {in_no_scene:,}.",
        "",
        (
            f"Entry points = share of the scene's top {ENTRY_POINT_DEPTH} pool albums by tag "
            "evidence that are in the catalog. Text = share with a Wikipedia article. "
            "Quartiles are Last.fm popularity (top, upper-mid, lower-mid, bottom, unknown)."
        ),
        "",
        "## Scenes",
        "",
        "| Scene | Albums | Live | "
        + " | ".join(batch_columns)
        + " | Artists | Max per artist | Entry points | Deep cuts | Text | Quartiles |",
        "|---" * (9 + len(batch_columns)) + "|",
    ]
    for row in scenes:
        batches = " | ".join(f"{row.by_batch.get(name, 0):,}" for name in batch_columns)
        quartiles = " / ".join(str(row.quartiles.get(q, 0)) for q in quartile_columns)
        lines.append(
            f"| {row.scene} | {row.albums:,} | {row.live:,} | {batches} | {row.artists:,} | "
            f"{row.max_per_artist} | {row.entry_point_coverage:.0%} | {row.deep_cuts:,} | "
            f"{row.with_text:.0%} | {quartiles} |"
        )
    lines += [
        "",
        "## Path edges",
        "",
        "Connectors = catalog albums at home in one scene that also carry the other's terms.",
        "",
        "| Path | From | To | Connectors |",
        "|---|---|---|---|",
        *(f"| {e.path} | {e.a} | {e.b} | {e.connectors:,} |" for e in edges),
        "",
    ]
    return "\n".join(lines)
