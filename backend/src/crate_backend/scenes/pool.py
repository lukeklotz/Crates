"""The scene pool: every release group in the dump that fits Crate's album
rules and has at least one descriptive term, stored as raw records in a
gzip JSON-lines file next to the dumps.

Scene matches are not stored. They are recomputed from scenes.toml on every
read, so retuning scenes never needs another pass over the dump.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

import gzip
import json
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from crate_backend.musicbrainz.extract import is_catalog_eligible, release_year
from crate_backend.scenes.config import SceneConfig
from crate_backend.scenes.matching import SceneMatch, classify, descriptive_terms

# What ingestion and matching need; everything else in a dump record is dropped.
POOL_FIELDS = (
    "id",
    "title",
    "primary-type",
    "secondary-types",
    "first-release-date",
    "artist-credit",
    "genres",
    "tags",
)


@dataclass(frozen=True)
class PoolAlbum:
    musicbrainz_id: str
    title: str
    artist_name: str
    year: int | None
    is_live: bool
    # The first credited artist's MBID; None when the credit has none.
    primary_artist_id: str | None
    terms: dict[str, int]
    match: SceneMatch | None
    record: dict[str, Any]

    @property
    def total_votes(self) -> int:
        return sum(self.terms.values())

    @property
    def n_terms(self) -> int:
        return len(self.terms)


def _credit_name(artist_credit: list[dict[str, Any]]) -> str:
    return "".join(
        (credit.get("name") or "") + (credit.get("joinphrase") or "") for credit in artist_credit
    )


def to_pool_album(record: dict[str, Any], config: SceneConfig) -> PoolAlbum | None:
    """None unless the record is a catalog-eligible album with at least one
    descriptive term."""
    if not is_catalog_eligible(record):
        return None
    terms = descriptive_terms(record.get("genres") or [], record.get("tags") or [], config)
    if not terms:
        return None
    artist_credit = record.get("artist-credit") or []
    first_artist = (artist_credit[0].get("artist") or {}) if artist_credit else {}
    year = release_year(record.get("first-release-date"))
    return PoolAlbum(
        musicbrainz_id=record["id"],
        title=record.get("title") or "",
        artist_name=_credit_name(artist_credit),
        year=year,
        is_live="Live" in (record.get("secondary-types") or []),
        primary_artist_id=first_artist.get("id") or None,
        terms=terms,
        match=classify(terms, year, config),
        record=record,
    )


def write_pool(records: Iterable[dict[str, Any]], path: Path) -> int:
    """Write the POOL_FIELDS of each record; returns how many were written.
    Writes to a temporary file first so an interrupted run keeps the old pool."""
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(path.name + ".partial")
    written = 0
    with gzip.open(partial, "wt", encoding="utf-8") as out:
        for record in records:
            kept = {field: record[field] for field in POOL_FIELDS if field in record}
            out.write(json.dumps(kept, ensure_ascii=False) + "\n")
            written += 1
    partial.replace(path)
    return written


def read_raw_pool(path: Path) -> Iterator[dict[str, Any]]:
    with gzip.open(path, "rt", encoding="utf-8") as lines:
        for line in lines:
            if line.strip():
                yield json.loads(line)


def read_pool(path: Path, config: SceneConfig) -> Iterator[PoolAlbum]:
    for record in read_raw_pool(path):
        album = to_pool_album(record, config)
        if album is not None:
            yield album
