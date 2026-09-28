"""Rate-limited clients for Wikidata (album item -> English article title)
and English Wikipedia (article plain text), mirroring lastfm/client.py's
retry/backoff shape and constants."""

import asyncio
from enum import Enum
from typing import Any, NamedTuple

import httpx

WIKIDATA_API_URL = "https://www.wikidata.org/w/api.php"
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"
REQUEST_INTERVAL_SECONDS = 0.25
MAX_WIKIDATA_IDS_PER_REQUEST = 50
MAX_RETRIES = 5
INITIAL_BACKOFF_SECONDS = 1.0
MAX_BACKOFF_SECONDS = 60.0
_RETRYABLE_STATUS_CODES = frozenset({429, 500, 502, 503, 504})

# Module-level so tests can replace waiting without patching asyncio globally.
_sleep = asyncio.sleep


def user_agent(contact_email: str) -> str:
    """Wikimedia's User-Agent policy asks API clients to identify themselves
    and give a way to reach the operator; anonymous clients get blocked."""
    return f"CrateBackend/0.1 (album recommendation research; {contact_email})"


class FetchOutcome(Enum):
    FOUND = "found"
    MISSING = "missing"
    FAILED = "failed"


class ArticleResult(NamedTuple):
    outcome: FetchOutcome
    title: str | None = None
    revision_id: int | None = None
    text: str | None = None
    redirected: bool = False


async def _get_json(
    client: httpx.AsyncClient, url: str, params: dict[str, str]
) -> dict[str, Any] | None:
    """GET with retry/backoff on 429/5xx and network errors. Returns the
    body as a JSON object, or None when retries run out or the response is
    anything else (other status, HTML, non-object JSON)."""
    backoff = INITIAL_BACKOFF_SECONDS
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = await client.get(url, params=params)
        except httpx.TransportError:
            response = None
        if response is not None and response.status_code not in _RETRYABLE_STATUS_CODES:
            if response.status_code != 200:
                return None
            try:
                body = response.json()
            except ValueError:
                return None
            return body if isinstance(body, dict) else None
        if attempt < MAX_RETRIES:
            await _sleep(backoff)
            backoff = min(backoff * 2, MAX_BACKOFF_SECONDS)
    return None


def _sitelink_title(entity: dict[str, Any]) -> str | None:
    if "missing" in entity:
        return None
    sitelink = (entity.get("sitelinks") or {}).get("enwiki")
    title = sitelink.get("title") if isinstance(sitelink, dict) else None
    return title if isinstance(title, str) and title else None


async def resolve_enwiki_titles(
    client: httpx.AsyncClient, qids: list[str]
) -> dict[str, str | None]:
    """Map up to 50 Wikidata ids to their English Wikipedia article titles,
    with None for an item that has no English article or doesn't exist.

    An id missing from the result could not be resolved (retries exhausted,
    an unrecognized response, or a response silent about it); callers
    should retry it later.
    """
    if len(qids) > MAX_WIKIDATA_IDS_PER_REQUEST:
        raise ValueError(f"at most {MAX_WIKIDATA_IDS_PER_REQUEST} ids per request")
    answers: dict[str, str | None] = {}
    pending = list(dict.fromkeys(qids))
    while pending:
        body = await _get_json(
            client,
            WIKIDATA_API_URL,
            {
                "action": "wbgetentities",
                "ids": "|".join(pending),
                "props": "sitelinks",
                "sitefilter": "enwiki",
                "format": "json",
            },
        )
        if body is None:
            return answers
        error = body.get("error")
        if isinstance(error, dict):
            unknown = error.get("id")
            if error.get("code") == "no-such-entity" and unknown in pending:
                # One unknown id rejects the whole request: answer it and
                # ask again for the rest.
                answers[unknown] = None
                pending.remove(unknown)
                continue
            return answers
        entities = body.get("entities")
        if not isinstance(entities, dict):
            return answers
        for key, entity in entities.items():
            if isinstance(entity, dict):
                requested = (entity.get("redirects") or {}).get("from", key)
                answers[requested] = _sitelink_title(entity)
        # Ids the response is silent about stay unresolved, to be retried.
        return answers
    return answers


async def fetch_article(client: httpx.AsyncClient, title: str) -> ArticleResult:
    """Fetch one English Wikipedia article as plain text with "== Section =="
    headings, following redirects.

    MISSING is definitive (no such page, or an invalid title). FAILED means
    retries ran out or the response was unrecognizable; retry later. A page
    with an empty extract is FOUND with text None.
    """
    body = await _get_json(
        client,
        WIKIPEDIA_API_URL,
        {
            "action": "query",
            "prop": "extracts|info",
            "explaintext": "1",
            "exsectionformat": "wiki",
            "redirects": "1",
            "titles": title,
            "format": "json",
            "formatversion": "2",
        },
    )
    query = body.get("query") if body else None
    pages = query.get("pages") if isinstance(query, dict) else None
    if not isinstance(pages, list) or len(pages) != 1 or not isinstance(pages[0], dict):
        return ArticleResult(FetchOutcome.FAILED)
    page = pages[0]
    if page.get("missing") or page.get("invalid"):
        return ArticleResult(FetchOutcome.MISSING)
    final_title = page.get("title")
    if not isinstance(final_title, str):
        return ArticleResult(FetchOutcome.FAILED)
    extract = page.get("extract")
    revision = page.get("lastrevid")
    return ArticleResult(
        FetchOutcome.FOUND,
        title=final_title,
        revision_id=revision if isinstance(revision, int) else None,
        text=extract if isinstance(extract, str) and extract.strip() else None,
        redirected=bool(query.get("redirects")),
    )
