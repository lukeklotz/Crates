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


def _parse(body: object) -> AlbumInfoResult:
    album = body.get("album") if isinstance(body, dict) else None
    if not isinstance(album, dict):
        return AlbumInfoResult(FetchOutcome.NOT_FOUND)
    try:
        listeners = int(album["listeners"])
    except (KeyError, TypeError, ValueError):
        return AlbumInfoResult(FetchOutcome.NOT_FOUND)
    return AlbumInfoResult(
        FetchOutcome.FOUND,
        listeners=listeners,
        artist=album.get("artist") or "",
        title=album.get("name") or "",
    )


async def fetch_album_info(
    client: httpx.AsyncClient, api_key: str, artist_name: str, album_title: str
) -> AlbumInfoResult:
    """Look up an album by artist and title. Never raises.

    NOT_FOUND is a definitive answer from Last.fm (404, error body, or no
    listener count). FAILED means retries on rate limiting, server errors or
    network errors were exhausted; callers should retry the album later.
    """
    params = {
        "method": "album.getinfo",
        "api_key": api_key,
        "artist": artist_name,
        "album": album_title,
        "format": "json",
    }
    backoff = INITIAL_BACKOFF_SECONDS
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = await client.get(BASE_URL, params=params)
        except httpx.TransportError:
            pass
        else:
            if response.status_code not in _RETRYABLE_STATUS_CODES:
                if response.status_code != 200:
                    return AlbumInfoResult(FetchOutcome.NOT_FOUND)
                try:
                    return _parse(response.json())
                except ValueError:
                    return AlbumInfoResult(FetchOutcome.NOT_FOUND)
        if attempt < MAX_RETRIES:
            await _sleep(backoff)
            backoff = min(backoff * 2, MAX_BACKOFF_SECONDS)
    return AlbumInfoResult(FetchOutcome.FAILED)
