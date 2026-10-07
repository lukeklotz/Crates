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
| 2 | TF-IDF text similarity | 4 | **Built** 2026-10-06, opt-in (`approach: "tfidf"`), not the default | Genre/tag votes + Wikipedia text, weighted by rarity | Pending (Phase 4, Milestone 3) |
| 3 | Semantic embeddings | 5 | Planned | Pretrained text embeddings of album descriptions | — |

## Evaluation

**No approach has been measured yet.** The answer key and the tools to build it exist (Phase 4, Milestone 3, 2026-10-07); grading is in progress.

### The answer key

The key lives in top-level `eval/` and is committed:

- `seeds.json`: 25 single-album seeds, 7 from the top popularity quartile and 6 from each of the others, spread across ten broad genres (jazz, rock, electronic, hip hop, metal, folk, pop, classical, soul/R&B, world), no two by the same artist, each with at least 5 genre/tag terms. Proposed by a script, then reviewed by hand: grading is only as good as the grader's familiarity with the seed.
- `judgments.jsonl`: one hand grade per line, `{seed_id, candidate_id, grade, graded_at}`. Grades are keyed by (seed, candidate), not by approach, so every approach, including Phase 5's, reuses them and only albums nobody has graded need grading. A grade can be corrected by appending a new line; the last line for a pair wins.
- `results/YYYY-MM-DD.md`: the report from each scoring run.

The rubric:

- **2:** I'd recommend it to someone who loves the seed.
- **1:** Clearly related and plausible.
- **0:** Not relevant.
- Grade same-artist albums on their merits.

### Running it

All commands run from `backend/`.

1. `uv run python -m crate_backend.evaluation.seeds propose` writes `eval/seeds.json` (refuses to overwrite it without `--force`).
2. `uv run python -m crate_backend.evaluation.seeds list` shows the seeds by number; `... seeds swap N "title words" [--artist NAME]` replaces seed N with an album you pick from the search results.
3. `uv run python -m crate_backend.evaluation.pool [--variants a,b,c]` takes each variant's top 10 per seed and writes the pairs nobody has graded to `eval/pool.jsonl` (a working file, not committed). Default: the three core variants.
4. `uv run python -m crate_backend.evaluation.grade` shows each pair one at a time, grouped by seed, in random order, without saying which approach produced it. Each album shows title, artist, year, top 8 genre/tag terms and the first sentence of its Wikipedia article. Keys (no Enter needed): `0`/`1`/`2` grade, `s` skip, `u` undo the last grade, `q` quit. Every grade is saved immediately; rerun to resume.
5. `uv run python -m crate_backend.evaluation.score [--variants a,b,c]` prints the report and saves it to `eval/results/`.

### Metrics

All at K = 10, per variant, over all seeds and per popularity quartile:

- **NDCG@10** (Normalized Discounted Cumulative Gain), the headline metric. Each result earns `2^grade − 1` (a 2 is worth three 1s), discounted the further down the list it sits, divided by the best score possible from every album graded for that seed. 1.0 means the best-graded albums found by any approach are at the top. Example: for *Kid A*, a list that puts *Amnesiac* (graded 2) first scores higher than one that has it tenth.
- **Pooled Recall@10:** of all the albums graded 1 or 2 for a seed (whichever approach found them), the share in this variant's top 10. Example: 6 good albums known for a seed, 3 in the top 10, so 0.5.
- **Judged@10:** the share of the top 10 that has a grade. Ungraded results count as 0, so a row where any seed is below 0.9 is marked ⚠: the approach changed since grading, and the new pool needs grading before the row means anything.
- **Median popularity** of returned albums: shows whether an approach leans to famous or obscure albums.
- **Artists in top 10:** mean number of distinct artists, a diversity check (same-artist crowding).
- **Wins / losses / ties:** per seed, which of two variants had the higher NDCG@10. With 25 seeds, a consistent win count is more trustworthy than a small difference in averages.

Seeds where nothing was graded 1 or 2 have no NDCG or Recall and are left out of the averages; the report's "Scored" column shows how many seeds counted.

**Catalog coverage** (the share of the catalog that ever appears in recommendations) is not measured yet.

### Variants

| Variant | What changes | Model file | Build |
|---|---|---|---|
| `overlap` | Approach 1 (Jaccard) | none | — |
| `tfidf-tags` | Approach 2, α = 1.0 (tags only) | `models/tfidf.joblib` | `scripts.build_tfidf_model` |
| `tfidf-tags+text` | Approach 2, α = 0.6 (the default blend) | `models/tfidf.joblib` | same |
| `tfidf-a0.4`, `tfidf-a0.8` | α = 0.4 / 0.8 (stretch) | `models/tfidf.joblib` | same |
| `tfidf-no-reception` | No Reception sections (stretch) | `models/tfidf-no-reception.joblib` | `... --no-reception --out models/tfidf-no-reception.joblib` |
| `tfidf-no-personnel` | No Personnel/Credits sections (stretch) | `models/tfidf-no-personnel.joblib` | `... --no-personnel --out models/tfidf-no-personnel.joblib` |
| `tfidf-no-bigrams` | Single words only (stretch) | `models/tfidf-no-bigrams.joblib` | `... --no-bigrams --out models/tfidf-no-bigrams.joblib` |

α (the tag weight in the TF-IDF blend) is applied at scoring time, so the α variants share one model file. Stretch variants are graded only after the core three; each usually adds 2–4 new pairs per seed.

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
{ "album_ids": ["<uuid>", "..."], "limit": 20, "approach": "overlap" }

// response
{
  "approach": "overlap",
  "model_version": null,
  "results": [
    { "id": "…", "title": "Impressions", "artist_name": "John Coltrane", "release_year": 1963,
      "cover_art_url": "…", "score": 0.778, "shared_terms": ["avant-garde jazz", "free jazz", "…"],
      "shared_text_terms": [] }
  ],
  "reason": null
}
```

- `album_ids`: 1–50 IDs. Duplicates are collapsed.
- `limit`: 1–50, default 20.
- `approach`: `"overlap"` (default) or `"tfidf"` (approach 2). Overlap responses always have `model_version: null` and empty `shared_text_terms`.
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

## 2. TF-IDF text similarity

**Status:** Built 2026-10-06. Opt-in with `approach: "tfidf"`; **not** the default. The default changes only if the Milestone 3 answer key says TF-IDF wins.
**Spec:** `docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md` (Milestone 2); plan `docs/superpowers/plans/2026-10-06-tfidf-recommender.md`.
**Code:** `backend/src/crate_backend/recommend/text_cleaning.py` (term and article preparation), `recommend/tfidf.py` (model build, scoring, explanations, save/load), `recommend/model_store.py` (per-process model cache), `scripts/build_tfidf_model.py` (build), `api/routes/recommendations.py` (endpoint). The frontend shows `shared_text_terms` as "Described alike: …".

### How it works

Each album gets two rows of weights, called *blocks*. Each row is scaled to length 1, so the dot product of two rows is their cosine similarity (0–1).

1. **Tag block (every album).** Each genre or tag name is one whole term, normalized first: lowercase, `-`/`_` → space, `&` → "and". "Post-Bop" and "post bop" are now one term, which fixes approach 1's duplicate-term problem. Weight = **TF × IDF**:
   - TF = 1 + ln(votes) (0 votes count as 1), so 10 votes count about 3× one vote, not 10×. When a term appears as both a genre and a tag, the higher vote count is used.
   - IDF = ln((1 + N) / (1 + albums with the term)) + 1, so rare terms ("spiritual jazz") outweigh common ones ("jazz").
2. **Text block (albums with a Wikipedia article).** The article is cleaned first. Track listings, charts, certifications, release history, references and similar sections are dropped. Personnel/Credits sections are kept, but only lines with a musical or production role; crew-only lines (mastering, engineering, photography, design…) are dropped. Then words and two-word phrases are counted, after removing English stop words and music-press filler ("album", "released", "billboard"…). Terms in only one article (`min_df=2`) or in over half of them (`max_df=0.5`) are dropped. TF = 1 + ln(count), and IDF is computed over the articles.
3. **Similarity.** If both albums have text: 0.6 × tag cosine + 0.4 × text cosine. Otherwise: tag cosine alone, so an album without an article is compared on tags, not penalized.
4. **Groups.** A candidate's score is its similarity to each seed, summed, so every seed has equal influence. Seeds are excluded, and only scores above 0 are returned.
5. **Order.** Score rounded to 9 decimals (high first), then title, then album ID. Fully deterministic.
6. **Explanations.** For each result, a term's *contribution* = (its weight summed over the seeds) × (its weight in the result). `shared_terms` lists the top 5 tag terms by contribution, and `shared_text_terms` the top 5 text terms.

### Worked example

Seed: *A Love Supreme* (John Coltrane). Model built 2026-10-06T16:19:44Z.

| # | Result | Score | Article? | Shares | Described alike |
|---|---|---|---|---|---|
| 1 | *The 7th Hand* (Immanuel Wilkins) | 0.610 | no | post bop, free jazz, spiritual jazz, jazz | — |
| 2 | *New York City Philharmonic Hall at Lincoln Center, February 12, 1964* (Miles Davis Quintet) | 0.599 | no | hard bop, post bop, jazz, modal | — |
| 4 | *"Live" at the Village Vanguard* (John Coltrane) | 0.563 | yes | modal jazz, spiritual jazz, hard bop, jazz, post bop | coltrane, garrison, jimmy garrison, impulse, trane |
| 6 | *Crescent* (John Coltrane Quartet) | 0.551 | yes | free jazz, hard bop, modal jazz, jazz, post bop | coltrane, garrison, tyner, supreme, love supreme |

Rarity weighting works: "spiritual jazz" now carries *The 7th Hand* and Matthew Halsall's *When the World Was One* into the top 10. The text terms are mostly people: the quartet's members and the Impulse! label, recovered from articles' prose and personnel lists.

### Building the model

```bash
cd backend && uv run python -m crate_backend.scripts.build_tfidf_model
```

- **Output:** writes `models/tfidf.joblib` at the repo root (gitignored; override with `CRATE_TFIDF_MODEL_PATH` or `--out`).
- **Evaluation flags:** `--alpha` (tag weight, 0–1), `--no-bigrams`, `--no-reception`, `--no-personnel`, `--max-features`.
- **Restarts:** the API loads the file on its first TF-IDF request and keeps it, so **restart the backend after a rebuild**. A first build needs no restart.
- **Metadata:** the file records its build time (`model_version`), α, vectorizer settings, album counts, the MusicBrainz dump date and the scikit-learn version.

### API

Same endpoint as approach 1, with `"approach": "tfidf"`. The response's `model_version` is the build time of the model that answered, and each result adds `shared_text_terms`.

- `503 {"detail": "TF-IDF model not built"}`: no model file exists. Overlap requests are unaffected.
- `reason: "seeds_not_in_model"`: none of the seeds existed when the model was built. Seeds added since are ignored when mixed with known ones.
- 404 / 422 / `seeds_have_no_terms`: as for approach 1.
- Albums removed from the catalog since the build are skipped.

### Performance

Measured on the dev machine, 2026-10-06, full catalog:

| Measure | Value |
|---|---|
| Build (load from Postgres + fit + save) | 25 s total (4.0 + 17.4 + 1.4 s); peak memory 724 MB |
| Vocabulary | 11,814 tag terms; 630,197 text terms |
| Nonzeros | 230,318 tag; 6,511,631 text |
| Model file | 88 MB; matrices 77 MB in memory (~150 MB process growth on load) |
| First-request load | 0.9 s |
| Request, 1 seed | 29–39 ms |
| Request, 5 seeds | 38–43 ms |
| Request, 50 seeds | 145–159 ms |

That is faster than approach 1 (0.06–1.5 s) because scoring is in-memory sparse matrix math instead of SQL. The 500 MB cap from the spec was not needed.

### Known limitations

- **Albums without an article outrank those with one.** Text cosines run lower than tag cosines, so the 0.6/0.4 blend usually scores an album with an article below one scored on tags alone. In the first by-eye check, 7 of *A Love Supreme*'s top 10 and 6 of *Kid A*'s had no article. The spec chose to measure this in Milestone 3 rather than correct it blind.
- **Mood tags dominate some seeds.** *Kid A*'s top results come from rare descriptor tags ("cold", "depressive", "cryptic", "winter") shared with depressive black metal and a Turkish album. IDF rewards rarity, and these tags are rare.
- **Text matches are mostly names.** "Described alike" is dominated by artist and band-member names ("coltrane", "yorke", "radiohead") and a few phrase fragments ("yorke said"). So text favours same-artist and same-circle albums more than shared sound. The artist name is deliberately kept; evaluation will show whether it crowds results.
- **Coverage is skewed.** Articles exist for 96% of the top popularity quartile but 9% of the bottom, so the text block barely helps obscure albums.
- **Snapshot.** Albums added after a build can't be seeds or results until the next build, and a rebuild needs an API restart.
- **Not evaluated.** Quality has only been judged by eye so far.

---

## Planned approaches

Short notes only; each gets a full section like approach 1 once it's built.

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
