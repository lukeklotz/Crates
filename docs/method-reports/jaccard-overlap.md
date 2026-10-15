# Recommendation report: genre/tag overlap (Jaccard)

## How it works

Each album becomes a **set** of its MusicBrainz genre and tag names. Names are lowercased and duplicates removed; vote counts are ignored. For one seed album and one candidate, Jaccard similarity is:

```text
shared terms / distinct terms across both albums
= |seed terms ∩ candidate terms| / |seed terms ∪ candidate terms|
```

The SQL in [`overlap.py`](../../backend/src/crate_backend/recommend/overlap.py) computes that fraction for each seed, then sums the fractions for a candidate:

```sql
SELECT s.candidate_id,
       sum(s.n_shared::float / (ss.n + cs.n - s.n_shared)) AS score
FROM shared s
JOIN seed_sizes ss ON ss.seed_id = s.seed_id
JOIN candidate_sizes cs ON cs.album_id = s.candidate_id
GROUP BY s.candidate_id
```

Here `ss.n + cs.n - s.n_shared` is the union size. Only albums sharing at least one term with a seed are candidates. Seed albums are excluded. Results are ordered by score, distinct shared-term count, title, then ID. A second query retrieves the actual shared terms for the “Shares” explanation. The API's default `approach` is `"overlap"`.

## Analogy and ELI5 example

Think of each album as a bag of labeled stickers. Two albums match when they have many of the same stickers **relative to all the different stickers in both bags**.

Suppose the seed has `{jazz, modal, spiritual}`. Candidate A has `{jazz, modal, spiritual, live}`: three shared stickers out of four distinct stickers, for **3/4 = 0.75**. Candidate B has `{jazz, modal, rock, electronic, ambient}`: two shared out of six distinct, for **2/6 ≈ 0.33**. A ranks higher. With two seed albums, calculate each pair's fraction and add them; each seed can contribute at most 1.

## Why it was chosen

The design calls this the first simple, explainable recommendation baseline. It gets real group recommendations working before introducing a trained model and gives later methods a benchmark to beat. Jaccard was chosen over raw shared-tag counting because heavily tagged albums, often well-known ones, would otherwise match almost everything. Dividing by the union size reduces that advantage. Genres and tags are already present in the MusicBrainz catalog, so this method needs no article text or offline model build.

## Tradeoffs

- **Strengths:** Simple scoring, direct explanations, no model file, and immediate use of current catalog tags. Multiple seeds have equal maximum influence.
- **Limitations:** A broad term such as `rock` counts exactly as much as a distinctive term such as `glitch`. Lowercasing alone does not merge `post-bop` with `post bop`, or recognize synonyms. Albums with few or no tags can be missed. Tag coverage reflects the biases of MusicBrainz contributors.
- **Operational cost:** Scores are recomputed in PostgreSQL on each request. Broad seed tags can make much of the catalog a candidate. The current implementation also has a documented floating-point tie-order issue: tiny rounding differences can decide ties before the explicit tie-breakers.
- **Scope:** This method measures metadata overlap, not acoustic similarity or personalized taste. It does not use the popularity preference.

## Source pointers

- [`backend/src/crate_backend/recommend/overlap.py`](../../backend/src/crate_backend/recommend/overlap.py), lines 20–124: term sets, scoring, ranking, explanations.
- [`backend/src/crate_backend/api/routes/recommendations.py`](../../backend/src/crate_backend/api/routes/recommendations.py), lines 20–26 and 85–92: default and dispatch.
- [`docs/superpowers/specs/2026-09-24-overlap-baseline-recommender-design.md`](../superpowers/specs/2026-09-24-overlap-baseline-recommender-design.md): design rationale.
