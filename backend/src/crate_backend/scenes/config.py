"""Load catalog/scenes.toml: the scenes the catalog batch selector pulls
albums from, and the paths between them.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from crate_backend.core.config import get_settings
from crate_backend.recommend.text_cleaning import normalize_term

TIERS = ("center", "neighbor", "roots", "echoes", "wider")


class SceneConfigError(ValueError):
    pass


@dataclass(frozen=True)
class Scene:
    id: str
    name: str
    tier: str
    # (from, to) inclusive; to is None for "to the present".
    years: tuple[int, int | None]
    share: float
    terms: frozenset[str]
    broad_terms: frozenset[str]
    requires_any: frozenset[str]
    exclude_terms: frozenset[str]
    min_matched_terms: int = 1

    def holds_year(self, year: int) -> bool:
        start, end = self.years
        return year >= start and (end is None or year <= end)


@dataclass(frozen=True)
class ScenePath:
    name: str
    scenes: tuple[str, ...]


@dataclass(frozen=True)
class SelectionSettings:
    live_share: float
    connector_share: float
    deep_cut_share: float
    broad_weight: float
    artist_free_albums: int
    artist_decay: float
    broad_only_halfway: float
    deprioritized_factor: float
    deep_cut_max_votes: int
    deep_cut_min_terms: int
    deep_cut_min_scene_terms: int


@dataclass(frozen=True)
class SceneConfig:
    settings: SelectionSettings
    scenes: tuple[Scene, ...]
    paths: tuple[ScenePath, ...]
    nondescriptive_terms: frozenset[str]
    deprioritized_terms: frozenset[str]

    def scene(self, scene_id: str) -> Scene:
        for scene in self.scenes:
            if scene.id == scene_id:
                return scene
        raise SceneConfigError(f"unknown scene id '{scene_id}'")

    def neighbors(self, scene_id: str) -> frozenset[str]:
        """Scenes one step away from `scene_id` on any path."""
        found: set[str] = set()
        for path in self.paths:
            for index, step in enumerate(path.scenes):
                if step != scene_id:
                    continue
                if index > 0:
                    found.add(path.scenes[index - 1])
                if index + 1 < len(path.scenes):
                    found.add(path.scenes[index + 1])
        found.discard(scene_id)
        return frozenset(found)


def _terms(values: Any) -> frozenset[str]:
    return frozenset(term for term in (normalize_term(v) for v in values or []) if term)


def _years(scene_id: str, values: Any) -> tuple[int, int | None]:
    if not isinstance(values, list) or len(values) not in (1, 2):
        raise SceneConfigError(f"scene '{scene_id}': years must be [from] or [from, to]")
    start = int(values[0])
    end = int(values[1]) if len(values) == 2 else None
    if end is not None and end < start:
        raise SceneConfigError(f"scene '{scene_id}': years {values} run backwards")
    return start, end


def _scene(raw: dict[str, Any]) -> Scene:
    scene_id = raw.get("id")
    if not scene_id:
        raise SceneConfigError("every [[scene]] needs an id")
    tier = raw.get("tier")
    if tier not in TIERS:
        raise SceneConfigError(f"scene '{scene_id}': tier '{tier}' is not one of {TIERS}")
    share = float(raw.get("share", 0))
    if share <= 0:
        raise SceneConfigError(f"scene '{scene_id}': share must be above 0")
    return Scene(
        id=scene_id,
        name=raw.get("name") or scene_id,
        tier=tier,
        years=_years(scene_id, raw.get("years")),
        share=share,
        terms=_terms(raw.get("terms")),
        broad_terms=_terms(raw.get("broad_terms")),
        requires_any=_terms(raw.get("requires_any")),
        exclude_terms=_terms(raw.get("exclude_terms")),
        min_matched_terms=int(raw.get("min_matched_terms", 1)),
    )


def _check_settings(settings: SelectionSettings) -> None:
    """Reject values that would break the selector's guarantees, such as
    reserved slices that together claim more than a scene's whole budget."""
    shares = ("live_share", "connector_share", "deep_cut_share")
    for name in shares:
        if getattr(settings, name) < 0:
            raise SceneConfigError(f"[settings]: {name} must not be negative")
    if sum(getattr(settings, name) for name in shares) > 1:
        raise SceneConfigError(f"[settings]: {', '.join(shares)} must add up to at most 1")
    if settings.broad_only_halfway <= 0:
        raise SceneConfigError("[settings]: broad_only_halfway must be above 0")
    if not 0 < settings.artist_decay <= 1:
        raise SceneConfigError("[settings]: artist_decay must be above 0 and at most 1")


def parse_scene_config(text: str) -> SceneConfig:
    data = tomllib.loads(text)
    raw_settings = dict(data.get("settings") or {})
    nondescriptive = raw_settings.pop("nondescriptive_terms", [])
    deprioritized = raw_settings.pop("deprioritized_terms", [])
    try:
        settings = SelectionSettings(**raw_settings)
    except TypeError as error:
        raise SceneConfigError(f"[settings]: {error}") from error
    _check_settings(settings)

    scenes = tuple(_scene(raw) for raw in data.get("scene") or [])
    seen: set[str] = set()
    for scene in scenes:
        if scene.id in seen:
            raise SceneConfigError(f"duplicate scene id '{scene.id}'")
        seen.add(scene.id)

    paths = []
    for raw in data.get("path") or []:
        name = raw.get("name") or "unnamed path"
        steps = tuple(raw.get("scenes") or [])
        unknown = [step for step in steps if step not in seen]
        if unknown:
            raise SceneConfigError(f"path '{name}' names unknown scenes {unknown}")
        if len(steps) < 2:
            raise SceneConfigError(f"path '{name}' needs at least two scenes")
        paths.append(ScenePath(name=name, scenes=steps))

    return SceneConfig(
        settings=settings,
        scenes=scenes,
        paths=tuple(paths),
        nondescriptive_terms=_terms(nondescriptive),
        deprioritized_terms=_terms(deprioritized),
    )


def load_scene_config(path: Path | None = None) -> SceneConfig:
    path = path or Path(get_settings().catalog_dir) / "scenes.toml"
    return parse_scene_config(path.read_text())
