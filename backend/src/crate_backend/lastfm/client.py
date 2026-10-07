"""Rate-limited client for Last.fm's album.getInfo endpoint, mirroring
musicbrainz/cover_art.py's retry/backoff shape and constants."""

import asyncio
from enum import Enum
from typing import NamedTuple

import httpx

BASE_URL = "https://ws.audioscrobbler.com/2.0/"
REQUEST_INTERVAL_SECONDS = 1.0
MAX_RETRIES = 5
INITIAL_BACKOFF_SECONDS = 1.0
MAX_BACKOFF_SECONDS = 60.0
_RETRYABLE_STATUS_CODES = frozenset({429, 500, 502, 503, 504})

# Module-level so tests can replace waiting without patching asyncio globally.
_sleep = asyncio.sleep


class FetchOutcome(Enum):
    FOUND = "found"
    NOT_FOUND = "not_found"
    FAILED = "failed"


class AlbumInfoResult(NamedTuple):
    outcome: FetchOutcome
    listeners: int | None = None
    artist: str | None = None
    title: str | None = None


class LastfmKeyRejected(Exception):
    """Last.fm refused the API key. Every later request would fail the same
    way, so callers must stop rather than record albums as unmatched."""


# Last.fm error codes (https://www.last.fm/api/errorcodes).
_NOT_FOUND_ERRORS = frozenset({6})
_KEY_ERRORS = frozenset({4, 9, 10, 26})
_TRANSIENT_ERRORS = frozenset({8, 11, 16, 29})


class _Retry(Exception):
    pass


def _classify(response: httpx.Response) -> AlbumInfoResult:
    """Turn one response into a result. Raises _Retry for transient failures
    and LastfmKeyRejected for key problems. Only a response Last.fm means as
    "no such album" becomes NOT_FOUND; anything unrecognized is FAILED, so
    the album is retried on a later run instead of recorded as unmatched."""
    if response.status_code in _RETRYABLE_STATUS_CODES:
        raise _Retry
    try:
        body = response.json()
    except ValueError:
        body = None
    error = body.get("error") if isinstance(body, dict) else None

    if response.status_code in (401, 403) or error in _KEY_ERRORS:
        message = body.get("message") if isinstance(body, dict) else None
        raise LastfmKeyRejected(message or f"HTTP {response.status_code}")
    if error in _TRANSIENT_ERRORS:
        raise _Retry
    if error in _NOT_FOUND_ERRORS or (response.status_code == 404 and error is None):
        return AlbumInfoResult(FetchOutcome.NOT_FOUND)

    album = body.get("album") if isinstance(body, dict) else None
    if response.status_code != 200 or not isinstance(album, dict):
        return AlbumInfoResult(FetchOutcome.FAILED)
    artist, title = album.get("artist"), album.get("name")
    try:
        listeners = int(album["listeners"])
    except (KeyError, TypeError, ValueError):
        return AlbumInfoResult(FetchOutcome.NOT_FOUND)
    if not isinstance(artist, str) or not isinstance(title, str):
        return AlbumInfoResult(FetchOutcome.NOT_FOUND)
    return AlbumInfoResult(FetchOutcome.FOUND, listeners=listeners, artist=artist, title=title)


# Last.fm files curly-quoted and Unicode-hyphenated spellings as separate,
# nearly empty entries ("Can’t Slow Down": 564 listeners; "Can't Slow
# Down": 411,998), so names are sent with plain ASCII punctuation. Dashes
# are left alone: titles like "Float Along – Fill Your Lungs" match as is.
_ASCII_PUNCTUATION = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "‐": "-", "‑": "-"})


def _lastfm_spelling(name: str) -> str:
    return name.translate(_ASCII_PUNCTUATION)


async def fetch_album_info(
    client: httpx.AsyncClient, api_key: str, artist_name: str, album_title: str
) -> AlbumInfoResult:
    """Look up an album by artist and title.

    NOT_FOUND is a definitive answer from Last.fm. FAILED means retries
    were exhausted or the response was unrecognizable; callers should retry
    the album later. Raises LastfmKeyRejected if the key is refused.
    """
    params = {
        "method": "album.getinfo",
        "api_key": api_key,
        "artist": _lastfm_spelling(artist_name),
        "album": _lastfm_spelling(album_title),
        "format": "json",
    }
    backoff = INITIAL_BACKOFF_SECONDS
    for attempt in range(MAX_RETRIES + 1):
        try:
            return _classify(await client.get(BASE_URL, params=params))
        except (httpx.TransportError, _Retry):
            pass
        if attempt < MAX_RETRIES:
            await _sleep(backoff)
            backoff = min(backoff * 2, MAX_BACKOFF_SECONDS)
    return AlbumInfoResult(FetchOutcome.FAILED)
