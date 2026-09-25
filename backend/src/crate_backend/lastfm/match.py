"""Exact normalized matching of Crate albums against Last.fm responses.

Exact-only by design: a wrong match would silently corrupt the popularity
signal, which is worse than a missing one.
"""

import unicodedata


def normalize(value: str) -> str:
    """Lowercase, strip diacritics and punctuation, collapse whitespace."""
    decomposed = unicodedata.normalize("NFKD", value)
    without_diacritics = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    words_only = "".join(ch if ch.isalnum() else " " for ch in without_diacritics)
    return " ".join(words_only.lower().split())


def verify_match(
    sent_artist: str, sent_title: str, returned_artist: str, returned_title: str
) -> bool:
    return normalize(sent_artist) == normalize(returned_artist) and normalize(
        sent_title
    ) == normalize(returned_title)
