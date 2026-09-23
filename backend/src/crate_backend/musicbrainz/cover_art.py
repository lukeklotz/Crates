"""Rate-limited existence check against the Cover Art Archive.

Requests the release group's /front URL without following its redirect, so
checking ~25,000 albums doesn't download ~25,000 full-size images.
"""

import asyncio
from collections.abc import AsyncIterator

import httpx

BASE_URL = "https://coverartarchive.org"
REQUEST_INTERVAL_SECONDS = 1.0
MAX_RETRIES = 5
INITIAL_BACKOFF_SECONDS = 1.0
MAX_BACKOFF_SECONDS = 60.0
_ART_EXISTS_STATUS_CODES = frozenset({200, 301, 302, 303, 307, 308})
_RETRYABLE_STATUS_CODES = frozenset({429, 500, 502, 503, 504})

# Module-level so tests can replace waiting without patching asyncio globally.
_sleep = asyncio.sleep


def front_cover_url(release_group_mbid: str) -> str:
    return f"{BASE_URL}/release-group/{release_group_mbid}/front"


async def fetch_cover_art_url(client: httpx.AsyncClient, release_group_mbid: str) -> str | None:
    """The front-cover URL if the release group has art, else None. Retries
    rate limiting, server errors and network errors; never raises."""
    url = front_cover_url(release_group_mbid)
    backoff = INITIAL_BACKOFF_SECONDS
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = await client.get(url, follow_redirects=False)
        except httpx.TransportError:
            pass
        else:
            if response.status_code in _ART_EXISTS_STATUS_CODES:
                return url
            if response.status_code not in _RETRYABLE_STATUS_CODES:
                return None
        if attempt < MAX_RETRIES:
            await _sleep(backoff)
            backoff = min(backoff * 2, MAX_BACKOFF_SECONDS)
    return None


async def iter_cover_art(
    client: httpx.AsyncClient, release_group_mbids: list[str]
) -> AsyncIterator[tuple[str, str | None]]:
    """Yield (mbid, url_or_none) one at a time, at most one request per
    REQUEST_INTERVAL_SECONDS, so callers can save progress as they go."""
    for mbid in release_group_mbids:
        yield mbid, await fetch_cover_art_url(client, mbid)
        await _sleep(REQUEST_INTERVAL_SECONDS)
