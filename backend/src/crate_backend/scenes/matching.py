"""Place an album in a catalog scene from its genre/tag votes and first
release year. Pure functions, shared by the dump profile, the batch
selector and the coverage and path-reach reports.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

import math
import re
from dataclasses import dataclass
from typing import Any

from crate_backend.recommend.text_cleaning import merge_term_votes
from crate_backend.scenes.config import Scene, SceneConfig

# "1995", "90s", "1990s": the year already places the album in time.
_YEAR_TERM = re.compile(r"^\d{2,4}s?$")


@dataclass(frozen=True)
class SceneMatch:
    home: str
    evidence: float
    # True when only the home scene's broad terms ("rock", "jazz") matched.
    broad_only: bool
    matched_terms: tuple[str, ...]
    # Scenes next to home on a path whose terms the album also carries.
    connects_to: tuple[str, ...]


def descriptive_terms(
    genres: list[dict[str, Any]], tags: list[dict[str, Any]], config: SceneConfig
) -> dict[str, int]:
    """Normalized term -> votes, keeping only positive votes on terms that
    describe the music (not "seen live", not a year or decade)."""
    merged = merge_term_votes(
        (entry.get("name") or "", entry.get("count", 0)) for entry in [*genres, *tags]
    )
    return {
        term: votes
        for term, votes in merged.items()
        if votes > 0 and term not in config.nondescriptive_terms and not _YEAR_TERM.match(term)
    }


def _matched(terms: dict[str, int], scene: Scene) -> list[str]:
    return sorted(t for t in terms if t in scene.terms or t in scene.broad_terms)


def scene_evidence(terms: dict[str, int], scene: Scene, broad_weight: float) -> float:
    return sum(
        (1.0 if term in scene.terms else broad_weight) * math.log2(1 + terms[term])
        for term in _matched(terms, scene)
    )


def _terms_fit(terms: dict[str, int], scene: Scene) -> bool:
    """Every rule except the year window."""
    if scene.requires_any and not any(t in terms for t in scene.requires_any):
        return False
    if any(t in terms for t in scene.exclude_terms):
        return False
    return len(_matched(terms, scene)) >= scene.min_matched_terms


def classify(terms: dict[str, int], year: int | None, config: SceneConfig) -> SceneMatch | None:
    """The album's home scene (highest evidence; ties go to the scene listed
    first), or None when no scene's year window and term rules fit."""
    if year is None:
        return None
    best: tuple[Scene, float] | None = None
    for scene in config.scenes:
        if not scene.holds_year(year) or not _terms_fit(terms, scene):
            continue
        evidence = scene_evidence(terms, scene, config.settings.broad_weight)
        if best is None or evidence > best[1]:
            best = (scene, evidence)
    if best is None:
        return None
    home, evidence = best
    matched = _matched(terms, home)
    # A neighbor's year window is ignored: a 1983 funk/electro record still
    # connects funk to early hip hop. Its broad terms alone don't count, or
    # every album tagged "electronic" would connect every electronic scene.
    connects_to = sorted(
        neighbor
        for neighbor in config.neighbors(home.id)
        if _terms_fit(terms, config.scene(neighbor))
        and any(t in config.scene(neighbor).terms for t in terms)
    )
    return SceneMatch(
        home=home.id,
        evidence=evidence,
        broad_only=not any(t in home.terms for t in matched),
        matched_terms=tuple(matched),
        connects_to=tuple(connects_to),
    )
