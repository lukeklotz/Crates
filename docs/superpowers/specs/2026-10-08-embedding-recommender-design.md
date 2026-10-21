# Sentence-embedding recommender (Phase 5a) — design

**Status:** Design approved in conversation 2026-10-08; pending review of this written spec.

## Purpose

Phase 5 of `crate-ml-engineering-project-plan.md` asks Crate to "learn similarities in meaning rather than requiring exact shared words." TF-IDF (Phase 4) treats "melancholic" and "sorrowful" as unrelated words. A pretrained sentence-embedding model places them close together.

This spec is **Phase 5a**: embed the *same* album documents TF-IDF uses (genre/tag terms + cleaned Wikipedia text), serve the result as a third approach, and measure it on the Phase 4 answer key. Same data, classical vs. neural representation, so the comparison is clean.

The phase answers one question with numbers: **does a pretrained embedding model find related albums that TF-IDF's shared vocabulary misses?** A Phase 5b (see "Not in scope") is only worth specifying if the answer is yes.

## Decisions made in conversation

- **Scope is 5a only.** Out of scope, deferred to a possible 5b spec: `pgvector` storage, the PyTorch projection model (negative sampling, metric learning), MLflow tracking and model registry. Vectors fit in one file (25,000 × 384 float32 ≈ 38 MB each), which is how the TF-IDF model is already served.
- **Long articles: chunk and average.** Sentence encoders read only a few hundred tokens at a time (512 for the chosen encoder). Each cleaned article is split into chunks, each chunk is embedded, and the chunk vectors are averaged into one text vector. Embedding only the article's lead was rejected because it drops the reception and personnel text Phase 4 deliberately kept.
- **Two vectors per album, blended with α**, exactly as in TF-IDF, so each representation is compared on identical inputs.
- **Coverage of text stays at ~51%.** Albums without an article keep a tag vector only and are compared on tags, as in TF-IDF. A 50-album spike (2026-10-08) tried Last.fm blurbs and tags, Discogs notes/styles and artist Wikipedia articles as extra text sources. Of 31 sampled albums with no Wikipedia album article, album prose was found for 6 (none in the bottom quartile; 0 of 8) and an artist article for 13 (1 of 8 in the bottom quartile). The obscure albums are missing from every source, so more text ingestion is not worth building for coverage. Discogs styles (12 of 31) remain a possible structured feature for 5b.
- **Rollout mirrors Phase 4:** `approach: "embeddings"` is opt-in; the default changes only if the answer key says embeddings win. No frontend toggle.
- **Encoder:** `BAAI/bge-small-en-v1.5` (384 dimensions, ~130 MB, 512-token limit). Small enough for an 8 GB machine, and it reads twice the window of the older `all-MiniLM-L6-v2` at the same vector size. Chosen 2026-10-08 over MiniLM on recalled benchmark scores, not on a Crate measurement. BGE's query-instruction prefix is for short-query-to-passage search and is **not** used: album-to-album similarity is symmetric, so every text is embedded as is. `all-MiniLM-L6-v2` is the first stretch variant (a one-line encoder swap); comparing larger encoders is not part of the phase.

## Scope

### Milestone 1 — Embedding model build
New module `recommend/embeddings.py` (model, build, scoring) and `scripts/build_embedding_model.py`.

### Milestone 2 — Serving
`approach: "embeddings"` in `POST /recommendations`, loader, setting.

### Milestone 3 — Evaluation and documentation
Two new evaluation variants, grading of the new pairs, results, and `docs/recommendation-systems.md`.

Each milestone ends at a checkpoint with the owner.

## Milestone 1 — Embedding model build

### Documents

Reuses `load_album_docs` from `build_tfidf_model` (term votes and `clean_article` text, same `--no-reception` / `--no-personnel` flags), so both approaches see identical inputs.

- **Tag string:** the album's normalized genre/tag terms ordered by vote count descending, top 20, joined with commas ("spiritual jazz, hard bop, modal jazz, …"). Every album has at least one term. The tag string is embedded as one text.
- **Text chunks:** the cleaned article is split on whitespace into windows of **250 words** (roughly 350 word-pieces for music prose full of names and accents, safely under the encoder's 512-token limit, which would otherwise truncate silently; the build sets `max_seq_length` to 512 explicitly and asserts no chunk exceeds it). A final window shorter than 50 words is merged into the previous one. No overlap. Each chunk is embedded.
- **Text vector:** the unweighted mean of the album's chunk vectors, re-normalized to unit length. Albums with no cleaned text get a zero row and `has_text = False`.
- Both vectors are L2-normalized, so dot products are cosines.

### Encoder interface

The encoder is a small protocol, `encode(texts: list[str]) -> np.ndarray` of unit-length float32 rows, so tests inject a deterministic fake and need neither `torch` nor a download. The real implementation wraps `SentenceTransformer(..., device=...)` and imports it lazily. `sentence-transformers` (which brings `torch`) goes in an optional dependency group `embeddings` in `backend/pyproject.toml`: only the build script needs it. The API loads stored vectors and never runs the encoder (seeds are catalog albums), so the API container stays free of `torch`.

### Model file and versioning

- `build_embedding_model` writes one joblib file to `settings.embeddings_model_path` (env `CRATE_EMBEDDINGS_MODEL_PATH`, default `<repo>/models/embeddings.joblib`; `models/*.joblib` is already gitignored). Written to a temp file and renamed, as for TF-IDF.
- Contents: `album_ids`, `titles`, `tag_vectors` (albums × 384), `text_vectors` (albums × 384, zero rows where no text), `has_text`, each album's `term_votes` (for explanations), and `metadata`.
- Metadata is the lightweight form of the plan's "version each embedding by album document, encoder, data snapshot, and creation time": `model_version` (ISO 8601 build time), `encoder_name`, `encoder_revision` (the Hugging Face commit hash), `embedding_dim`, `chunk_words`, `tag_terms_per_album`, α, document flags (`drop_reception`, `drop_personnel`), `n_albums`, `n_with_text`, `n_chunks`, catalog snapshot (MusicBrainz dump date, as in the TF-IDF metadata), `sentence_transformers_version`, `torch_version`.
- Command line: `--alpha` (default 0.6, stored in metadata and overridable at scoring time as for TF-IDF), `--no-reception`, `--no-personnel`, `--device cpu|mps`, `--batch-size`, `--out`.
- Records build time, peak memory and chunks per second in `docs/recommendation-systems.md`. Estimate before measuring: roughly 50,000 chunks (79 MB of text at 250 words each), minutes on this machine.

### Milestone 1 tests

No `torch`, no network, no database (tiny made-up catalogs, a fake encoder whose vectors are derived from word hashes or fixed per text):
- Chunker: 250-word windows; a 40-word tail merged into the previous chunk; text shorter than a window gives one chunk; empty text gives none.
- Text vector is the re-normalized mean of its chunk vectors; an album without text has a zero row and `has_text = False`.
- Tag string: ordered by votes, capped at 20, deterministic tie order.
- Save → load round-trip gives identical vectors and metadata.
- Build over the fake encoder is deterministic (same inputs, same file contents apart from `model_version`).

**Checkpoint:** show the build's size, time and metadata, and inspect results by eye for the same familiar seeds as Phase 4 (*A Love Supreme*, *Kid A*) next to TF-IDF's.

## Milestone 2 — Serving

### Similarity

Identical to TF-IDF, with embedding cosines in place of TF-IDF cosines:

```
sim(a, b) = tag_cos(a, b)                              if a or b has no text vector
          = α·tag_cos(a, b) + (1 − α)·text_cos(a, b)   otherwise, α = 0.6
```

Group score = Σ over seeds of `sim(seed, candidate)`; seeds are never returned; candidates must score above 0; order is `round(score, 9)` descending, then title, then album id. Cosine of unit vectors can be negative, so the "score > 0" filter applies as before. The scoring rule (blend, group sum, ranking) is shared code or a straight copy of the TF-IDF functions; if copied, a test pins that both give the same ordering on the same toy matrices.

**Known risk, measured rather than corrected:** text-vector cosines for averaged chunks are typically *higher and tighter* than tag-string cosines (averaging pulls vectors toward a common centre), so the blend may favour albums that have an article. The per-quartile evaluation and the median-popularity column will show whether it happens. This is the opposite direction from the TF-IDF risk, which is why both are measured.

### Explanations

Embeddings cannot name the words that matched, and Wikipedia text is never displayed (licence: features only).
- `shared_terms`: the candidate's genre/tag terms that also appear on any seed, ranked by Σ over seeds of (seed vote × candidate vote), top 5. Computed from the stored `term_votes`. This is real shared evidence, the same kind the overlap approach shows.
- `shared_text_terms`: always `[]` for this approach.
- No "similar description" indicator in 5a. If the answer key says embeddings help, a text-similarity display is a 5b/UI decision.

### Loader and API

- `model_store.get_embedding_model()`: lazy, cached per process, `None` if the file doesn't exist, as `get_tfidf_model`.
- `approach` accepts `"embeddings"` alongside `"overlap"` and `"tfidf"`. Default stays `"overlap"`.
- Response fields unchanged: `approach`, `model_version`, per result `shared_terms`, `shared_text_terms`.
- Errors: `503 {"detail": "Embedding model not built"}` when requested without a file; `reason: "seeds_not_in_model"` with empty results when no seed is in the model; existing `404`, `422` and `seeds_have_no_terms` behaviour unchanged.
- The frontend is unchanged.

### Milestone 2 tests

Unit (`tests/test_recommend_embeddings.py`): a candidate closer in meaning outranks a farther one (fake-encoder vectors placed by hand); no-text fallback equals the tag cosine when either album lacks a text vector; multi-seed summing with equal seed influence; seeds excluded; deterministic ties; `shared_terms` ranking; scoring parity with TF-IDF's functions on toy matrices.

API (`tests/test_recommendations_api.py`, extended): the `embeddings` switch with an injected model, response fields, `503` without a model, `seeds_not_in_model`, the default still `overlap`.

Record per-request latency for 1, 5 and 50 seeds, the file size and the in-memory size in `docs/recommendation-systems.md`.

## Milestone 3 — Evaluation and documentation

### Variants

Added to `evaluation/variants.py`:
- `embed-tags`: `alpha=1.0`, tag vectors only (does embedding the tag string beat TF-IDF on tags?).
- `embed-tags+text`: `alpha=0.6` (does adding averaged article embeddings beat TF-IDF with text?).

`Variant.approach` gains `"embeddings"`; both share one model file, as the TF-IDF α variants do. They are added to `CORE_VARIANTS` so a default `pool` run includes them, and `ModelNotBuilt` gets an embeddings-specific message with the build command. Stretch variants (α 0.4/0.8, `--no-reception`, a different encoder) follow only after the core is graded.

### Grading load

The answer key is 10 seeds, top 5 per variant, graded in a terminal. Existing grades are keyed by (seed, candidate), so only pairs no earlier approach surfaced need grading. Estimate: 2–4 new pairs per seed per new variant, so roughly 20–40 pairs. Pooling shows the count before any grading.

### Choosing the default

Embeddings become the default approach only if, on the key, they beat both overlap and TF-IDF on NDCG@5 and also win more seeds than they lose against TF-IDF. With 10 seeds, a small difference is noise: the report's win/loss/tie counts and per-quartile columns decide, not the average alone. If the result is unclear, the default stays and the report says so. The default changes in a separate, explicit commit.

### Documentation

`docs/recommendation-systems.md`: approach #3 row (status, signal), how the approach works (with jargon defined by Crate example), build time/size/latency, the explanation limitation, the spike's text-coverage finding, the results table, and what went wrong.

### Milestone 3 tests

Variant parsing and the `ModelNotBuilt` message; pooling includes embedding variants (with an injected model); existing evaluation tests unchanged.

## Error handling summary

- Missing model file: `503` from the API; `ModelNotBuilt` with the build command from evaluation tools.
- Seeds not in the model: empty result with a reason.
- Build without `sentence-transformers` installed: the script exits with `uv sync --group embeddings`.
- Encoder download failure at build: the script exits with the underlying error; nothing is written (temp file then rename).

## Not in scope

`pgvector`, the PyTorch projection model, MLflow, Discogs/Last.fm/other text ingestion, LLM-extracted descriptors, a frontend toggle or text-similarity display, fine-tuning the encoder, comparing encoders, SVD/MMR.

## Related files

- Phase 4 spec: `docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md`
- `backend/src/crate_backend/recommend/tfidf.py`, `model_store.py`, `text_cleaning.py`
- `backend/src/crate_backend/scripts/build_tfidf_model.py`
- `backend/src/crate_backend/evaluation/variants.py`
- `docs/recommendation-systems.md`
