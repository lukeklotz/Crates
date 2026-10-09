"""Ordering rule shared by the TF-IDF and embedding recommenders."""

import uuid

import numpy as np


def rank_rows(
    titles: list[str],
    album_ids: list[uuid.UUID],
    rounded: np.ndarray,
    seed_rows: list[int],
    limit: int,
) -> list[int]:
    """Rows ordered by rounded score desc, then title, then album id. Seeds
    and rows scoring 0 or less are never returned."""
    rounded = rounded.copy()
    rounded[seed_rows] = 0.0
    candidates = np.flatnonzero(rounded > 0)
    if len(candidates) > limit:
        # Keep everything tied with the limit-th score so the title/id
        # tie-break, not np.partition, decides who makes the cut.
        cutoff = np.partition(rounded[candidates], -limit)[-limit]
        candidates = candidates[rounded[candidates] >= cutoff]
    ordered = sorted(
        (int(row) for row in candidates),
        key=lambda row: (-rounded[row], titles[row], str(album_ids[row])),
    )
    return ordered[:limit]
