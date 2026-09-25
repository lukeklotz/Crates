# Last.fm Popularity Signal Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give every album in Crate's catalog a validated popularity signal sourced from Last.fm, plus a separately-tracked internal "added to sandbox" counter, unblocking Phase 3's popularity baseline.

**Architecture:** A new `lastfm/` package (client, matcher, ingest, scoring) mirrors the existing `musicbrainz/` package's shape — rate-limited `httpx` client, pure matching logic, idempotent upsert into a new `PopularitySignal` table keyed by `album_id`. A batch script backfills the whole catalog and recomputes `Album.popularity` as each matched album's percentile rank of Last.fm listeners. A new authenticated endpoint increments the separate, unblended internal counter.

**Tech Stack:** Python 3.12, FastAPI, SQLAlchemy 2.0 (async), Alembic, httpx, pytest + pytest-asyncio, uv.

**Spec:** `docs/superpowers/specs/2026-09-24-lastfm-popularity-signal-design.md`

## Global Constraints

- Last.fm requests are paced at 1 request/second, with up to 5 retries on 429/5xx using exponential backoff from 1s doubling to a 60s cap — the same constants `musicbrainz/cover_art.py` already uses for the Cover Art Archive.
- Match verification is exact-normalized-string-equality only (lowercase, diacritics/punctuation stripped, whitespace collapsed) on both artist name and album title. No fuzzy/similarity matching.
- `lastfm_listeners` null means "no verified match found or not yet attempted," never "zero listeners."
- `lastfm_fetched_at` is set on every lookup attempt that gets a definitive answer (verified match, confirmed no-match, or a mismatch) — but is left unset when retries are exhausted (a transient failure), so the next backfill run retries it.
- `sandbox_add_count` and `lastfm_listeners` are never combined into a single score in this phase. `Album.popularity` is derived from `lastfm_listeners` only, and is written only by the score-recomputation step — never directly by the client, ingest, or the add-to-sandbox endpoint.
- `CRATE_LASTFM_API_KEY` is read from environment/`.env` via `core/config.py`; it must never be hardcoded or committed.
- Tests use the project's existing `db_session` fixture (`tests/conftest.py`), which runs against a real local Postgres inside a rolled-back transaction. Before running any test in this plan, ensure Postgres is up (`docker compose up -d db` from the repo root) and migrations are current (`cd backend && uv run alembic upgrade head`).

## Review Focus

- An album with no `artist_name` must never trigger a Last.fm HTTP request, and must not get a `PopularitySignal` row created for that reason alone.
- A Last.fm response that comes back for the *wrong* album (mismatched artist or title after normalization) must set `lastfm_fetched_at` but leave `lastfm_listeners` null — distinct from a transient failure, which must leave `lastfm_fetched_at` unset entirely.
- Re-running the backfill script must skip every album that already has a `lastfm_fetched_at` set, regardless of whether that attempt found listeners or not.
- Two albums with identical `lastfm_listeners` values must receive the same percentile-rank score, not an arbitrary order-dependent one.
- `POST /albums/{album_id}/add-to-sandbox` must return 401 before touching the database when unauthenticated, and 404 for an unknown `album_id` without creating any `PopularitySignal` or `Event` row.

---

### Task 1: `PopularitySignal` model and migration

**Files:**
- Create: `backend/src/crate_backend/models/popularity.py`
- Modify: `backend/src/crate_backend/models/__init__.py`
- Test: `backend/tests/test_models.py`
- Create (generated): `backend/migrations/versions/<hash>_add_popularity_signals_table.py`

**Interfaces:**
- Produces: `PopularitySignal` (fields: `id`, `album_id` (unique FK to `albums.id`), `lastfm_listeners: int | None`, `lastfm_matched_artist: str | None`, `lastfm_matched_title: str | None`, `lastfm_fetched_at: datetime | None`, `sandbox_add_count: int` (default 0), `album` relationship). Consumed by every later task.

- [ ] **Step 1: Write the failing test**

Add to `backend/tests/test_models.py` (open the file first to match its existing style; append this test):

```python
async def test_popularity_signal_defaults_and_relationship(db_session):
    from crate_backend.models.catalog import Album
    from crate_backend.models.popularity import PopularitySignal

    album = Album(title="Test Album", artist_name="Test Artist")
    db_session.add(album)
    await db_session.flush()

    signal = PopularitySignal(album_id=album.id)
    db_session.add(signal)
    await db_session.commit()
    await db_session.refresh(signal)

    assert signal.lastfm_listeners is None
    assert signal.lastfm_fetched_at is None
    assert signal.sandbox_add_count == 0
    assert signal.album_id == album.id
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd backend && uv run pytest tests/test_models.py::test_popularity_signal_defaults_and_relationship -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.models.popularity'`

- [ ] **Step 3: Write the model**

Create `backend/src/crate_backend/models/popularity.py`:

```python
import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.catalog import Album


class PopularitySignal(UUIDPkMixin, TimestampMixin, Base):
    """Raw popularity signals for one album, kept separate by source so
    each can be inspected, re-verified, or used independently. Two signals
    live here today and are never blended into one score:

    - lastfm_listeners: Last.fm's verified unique-listener count. Null
      means no verified match was found, or no attempt has succeeded yet
      -- never "zero listeners".
    - sandbox_add_count: how many times any user has added this album to
      their sandbox in Crate. Always present, starts at 0. Tracked from
      now on but not currently used in Album.popularity.

    Album.popularity is derived from lastfm_listeners only (see
    crate_backend.lastfm.scoring) and must not be written here.
    """

    __tablename__ = "popularity_signals"

    album_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("albums.id"), unique=True, index=True
    )

    lastfm_listeners: Mapped[int | None] = mapped_column(nullable=True)
    lastfm_matched_artist: Mapped[str | None] = mapped_column(String(255), nullable=True)
    lastfm_matched_title: Mapped[str | None] = mapped_column(String(500), nullable=True)
    # Set on every attempt that reaches a definitive answer (match, no
    # match, or mismatch); left null when retries are exhausted, so the
    # next backfill run retries this album.
    lastfm_fetched_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    sandbox_add_count: Mapped[int] = mapped_column(default=0)

    album: Mapped["Album"] = relationship()
```

- [ ] **Step 4: Register the model**

Modify `backend/src/crate_backend/models/__init__.py`:

```python
from crate_backend.models.artist_relationship import ArtistRelationship
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Artist, Genre, Tag
from crate_backend.models.event import Event
from crate_backend.models.group import AlbumGroup, GroupAlbumMembership, GroupSettings
from crate_backend.models.popularity import PopularitySignal
from crate_backend.models.rating import Descriptor, Rating
from crate_backend.models.recommendation import ModelVersion, Recommendation, RecommendationRun
from crate_backend.models.user import User
from crate_backend.models.workspace import CanvasAlbumInstance, Workspace

__all__ = [
    "Album",
    "AlbumGenre",
    "AlbumGroup",
    "AlbumTag",
    "Artist",
    "ArtistRelationship",
    "CanvasAlbumInstance",
    "Descriptor",
    "Event",
    "Genre",
    "GroupAlbumMembership",
    "GroupSettings",
    "ModelVersion",
    "PopularitySignal",
    "Rating",
    "Recommendation",
    "RecommendationRun",
    "Tag",
    "User",
    "Workspace",
]
```

- [ ] **Step 5: Generate and review the migration**

Run: `cd backend && uv run alembic revision --autogenerate -m "add popularity signals table"`

Open the generated file in `backend/migrations/versions/` and confirm it creates `popularity_signals` with: `id` (UUID PK), `album_id` (UUID, FK to `albums.id`, unique index), `lastfm_listeners` (Integer, nullable), `lastfm_matched_artist` (String(255), nullable), `lastfm_matched_title` (String(500), nullable), `lastfm_fetched_at` (DateTime(timezone=True), nullable), `sandbox_add_count` (Integer, not null), `created_at`/`updated_at`. If autogenerate produces anything else (e.g. missing the unique constraint on `album_id`), edit the migration file by hand to match.

- [ ] **Step 6: Apply the migration**

Run: `cd backend && uv run alembic upgrade head`
Expected: no errors; `popularity_signals` table now exists in the local dev database.

- [ ] **Step 7: Run test to verify it passes**

Run: `cd backend && uv run pytest tests/test_models.py::test_popularity_signal_defaults_and_relationship -v`
Expected: PASS

- [ ] **Step 8: Commit**

```bash
cd backend
git add src/crate_backend/models/popularity.py src/crate_backend/models/__init__.py \
  migrations/versions/*_add_popularity_signals_table.py tests/test_models.py
git commit -m "feat: add PopularitySignal model and migration"
```

---

### Task 2: `CRATE_LASTFM_API_KEY` config setting

**Files:**
- Modify: `backend/src/crate_backend/core/config.py`
- Modify: `backend/.env` (already done — `CRATE_LASTFM_API_KEY` is already set locally; no action needed here beyond the code change)
- Test: `backend/tests/test_config.py` (create if it doesn't exist yet — check first)

**Interfaces:**
- Produces: `Settings.lastfm_api_key: str`, read via `get_settings().lastfm_api_key`. Consumed by Task 5 (ingest) and Task 7 (backfill script).

- [ ] **Step 1: Check whether a config test file already exists**

Run: `cd backend && ls tests/test_config.py 2>/dev/null || echo "no existing config test file"`

- [ ] **Step 2: Write the failing test**

Create (or append to) `backend/tests/test_config.py`:

```python
from crate_backend.core.config import Settings


def test_lastfm_api_key_reads_from_env(monkeypatch):
    monkeypatch.setenv("CRATE_LASTFM_API_KEY", "test-key-value")
    settings = Settings(_env_file=None)
    assert settings.lastfm_api_key == "test-key-value"
```

- [ ] **Step 3: Run test to verify it fails**

Run: `cd backend && uv run pytest tests/test_config.py::test_lastfm_api_key_reads_from_env -v`
Expected: FAIL with `pydantic_core._pydantic_core.ValidationError` or `AttributeError: 'Settings' object has no attribute 'lastfm_api_key'`

- [ ] **Step 4: Add the setting**

Modify `backend/src/crate_backend/core/config.py`, adding after `musicbrainz_target_catalog_size`:

```python
    # Last.fm popularity signal (Phase 3). Register a free key at
    # https://www.last.fm/api/account/create -- homepage/callback URL
    # fields on that form are unused by the read-only endpoints this
    # project calls and can be any placeholder value.
    lastfm_api_key: str = ""
```

- [ ] **Step 5: Run test to verify it passes**

Run: `cd backend && uv run pytest tests/test_config.py::test_lastfm_api_key_reads_from_env -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
cd backend
git add src/crate_backend/core/config.py tests/test_config.py
git commit -m "feat: add CRATE_LASTFM_API_KEY setting"
```

---

### Task 3: Artist/title normalization and match verification

**Files:**
- Create: `backend/src/crate_backend/lastfm/__init__.py` (empty)
- Create: `backend/src/crate_backend/lastfm/match.py`
- Test: `backend/tests/test_lastfm_match.py`

**Interfaces:**
- Produces: `normalize(value: str) -> str`, `verify_match(sent_artist: str, sent_title: str, returned_artist: str, returned_title: str) -> bool`. Consumed by Task 5 (`ingest.py`).

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_lastfm_match.py`:

```python
from crate_backend.lastfm.match import normalize, verify_match


def test_normalize_lowercases():
    assert normalize("Kid A") == "kid a"


def test_normalize_strips_diacritics():
    assert normalize("Beyoncé") == "beyonce"


def test_normalize_strips_punctuation_and_collapses_whitespace():
    assert normalize("Rock & Roll!!  Part  One") == "rock roll part one"


def test_verify_match_true_for_exact_match():
    assert verify_match("Radiohead", "Kid A", "Radiohead", "Kid A") is True


def test_verify_match_true_ignoring_case_and_diacritics():
    assert verify_match("Beyonce", "Lemonade", "Beyoncé", "Lemonade") is True


def test_verify_match_false_for_artist_mismatch():
    assert verify_match("Radiohead", "Kid A", "Thom Yorke", "Kid A") is False


def test_verify_match_false_for_title_mismatch():
    assert verify_match("Radiohead", "Kid A", "Radiohead", "OK Computer") is False
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_lastfm_match.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.lastfm'`

- [ ] **Step 3: Write the implementation**

Create `backend/src/crate_backend/lastfm/__init__.py` (empty file).

Create `backend/src/crate_backend/lastfm/match.py`:

```python
"""Normalization and verification for matching Crate album records
against Last.fm's album.getInfo responses. Exact-match only, by design
(spec: docs/superpowers/specs/2026-09-24-lastfm-popularity-signal-design.md)
-- a wrong match would silently corrupt a popularity signal, which is a
worse failure than a missing one."""

import unicodedata


def normalize(value: str) -> str:
    """Lowercase, strip diacritics and punctuation, collapse whitespace."""
    decomposed = unicodedata.normalize("NFKD", value)
    without_diacritics = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    letters_digits_and_spaces = "".join(
        ch if ch.isalnum() or ch.isspace() else " " for ch in without_diacritics
    )
    return " ".join(letters_digits_and_spaces.lower().split())


def verify_match(
    sent_artist: str, sent_title: str, returned_artist: str, returned_title: str
) -> bool:
    """True only if both artist name and album title match exactly after
    normalization."""
    return normalize(sent_artist) == normalize(returned_artist) and normalize(
        sent_title
    ) == normalize(returned_title)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_lastfm_match.py -v`
Expected: PASS (7 tests)

- [ ] **Step 5: Commit**

```bash
cd backend
git add src/crate_backend/lastfm/__init__.py src/crate_backend/lastfm/match.py tests/test_lastfm_match.py
git commit -m "feat: add Last.fm normalization and match verification"
```

---

### Task 4: Rate-limited Last.fm client

**Files:**
- Create: `backend/src/crate_backend/lastfm/client.py`
- Test: `backend/tests/test_lastfm_client.py`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: `FetchOutcome` (Enum: `FOUND`, `NOT_FOUND`, `FAILED`), `AlbumInfoResult` (NamedTuple: `outcome: FetchOutcome`, `listeners: int | None = None`, `artist: str | None = None`, `title: str | None = None`), `async fetch_album_info(client: httpx.AsyncClient, api_key: str, artist_name: str, album_title: str) -> AlbumInfoResult`. Consumed by Task 5 (`ingest.py`).

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_lastfm_client.py` (mirrors `tests/test_cover_art.py`'s structure exactly):

```python
import httpx
import pytest

from crate_backend.lastfm import client

pytestmark = pytest.mark.asyncio


@pytest.fixture
def sleeps(monkeypatch) -> list[float]:
    recorded: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        recorded.append(seconds)

    monkeypatch.setattr(client, "_sleep", fake_sleep)
    return recorded


def _client(responses: list) -> tuple[httpx.AsyncClient, list[httpx.Request]]:
    """Client whose transport returns (or raises) `responses` in order."""
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        item = responses[min(len(requests), len(responses)) - 1]
        if isinstance(item, Exception):
            raise item
        return item

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requests


def _found_response(listeners: int = 12345, artist: str = "Radiohead", title: str = "Kid A"):
    return httpx.Response(
        200,
        json={"album": {"name": title, "artist": artist, "listeners": str(listeners)}},
    )


def _not_found_response():
    return httpx.Response(200, json={"error": 6, "message": "Album not found"})


async def test_found_album_returns_listeners_artist_and_title(sleeps):
    ac, _ = _client([_found_response(listeners=999, artist="Radiohead", title="Kid A")])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert result.listeners == 999
    assert result.artist == "Radiohead"
    assert result.title == "Kid A"


async def test_error_body_means_not_found_without_retrying(sleeps):
    ac, requests = _client([_not_found_response()])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Nobody", "Nothing")
    assert result.outcome is client.FetchOutcome.NOT_FOUND
    assert len(requests) == 1


async def test_404_status_means_not_found_without_retrying(sleeps):
    ac, requests = _client([httpx.Response(404)])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Nobody", "Nothing")
    assert result.outcome is client.FetchOutcome.NOT_FOUND
    assert len(requests) == 1


async def test_429_retries_with_backoff_then_succeeds(sleeps):
    ac, requests = _client([httpx.Response(429), httpx.Response(429), _found_response()])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert len(requests) == 3
    assert sleeps == [1.0, 2.0]


async def test_network_error_is_retried(sleeps):
    ac, _ = _client([httpx.ConnectError("connection reset"), _found_response()])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND


async def test_gives_up_after_max_retries_and_reports_failed(sleeps):
    ac, requests = _client([httpx.Response(503)])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED
    assert len(requests) == client.MAX_RETRIES + 1
    assert sleeps == [1.0, 2.0, 4.0, 8.0, 16.0]


async def test_backoff_is_capped(monkeypatch, sleeps):
    monkeypatch.setattr(client, "MAX_RETRIES", 8)
    ac, _ = _client([httpx.Response(503)])
    async with ac:
        await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert max(sleeps) == client.MAX_BACKOFF_SECONDS
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_lastfm_client.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.lastfm.client'`

- [ ] **Step 3: Write the implementation**

Create `backend/src/crate_backend/lastfm/client.py`:

```python
"""Rate-limited client for Last.fm's album.getInfo endpoint.

Mirrors musicbrainz/cover_art.py's retry/backoff shape and constants.
"""

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


def _parse_found(body: dict) -> AlbumInfoResult:
    album = body.get("album")
    if not isinstance(album, dict) or "listeners" not in album:
        return AlbumInfoResult(FetchOutcome.NOT_FOUND)
    try:
        listeners = int(album["listeners"])
    except (TypeError, ValueError):
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
    """Query album.getInfo for `artist_name`/`album_title`. Retries rate
    limiting, server errors and network errors; never raises.

    FAILED means retries were exhausted (a transient failure -- callers
    should treat this album as not yet attempted and retry later).
    NOT_FOUND means Last.fm gave a definitive no-match answer (404, an
    error body, or a response with no listener count).
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
                    body = response.json()
                except ValueError:
                    return AlbumInfoResult(FetchOutcome.NOT_FOUND)
                return _parse_found(body)
        if attempt < MAX_RETRIES:
            await _sleep(backoff)
            backoff = min(backoff * 2, MAX_BACKOFF_SECONDS)
    return AlbumInfoResult(FetchOutcome.FAILED)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_lastfm_client.py -v`
Expected: PASS (7 tests)

- [ ] **Step 5: Commit**

```bash
cd backend
git add src/crate_backend/lastfm/client.py tests/test_lastfm_client.py
git commit -m "feat: add rate-limited Last.fm client"
```

---

### Task 5: Idempotent ingest into `PopularitySignal`

**Files:**
- Create: `backend/src/crate_backend/lastfm/ingest.py`
- Test: `backend/tests/test_lastfm_ingest.py`

**Interfaces:**
- Consumes: `crate_backend.lastfm.client.fetch_album_info`, `FetchOutcome`, `AlbumInfoResult` (Task 4); `crate_backend.lastfm.match.verify_match` (Task 3); `PopularitySignal` (Task 1).
- Produces: `async sync_album_popularity(session: AsyncSession, client: httpx.AsyncClient, api_key: str, album: Album) -> PopularitySignal | None`. Consumed by Task 7 (backfill script).

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_lastfm_ingest.py`:

```python
from datetime import UTC, datetime

import httpx
import pytest
from sqlalchemy import select

from crate_backend.lastfm import ingest
from crate_backend.lastfm.client import AlbumInfoResult, FetchOutcome
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal

pytestmark = pytest.mark.asyncio


async def _album(db_session, **overrides) -> Album:
    fields = {"title": "Kid A", "artist_name": "Radiohead"}
    fields.update(overrides)
    album = Album(**fields)
    db_session.add(album)
    await db_session.flush()
    return album


async def _signal(db_session, album_id):
    return await db_session.scalar(
        select(PopularitySignal).where(PopularitySignal.album_id == album_id)
    )


async def test_skips_album_with_no_artist_name(db_session, monkeypatch):
    called = False

    async def fake_fetch(*args, **kwargs):
        nonlocal called
        called = True
        return AlbumInfoResult(FetchOutcome.FOUND)

    monkeypatch.setattr(ingest, "fetch_album_info", fake_fetch)
    album = await _album(db_session, artist_name=None)

    result = await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)

    assert result is None
    assert called is False
    assert await _signal(db_session, album.id) is None


async def test_verified_match_stores_listeners_and_fetched_at(db_session, monkeypatch):
    async def fake_fetch(*args, **kwargs):
        return AlbumInfoResult(FetchOutcome.FOUND, listeners=500, artist="Radiohead", title="Kid A")

    monkeypatch.setattr(ingest, "fetch_album_info", fake_fetch)
    album = await _album(db_session)

    signal = await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)

    assert signal.lastfm_listeners == 500
    assert signal.lastfm_matched_artist == "Radiohead"
    assert signal.lastfm_matched_title == "Kid A"
    assert signal.lastfm_fetched_at is not None


async def test_mismatch_sets_fetched_at_but_leaves_listeners_null(db_session, monkeypatch):
    async def fake_fetch(*args, **kwargs):
        return AlbumInfoResult(
            FetchOutcome.FOUND, listeners=500, artist="Someone Else", title="A Different Album"
        )

    monkeypatch.setattr(ingest, "fetch_album_info", fake_fetch)
    album = await _album(db_session)

    signal = await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)

    assert signal.lastfm_listeners is None
    assert signal.lastfm_fetched_at is not None


async def test_not_found_sets_fetched_at_and_leaves_listeners_null(db_session, monkeypatch):
    async def fake_fetch(*args, **kwargs):
        return AlbumInfoResult(FetchOutcome.NOT_FOUND)

    monkeypatch.setattr(ingest, "fetch_album_info", fake_fetch)
    album = await _album(db_session)

    signal = await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)

    assert signal.lastfm_listeners is None
    assert signal.lastfm_fetched_at is not None


async def test_failed_outcome_leaves_fetched_at_unset_for_retry(db_session, monkeypatch):
    async def fake_fetch(*args, **kwargs):
        return AlbumInfoResult(FetchOutcome.FAILED)

    monkeypatch.setattr(ingest, "fetch_album_info", fake_fetch)
    album = await _album(db_session)

    signal = await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)

    assert signal.lastfm_fetched_at is None
    assert signal.lastfm_listeners is None


async def test_is_idempotent_on_rerun(db_session, monkeypatch):
    async def fake_fetch(*args, **kwargs):
        return AlbumInfoResult(FetchOutcome.FOUND, listeners=500, artist="Radiohead", title="Kid A")

    monkeypatch.setattr(ingest, "fetch_album_info", fake_fetch)
    album = await _album(db_session)

    await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)
    await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)

    rows = (
        await db_session.scalars(select(PopularitySignal).where(PopularitySignal.album_id == album.id))
    ).all()
    assert len(rows) == 1
    assert rows[0].lastfm_listeners == 500


async def test_does_not_touch_sandbox_add_count(db_session, monkeypatch):
    async def fake_fetch(*args, **kwargs):
        return AlbumInfoResult(FetchOutcome.FOUND, listeners=500, artist="Radiohead", title="Kid A")

    monkeypatch.setattr(ingest, "fetch_album_info", fake_fetch)
    album = await _album(db_session)
    db_session.add(PopularitySignal(album_id=album.id, sandbox_add_count=3))
    await db_session.flush()

    signal = await ingest.sync_album_popularity(db_session, httpx.AsyncClient(), "key", album)

    assert signal.sandbox_add_count == 3
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_lastfm_ingest.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.lastfm.ingest'`

- [ ] **Step 3: Write the implementation**

Create `backend/src/crate_backend/lastfm/ingest.py`:

```python
"""Idempotent sync of a single album's PopularitySignal row against
Last.fm. Matched by album_id; safe to re-run."""

from datetime import UTC, datetime

import httpx
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.lastfm.client import FetchOutcome, fetch_album_info
from crate_backend.lastfm.match import verify_match
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal


async def _get_or_create_signal(session: AsyncSession, album_id) -> PopularitySignal:
    signal = await session.scalar(
        select(PopularitySignal).where(PopularitySignal.album_id == album_id)
    )
    if signal is None:
        signal = PopularitySignal(album_id=album_id)
        session.add(signal)
        await session.flush()
    return signal


async def sync_album_popularity(
    session: AsyncSession, client: httpx.AsyncClient, api_key: str, album: Album
) -> PopularitySignal | None:
    """Look up `album` on Last.fm, verify the match, and upsert its
    PopularitySignal row. Returns None without any request or row change
    if the album has no artist_name to search with.

    lastfm_fetched_at is set for every definitive answer (verified match,
    confirmed no-match, or a mismatch) but left unset when retries are
    exhausted, so a resumed backfill run retries this album.
    """
    if not album.artist_name:
        return None

    signal = await _get_or_create_signal(session, album.id)
    result = await fetch_album_info(client, api_key, album.artist_name, album.title)

    if result.outcome is FetchOutcome.FAILED:
        return signal

    signal.lastfm_fetched_at = datetime.now(UTC)
    if result.outcome is FetchOutcome.FOUND and verify_match(
        album.artist_name, album.title, result.artist, result.title
    ):
        signal.lastfm_listeners = result.listeners
        signal.lastfm_matched_artist = result.artist
        signal.lastfm_matched_title = result.title
    await session.flush()
    return signal
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_lastfm_ingest.py -v`
Expected: PASS (7 tests)

- [ ] **Step 5: Commit**

```bash
cd backend
git add src/crate_backend/lastfm/ingest.py tests/test_lastfm_ingest.py
git commit -m "feat: add idempotent Last.fm popularity ingest"
```

---

### Task 6: Percentile-rank score computation

**Files:**
- Create: `backend/src/crate_backend/lastfm/scoring.py`
- Test: `backend/tests/test_lastfm_scoring.py`

**Interfaces:**
- Consumes: `PopularitySignal`, `Album` (Task 1 and existing `catalog.py`).
- Produces: `async recompute_popularity_scores(session: AsyncSession) -> int` (returns count of albums scored). Consumed by Task 7 (backfill script).

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_lastfm_scoring.py`:

```python
import pytest
from sqlalchemy import select

from crate_backend.lastfm.scoring import recompute_popularity_scores
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal

pytestmark = pytest.mark.asyncio


async def _album_with_signal(db_session, listeners: int | None) -> Album:
    album = Album(title=f"Album {listeners}", artist_name="Test Artist")
    db_session.add(album)
    await db_session.flush()
    db_session.add(PopularitySignal(album_id=album.id, lastfm_listeners=listeners))
    await db_session.flush()
    return album


async def test_returns_zero_when_no_albums_have_listeners(db_session):
    await _album_with_signal(db_session, None)

    scored = await recompute_popularity_scores(db_session)

    assert scored == 0


async def test_min_and_max_get_zero_and_one(db_session):
    low = await _album_with_signal(db_session, 100)
    high = await _album_with_signal(db_session, 100_000)

    await recompute_popularity_scores(db_session)
    await db_session.refresh(low)
    await db_session.refresh(high)

    assert low.popularity == 0.0
    assert high.popularity == 1.0


async def test_middle_value_is_between_zero_and_one(db_session):
    low = await _album_with_signal(db_session, 100)
    mid = await _album_with_signal(db_session, 500)
    high = await _album_with_signal(db_session, 100_000)

    await recompute_popularity_scores(db_session)
    await db_session.refresh(mid)

    assert 0.0 < mid.popularity < 1.0


async def test_tied_listener_counts_get_the_same_score(db_session):
    first = await _album_with_signal(db_session, 500)
    second = await _album_with_signal(db_session, 500)
    await _album_with_signal(db_session, 100_000)

    await recompute_popularity_scores(db_session)
    await db_session.refresh(first)
    await db_session.refresh(second)

    assert first.popularity == second.popularity


async def test_unmatched_album_popularity_stays_null(db_session):
    unmatched = await _album_with_signal(db_session, None)
    await _album_with_signal(db_session, 500)

    await recompute_popularity_scores(db_session)
    await db_session.refresh(unmatched)

    assert unmatched.popularity is None


async def test_single_matched_album_scores_at_one(db_session):
    only = await _album_with_signal(db_session, 500)

    scored = await recompute_popularity_scores(db_session)
    await db_session.refresh(only)

    assert scored == 1
    assert only.popularity == 1.0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_lastfm_scoring.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.lastfm.scoring'`

- [ ] **Step 3: Write the implementation**

Create `backend/src/crate_backend/lastfm/scoring.py`:

```python
"""Recomputes Album.popularity as each matched album's percentile rank of
Last.fm listeners. Not called per-request -- percentile rank is only
meaningful relative to the whole current distribution, so this runs as a
batch step at the end of the backfill script."""

import bisect

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal


def _percentile_rank(sorted_values: list[int], value: int) -> float:
    """Fraction of sorted_values <= value, using the average rank among
    ties. 0.0 for the minimum, 1.0 for the maximum, when there's more than
    one distinct album; 1.0 if this is the only album."""
    n = len(sorted_values)
    if n == 1:
        return 1.0
    lo = bisect.bisect_left(sorted_values, value)
    hi = bisect.bisect_right(sorted_values, value)
    average_zero_based_rank = (lo + hi - 1) / 2
    return average_zero_based_rank / (n - 1)


async def recompute_popularity_scores(session: AsyncSession) -> int:
    """Set Album.popularity to each matched album's percentile rank of
    lastfm_listeners among all albums with a verified match. Albums with
    no verified match are left untouched (popularity stays null). Returns
    the number of albums scored."""
    rows = (
        await session.execute(
            select(PopularitySignal.album_id, PopularitySignal.lastfm_listeners).where(
                PopularitySignal.lastfm_listeners.is_not(None)
            )
        )
    ).all()
    if not rows:
        return 0

    sorted_values = sorted(listeners for _, listeners in rows)
    album_ids = [album_id for album_id, _ in rows]
    albums = {
        album.id: album
        for album in (await session.scalars(select(Album).where(Album.id.in_(album_ids)))).all()
    }
    for album_id, listeners in rows:
        albums[album_id].popularity = _percentile_rank(sorted_values, listeners)
    await session.flush()
    return len(rows)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_lastfm_scoring.py -v`
Expected: PASS (6 tests)

- [ ] **Step 5: Commit**

```bash
cd backend
git add src/crate_backend/lastfm/scoring.py tests/test_lastfm_scoring.py
git commit -m "feat: add percentile-rank popularity score computation"
```

---

### Task 7: Backfill script

**Files:**
- Create: `backend/src/crate_backend/scripts/backfill_lastfm_popularity.py`
- Test: `backend/tests/test_backfill_lastfm_popularity_script.py`

**Interfaces:**
- Consumes: `crate_backend.lastfm.ingest.sync_album_popularity` (Task 5), `crate_backend.lastfm.scoring.recompute_popularity_scores` (Task 6), `crate_backend.db.session.async_session_factory`, `crate_backend.core.config.get_settings`.
- Produces: `async backfill(request_interval_seconds: float = 1.0) -> None`, `main() -> None`. No later task consumes this directly; it's the operator-facing entry point.

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_backfill_lastfm_popularity_script.py` (mirrors `tests/test_ingest_musicbrainz_script.py`'s session-factory-substitution pattern):

```python
import pytest
from sqlalchemy import select

from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal
from crate_backend.scripts import backfill_lastfm_popularity

pytestmark = pytest.mark.asyncio


class _SessionFactory:
    """Stands in for async_session_factory: `async with factory() as s`
    yields the rollback-wrapped test session instead of a real one."""

    def __init__(self, session):
        self._session = session

    def __call__(self):
        return self

    async def __aenter__(self):
        return self._session

    async def __aexit__(self, *exc_info):
        return False


@pytest.fixture
def script(monkeypatch, db_session):
    monkeypatch.setattr(backfill_lastfm_popularity, "async_session_factory", _SessionFactory(db_session))

    async def fake_sleep(seconds):
        pass

    monkeypatch.setattr(backfill_lastfm_popularity, "_sleep", fake_sleep)
    return backfill_lastfm_popularity


async def test_backfill_syncs_only_unattempted_albums(script, db_session, monkeypatch):
    never_tried = Album(title="Never Tried", artist_name="Test Artist")
    already_tried = Album(title="Already Tried", artist_name="Test Artist")
    db_session.add_all([never_tried, already_tried])
    await db_session.flush()
    db_session.add(
        PopularitySignal(album_id=already_tried.id, lastfm_fetched_at=__import__("datetime").datetime.now())
    )
    await db_session.flush()

    synced_album_ids = []

    async def fake_sync(session, client, api_key, album):
        synced_album_ids.append(album.id)
        return None

    monkeypatch.setattr(script, "sync_album_popularity", fake_sync)
    monkeypatch.setattr(script, "recompute_popularity_scores", lambda session: 0)

    await script.backfill()

    assert synced_album_ids == [never_tried.id]


async def test_backfill_calls_recompute_at_the_end(script, db_session, monkeypatch):
    album = Album(title="Some Album", artist_name="Test Artist")
    db_session.add(album)
    await db_session.flush()

    async def fake_sync(session, client, api_key, album):
        return None

    recompute_called = False

    async def fake_recompute(session):
        nonlocal recompute_called
        recompute_called = True
        return 0

    monkeypatch.setattr(script, "sync_album_popularity", fake_sync)
    monkeypatch.setattr(script, "recompute_popularity_scores", fake_recompute)

    await script.backfill()

    assert recompute_called is True


async def test_backfill_paces_requests(script, db_session, monkeypatch):
    albums = [Album(title=f"Album {i}", artist_name="Test Artist") for i in range(3)]
    db_session.add_all(albums)
    await db_session.flush()

    sleeps: list[float] = []

    async def fake_sleep(seconds):
        sleeps.append(seconds)

    monkeypatch.setattr(script, "_sleep", fake_sleep)

    async def fake_sync(session, client, api_key, album):
        return None

    monkeypatch.setattr(script, "sync_album_popularity", fake_sync)
    monkeypatch.setattr(script, "recompute_popularity_scores", lambda session: 0)

    await script.backfill(request_interval_seconds=2.5)

    assert sleeps == [2.5, 2.5, 2.5]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_backfill_lastfm_popularity_script.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.scripts.backfill_lastfm_popularity'`

- [ ] **Step 3: Write the implementation**

Create `backend/src/crate_backend/scripts/backfill_lastfm_popularity.py`:

```python
"""Backfill Last.fm popularity signals for the catalog (Phase 3
prerequisite).

Design: docs/superpowers/specs/2026-09-24-lastfm-popularity-signal-design.md

Run with: uv run python -m crate_backend.scripts.backfill_lastfm_popularity
"""

import asyncio

import httpx
from sqlalchemy import select

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.lastfm.ingest import sync_album_popularity
from crate_backend.lastfm.scoring import recompute_popularity_scores
from crate_backend.models.catalog import Album
from crate_backend.models.popularity import PopularitySignal

_PROGRESS_EVERY = 500
_COMMIT_EVERY = 50

# Module-level so tests can replace waiting without patching asyncio globally.
_sleep = asyncio.sleep


async def backfill(request_interval_seconds: float = 1.0) -> None:
    """Sync every album that has never had a Last.fm lookup attempt (no
    lastfm_fetched_at), then recompute Album.popularity for the whole
    catalog. Safe to re-run: already-attempted albums are skipped."""
    settings = get_settings()
    async with async_session_factory() as session:
        albums = (
            await session.scalars(
                select(Album)
                .outerjoin(PopularitySignal, PopularitySignal.album_id == Album.id)
                .where(PopularitySignal.lastfm_fetched_at.is_(None))
            )
        ).all()
        total = len(albums)
        print(f"Looking up {total} albums without a completed Last.fm attempt...")

        async with httpx.AsyncClient() as client:
            for index, album in enumerate(albums, start=1):
                await sync_album_popularity(session, client, settings.lastfm_api_key, album)
                if index % _COMMIT_EVERY == 0:
                    await session.commit()
                if index % _PROGRESS_EVERY == 0:
                    print(f"  checked {index}/{total}")
                await _sleep(request_interval_seconds)
        await session.commit()

    async with async_session_factory() as session:
        scored = await recompute_popularity_scores(session)
        await session.commit()
    print(f"Recomputed popularity for {scored} matched albums.")


def main() -> None:
    asyncio.run(backfill())


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_backfill_lastfm_popularity_script.py -v`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
cd backend
git add src/crate_backend/scripts/backfill_lastfm_popularity.py tests/test_backfill_lastfm_popularity_script.py
git commit -m "feat: add Last.fm popularity backfill script"
```

---

### Task 8: `POST /albums/{album_id}/add-to-sandbox` endpoint

**Files:**
- Modify: `backend/src/crate_backend/api/routes/albums.py`
- Test: `backend/tests/test_albums.py`

**Interfaces:**
- Consumes: `current_active_user` (`crate_backend.auth.backend`), `PopularitySignal` (Task 1), `Event` (existing `crate_backend.models.event`).
- Produces: the endpoint itself; nothing else depends on it within this plan.

- [ ] **Step 1: Write the failing tests**

Append to `backend/tests/test_albums.py`:

```python
from crate_backend.models.event import Event
from crate_backend.models.popularity import PopularitySignal


async def _register_and_login(ac, email: str = "sandbox-user@example.com") -> None:
    await ac.post("/auth/register", json={"email": email, "password": "correct horse battery staple"})
    login_response = await ac.post(
        "/auth/login", data={"username": email, "password": "correct horse battery staple"}
    )
    assert login_response.status_code == 204


async def test_add_to_sandbox_requires_auth(client, db_session):
    await _seed(db_session, Album(title="Kid A", artist_name="Radiohead"))
    album = await db_session.scalar(select(Album).where(Album.title == "Kid A"))

    async with client as ac:
        response = await ac.post(f"/albums/{album.id}/add-to-sandbox")

    assert response.status_code == 401


async def test_add_to_sandbox_404s_for_unknown_album(client, db_session):
    async with client as ac:
        await _register_and_login(ac)
        response = await ac.post("/albums/00000000-0000-0000-0000-000000000000/add-to-sandbox")

    assert response.status_code == 404
    assert (await db_session.scalars(select(PopularitySignal))).first() is None


async def test_add_to_sandbox_increments_counter_and_emits_event(client, db_session):
    await _seed(db_session, Album(title="Kid A", artist_name="Radiohead"))
    album = await db_session.scalar(select(Album).where(Album.title == "Kid A"))

    async with client as ac:
        await _register_and_login(ac)
        response = await ac.post(f"/albums/{album.id}/add-to-sandbox")

    assert response.status_code == 204
    signal = await db_session.scalar(
        select(PopularitySignal).where(PopularitySignal.album_id == album.id)
    )
    assert signal.sandbox_add_count == 1
    event = await db_session.scalar(select(Event).where(Event.event_type == "album_added_to_sandbox"))
    assert event.payload["album_id"] == str(album.id)


async def test_add_to_sandbox_increments_existing_counter(client, db_session):
    await _seed(db_session, Album(title="Kid A", artist_name="Radiohead"))
    album = await db_session.scalar(select(Album).where(Album.title == "Kid A"))
    db_session.add(PopularitySignal(album_id=album.id, sandbox_add_count=4))
    await db_session.commit()

    async with client as ac:
        await _register_and_login(ac)
        await ac.post(f"/albums/{album.id}/add-to-sandbox")

    signal = await db_session.scalar(select(PopularitySignal).where(PopularitySignal.album_id == album.id))
    assert signal.sandbox_add_count == 5
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_albums.py -v -k add_to_sandbox`
Expected: FAIL with 404/405 (route doesn't exist yet)

- [ ] **Step 3: Write the implementation**

Modify `backend/src/crate_backend/api/routes/albums.py` — replace the top of the file (imports and router setup) and append the new endpoint. Full resulting file:

```python
import uuid
from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.auth.backend import current_active_user
from crate_backend.db.session import get_session
from crate_backend.models.catalog import Album
from crate_backend.models.event import Event
from crate_backend.models.popularity import PopularitySignal
from crate_backend.models.user import User

router = APIRouter(prefix="/albums", tags=["albums"])

MAX_RESULTS = 24


class AlbumSearchResult(BaseModel):
    id: str
    title: str
    artist_name: str | None
    release_year: int | None
    cover_art_url: str | None


@router.get("/search", response_model=list[AlbumSearchResult])
async def search_albums(
    q: str = Query(..., max_length=200),
    session: AsyncSession = Depends(get_session),
) -> list[AlbumSearchResult]:
    term = q.strip()
    if not term:
        return []

    pattern = f"%{term}%"
    stmt = (
        select(Album)
        .where(Album.title.ilike(pattern) | Album.artist_name.ilike(pattern))
        .order_by(Album.title)
        .limit(MAX_RESULTS)
    )
    albums = (await session.scalars(stmt)).all()
    return [
        AlbumSearchResult(
            id=str(album.id),
            title=album.title,
            artist_name=album.artist_name,
            release_year=album.release_year,
            cover_art_url=album.cover_art_url,
        )
        for album in albums
    ]


@router.post("/{album_id}/add-to-sandbox", status_code=status.HTTP_204_NO_CONTENT)
async def add_to_sandbox(
    album_id: uuid.UUID,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_session),
) -> None:
    """Records that a user added `album_id` to their sandbox: increments
    its internal popularity counter and logs an audit Event. This is
    tracked separately from the Last.fm signal and does not itself affect
    Album.popularity (see crate_backend.lastfm.scoring)."""
    album = await session.get(Album, album_id)
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")

    signal = await session.scalar(
        select(PopularitySignal).where(PopularitySignal.album_id == album_id)
    )
    if signal is None:
        signal = PopularitySignal(album_id=album_id)
        session.add(signal)
        await session.flush()
    signal.sandbox_add_count += 1

    session.add(
        Event(
            user_id=user.id,
            event_type="album_added_to_sandbox",
            payload={"album_id": str(album_id)},
        )
    )
    await session.commit()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_albums.py -v`
Expected: PASS (all tests in the file, including the 4 new ones)

- [ ] **Step 5: Run the full backend test suite**

Run: `cd backend && uv run pytest -v`
Expected: PASS (every test in the suite, confirming this task didn't break existing routes/models)

- [ ] **Step 6: Commit**

```bash
cd backend
git add src/crate_backend/api/routes/albums.py tests/test_albums.py
git commit -m "feat: add POST /albums/{album_id}/add-to-sandbox endpoint"
```

---

## After all tasks

Run `cd backend && uv run ruff check . && uv run pytest -v` once more to confirm lint and the full suite are clean. The catalog now has the schema and pipeline needed to run `uv run python -m crate_backend.scripts.backfill_lastfm_popularity` against the real ~25,000-album catalog — that real run (several hours, paced at 1 req/sec) is an operational step for whoever runs it, not part of this plan's automated tests.
