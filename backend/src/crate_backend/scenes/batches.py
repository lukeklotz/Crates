"""Catalog batch files: one JSON line per album picked for a batch, kept in
catalog/batches/ as the record of which albums each batch added.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from crate_backend.scenes.pool import PoolAlbum
from crate_backend.scenes.select import Pick


def batch_line(pick: Pick, album: PoolAlbum) -> dict[str, Any]:
    return {
        "musicbrainz_id": pick.musicbrainz_id,
        "title": album.title,
        "artist_name": album.artist_name,
        "year": album.year,
        "scene": pick.scene,
        "slice": pick.slice,
        "gain": round(pick.gain, 4),
        "live": album.is_live,
    }


def write_batch(lines: Iterable[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(line, ensure_ascii=False) + "\n" for line in lines))


def read_batch(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def read_batch_ids(path: Path) -> list[str]:
    return [line["musicbrainz_id"] for line in read_batch(path)]


def batch_memberships(batch_dir: Path) -> dict[str, set[str]]:
    """Batch name (file stem) -> the MusicBrainz IDs it added."""
    if not batch_dir.exists():
        return {}
    return {path.stem: set(read_batch_ids(path)) for path in sorted(batch_dir.glob("*.jsonl"))}
