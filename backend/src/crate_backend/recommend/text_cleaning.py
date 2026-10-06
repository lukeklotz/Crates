"""Prepare genre/tag terms and Wikipedia article text for the TF-IDF
recommender (Phase 4, Milestone 2).

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md
"""

import re
import unicodedata
from collections.abc import Iterable

# Top-level sections that list facts (tracks, chart positions) or point
# elsewhere instead of describing the music. Matched against the normalized
# heading; subsections go with their parent. The spec's list plus spelling
# variants found in the stored articles (2026-10-06).
DROPPED_SECTIONS = frozenset(
    {
        "track listing",
        "track listings",
        "charts",
        "weekly charts",
        "year end charts",
        "chart positions",
        "charts and certifications",
        "certifications",
        "certifications and sales",
        "release history",
        "references",
        "notes",
        "sources",
        "bibliography",
        "further reading",
        "external links",
        "see also",
        "accolades",
        "awards",
        "sales",
    }
)

# Credits sections: shared musicians and producers link albums, so these are
# kept, but only their "Name – roles" lines with a musical or production role.
PERSONNEL_SECTIONS = frozenset({"personnel", "credits", "credits and personnel"})

# Crew roles that say nothing about the music. The most-credited names in the
# stored articles are mastering engineers (Bob Ludwig on 226 albums), which
# would otherwise link unrelated albums. Matched as substrings of each role.
CREW_ROLE_WORDS = (
    "master",
    "engineer",
    "photo",
    "design",
    "art direction",
    "artwork",
    "illustration",
    "layout",
    "liner notes",
    "cover",
)

# "== Heading ==" (top level) or deeper "=== Subheading ===".
_HEADING = re.compile(r"^(={2,})\s*(.*?)\s*\1\s*$")
# "Name – role, role and role" (en dash, em dash or spaced hyphen).
_CREDIT_LINE = re.compile(r"^(.+?)\s[–—-]\s(.+)$")
_ROLE_SEPARATORS = re.compile(r",|;|&|\band\b")


def normalize_term(name: str) -> str:
    """One spelling per term: "Post-Bop" and "post bop" become "post bop"."""
    name = unicodedata.normalize("NFKC", name).lower()
    name = name.replace("-", " ").replace("_", " ").replace("&", " and ")
    return " ".join(name.split())


def merge_term_votes(pairs: Iterable[tuple[str, int]]) -> dict[str, int]:
    """Normalize (name, vote count) pairs from an album's genres and tags.
    When several names normalize to the same term, the largest count wins."""
    merged: dict[str, int] = {}
    for name, votes in pairs:
        term = normalize_term(name)
        if term:
            merged[term] = max(votes, merged.get(term, votes))
    return merged


def clean_article(text: str, *, drop_reception: bool = False, drop_personnel: bool = False) -> str:
    """Article body text without the dropped sections, crew-only credit lines
    or any heading lines. The flags are evaluation variants:
    `drop_reception` drops every top-level section whose heading contains
    the word "reception"; `drop_personnel` drops credits sections entirely."""
    kept: list[str] = []
    section = "keep"
    for line in text.splitlines():
        match = _HEADING.match(line)
        if match is None:
            if section == "keep" or (section == "credits" and _is_musical_credit(line)):
                kept.append(line)
            continue
        if len(match.group(1)) == 2:
            section = _section_kind(normalize_term(match.group(2)), drop_reception, drop_personnel)
    return "\n".join(kept).strip()


def _section_kind(heading: str, drop_reception: bool, drop_personnel: bool) -> str:
    """Classify a top-level section: keep, drop, or credits (musical credit lines only)."""
    if heading in DROPPED_SECTIONS or (drop_reception and "reception" in heading.split()):
        return "drop"
    if heading in PERSONNEL_SECTIONS:
        return "drop" if drop_personnel else "credits"
    return "keep"


def _is_musical_credit(line: str) -> bool:
    """A "Name – roles" line with at least one role that isn't crew work.
    Other lines in credits sections ("Credits adapted from liner notes.")
    are boilerplate and dropped."""
    match = _CREDIT_LINE.match(line.strip())
    if match is None:
        return False
    roles = [r.strip().lower() for r in _ROLE_SEPARATORS.split(match.group(2)) if r.strip()]
    return any(not any(word in role for word in CREW_ROLE_WORDS) for role in roles)
