# Recommendation systems

This is the home for every recommendation approach Crate has tried. It covers how each one works, how it performed, and what went wrong. Each approach gets its own section. The summary table shows at a glance what exists and how they compare.

Design specs record *why* an approach was built the way it was. This document records *what it is and how it's doing*. Keep it up to date when an approach ships, changes, or is retired.

## How recommendations work in Crate

Every approach answers the same question: **given the albums in a user's group (the "seeds"), which other albums in the catalog are related to them?**

- **Catalog:** about 25,000 albums, each a MusicBrainz *release group* (one entry per album, not per pressing). The data comes from the 2026-09-23 MusicBrainz snapshot. Each album has MusicBrainz genres (a curated vocabulary) and tags (free-form labels voted on by volunteers), plus artist relationships (band membership, collaborations). Per-album credits (musicians, producers, labels) are **not** available; see Phase 2's status in the project plan.
- **Wikipedia text (Phase 4):** full English Wikipedia article text for albums that MusicBrainz links to Wikidata or English Wikipedia, stored in `album_texts` (fetched 2026-09-28; 12,799 albums, 51% of the catalog, 79 MB of text). Coverage is strongly skewed to popular albums: 96% of the top popularity quartile vs 9% of the bottom. Links that redirect to the artist's own article or discography (217 albums) are stored as "no text". Text is CC BY-SA and is used only as model features, never displayed. Refresh with `scripts/link_wikidata.py` then `scripts/backfill_wikipedia_text.py`.
- **Request:** the frontend sends the distinct album IDs in a group to `POST /recommendations`. One seed is enough; groups can have up to 50.
- **Contract every approach must keep:**
  - Seeds are never recommended back.
  - Results are ranked, and ties are broken deterministically.
  - Every result carries an explanation built from real shared evidence.
  - Adding an album to a group is *search context*, not a rating. It says "find things like these," not "I like this."
- **Popularity** (Last.fm listener percentile, `Album.popularity`) exists as a separate signal but is **not** used by any approach yet. See `docs/superpowers/specs/2026-09-24-lastfm-popularity-signal-design.md`.

## Summary

| # | Approach | Phase | Status | Signal used | Evaluated? |
|---|---|---|---|---|---|
| 1 | Genre/tag overlap (Jaccard) | 3 | **Live** since 2026-09-24 | Genre + tag names | No (see [Evaluation](#evaluation)) |
| 2 | TF-IDF text similarity | 4 | Planned | Genre + tag text, weighted by rarity | — |
| 3 | Semantic embeddings | 5 | Planned | Pretrained text embeddings of album descriptions | — |

## Evaluation

**No approach has been measured yet.** The metrics this project will use, defined once here:

- **Recall@K:** of the albums that truly belong in a seed's recommendations, the fraction that appear in the top K results. Example: 5 good matches exist and 3 are in the top 10, so Recall@10 = 0.6.
- **NDCG@K** (Normalized Discounted Cumulative Gain): like recall, but it also rewards ranking the good albums near the top. It runs from 0.0 to 1.0.
- **Catalog coverage:** the share of the catalog that ever appears in recommendations. Low coverage means the recommender keeps suggesting the same albums.

Both Recall@K and NDCG@K need an **answer key**: seed albums paired with hand-graded candidates (0 = not relevant, 1 = related, 2 = great match), built by pooling each approach's top results. Building that key was deliberately deferred. It is required before Phase 4's TF-IDF can honestly be claimed to beat approach 1. Until then, judge results by eye and say so.

---

## 1. Genre/tag overlap (Jaccard)

**Status:** Live since 2026-09-24. It is the Phase 3 baseline that later approaches must beat.
**Spec:** `docs/superpowers/specs/2026-09-24-overlap-baseline-recommender-design.md`
**Code:** `backend/src/crate_backend/recommend/overlap.py` (scoring), `backend/src/crate_backend/api/routes/recommendations.py` (endpoint). The frontend lives in `frontend/app/page.tsx` (group panel) and `frontend/app/api/recommendations/route.ts` (proxy).

### How it works

1. **Terms.** Each album's terms are its genre names plus its tag names, lowercased, with duplicates removed. A genre "rock" and a tag "Rock" count once. MusicBrainz vote counts are ignored.
2. **Similarity.** For a seed and a candidate, the score is their Jaccard similarity: *shared terms ÷ all distinct terms across both albums*, from 0 to 1.
3. **Groups.** A candidate's score is its Jaccard similarity to each seed, **summed**. Each seed can contribute at most 1.0, so every seed has equal influence.
4. **Candidates.** Any album sharing at least one term with any seed is a candidate. Seeds are excluded. Other albums by a seed's artist are allowed.
5. **Order.** Score (high first), then number of distinct shared terms, then title, then album ID. The order is fully deterministic.
6. **Explanation.** Each result lists its shared terms, starting with those shared by the most seeds, then alphabetically. The UI shows them as "Shares: …".

**Why Jaccard rather than counting shared tags?** Heavily tagged albums, often the famous ones with 30–40 tags, share *something* with almost everything and would dominate a raw count. Jaccard divides by the size of the combined term set, so an album sharing 4 of its 5 tags beats one sharing 4 of its 40.

### Worked example

Seed: *A Love Supreme* (John Coltrane). Top result: *Impressions* (John Coltrane).

| | Terms |
|---|---|
| *A Love Supreme* (9) | avant-garde jazz, free jazz, hard bop, jazz, modal, modal jazz, post bop, post-bop, spiritual jazz |
| *Impressions* (7) | avant-garde jazz, free jazz, jazz, modal, modal jazz, post bop, post-bop |

All 7 of *Impressions*' terms are shared, and there are 9 distinct terms across both albums. Score = 7 / 9 = **0.778**. The next results are *Africa/Brass* (0.667) and *Crescent* (0.583), then Alice Coltrane's *Journey in Satchidananda* and several modal-era Miles Davis albums.

The example also shows a limitation: "post bop" and "post-bop" are counted as two different terms.

### API

`POST /recommendations`, no login required.

```json
// request
{ "album_ids": ["<uuid>", "..."], "limit": 20 }

// response
{
  "results": [
    { "id": "…", "title": "Impressions", "artist_name": "John Coltrane", "release_year": 1963,
      "cover_art_url": "…", "score": 0.778, "shared_terms": ["avant-garde jazz", "free jazz", "…"] }
  ],
  "reason": null
}
```

- `album_ids`: 1–50 IDs. Duplicates are collapsed.
- `limit`: 1–50, default 20.
- `reason`: `"seeds_have_no_terms"` means none of the seeds has any genres or tags. An empty `results` with `reason: null` means the seeds have terms but no other album shares them.
- Errors: `404` when some IDs aren't in the catalog (the response lists the `missing` IDs); `422` for invalid input.
- Live schema: http://localhost:8000/docs while the backend is running.

### Performance

Scores are computed on every request with no precomputation, against the full catalog. Measured on the dev machine, 2026-09-24:

| Seeds | Time |
|---|---|
| 1 album with specific tags (*A Love Supreme*) | ~0.06 s |
| 1 album with broad tags (*Kid A*: rock, electronic…) | ~0.5 s |
| 5 albums with broad tags | ~0.6 s |
| 50 most heavily tagged albums (extreme case) | ~1.4–1.6 s |

Broad terms make most of the catalog a candidate, and counting every candidate's full term set is what costs the time. If real groups get large, precompute each album's term count.

### Known limitations

- **Common and rare terms count the same.** Sharing "rock" counts as much as sharing "glitch." This is the main thing Phase 4's TF-IDF should improve.
- **No text normalization beyond lowercasing.** "post bop" and "post-bop" are different terms, and synonyms aren't merged.
- **Only as good as MusicBrainz tagging.** Albums with few or no genres and tags get weak or no recommendations. Tagging is densest for Western rock, pop and electronic music, so other genres are likely served worse.
- **No popularity steering.** The popularity options in the UI are disabled.
- **Albums already on the canvas** (outside the group) can be recommended. Only seeds are excluded.
- **Not evaluated.** Quality so far has only been judged by eye.

### Known issues (deferred)

From the final code review, 2026-09-24. None blocked shipping.

1. **Tie order can hinge on rounding.** Floating-point summation can separate true ties by the last bit, so rounding noise, not the shared-term/title tie-breaks, decides their order. Fix: order by `round(score::numeric, 9)`.
2. **"Group changed" note with nothing under it.** The note can appear when there are no results to be stale, for example after a failed first request. Fix: only show it when there are results.
3. **Misleading error for missing albums.** An album that has left the catalog produces a 404, which the panel shows as "unavailable, try again." Retrying can never help.
4. **Saved results for deleted groups are never cleared from memory.** This is harmless, and it lets Undo bring results back.
5. **No login or rate limit on the endpoint.** Its worst case is about 1.5 s per request. This must be revisited before any public deployment.

---

## Planned approaches

Short notes only; each gets a full section like approach 1 once it's built.

### 2. TF-IDF text similarity (Phase 4)

Each album becomes a short "document" of its terms. TF-IDF (Term Frequency–Inverse Document Frequency) weights each term by how strongly it applies to the album and how *rare* it is across the catalog, so sharing "glitch" counts for more than sharing "rock." Albums are compared by cosine similarity of these weighted vectors. It should fix approach 1's biggest weakness directly. Comparing it fairly requires the evaluation answer key described above.

### 3. Semantic embeddings (Phase 5)

A pretrained text-embedding model turns album descriptions into vectors, so albums described in *different words with similar meaning* can match. This is something neither approach 1 nor 2 can do.

---

## Adding a new approach

Copy the structure of approach 1:
- status and dates
- links to the spec and code
- how it works
- a worked example with real numbers
- API or interface changes
- measured performance
- evaluation results against the previous approaches, using the same answer key
- known limitations and known issues

Then add a row to the summary table. When an approach is retired, keep its section and mark it **Retired**, with the reason. What didn't work is part of the record.
