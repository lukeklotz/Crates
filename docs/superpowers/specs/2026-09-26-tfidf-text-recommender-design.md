# TF-IDF text recommender with Wikipedia text — design

**Status:** Design approved in conversation 2026-09-26; pending review of this written spec.

## Purpose

Phase 4 of `crate-ml-engineering-project-plan.md` introduces classical information retrieval: represent each album as a TF-IDF vector and recommend by cosine similarity. It must beat the Phase 3 Jaccard genre/tag-overlap baseline, and it must be *measured* doing so.

The plan's Phase 4 assumes album documents built from credits, labels and annotations. Phase 2 did not deliver those, so without new data an album's document would be only its tag list. This phase therefore adds **English Wikipedia article text** as a second source of descriptive words.

The phase answers two questions with numbers:
1. Does TF-IDF (which weights rare terms like "glitch" above common ones like "rock") beat Jaccard?
2. Does adding Wikipedia text improve on TF-IDF over tags alone, and for which albums?

## Decisions made in conversation

- **Phase 4 = classical TF-IDF over tags + Wikipedia text. Phase 5 = neural sentence embeddings over the same fetched text.** Wikipedia fetching is built once and serves both phases. That gives a clean comparison later: same data, classical vs. neural representation.
- **LLM extraction** (a language model reading articles and producing structured descriptors such as personnel and instruments) is deliberately *not* part of this phase. It is a separate data-enrichment project that could recover the missing credits later.
- **Evaluation is in scope:** a small hand-graded answer key, graded through a terminal script.
- **Rollout:** `POST /recommendations` gains an `approach` switch; the default changes to TF-IDF only if the answer key says it wins. There is no frontend toggle.
- **One spec, three milestones** in order: Wikipedia ingestion → TF-IDF recommender → evaluation harness. Each ends at a checkpoint with the owner.
- **Stretch variants** (α sweep, Reception on/off, no bigrams, SVD, MMR) come only after the core evaluation is graded. The phase is complete without them.

## Measured starting point (2026-09-26)

- 25,000 albums, all with at least one genre or tag; median 15 terms per album (25th percentile 11, 95th 26).
- 24,875 albums have Last.fm popularity (the backfill has run).
- From a scan of the MusicBrainz release-group dump: **13,531 albums (54%)** link to Wikidata (13,472) or directly to Wikipedia (2,245). Not every Wikidata entry has an English article, so real article coverage will be somewhat lower.
- Coverage is strongly biased toward popular albums:

| Popularity quartile | Albums | With a wiki link |
|---|---|---|
| Top 25% | 6,219 | 96% |
| 50–75% | 6,219 | 74% |
| 25–50% | 6,216 | 36% |
| Bottom 25% | 6,221 | 11% |

The design must not penalize albums without an article, and evaluation must report results per popularity quartile.

## Scope

In scope:
- Milestone 1: Wikidata linking, Wikipedia text fetch and storage.
- Milestone 2: TF-IDF model build, serving, API `approach` switch, text-based explanations and a one-line UI addition.
- Milestone 3: seed selection, pooling, terminal grader, scorer, report, and docs update.

Out of scope (deferred):
- LLM extraction; neural embeddings (Phase 5).
- Combining with graph features (plan step 7). Artist relationships are the only graph data, and blending them is a later follow-up.
- A precomputed nearest-neighbour table (plan step 6). In-memory scoring over 25,000 albums is fast enough; revisit at Phase 8 scale.
- Multi-album group queries in the answer key (single-album seeds only).
- Popularity steering, persisted recommendation runs, displaying Wikipedia text or excerpts in the product UI.
- Fixing the Jaccard float-tie issue (the new recommender avoids it; the old one keeps its logged issue).

---

## Milestone 1 — Wikipedia text ingestion

### Linking albums to Wikidata

- New nullable column `albums.wikidata_id` (`String(20)`, e.g. `Q24965303`), plus nullable `albums.wikipedia_title` (`String(500)`) for albums whose only link is a direct English Wikipedia URL.
- Script `crate_backend.scripts.link_wikidata` streams `release-group.tar.xz` with `musicbrainz.dump_reader.stream_jsonl_from_tar`, and for each catalog album reads relations of type `wikidata` and `wikipedia`:
  - `wikidata`: store the Q-id parsed from the URL.
  - `wikipedia`: store the article title only if the URL is on `en.wikipedia.org` (URL-decoded, underscores kept as the API accepts them).
  - Non-English Wikipedia links are ignored.
- Re-runnable: it overwrites both columns from the dump each run. Prints counts at the end.
- Alembic migration adds both columns.

### Storage: `album_texts`

New model `AlbumText` (`models/album_text.py`), table `album_texts`, mirroring `PopularitySignal`:

| Column | Type | Meaning |
|---|---|---|
| `album_id` | FK → albums.id | |
| `source` | `String(20)` | `"wikipedia"` (only value this phase) |
| `article_title` | `String(500)`, nullable | Resolved English article title |
| `revision_id` | `BigInteger`, nullable | Wikipedia revision fetched, for reproducibility |
| `text` | `Text`, nullable | Full plain-text article with `== Section ==` headings |
| `fetched_at` | timestamptz, nullable | Set on a definitive answer; null means retry next run |

Unique on (`album_id`, `source`). Rules:
- The Wikidata entry has no English article, or the article is missing: row with `text = null` and `fetched_at` set (not retried).
- Retries exhausted or network failure: `fetched_at` stays null (retried on the next run).
- The **full** article is stored. Section filtering happens at model-build time so it can be tuned without re-fetching (roughly 100 MB total).

### Fetcher

Package `crate_backend/wikipedia/`:
- `client.py`: `httpx` client with the same retry/backoff constants and shape as `lastfm/client.py` (retry on 429/5xx, exponential backoff capped at 60 s). A descriptive `User-Agent` including a contact email, per Wikimedia's User-Agent policy.
  - `resolve_enwiki_titles(qids)`: Wikidata `wbgetentities` with `props=sitelinks&sitefilter=enwiki`, up to 50 ids per request. Returns `{qid: title | None}`.
  - `fetch_article(title)`: Wikipedia `action=query&prop=extracts|info&explaintext=1&redirects=1&format=json`, one article per request. Returns text, final title (after redirects) and `lastrevid`, or "missing".
- `ingest.py`: logic for one album (resolve title → fetch → upsert `AlbumText`), kept separate from the script for testing.

Script `crate_backend.scripts.backfill_wikipedia_text`:
- Selects albums with `wikidata_id` or `wikipedia_title` and no `AlbumText` row with `fetched_at` set.
- Resolves Wikidata ids in batches of 50, then fetches articles one at a time at about 4 requests/second (`REQUEST_INTERVAL_SECONDS = 0.25`).
- Commits every 50 albums, prints progress every 500, and stops after 10 consecutive failures, saying progress is saved. The same safety net as the Last.fm backfill.
- Expected run: roughly 270 Wikidata requests plus about 13,500 article requests, about an hour.

### Licensing

Wikipedia text is CC BY-SA. This phase uses it only as model features and derived single-word/phrase explanation terms; no article text is displayed. Displaying excerpts later requires attribution and is noted as a follow-up.

### Milestone 1 tests

- Parsing recorded Wikidata and Wikipedia JSON responses (found, no enwiki sitelink, missing page, redirect), with no live network.
- Retry/backoff and give-up behaviour, using the injectable `_sleep` pattern from `lastfm/client.py`.
- Resume: albums with `fetched_at` set are skipped; failed ones are retried.
- Dump-relation parsing for `link_wikidata` (wikidata, en.wikipedia, non-English wikipedia, no relations).

**Checkpoint:** report actual article coverage overall and per popularity quartile before starting Milestone 2.

---

## Milestone 2 — TF-IDF recommender

### Code layout

- `recommend/text_cleaning.py`: `clean_article(text) -> str` (section filtering) and `normalize_term(name) -> str`.
- `recommend/tfidf.py`: pure functions over in-memory data (no database). Build matrices, score seeds, explain results, save/load.
- `scripts/build_tfidf_model.py`: loads albums, genre/tag votes and article text from Postgres, calls `tfidf.py`, writes the model file.
- New dependency: `scikit-learn` (brings `scipy`, `joblib`).

### Term normalization (tag block)

`normalize_term`: Unicode NFKC, lowercase, `-` and `_` → space, `&` → `and`, collapse whitespace, strip. "Post-Bop" and "post bop" become `post bop`. Each normalized genre or tag name is **one whole term** (not split into words).

### Article cleaning (text block)

`clean_article` splits on `==`-level headings and **drops** sections whose normalized heading is one of: track listing, charts, weekly charts, year-end charts, certifications, release history, references, notes, external links, see also, accolades, awards, sales. Everything else is kept: the lead, Background, Recording, Composition/Music/Style, Themes/Lyrics and **Reception**. Subsections follow their parent section. The drop list is a module constant; the Reception on/off experiment toggles one entry.

*Amended 2026-10-06 (owner decision):* Personnel/Credits sections are **kept but filtered**: only `Name – roles` lines with at least one musical or production role stay; crew-only lines (mastering, engineering, photography, design, artwork…) are dropped, because the most-credited names in the data are mastering engineers. `--no-personnel` drops these sections entirely. See the Milestone 2 plan (`docs/superpowers/plans/2026-10-06-tfidf-recommender.md`, Deviations) for this and other drop-list variants.

### Tag block

- Term weight before IDF: **TF = 1 + ln(votes)**, where a vote count of 0 is treated as 1. If a normalized term appears as both a genre and a tag (or as two tags that normalize the same), use the largest vote count.
- IDF: scikit-learn's smoothed IDF, `ln((1 + N) / (1 + df)) + 1`, via `TfidfTransformer(sublinear_tf=False, smooth_idf=True)` applied to the TF matrix built above.
- Each album row L2-normalized. Every album has a tag row.

### Text block

- Only albums with non-empty cleaned text get a text row.
- `TfidfVectorizer(stop_words=<English list + music-press list>, ngram_range=(1, 2), min_df=2, max_df=0.5, sublinear_tf=True)`, rows L2-normalized.
- Music-press stopwords (module constant): album, albums, song, songs, track, tracks, record, records, recorded, recording, released, release, single, singles, chart, charts, billboard, band, label, lp, ep, version, edition, also, first, second, including. The artist's own name is **not** removed: same-artist affinity is legitimate, and evaluation will show if it dominates.
- `max_features` is unset by default. If the fitted model exceeds about 500 MB in memory, cap it at 100,000 and record the change.

### Similarity

```
sim(a, b) = tag_cos(a, b)                              if a or b has no text row
          = α·tag_cos(a, b) + (1 − α)·text_cos(a, b)   otherwise, α = 0.6
```

Text counts only when both albums have an article, so albums without one are compared purely on tags rather than penalized.

**Known risk, measured rather than corrected:** text cosines tend to be lower than tag cosines, so the blend may favour candidates without articles over equally good ones with them. The per-quartile evaluation and median-popularity column will show whether it happens.

### Groups, exclusions, ordering

- Group score = Σ over seeds of `sim(seed, candidate)`; every seed has equal influence.
- Candidates: every album in the model except the seeds, with score > 0.
- Order: `round(score, 9)` descending, then title ascending, then album id. Deterministic.
- Seeds not in the model (added to the catalog after the build) contribute nothing.

### Explanations

For each returned album, per-term **contribution** = Σ over seeds of (seed weight × candidate weight) for that term, within each block:
- `shared_terms`: top 5 tag-block terms by contribution (the existing field, now ordered by contribution rather than alphabetically).
- `shared_text_terms`: top 5 text-block terms by contribution (words or bigrams); empty if the candidate or no seed has text.

### Model file and serving

- `build_tfidf_model` writes a single joblib file to `settings.tfidf_model_path`. New setting `tfidf_model_path`, env `CRATE_TFIDF_MODEL_PATH`, default `<repo>/models/tfidf.joblib`. `models/*.joblib` is gitignored.
- File contents: fitted vectorizer/transformer vocabularies, the two sparse matrices, album-id ↔ row index, and metadata: `model_version` (build timestamp, ISO 8601), α, vectorizer parameters, number of albums, number with text, catalog source (MusicBrainz dump date), scikit-learn version.
- Build parameters are overridable on the command line (`--alpha`, `--no-bigrams`, `--no-reception`, `--no-personnel`, `--out`) so evaluation variants are separate model files built by the same code.
- The API loads the model once, lazily on first `tfidf` request, cached per process (`functools.lru_cache` around the loader). Tests can inject a model. If the file is missing, the loader returns `None`.
- Per request: take the seed rows, multiply by the transposed matrices (sparse, milliseconds), combine per the similarity rule, then rank.
- Record the built model's file size, in-memory size and build time, and per-request latency for 1, 5 and 50 seeds, in `docs/recommendation-systems.md`.

### API changes (backward compatible)

Request adds:
```json
{ "album_ids": ["…"], "limit": 20, "approach": "overlap" }
```
- `approach`: `"overlap"` | `"tfidf"`, default `"overlap"` until evaluation picks a winner (then the default changes in a separate, explicit commit).

Response adds `approach`, `model_version` (null for overlap), and per result `shared_text_terms` (always `[]` for overlap).

Errors and reasons:
- `503 {"detail": "TF-IDF model not built"}` when `tfidf` is requested and no model file exists.
- `reason: "seeds_not_in_model"` with empty results when no seed is in the model.
- Existing `404` (unknown ids), `422` (invalid input) and `seeds_have_no_terms` behaviour unchanged.

### Frontend

- The proxy is unchanged (it forwards the body).
- The group panel shows `shared_text_terms`, when non-empty, as a second line "Described alike: …" under "Shares: …". The panel sends no `approach`, so it gets the default.

### Milestone 2 tests

Unit tests (`tests/test_recommend_tfidf.py`, tiny made-up catalogs, no database):
- A rare shared tag outranks a common shared tag (the core IDF claim).
- A higher-voted shared tag outweighs a lower-voted one.
- `normalize_term` merges "Post-Bop"/"post bop"; genre+tag duplicates use the max vote count.
- `clean_article` drops listed sections and keeps others, including subsections.
- No-text fallback: similarity equals tag cosine when either album lacks text.
- Multi-seed summing, with equal seed influence; seeds excluded.
- Deterministic tie-breaking.
- Explanation ordering by contribution; empty `shared_text_terms` when text is absent.
- Save → load round-trip gives identical scores.

API tests (`tests/test_recommendations_api.py`, extended): the `approach` switch, response fields, 503 without a model, `seeds_not_in_model`, and the default still `overlap`.

Frontend: `oxlint` and `tsc --noEmit`; owner checks visually.

**Checkpoint:** show TF-IDF results by eye for a few familiar seeds (e.g. *A Love Supreme*, *Kid A*) before building the evaluation harness.

---

## Milestone 3 — Evaluation harness

### Layout

- Code: `backend/src/crate_backend/evaluation/` (`seeds.py`, `pool.py`, `grade.py`, `score.py`, `variants.py`), each runnable with `python -m`.
- Committed data: top-level `eval/`
  - `seeds.json`: list of `{album_id, title, artist_name, popularity_quartile}`. Human-readable and hand-editable.
  - `judgments.jsonl`: one line per graded pair: `{seed_id, candidate_id, grade, graded_at}`. Appended as grades are made; the grader's undo removes the most recent line it wrote in the current session.
  - `results/YYYY-MM-DD.md`: saved report per scoring run.

Judgments are keyed by (seed, candidate), not by variant, so they are reused by every present and future variant, including Phase 5.

### Variants

`variants.py` holds a registry of named variants: a name, an approach, and (for TF-IDF) a model file path.
- Core: `overlap`, `tfidf-tags` (α = 1.0: tag block only), `tfidf-tags+text` (α = 0.6).
- α is applied at scoring time, so `tfidf-tags` and the α sweep use the same model file. Variants that change the text block (`--no-bigrams`, `--no-reception`, `--no-personnel`, SVD) need their own model file.

### 1. Seed selection (`evaluation.seeds propose`)

- Proposes 25 single-album seeds: 6–7 per popularity quartile, spread across broad genres (jazz, rock, electronic, hip hop, metal, folk, pop, classical, soul/R&B, world) by the album's highest-voted genre; each seed has at least 5 terms. Deterministic (fixed random seed).
- Writes `eval/seeds.json`. The owner reviews and swaps any seed they don't know well. Grading is only as good as the grader's familiarity with the seed.
- A `swap` subcommand replaces one seed with a searched title, keeping the file consistent.

### 2. Pooling (`evaluation.pool`)

For each seed and each requested variant, take the top 10, and list every (seed, candidate) pair not already in `judgments.jsonl`. Writes `eval/pool.jsonl` (uncommitted working file) and prints how many new pairs need grading.

### 3. Grader (`evaluation.grade`, terminal)

- Prints the rubric at start:
  - **2:** I'd recommend it to someone who loves the seed.
  - **1:** Clearly related and plausible.
  - **0:** Not relevant.
  - Grade same-artist albums on their merits.
- Per seed: a header with title, artist, year, top tags and the first sentence of the Wikipedia lead (if any).
- Candidates are shown one at a time **in random order with the producing variant hidden**: title, artist, year, top 8 terms, first sentence of the lead.
- Keys: `0`/`1`/`2` grade, `s` skip (stays in the pool), `u` undo the last grade, `q` quit. Each grade is written immediately; rerunning resumes with ungraded pairs.
- Input and output are injectable so tests can drive it with scripted keystrokes.

### 4. Scorer (`evaluation.score`)

For each variant, overall and per popularity quartile:
- **NDCG@10** with gain `2^grade − 1` (a 2 is worth three times a 1). Ideal ranking built from all graded pairs for the seed. The headline metric.
- **Pooled Recall@10:** the share of the seed's candidates graded ≥ 1 (across all variants) that appear in this variant's top 10.
- **Judged@10:** the share of the top 10 that has a grade. Ungraded results count as 0 and are flagged when Judged@10 < 0.9.
- **Median popularity** of returned albums.
- **Distinct artists in top 10** (a diversity measure, mainly for MMR).
- **Per-seed win/loss/tie counts** on NDCG@10 between each pair of variants. With 25 seeds, consistent win counts are more trustworthy than small differences in averages.

Prints a table and writes `eval/results/YYYY-MM-DD.md`.

### Choosing the default approach

The scorer only reports; the owner decides at the checkpoint. Suggested rule: make `tfidf` (with the winning α) the default if it beats `overlap` on NDCG@10 overall **and** does not lose in the bottom popularity quartile. The default change is its own commit, and `docs/recommendation-systems.md` records the decision and numbers.

### Stretch variants (optional, after core grading)

Each changes one setting; each needs grading of only the newly surfaced pairs (typically 2–4 per seed).

| Variant | Change | Question it answers |
|---|---|---|
| `tfidf-a0.4`, `tfidf-a0.8` | α = 0.4 / 0.8 | How much to trust text vs tags |
| `tfidf-no-reception` | Drop Reception sections | Does critics' language help or add fame bias? |
| `tfidf-no-personnel` | Drop Personnel/Credits sections | Do shared musicians and producers help, or add same-artist crowding and noise? |
| `tfidf-no-bigrams` | `ngram_range=(1, 1)` | Are phrases worth the bigger vocabulary? |
| `tfidf-svd200` | `TruncatedSVD(200)` on the text block | Does topic-level matching beat exact words? |
| `tfidf-mmr0.7` | MMR re-rank, λ = 0.7, over the top 50 | Does diversity cost relevance? (judged with distinct-artist count alongside NDCG) |

SVD and MMR add code (`TruncatedSVD` on the text matrix; an MMR re-ranker in `tfidf.py` using the same `sim`). Explanations always use raw TF-IDF terms.

### Milestone 3 tests

- NDCG@10 and pooled Recall@10 on hand-computed examples, including all-zero grades and a seed with no relevant items.
- Ungraded results counted as 0, and the Judged@10 flag.
- Pooling skips already-judged pairs and de-duplicates across variants.
- Grader: resume, skip, undo, quit, with scripted input.
- Seed proposal: deterministic, quartile/genre spread, minimum-terms rule.

### Owner time

About 25 seeds × 20–25 unique candidates ≈ 500–600 grades, about 1.5–2 hours, splittable across sessions. Stretch variants add a few grades per seed each.

---

## Documentation

- `docs/recommendation-systems.md`: add section 2 (TF-IDF): how it works, a worked example, API, performance, known limitations. Fill in the Evaluation section with real numbers for all graded variants. Update the summary table.
- Record the Wikipedia text source (coverage, fetch date, licence) alongside the existing data description.

## Error handling summary

- Wikipedia/Wikidata outages: fetcher retries, then leaves `fetched_at` null and stops after 10 consecutive failures; re-run resumes.
- Missing model file: `tfidf` requests return 503; `overlap` unaffected.
- Model older than catalog: unknown seeds contribute nothing; all-unknown → `seeds_not_in_model`.
- Empty cleaned text (article was only track listing, etc.): treated as no text.

## Related files

- `crate-ml-engineering-project-plan.md`: Phase 4 (steps 1–5, 8, 9, 10; steps 6–7 deferred as above).
- `docs/superpowers/specs/2026-09-24-overlap-baseline-recommender-design.md`: the baseline this must beat.
- `backend/src/crate_backend/recommend/overlap.py`, `api/routes/recommendations.py`: existing recommender and endpoint.
- `backend/src/crate_backend/lastfm/client.py`, `scripts/backfill_lastfm_popularity.py`: fetcher pattern to mirror.
- `backend/src/crate_backend/musicbrainz/dump_reader.py`: dump streaming for `link_wikidata`.
- `frontend/app/page.tsx`: group panel.
