"""Pure filter/rank/resolve logic over parsed MusicBrainz dump records.
No I/O, so it's unit-testable against small synthetic record lists."""

import heapq
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any

ALLOWED_SECONDARY_TYPES = frozenset({"Live"})
ARTIST_RELATIONSHIP_ALLOWLIST = frozenset({"member of band", "collaboration"})


@dataclass
class CandidateAlbum:
    musicbrainz_id: str
    title: str
    first_release_date: str | None
    artist_credit: list[dict[str, Any]]
    genres: list[dict[str, Any]]
    tags: list[dict[str, Any]]

    @property
    def tag_vote_total(self) -> int:
        return sum(tag.get("count", 0) for tag in self.tags)


@dataclass
class ResolvedArtistRelationship:
    related_artist_id: str
    related_artist_name: str
    relationship_type: str
    direction: str


@dataclass
class ResolvedArtist:
    musicbrainz_id: str
    name: str
    relationships: list[ResolvedArtistRelationship] = field(default_factory=list)


def release_year(first_release_date: str | None) -> int | None:
    year = (first_release_date or "")[:4]
    # isascii() too: str.isdigit() accepts characters like "¹" that int() rejects.
    return int(year) if len(year) == 4 and year.isascii() and year.isdigit() else None


def is_catalog_eligible(record: dict[str, Any]) -> bool:
    if record.get("primary-type") != "Album":
        return False
    if not all(t in ALLOWED_SECONDARY_TYPES for t in record.get("secondary-types") or []):
        return False
    # The candidate set is fixed before the artist pass runs, so this bar can
    # only use release-group-level data.
    return bool(record.get("genres")) or bool(record.get("tags"))


def to_candidate(record: dict[str, Any]) -> CandidateAlbum:
    return CandidateAlbum(
        musicbrainz_id=record["id"],
        title=record["title"],
        first_release_date=record.get("first-release-date") or None,
        artist_credit=record.get("artist-credit") or [],
        genres=record.get("genres") or [],
        tags=record.get("tags") or [],
    )


def filter_and_rank_release_groups(
    records: Iterable[dict[str, Any]], target_size: int
) -> list[CandidateAlbum]:
    """The `target_size` eligible release groups with the most tag votes,
    highest first. Holds at most `target_size` candidates in memory, since
    `records` is a single pass over a multi-million-row dump."""
    candidates = (to_candidate(r) for r in records if is_catalog_eligible(r))
    return heapq.nlargest(target_size, candidates, key=lambda c: c.tag_vote_total)


def artist_ids_in_credits(candidates: Iterable[CandidateAlbum]) -> set[str]:
    return {
        credit["artist"]["id"]
        for candidate in candidates
        for credit in candidate.artist_credit
        if (credit.get("artist") or {}).get("id")
    }


def _to_resolved_artist(record: dict[str, Any]) -> ResolvedArtist:
    relationships = [
        ResolvedArtistRelationship(
            related_artist_id=relation["artist"]["id"],
            related_artist_name=relation["artist"].get("name") or "",
            relationship_type=relation["type"],
            direction=relation.get("direction") or "forward",
        )
        for relation in record.get("relations") or []
        if relation.get("type") in ARTIST_RELATIONSHIP_ALLOWLIST
        and (relation.get("artist") or {}).get("id")
    ]
    return ResolvedArtist(
        musicbrainz_id=record["id"], name=record["name"], relationships=relationships
    )


def resolve_artists(
    records: Iterable[dict[str, Any]], wanted_ids: set[str]
) -> dict[str, ResolvedArtist]:
    """Resolve the wanted artists from a single pass over the artist dump.
    IDs never seen in the dump are simply absent from the result."""
    resolved: dict[str, ResolvedArtist] = {}
    remaining = set(wanted_ids)
    for record in records:
        if not remaining:
            break
        if record.get("id") in remaining:
            resolved[record["id"]] = _to_resolved_artist(record)
            remaining.discard(record["id"])
    return resolved
