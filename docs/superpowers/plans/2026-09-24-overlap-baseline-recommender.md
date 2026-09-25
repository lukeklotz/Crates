# Genre/Tag-Overlap Baseline Recommender Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A user groups albums on the canvas, presses **Find recommendations**, and sees related albums ranked by Jaccard genre/tag overlap, each with the terms it shares — Crate's first real recommendations (thin Phase 3 baseline).

**Architecture:** A backend `recommend/overlap.py` module scores candidates with one SQL query (per-album term sets = lowercased genre + tag names; Jaccard per seed, summed across seeds), exposed as `POST /recommendations`. The frontend keeps each canvas card's backend album id, proxies the request through a Next-style route handler, and renders results in the existing group panel.

**Tech Stack:** Backend: Python 3.12, FastAPI, SQLAlchemy 2.0 async (`text()` query with CTEs), Pydantic, pytest + pytest-asyncio, uv. Frontend: React (vinext/Next-style app router), TypeScript, oxlint.

**Spec:** `docs/superpowers/specs/2026-09-24-overlap-baseline-recommender-design.md`

## Global Constraints

- Terms = union of genre names and tag names, **lowercased and de-duplicated per album**; vote counts are ignored.
- Score = sum over seeds of `|shared| / |union|` (Jaccard). Seeds are never returned. Same-artist albums are allowed.
- Order: score desc, then distinct shared terms desc, then title asc, then album id asc.
- `shared_terms` per result: terms shared with the union of seed terms, ordered by number of seeds sharing the term desc, then alphabetically.
- `POST /recommendations` — no auth; `album_ids` 1–50 UUIDs (duplicates collapsed); `limit` default 20, range 1–50; 404 lists unknown ids; 422 for invalid input; response `{"results": [...], "reason": null | "seeds_have_no_terms"}`.
- Out of scope: popularity steering (UI options shown **disabled**), persisted `RecommendationRun`s, precomputation, evaluation sets/scoring scripts, diversity, a frontend test framework.
- The dev Postgres used by the `db_session` fixture holds the real ~25,000-album catalog. Backend test fixtures must use terms prefixed `zzfixture-` so no real album can match them. Before running backend tests: `docker compose up -d db` (repo root) and `cd backend && uv run alembic upgrade head`.
- Frontend lint baseline: `npx oxlint app/` reports 6 pre-existing errors (3× `next(no-img-element)`, 1× `next(no-html-link-for-pages)`, 1× `react(react-compiler)`, 1× `typescript(no-deprecated)`). New code may add `no-img-element` findings for `<img>` tags (the page uses `<img>` throughout, by convention) but no other new findings. `npx tsc --noEmit -p .` must stay clean.

## Review Focus

- A group containing the same album twice (a duplicated card) must send and score that album once, not double its influence.
- Seeds with very common terms (e.g. "rock", "electronic") make most of the catalog a candidate; the request must still finish in well under a couple of seconds on the real catalog, with a stable order.
- If the group's albums change while a request is in flight, the returned results must be shown as stale ("Group changed"), not as current.
- A multi-seed group where one seed has no genres or tags must still return recommendations from the tagged seeds.
- If the backend is down, the panel must show the error state and keep any previous results visible.

Measured during planning (warm cache, real catalog, the query as written in Task 1): 1 seed with specific jazz tags ≈ 65 ms; 1 seed with broad rock/electronic tags ≈ 560 ms; 3 mixed seeds ≈ 590 ms. The early-filtering query was checked to return top-50 results identical to a straightforward full-catalog version for 1, 3 and 5 seeds.

---

### Task 1: Overlap recommender module

**Files:**
- Create: `backend/src/crate_backend/recommend/__init__.py` (empty)
- Create: `backend/src/crate_backend/recommend/overlap.py`
- Test: `backend/tests/test_recommend_overlap.py`

**Interfaces:**
- Consumes: existing tables `albums`, `album_genres`, `genres`, `album_tags`, `tags`.
- Produces:
  - `OverlapRecommendation` — frozen dataclass: `album_id: uuid.UUID`, `score: float`, `shared_terms: list[str]`.
  - `async recommend_by_overlap(session: AsyncSession, seed_ids: list[uuid.UUID], limit: int) -> list[OverlapRecommendation]` — caller guarantees `seed_ids` are distinct, existing album ids.
  - `async seeds_have_terms(session: AsyncSession, seed_ids: list[uuid.UUID]) -> bool`.
  Consumed by Task 2.

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_recommend_overlap.py`:

```python
import uuid

import pytest
from sqlalchemy import select

from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.recommend.overlap import recommend_by_overlap, seeds_have_terms

pytestmark = pytest.mark.asyncio


def terms(*names: str) -> list[str]:
    """Fixture terms no real catalog album can have."""
    return [f"zzfixture-{name}" for name in names]


async def _genre(db_session, name: str) -> Genre:
    genre = await db_session.scalar(select(Genre).where(Genre.name == name))
    if genre is None:
        genre = Genre(musicbrainz_id=str(uuid.uuid4()), name=name)
        db_session.add(genre)
        await db_session.flush()
    return genre


async def _tag(db_session, name: str) -> Tag:
    tag = await db_session.scalar(select(Tag).where(Tag.name == name))
    if tag is None:
        tag = Tag(name=name)
        db_session.add(tag)
        await db_session.flush()
    return tag


async def _album(db_session, title: str, tags=(), genres=()) -> Album:
    album = Album(title=title, artist_name="Fixture Artist")
    db_session.add(album)
    await db_session.flush()
    for name in genres:
        db_session.add(AlbumGenre(album_id=album.id, genre_id=(await _genre(db_session, name)).id))
    for name in tags:
        db_session.add(AlbumTag(album_id=album.id, tag_id=(await _tag(db_session, name)).id))
    await db_session.flush()
    return album


async def _recommend(db_session, *seeds: Album, limit: int = 20):
    return await recommend_by_overlap(db_session, [s.id for s in seeds], limit)


async def test_small_overlap_outranks_heavily_tagged_album(db_session):
    seed = await _album(db_session, "Seed", tags=terms("a", "b", "c", "d", "e"))
    focused = await _album(db_session, "Focused", tags=terms("a", "b", "c", "d"))
    heavy = await _album(
        db_session, "Heavy", tags=terms("a", "b", "c", "d", *[f"x{i}" for i in range(36)])
    )

    results = await _recommend(db_session, seed)

    assert [r.album_id for r in results] == [focused.id, heavy.id]
    assert results[0].score == pytest.approx(4 / 5)
    assert results[1].score == pytest.approx(4 / 41)


async def test_seeds_are_never_recommended(db_session):
    first = await _album(db_session, "First Seed", tags=terms("a", "b"))
    second = await _album(db_session, "Second Seed", tags=terms("a", "b"))
    other = await _album(db_session, "Other", tags=terms("a"))

    results = await _recommend(db_session, first, second)

    assert [r.album_id for r in results] == [other.id]


async def test_group_score_sums_each_seeds_similarity(db_session):
    first = await _album(db_session, "First Seed", tags=terms("a", "b"))
    second = await _album(db_session, "Second Seed", tags=terms("c", "d"))
    matches_one_fully = await _album(db_session, "One", tags=terms("a", "b"))
    bridges_both = await _album(db_session, "Both", tags=terms("a", "c"))

    results = await _recommend(db_session, first, second)

    assert [r.album_id for r in results] == [matches_one_fully.id, bridges_both.id]
    assert results[0].score == pytest.approx(1.0)
    assert results[1].score == pytest.approx(1 / 3 + 1 / 3)


async def test_untagged_seed_does_not_block_tagged_seed(db_session):
    tagged = await _album(db_session, "Tagged Seed", tags=terms("a", "b"))
    untagged = await _album(db_session, "Untagged Seed")
    match = await _album(db_session, "Match", tags=terms("a", "b"))

    results = await _recommend(db_session, tagged, untagged)

    assert [r.album_id for r in results] == [match.id]
    assert results[0].score == pytest.approx(1.0)


async def test_genre_and_tag_with_the_same_name_count_once(db_session):
    seed = await _album(
        db_session, "Seed", genres=terms("rock"), tags=["ZZFIXTURE-ROCK", *terms("x")]
    )
    candidate = await _album(db_session, "Candidate", tags=terms("rock"))

    [result] = await _recommend(db_session, seed)

    assert result.album_id == candidate.id
    assert result.score == pytest.approx(1 / 2)
    assert result.shared_terms == terms("rock")


async def test_ties_prefer_more_shared_terms_then_title(db_session):
    seed = await _album(db_session, "Seed", tags=terms("a", "b", "c", "d"))
    beta = await _album(db_session, "Beta", tags=terms("a", "b"))
    alpha = await _album(db_session, "Alpha", tags=terms("c", "d"))
    many = await _album(db_session, "Many", tags=terms("a", "b", "c", "d", "e", "f", "g", "h"))

    results = await _recommend(db_session, seed)

    assert [r.score for r in results] == [0.5, 0.5, 0.5]
    assert [r.album_id for r in results] == [many.id, alpha.id, beta.id]


async def test_shared_terms_ordered_by_seed_count_then_name(db_session):
    first = await _album(db_session, "First Seed", tags=terms("a", "b"))
    second = await _album(db_session, "Second Seed", tags=terms("b", "c"))
    await _album(db_session, "Candidate", tags=terms("a", "b", "c", "z"))

    [result] = await _recommend(db_session, first, second)

    assert result.shared_terms == terms("b", "a", "c")


async def test_limit_caps_results(db_session):
    seed = await _album(db_session, "Seed", tags=terms("a"))
    for i in range(5):
        await _album(db_session, f"Candidate {i}", tags=terms("a"))

    assert len(await _recommend(db_session, seed, limit=3)) == 3


async def test_no_shared_terms_means_no_results(db_session):
    seed = await _album(db_session, "Seed", tags=terms("lonely"))

    assert await _recommend(db_session, seed) == []


async def test_seeds_have_terms(db_session):
    untagged = await _album(db_session, "Untagged")
    genre_only = await _album(db_session, "Genre Only", genres=terms("g"))
    tag_only = await _album(db_session, "Tag Only", tags=terms("t"))

    assert await seeds_have_terms(db_session, [untagged.id]) is False
    assert await seeds_have_terms(db_session, [untagged.id, genre_only.id]) is True
    assert await seeds_have_terms(db_session, [tag_only.id]) is True
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_recommend_overlap.py -q`
Expected: FAIL — collection error, `ModuleNotFoundError: No module named 'crate_backend.recommend'`

- [ ] **Step 3: Write the implementation**

Create `backend/src/crate_backend/recommend/__init__.py` (empty file).

Create `backend/src/crate_backend/recommend/overlap.py`:

```python
"""Genre/tag-overlap baseline recommender (thin Phase 3).

An album's terms are its genre and tag names, lowercased and de-duplicated.
A candidate's score is its Jaccard similarity to each seed, summed across
seeds, so every seed has equal influence.

Design: docs/superpowers/specs/2026-09-24-overlap-baseline-recommender-design.md
"""

import uuid
from dataclasses import dataclass

from sqlalchemy import bindparam, text
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.ext.asyncio import AsyncSession

_UUID_ARRAY = ARRAY(UUID(as_uuid=True))


def _terms_where(condition: str) -> str:
    """SQL yielding distinct (album_id, term) rows for albums matching
    `condition`, a predicate on the placeholder {album_id}."""
    return f"""
        SELECT ag.album_id, lower(g.name) AS term
        FROM album_genres ag JOIN genres g ON g.id = ag.genre_id
        WHERE {condition.format(album_id="ag.album_id")}
        UNION
        SELECT at.album_id, lower(t.name) AS term
        FROM album_tags at JOIN tags t ON t.id = at.tag_id
        WHERE {condition.format(album_id="at.album_id")}"""


# Filters to terms the seeds actually have before touching the rest of the
# catalog; only candidates' full term counts need a second pass.
_RANK = text(f"""
WITH seed_terms AS ({_terms_where("{album_id} = ANY(:seed_ids)")}),
seed_sizes AS (
    SELECT album_id AS seed_id, count(*) AS n FROM seed_terms GROUP BY album_id
),
wanted AS (SELECT DISTINCT term FROM seed_terms),
matching AS (
    SELECT ag.album_id, lower(g.name) AS term
    FROM album_genres ag JOIN genres g ON g.id = ag.genre_id
    WHERE lower(g.name) IN (SELECT term FROM wanted) AND ag.album_id <> ALL(:seed_ids)
    UNION
    SELECT at.album_id, lower(t.name) AS term
    FROM album_tags at JOIN tags t ON t.id = at.tag_id
    WHERE lower(t.name) IN (SELECT term FROM wanted) AND at.album_id <> ALL(:seed_ids)
),
shared AS (
    SELECT m.album_id AS candidate_id, st.album_id AS seed_id, count(*) AS n_shared
    FROM matching m JOIN seed_terms st ON st.term = m.term
    GROUP BY m.album_id, st.album_id
),
distinct_shared AS (
    SELECT album_id AS candidate_id, count(*) AS n FROM matching GROUP BY album_id
),
candidate_sizes AS (
    SELECT album_id, count(*) AS n
    FROM ({_terms_where("{album_id} IN (SELECT candidate_id FROM distinct_shared)")}) c
    GROUP BY album_id
),
scored AS (
    SELECT s.candidate_id,
           sum(s.n_shared::float / (ss.n + cs.n - s.n_shared)) AS score
    FROM shared s
    JOIN seed_sizes ss ON ss.seed_id = s.seed_id
    JOIN candidate_sizes cs ON cs.album_id = s.candidate_id
    GROUP BY s.candidate_id
)
SELECT sc.candidate_id, sc.score
FROM scored sc
JOIN distinct_shared ds ON ds.candidate_id = sc.candidate_id
JOIN albums a ON a.id = sc.candidate_id
ORDER BY sc.score DESC, ds.n DESC, a.title ASC, a.id ASC
LIMIT :limit
""").bindparams(bindparam("seed_ids", type_=_UUID_ARRAY))

_SHARED_TERMS = text(f"""
WITH seed_terms AS ({_terms_where("{album_id} = ANY(:seed_ids)")}),
candidate_terms AS ({_terms_where("{album_id} = ANY(:candidate_ids)")})
SELECT ct.album_id, ct.term
FROM candidate_terms ct JOIN seed_terms st ON st.term = ct.term
GROUP BY ct.album_id, ct.term
ORDER BY ct.album_id, count(DISTINCT st.album_id) DESC, ct.term ASC
""").bindparams(
    bindparam("seed_ids", type_=_UUID_ARRAY),
    bindparam("candidate_ids", type_=_UUID_ARRAY),
)

_SEEDS_HAVE_TERMS = text("""
SELECT EXISTS (SELECT 1 FROM album_genres WHERE album_id = ANY(:seed_ids))
    OR EXISTS (SELECT 1 FROM album_tags WHERE album_id = ANY(:seed_ids))
""").bindparams(bindparam("seed_ids", type_=_UUID_ARRAY))


@dataclass(frozen=True)
class OverlapRecommendation:
    album_id: uuid.UUID
    score: float
    shared_terms: list[str]


async def recommend_by_overlap(
    session: AsyncSession, seed_ids: list[uuid.UUID], limit: int
) -> list[OverlapRecommendation]:
    """Rank albums related to the seeds. Callers pass distinct, existing
    album ids; seeds themselves are never returned."""
    ranked = (await session.execute(_RANK, {"seed_ids": seed_ids, "limit": limit})).all()
    if not ranked:
        return []

    shared: dict[uuid.UUID, list[str]] = {}
    rows = await session.execute(
        _SHARED_TERMS,
        {"seed_ids": seed_ids, "candidate_ids": [album_id for album_id, _ in ranked]},
    )
    for album_id, term in rows:
        shared.setdefault(album_id, []).append(term)

    return [
        OverlapRecommendation(album_id=album_id, score=score, shared_terms=shared[album_id])
        for album_id, score in ranked
    ]


async def seeds_have_terms(session: AsyncSession, seed_ids: list[uuid.UUID]) -> bool:
    return bool(await session.scalar(_SEEDS_HAVE_TERMS, {"seed_ids": seed_ids}))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_recommend_overlap.py -q`
Expected: PASS (10 tests)

- [ ] **Step 5: Lint**

Run: `cd backend && uv run ruff check src/crate_backend/recommend tests/test_recommend_overlap.py`
Expected: `All checks passed!`

- [ ] **Step 6: Commit**

```bash
cd backend
git add src/crate_backend/recommend/__init__.py src/crate_backend/recommend/overlap.py tests/test_recommend_overlap.py
git commit -m "feat: add Jaccard genre/tag-overlap recommender"
```

---

### Task 2: `POST /recommendations` endpoint

**Files:**
- Create: `backend/src/crate_backend/api/routes/recommendations.py`
- Modify: `backend/src/crate_backend/main.py` (register the router)
- Test: `backend/tests/test_recommendations_api.py`

**Interfaces:**
- Consumes: `recommend_by_overlap`, `seeds_have_terms`, `OverlapRecommendation` (Task 1); `get_session`; `Album`.
- Produces: `POST /recommendations` — request `{"album_ids": [uuid, ...], "limit": int}`; response `{"results": [{"id", "title", "artist_name", "release_year", "cover_art_url", "score", "shared_terms"}], "reason": null | "seeds_have_no_terms"}`. Consumed by Task 3's proxy route.

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_recommendations_api.py`:

```python
import uuid

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import select

from crate_backend.db.session import get_session
from crate_backend.main import app
from crate_backend.models.catalog import Album, AlbumTag, Tag

pytestmark = pytest.mark.asyncio


@pytest.fixture
async def client(db_session):
    """An open client (an httpx client can't be reopened, and some tests
    post twice)."""

    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session
    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            yield ac
    finally:
        app.dependency_overrides.pop(get_session, None)


async def _album(db_session, title: str, *tag_names: str, **fields) -> Album:
    album = Album(title=title, artist_name="Fixture Artist", **fields)
    db_session.add(album)
    await db_session.flush()
    for name in tag_names:
        tag = Tag(name=f"zzfixture-api-{name}")
        db_session.add(tag)
        await db_session.flush()
        db_session.add(AlbumTag(album_id=album.id, tag_id=tag.id))
    await db_session.flush()
    return album


async def _link(db_session, album: Album, *tag_names: str) -> None:
    """Give `album` tags that already exist (created by _album)."""
    for name in tag_names:
        tag = await db_session.scalar(select(Tag).where(Tag.name == f"zzfixture-api-{name}"))
        db_session.add(AlbumTag(album_id=album.id, tag_id=tag.id))
    await db_session.flush()


async def _post(client, **body):
    return await client.post("/recommendations", json=body)


async def test_returns_ranked_albums_with_shared_terms(client, db_session):
    seed = await _album(db_session, "Seed", "a", "b")
    match = await _album(db_session, "Match", release_year=1999, cover_art_url="https://x.test/c")
    await _link(db_session, match, "a", "b")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.status_code == 200
    body = response.json()
    assert body["reason"] is None
    assert body["results"] == [
        {
            "id": str(match.id),
            "title": "Match",
            "artist_name": "Fixture Artist",
            "release_year": 1999,
            "cover_art_url": "https://x.test/c",
            "score": pytest.approx(1.0),
            "shared_terms": ["zzfixture-api-a", "zzfixture-api-b"],
        }
    ]


async def test_limit_is_respected(client, db_session):
    seed = await _album(db_session, "Seed", "a")
    for i in range(4):
        await _link(db_session, await _album(db_session, f"Candidate {i}"), "a")

    response = await _post(client, album_ids=[str(seed.id)], limit=2)

    assert len(response.json()["results"]) == 2


async def test_duplicate_seed_ids_are_collapsed(client, db_session):
    seed = await _album(db_session, "Seed", "a", "b")
    await _link(db_session, await _album(db_session, "Partial"), "a")

    once = (await _post(client, album_ids=[str(seed.id)])).json()
    twice = (await _post(client, album_ids=[str(seed.id), str(seed.id)])).json()

    assert twice == once
    assert twice["results"][0]["score"] == pytest.approx(1 / 2)


async def test_unknown_album_ids_are_404_and_listed(client, db_session):
    seed = await _album(db_session, "Seed", "a")
    missing = str(uuid.uuid4())

    response = await _post(client, album_ids=[str(seed.id), missing])

    assert response.status_code == 404
    assert response.json()["detail"]["missing"] == [missing]


@pytest.mark.parametrize(
    "body",
    [
        {"album_ids": []},
        {"album_ids": [str(uuid.uuid4()) for _ in range(51)]},
        {"album_ids": ["not-a-uuid"]},
        {"album_ids": [str(uuid.uuid4())], "limit": 0},
        {"album_ids": [str(uuid.uuid4())], "limit": 51},
    ],
)
async def test_invalid_input_is_422(client, body):
    response = await _post(client, **body)

    assert response.status_code == 422


async def test_seeds_without_terms_explain_the_empty_result(client, db_session):
    seed = await _album(db_session, "Untagged Seed")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.status_code == 200
    assert response.json() == {"results": [], "reason": "seeds_have_no_terms"}


async def test_tagged_seed_with_no_matches_has_no_reason(client, db_session):
    seed = await _album(db_session, "Lonely Seed", "lonely")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.json() == {"results": [], "reason": None}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_recommendations_api.py -q`
Expected: FAIL — most tests get `404 Not Found` for the unregistered route (the 422 cases may also fail on 404).

- [ ] **Step 3: Write the route**

Create `backend/src/crate_backend/api/routes/recommendations.py`:

```python
import uuid

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.db.session import get_session
from crate_backend.models.catalog import Album
from crate_backend.recommend.overlap import recommend_by_overlap, seeds_have_terms

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


class RecommendationRequest(BaseModel):
    album_ids: list[uuid.UUID] = Field(min_length=1, max_length=50)
    limit: int = Field(default=20, ge=1, le=50)


class RecommendedAlbum(BaseModel):
    id: str
    title: str
    artist_name: str | None
    release_year: int | None
    cover_art_url: str | None
    score: float
    shared_terms: list[str]


class RecommendationResponse(BaseModel):
    results: list[RecommendedAlbum]
    reason: str | None


@router.post("", response_model=RecommendationResponse)
async def recommend(
    request: RecommendationRequest, session: AsyncSession = Depends(get_session)
) -> RecommendationResponse:
    """Albums related to a group's seed albums by shared genres and tags."""
    seed_ids = list(dict.fromkeys(request.album_ids))
    found = set(await session.scalars(select(Album.id).where(Album.id.in_(seed_ids))))
    missing = [str(album_id) for album_id in seed_ids if album_id not in found]
    if missing:
        raise HTTPException(
            status_code=404, detail={"message": "Unknown album ids", "missing": missing}
        )

    if not await seeds_have_terms(session, seed_ids):
        return RecommendationResponse(results=[], reason="seeds_have_no_terms")

    ranked = await recommend_by_overlap(session, seed_ids, request.limit)
    albums = {
        album.id: album
        for album in await session.scalars(
            select(Album).where(Album.id.in_([r.album_id for r in ranked]))
        )
    }
    return RecommendationResponse(
        results=[
            RecommendedAlbum(
                id=str(r.album_id),
                title=albums[r.album_id].title,
                artist_name=albums[r.album_id].artist_name,
                release_year=albums[r.album_id].release_year,
                cover_art_url=albums[r.album_id].cover_art_url,
                score=r.score,
                shared_terms=r.shared_terms,
            )
            for r in ranked
        ],
        reason=None,
    )
```

- [ ] **Step 4: Register the router**

Modify `backend/src/crate_backend/main.py`: add the import after the albums router import, and include it after `app.include_router(albums_router)`:

```python
from crate_backend.api.routes.recommendations import router as recommendations_router
```

```python
    app.include_router(albums_router)
    app.include_router(recommendations_router)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_recommendations_api.py -q`
Expected: PASS (11 tests: 7 functions, one parametrized ×5)

- [ ] **Step 6: Measure latency on the real catalog**

Start the API: `cd backend && uv run uvicorn crate_backend.main:app --port 8000` (in the background), then run:

```bash
cd /Users/lukeklotz/Desktop/dev/crates
for title in "A Love Supreme" "Kid A"; do
  id=$(docker compose exec -T db psql -U crate -d crate -tAc "select id from albums where title = '$title' limit 1")
  curl -s -o /dev/null -w "$title: %{http_code} in %{time_total}s\n" \
    -X POST localhost:8000/recommendations -H 'Content-Type: application/json' \
    -d "{\"album_ids\": [\"$id\"]}"
done
```

Expected: both `200`, each well under 2 s (planning measured ~0.07 s and ~0.6 s for the query alone). Record both timings in the ledger. Stop the server afterwards.

- [ ] **Step 7: Full backend suite and lint**

Run: `cd backend && uv run pytest -q && uv run ruff check .`
Expected: all tests pass; `All checks passed!`

- [ ] **Step 8: Commit**

```bash
cd backend
git add src/crate_backend/api/routes/recommendations.py src/crate_backend/main.py tests/test_recommendations_api.py
git commit -m "feat: add POST /recommendations endpoint"
```

---

### Task 3: Frontend — album ids on cards and the proxy route

**Files:**
- Modify: `frontend/app/page.tsx` (`Item` type, `add()`, its one caller in the search results)
- Create: `frontend/app/api/recommendations/route.ts`

**Interfaces:**
- Consumes: `POST /recommendations` (Task 2).
- Produces: `Item.albumId: string` on every canvas card; `add(albumId, title, artist, src, x?, y?)`; frontend route `POST /api/recommendations` returning the backend body on success, `{"error": "Recommendations unavailable"}` with status 404/422 passed through or 502 otherwise. Consumed by Task 4.

There is no frontend test framework (adding one is out of scope per the spec). Verification is the TypeScript check, lint against the baseline, and calling the route against the running backend.

- [ ] **Step 1: Record baselines**

Run: `cd frontend && npx tsc --noEmit -p . ; echo "tsc exit $?" ; npx oxlint app/ 2>&1 | grep -oE "error [a-z-]+\([a-z-]+\)" | sort | uniq -c`
Expected: `tsc exit 0`; the 6 baseline findings listed in Global Constraints.

- [ ] **Step 2: Add `albumId` to cards**

In `frontend/app/page.tsx`, add the field to the `Item` type:

```ts
type Item = {
  id: string;
  albumId: string;
  title: string;
```

Change `add()` to take the album id first and store it:

```ts
  function add(
    albumId: string,
    title: string,
    artist: string,
    src: string,
    x?: number,
    y?: number,
  ) {
    checkpoint();
    const id = uid();
    setItems((a) => [
      ...a,
      {
        id,
        albumId,
        title,
```

(the rest of `add()` is unchanged). `duplicate()` already spreads `...item`, so copies keep `albumId`.

Update the one caller, in the search results list:

```tsx
                        add(
                          r.id,
                          r.title,
                          r.artist_name ?? 'Unknown artist',
                          r.cover_art_url ?? '/album-placeholder.svg',
                        );
```

- [ ] **Step 3: Type-check**

Run: `cd frontend && npx tsc --noEmit -p . ; echo "tsc exit $?"`
Expected: `tsc exit 0`. (If any other `add(` caller or `Item` literal surfaces, give it the album id — `grep -n "add(" app/page.tsx` found only the search-result caller at planning time.)

- [ ] **Step 4: Create the proxy route**

Create `frontend/app/api/recommendations/route.ts`:

```ts
const CRATE_API_URL = process.env.CRATE_API_URL ?? 'http://localhost:8000';

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return Response.json({ error: 'Invalid request' }, { status: 400 });
  }
  try {
    const response = await fetch(`${CRATE_API_URL}/recommendations`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(10000),
    });
    if (!response.ok) {
      const status = response.status === 404 || response.status === 422 ? response.status : 502;
      return Response.json({ error: 'Recommendations unavailable' }, { status });
    }
    return Response.json(await response.json());
  } catch {
    return Response.json({ error: 'Recommendations unavailable' }, { status: 502 });
  }
}
```

- [ ] **Step 5: Type-check and lint**

Run: `cd frontend && npx tsc --noEmit -p . ; echo "tsc exit $?" ; npx oxlint app/ 2>&1 | grep -oE "error [a-z-]+\([a-z-]+\)" | sort | uniq -c`
Expected: `tsc exit 0`; lint findings identical to the Step 1 baseline.

- [ ] **Step 6: Call the route against the running backend**

Start the backend (`cd backend && uv run uvicorn crate_backend.main:app --port 8000`) and the frontend (`cd frontend && npm run dev`) in the background; note the port the frontend prints (default 3000). Then:

```bash
cd /Users/lukeklotz/Desktop/dev/crates
id=$(docker compose exec -T db psql -U crate -d crate -tAc "select id from albums where title = 'A Love Supreme' limit 1")
curl -s -X POST localhost:3000/api/recommendations -H 'Content-Type: application/json' \
  -d "{\"album_ids\": [\"$id\"], \"limit\": 3}" | python3 -m json.tool | head -20
curl -s -o /dev/null -w "unknown id -> %{http_code}\n" -X POST localhost:3000/api/recommendations \
  -H 'Content-Type: application/json' -d '{"album_ids": ["00000000-0000-0000-0000-000000000000"]}'
```

Expected: the first prints 3 results with `title`, `score`, `shared_terms`; the second prints `unknown id -> 404`. Then stop the backend and repeat the first curl: expect `{"error": "Recommendations unavailable"}` (HTTP 502). Stop both servers.

- [ ] **Step 7: Commit**

```bash
git add frontend/app/page.tsx frontend/app/api/recommendations/route.ts
git commit -m "feat: keep album ids on canvas cards and proxy recommendation requests"
```

---

### Task 4: Frontend — recommendations in the group panel

**Files:**
- Modify: `frontend/app/page.tsx` (types, state, `findRecommendations`, group panel JSX)
- Modify: `frontend/app/globals.css` (styles for the results section)

**Interfaces:**
- Consumes: `Item.albumId`, `add(albumId, …)`, `POST /api/recommendations` (Task 3).
- Produces: the user-facing feature; nothing later depends on it.

- [ ] **Step 1: Add types, state, and the request function**

In `frontend/app/page.tsx`, add `Spinner` to the imports:

```ts
import { Spinner } from '@/components/ui/spinner';
```

Below the `SearchResult` type, add:

```ts
type Recommendation = {
  id: string;
  title: string;
  artist_name: string | null;
  release_year: number | null;
  cover_art_url: string | null;
  score: number;
  shared_terms: string[];
};
type RecommendationState = {
  status: 'loading' | 'ready' | 'error';
  results: Recommendation[];
  reason: string | null;
  // Sorted album ids the results were computed for; differs from the
  // group's current key when the group has changed since.
  seedKey: string;
};
const seedKeyOf = (albumIds: string[]) => [...new Set(albumIds)].sort().join(',');
```

Next to the other `useState` calls in `Home`, add:

```ts
  const [recommendations, setRecommendations] = useState<
    Record<string, RecommendationState>
  >({});
```

After `function createGroup() { … }`, add:

```ts
  async function findRecommendations(groupId: string) {
    const albumIds = [
      ...new Set(items.filter((i) => i.group === groupId).map((i) => i.albumId)),
    ];
    if (!albumIds.length) return;
    const seedKey = seedKeyOf(albumIds);
    setRecommendations((r) => ({
      ...r,
      [groupId]: {
        results: [],
        reason: null,
        seedKey,
        ...r[groupId],
        status: 'loading',
      },
    }));
    try {
      const response = await fetch('/api/recommendations', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ album_ids: albumIds }),
      });
      if (!response.ok) throw new Error();
      const data = (await response.json()) as {
        results: Recommendation[];
        reason: string | null;
      };
      setRecommendations((r) => ({
        ...r,
        [groupId]: { status: 'ready', results: data.results, reason: data.reason, seedKey },
      }));
    } catch {
      setRecommendations((r) => ({
        ...r,
        [groupId]: {
          results: [],
          reason: null,
          seedKey,
          ...r[groupId],
          status: 'error',
        },
      }));
    }
  }
```

Right after the existing line `const group = groups.find((g) => g.id === activeGroup);`, add:

```ts
  const groupSeedKey = group
    ? seedKeyOf(items.filter((i) => i.group === group.id).map((i) => i.albumId))
    : '';
  const groupRecs = group ? recommendations[group.id] : undefined;
  const recsStale = !!groupRecs && groupRecs.seedKey !== groupSeedKey;
```

- [ ] **Step 2: Disable the popularity options**

In the group panel, add `disabled` to the `RadioGroup`:

```tsx
                <RadioGroup
                  className="popularity-options"
                  value={group.popularity}
                  disabled
```

- [ ] **Step 3: Replace the design-preview note with the recommendations section**

Replace the whole `<div className="prototype-note"> … </div>` block with:

```tsx
                <p className="rec-note">
                  Coming soon — popularity data is still being collected.
                </p>
                <div className="control-heading">
                  <h3>RECOMMENDATIONS</h3>
                  <span>02 / RESULTS</span>
                </div>
                {recsStale && groupRecs?.status !== 'loading' && (
                  <p className="rec-note">
                    Group changed. These results are for its earlier albums.
                  </p>
                )}
                <button
                  className="primary find-button"
                  disabled={!groupSeedKey || groupRecs?.status === 'loading'}
                  onClick={() => void findRecommendations(group.id)}
                >
                  {groupRecs?.status === 'loading' ? (
                    <>
                      <Spinner /> FINDING RECOMMENDATIONS…
                    </>
                  ) : recsStale ? (
                    'UPDATE RECOMMENDATIONS'
                  ) : (
                    'FIND RECOMMENDATIONS'
                  )}
                </button>
                {groupRecs?.status === 'error' && (
                  <p className="rec-note" role="alert">
                    Recommendations are unavailable. Try again.
                  </p>
                )}
                {groupRecs?.status === 'ready' && !groupRecs.results.length && (
                  <p className="rec-note">
                    {groupRecs.reason === 'seeds_have_no_terms'
                      ? 'No related albums found — these albums have few genres or tags in the catalog.'
                      : 'No related albums found.'}
                  </p>
                )}
                {!!groupRecs?.results.length && (
                  <div className="rec-results">
                    {groupRecs.results.map((r) => (
                      <div className="rec-result" key={r.id}>
                        <img src={r.cover_art_url ?? '/album-placeholder.svg'} alt="" />
                        <span>
                          <strong>{r.title}</strong>
                          <small>
                            {r.artist_name ?? 'Unknown artist'}
                            {r.release_year ? ` / ${r.release_year}` : ''}
                          </small>
                          <small className="rec-terms">
                            Shares: {r.shared_terms.join(', ')}
                          </small>
                        </span>
                        <button
                          aria-label={`Add ${r.title} to sandbox`}
                          title="Add to sandbox"
                          onClick={() =>
                            add(
                              r.id,
                              r.title,
                              r.artist_name ?? 'Unknown artist',
                              r.cover_art_url ?? '/album-placeholder.svg',
                            )
                          }
                        >
                          <Plus size={18} />
                        </button>
                      </div>
                    ))}
                  </div>
                )}
```

(The existing `KEEP EXPLORING` button below stays as it is.)

- [ ] **Step 4: Add styles**

Append to `frontend/app/globals.css`, next to the existing `.prototype-note` rules (which can be deleted, since the note is gone):

```css
.rec-note {
  font-size: 13px;
  line-height: 1.6;
  color: #626457;
  margin-top: 8px;
}
.find-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px;
  margin-top: 12px;
}
.rec-results {
  display: flex;
  flex-direction: column;
  gap: 3px;
  margin-top: 12px;
}
.rec-result {
  display: flex;
  align-items: center;
  gap: 14px;
  border-bottom: 1px solid #24439422;
  padding: 10px 0;
}
.rec-result img {
  width: 58px;
  height: 58px;
  object-fit: cover;
  border: 1px solid #17171733;
}
.rec-result > span {
  flex: 1;
  min-width: 0;
}
.rec-result strong {
  display: block;
  font-weight: 500;
  font-size: 14px;
}
.rec-result small {
  display: block;
  font-family: var(--font-label), monospace;
  font-size: 11px;
  color: #676858;
  margin-top: 5px;
}
.rec-result .rec-terms {
  color: var(--blue);
}
```

Before deleting `.prototype-note` rules, confirm nothing else uses the class: `grep -rn "prototype-note" app/` must show only `globals.css`.

- [ ] **Step 5: Type-check and lint**

Run: `cd frontend && npx tsc --noEmit -p . ; echo "tsc exit $?" ; npx oxlint app/ 2>&1 | grep -oE "error [a-z-]+\([a-z-]+\)" | sort | uniq -c`
Expected: `tsc exit 0`; lint = baseline plus exactly one more `next(no-img-element)` (the result cover), nothing else new. If `react(react-compiler)` count rises, read the message and fix the code rather than accept it.

- [ ] **Step 6: Smoke-check the page renders**

Start backend and frontend as in Task 3 Step 6. Run `curl -s localhost:3000 | grep -c "UNTITLED SANDBOX"` — expected `1` or more (the page's `<h1>` renders without a server error). Stop both servers.

- [ ] **Step 7: Commit**

```bash
git add frontend/app/page.tsx frontend/app/globals.css
git commit -m "feat: show genre/tag-overlap recommendations in the group panel"
```

- [ ] **Step 8: Hand the visual check to the owner**

The executor cannot click through the UI. Include this checklist in the final message for the owner to run in a browser (backend + `npm run dev` running):

1. Search "A Love Supreme", add it; search "Kind of Blue", add it. Select both, **Create group**, open the group panel.
2. Popularity options are greyed out with the "Coming soon" note.
3. Press **Find recommendations** → spinner, then jazz albums with "Shares: …" lines.
4. Press **+** on a result → it appears on the canvas, not in the group.
5. Duplicate a card in the group (so the same album appears twice) → recommendations don't change when updated.
6. Add another album to the group → "Group changed" note appears and the button reads **Update recommendations**; pressing it replaces the results.
7. Stop the backend and press the button → "Recommendations are unavailable" and the old results stay visible.
