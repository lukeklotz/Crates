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
