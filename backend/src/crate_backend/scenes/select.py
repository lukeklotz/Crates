"""Pick a batch of albums to add to the catalog, scene by scene.

Each scene's share of the batch is filled in two phases. First come its
reserved slices: live albums, connectors to neighboring scenes, and deep
cuts (little-known but well-described albums). Then the open slice takes
the strongest remaining studio albums. Within a slice albums are taken
greedily by gain, which is tag evidence reduced for an artist's later
albums and for albums whose main tag is a deprioritized term. Gains only
fall as albums are taken, so a lazy greedy
(re-score the top of the heap, take it if it still leads) gives the same
result as re-scoring everything.

A scene that runs out of candidates hands the rest of its budget to the
scenes that still have some, by share. A batch whose scenes all run out is
smaller than its target rather than padded.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

import heapq
import math
from collections import Counter, defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field

from crate_backend.scenes.catalog import CatalogAlbum
from crate_backend.scenes.config import SceneConfig, SelectionSettings
from crate_backend.scenes.matching import main_terms
from crate_backend.scenes.pool import PoolAlbum

SLICES = ("live", "connector", "deep", "open")


@dataclass(frozen=True)
class Pick:
    musicbrainz_id: str
    scene: str
    slice: str
    gain: float
    evidence: float


@dataclass
class BatchResult:
    picks: list[Pick]
    # Each scene's share of the target before any redistribution.
    budgets: dict[str, int]
    # Budget a scene could not fill from its own candidates; it went to others.
    shortfalls: dict[str, int] = field(default_factory=dict)
    # Scenes with no studio candidates left once the batch is picked,
    # including any that ran dry after taking redistributed budget.
    exhausted: list[str] = field(default_factory=list)


def is_deep_cut(album: PoolAlbum | CatalogAlbum, settings: SelectionSettings) -> bool:
    """Less famous but well described: few votes in total, several
    descriptive terms, and at least two of them scene terms. Tag votes stand
    in for fame because albums outside the catalog have no Last.fm data."""
    return (
        album.match is not None
        and sum(album.terms.values()) <= settings.deep_cut_max_votes
        and len(album.terms) >= settings.deep_cut_min_terms
        and len(album.match.matched_terms) >= settings.deep_cut_min_scene_terms
    )


def scene_budgets(
    config: SceneConfig, target: int, scene_ids: Iterable[str] | None = None
) -> dict[str, int]:
    """Split `target` across scenes by share, with largest-remainder rounding
    so the parts sum exactly to the target. Ties go to the scene listed first."""
    wanted = None if scene_ids is None else set(scene_ids)
    scenes = [s for s in config.scenes if wanted is None or s.id in wanted]
    total = sum(s.share for s in scenes)
    if not scenes or total <= 0:
        return {}
    exact = [(s.id, target * s.share / total) for s in scenes]
    budgets = {sid: math.floor(value) for sid, value in exact}
    by_remainder = sorted(
        range(len(exact)), key=lambda i: (-(exact[i][1] - budgets[exact[i][0]]), i)
    )
    for i in by_remainder[: target - sum(budgets.values())]:
        budgets[exact[i][0]] += 1
    return budgets


def _artist_factor(albums_so_far: int, settings: SelectionSettings) -> float:
    if albums_so_far < settings.artist_free_albums:
        return 1.0
    return settings.artist_decay ** (albums_so_far - settings.artist_free_albums + 1)


class _Selection:
    def __init__(self, catalog: list[CatalogAlbum], config: SceneConfig) -> None:
        self.config = config
        self.settings = config.settings
        self.artists = Counter(c.primary_artist_id for c in catalog if c.primary_artist_id)
        self.taken: set[str] = set()
        self.picks: list[Pick] = []

    def gain(self, album: PoolAlbum) -> float:
        match = album.match
        gain = match.evidence
        if album.primary_artist_id:
            gain *= _artist_factor(self.artists[album.primary_artist_id], self.settings)
        if self.config.deprioritized_terms & main_terms(album.terms):
            gain *= self.settings.deprioritized_factor
        return gain

    def fill(
        self, scene_id: str, slice_name: str, candidates: list[PoolAlbum], capacity: int
    ) -> int:
        """Take up to `capacity` of `candidates` by lazy greedy; returns how many."""
        heap = [
            (-self.gain(album), album.musicbrainz_id, index)
            for index, album in enumerate(candidates)
            if album.musicbrainz_id not in self.taken
        ]
        heapq.heapify(heap)
        taken = 0
        while taken < capacity and heap:
            _, mbid, index = heapq.heappop(heap)
            if mbid in self.taken:
                continue
            album = candidates[index]
            gain = self.gain(album)
            if heap and (-gain, mbid) > heap[0][:2]:
                heapq.heappush(heap, (-gain, mbid, index))
                continue
            self.take(album, scene_id, slice_name, gain)
            taken += 1
        return taken

    def take(self, album: PoolAlbum, scene_id: str, slice_name: str, gain: float) -> None:
        self.taken.add(album.musicbrainz_id)
        if album.primary_artist_id:
            self.artists[album.primary_artist_id] += 1
        self.picks.append(
            Pick(album.musicbrainz_id, scene_id, slice_name, gain, album.match.evidence)
        )


def select_batch(
    pool: Iterable[PoolAlbum], catalog: Iterable[CatalogAlbum], config: SceneConfig, target: int
) -> BatchResult:
    catalog = list(catalog)
    in_catalog = {c.musicbrainz_id for c in catalog if c.musicbrainz_id}
    by_scene: dict[str, list[PoolAlbum]] = defaultdict(list)
    for album in pool:
        if album.match is not None and album.musicbrainz_id not in in_catalog:
            by_scene[album.match.home].append(album)

    selection = _Selection(catalog, config)
    settings = config.settings
    budgets = scene_budgets(config, target)

    open_capacity: dict[str, int] = {}
    for scene in config.scenes:
        budget = budgets.get(scene.id, 0)
        candidates = by_scene[scene.id]
        studio = [a for a in candidates if not a.is_live]
        reserved = (
            ("live", [a for a in candidates if a.is_live], settings.live_share),
            ("connector", [a for a in studio if a.match.connects_to], settings.connector_share),
            ("deep", [a for a in studio if is_deep_cut(a, settings)], settings.deep_cut_share),
        )
        filled = sum(
            selection.fill(scene.id, name, members, math.floor(budget * share))
            for name, members, share in reserved
        )
        open_capacity[scene.id] = budget - filled

    def studio_left(scene_id: str) -> list[PoolAlbum]:
        return [
            a
            for a in by_scene[scene_id]
            if not a.is_live and a.musicbrainz_id not in selection.taken
        ]

    shortfalls: dict[str, int] = {}
    first_round = True
    while True:
        leftover = 0
        for scene in config.scenes:
            capacity = open_capacity.get(scene.id, 0)
            if capacity <= 0:
                continue
            got = selection.fill(scene.id, "open", studio_left(scene.id), capacity)
            if got < capacity:
                leftover += capacity - got
                if first_round:
                    shortfalls[scene.id] = capacity - got
        first_round = False
        with_candidates = [s.id for s in config.scenes if studio_left(s.id)]
        if leftover == 0 or not with_candidates:
            break
        open_capacity = scene_budgets(config, leftover, with_candidates)

    exhausted = [s.id for s in config.scenes if not studio_left(s.id)]
    return BatchResult(
        picks=selection.picks, budgets=budgets, shortfalls=shortfalls, exhausted=exhausted
    )
