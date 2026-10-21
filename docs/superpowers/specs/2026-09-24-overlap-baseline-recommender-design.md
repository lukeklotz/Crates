# Genre/tag-overlap baseline recommender — design

**Status:** Design approved in conversation 2026-09-24; pending review of this written spec.

## Purpose

Phase 3 of `crate-ml-engineering-project-plan.md` calls for non-ML recommendation baselines that later models must beat. This project deliberately runs a **thin** Phase 3: one simple, explainable baseline, then straight on to Phase 4 (TF-IDF). The goal of this slice is that a user can put albums in a group, press **Find recommendations**, and see related albums with the reason each was suggested — the first time Crate shows real recommendations.

## Scope

In scope:
- A Jaccard genre/tag-overlap recommender and a `POST /recommendations` endpoint.
- Wiring the frontend group panel to call it and display results.

Explicitly out of scope for this slice (deferred, not forgotten):
- **Evaluation:** no hand-labelled answer key, no scoring script, no Recall@K/NDCG@K. The owner will handle evaluation later.
- **Popularity steering:** the recommender ignores popularity; the panel's popularity options are shown disabled. (Popularity data is being backfilled separately — see `2026-09-24-lastfm-popularity-signal-design.md`.)
- **Persisted runs:** no `RecommendationRun`/`Recommendation` rows. Those tables require a server-side group, and groups currently exist only in the browser.
- **Precomputation:** scores are computed per request.
- Diversity re-ranking, per-album influence, same-artist limits, the shared-musician graph (blocked by missing per-album credits from Phase 2), and any frontend test framework.

## Scoring

**Terms.** An album's term set is the union of its genre names and tag names, lowercased and de-duplicated, so a MusicBrainz genre "rock" and a tag "rock" count as one term. Vote counts are ignored.

**Similarity.** For a seed `S` and candidate `C`, similarity is Jaccard:

```
jaccard(S, C) = |terms(S) ∩ terms(C)| / |terms(S) ∪ terms(C)|
```

Jaccard was chosen over counting shared terms (and over vote-weighted overlap) because heavily tagged albums — often the famous ones, with 30–40 tags — share *something* with nearly everything and would dominate a raw count. Under Jaccard, an album sharing 4 of its 5 terms outranks one sharing 4 of its 40. Its known weakness — sharing a common term like "rock" counts as much as sharing a rare one like "glitch" — is exactly what Phase 4's TF-IDF addresses, which keeps the later comparison meaningful.

**Groups.** A candidate's score is the sum of its Jaccard similarity to each seed, so every seed has equal influence (each contributes at most 1.0).

**Candidates and ordering.**
- Candidates are albums sharing at least one term with at least one seed.
- Seed albums are never returned. Other albums by a seed's artist are allowed.
- Order: score descending, then total number of distinct shared terms descending, then title ascending, then album id — fully deterministic.

**Explanations.** Each result lists the terms it shares with the union of the seeds' terms, ordered by how many seeds share the term (descending), then alphabetically.

## Backend

**Module:** `backend/src/crate_backend/recommend/overlap.py`

```python
@dataclass(frozen=True)
class OverlapRecommendation:
    album_id: uuid.UUID
    score: float
    shared_terms: list[str]

async def recommend_by_overlap(
    session: AsyncSession, seed_ids: list[uuid.UUID], limit: int
) -> list[OverlapRecommendation]: ...
```

Implemented as one SQL query (CTEs: per-album term sets, seed terms, per-candidate shared counts and term totals, Jaccard summed per candidate, ordered and limited), plus a second query fetching shared term names for only the returned albums. Callers are responsible for validating `seed_ids`.

**Endpoint:** `POST /recommendations` in `backend/src/crate_backend/api/routes/recommendations.py`, registered in `main.py`.

Request:
```json
{ "album_ids": ["<uuid>", "..."], "limit": 20 }
```
- `album_ids`: 1–50 UUIDs; duplicates are collapsed.
- `limit`: optional, default 20, 1–50.
- No authentication (same as `/albums/search`).

Response `200`:
```json
{
  "results": [
    {
      "id": "<uuid>", "title": "…", "artist_name": "…", "release_year": 2000,
      "cover_art_url": "…", "score": 0.83, "shared_terms": ["post-rock", "ambient"]
    }
  ],
  "reason": null
}
```
- `reason` is `"seeds_have_no_terms"` (with empty `results`) when none of the seeds has any genre or tag, so the UI can explain the empty result instead of looking broken. An empty `results` with `reason: null` means the seeds have terms but nothing else in the catalog shares them.

Errors:
- `404` if any `album_ids` are not in the catalog; the detail lists the missing ids.
- `422` for malformed input (empty list, more than 50 ids, non-UUID values, `limit` out of range) — FastAPI/Pydantic validation.

**Performance.** Computed per request over the ~25,000-album catalog. Expected to be a few hundred milliseconds; measured against the real dev catalog during implementation and recorded. If it's far slower, add an index or precompute term sets — but not preemptively.

## Frontend

- **Album identity on cards:** `Item` in `frontend/app/page.tsx` gains `albumId: string`; `add()` receives it from the search result; duplicating a card preserves it.
- **Proxy:** `frontend/app/api/recommendations/route.ts` forwards a POST to `${CRATE_API_URL}/recommendations`, mirroring `app/api/search/route.ts` (10-second timeout; `502 {"error": "Recommendations unavailable"}` on failure; passes a backend `404` through as an error).
- **Group panel:**
  - The "DESIGN PREVIEW" placeholder becomes a **Find recommendations** button, sending the group's distinct `albumId`s.
  - Results show cover, title, artist, year, "Shares: …" (shared terms), and an **Add to sandbox** button that places the album on the canvas (not into the group — results never automatically become group members).
  - States: loading (spinner), error ("Recommendations are unavailable. Try again."), empty ("No related albums found — these albums have few genres or tags in the catalog." for `seeds_have_no_terms`; "No related albums found." otherwise), and **stale**: if the group's membership changes after results arrive, the previous results stay visible with a "Group changed" note and the button reads **Update recommendations**.
  - Results are kept per group in page state (not persisted).
  - Popularity options are rendered disabled with the note "Coming soon — popularity data is still being collected."

## Error handling and edge cases

- A single-album group is valid and produces recommendations.
- Seeds that share no terms with any other album yield empty results with `reason: null`.
- A mix of tagged and untagged seeds: untagged seeds contribute nothing; tagged seeds still produce results.
- The same album on the canvas twice in one group is sent once.
- Backend unreachable: the panel shows the error state; existing results (if any) remain visible.

## Testing

Backend (pytest, `backend/tests/test_recommend_overlap.py` and `backend/tests/test_recommendations_api.py`). The dev database holds the real catalog, so fixtures use distinctive terms (e.g. `zzfixture-ambient`) that no real album has:
- Jaccard ordering, including a candidate sharing 4 of 5 terms outranking one sharing 4 of 40.
- Multi-seed summing, with equal seed influence.
- Seeds excluded from results.
- A genre and tag with the same name counted once.
- Deterministic tie-breaking.
- Shared-term explanations.
- API: 200 shape, `limit` respected, duplicate ids collapsed, 404 for unknown ids, 422 for empty/oversized/malformed input, `seeds_have_no_terms` reason.

Frontend (no test framework exists; adding one is out of scope): `oxlint`, a TypeScript type check (`tsc --noEmit`), and calling the proxy route directly against a running backend. The owner does the final visual check in the browser, following steps provided at hand-off.

## Related files

- `crate-ml-engineering-project-plan.md` — Phase 3 (thin version of steps 2, 5 and 7).
- `backend/src/crate_backend/models/catalog.py` — `Album`, `Genre`, `Tag`, `AlbumGenre`, `AlbumTag`.
- `backend/src/crate_backend/api/routes/albums.py` — existing search route (response-shape conventions).
- `frontend/app/page.tsx` — canvas, groups, and the group panel.
- `frontend/app/api/search/route.ts` — the proxy pattern to mirror.
