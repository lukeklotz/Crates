"""Pick a batch of albums to add to the catalog, scene by scene.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

from crate_backend.scenes.config import SelectionSettings
from crate_backend.scenes.pool import PoolAlbum


def is_deep_cut(album: PoolAlbum, settings: SelectionSettings) -> bool:
    """Less famous but well described: few votes in total, several
    descriptive terms, and at least two of them scene terms. Tag votes stand
    in for fame because albums outside the catalog have no Last.fm data."""
    return (
        album.match is not None
        and album.total_votes <= settings.deep_cut_max_votes
        and album.n_terms >= settings.deep_cut_min_terms
        and len(album.match.matched_terms) >= settings.deep_cut_min_scene_terms
    )
