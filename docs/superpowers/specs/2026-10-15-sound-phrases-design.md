# Sound-phrase recommender — design

**Status:** Design approved in conversation 2026-10-15; pending review of this written spec.

## Purpose

Reading the exact embedding text of 300 random albums (`eval/text-relevance/`) showed that most stored Wikipedia text is not about how an album sounds. It is mostly release dates, labels, chart positions, tours, band history and personnel lists. Graded results agree: adding whole-article text lowered NDCG@5 for TF-IDF (0.665 → 0.499) and for embeddings (0.598 → 0.415), and a sentence-level filter (`embed-tags+sound`) recovered only a little (0.451). (NDCG@5 is a 0-to-1 score for the top 5 picks; good picks near the top count more.)

This spec adds a recommendation approach that uses only the **sound-describing phrases** in each article, extracted with the spaCy parser and weighted with TF-IDF. It is served as a new approach, `phrases`, selectable in the frontend, so the owner can compare it by hand against the existing `tfidf` approach. The method is described in `docs/method-reports/sound-phrases.md`.

## Decisions made in conversation

- **spaCy extraction**, chosen over a fixed vocabulary list and over LLM-written descriptions. Two throwaway probes (2026-10-15, the 300-album sample) shaped the rules:
  - Round 1 extracted 1.8% of article words, with sales/opinion noise and missed hyphenated words.
  - Round 2 reached 19/300 albums with no prose phrases and a median of 5 phrases per album, and 87% of phrases were not already in the album's tags.
- **Phrases replace the text block in a separate TF-IDF model file** (option A), rather than adding a third block to the existing model or merging phrases into the tag block. The model format, scoring, α blend and explanations stay as they are, and the existing `tfidf` approach stays as a baseline beside the new one.
- **Prose only.** Credit lines ("Name – bass guitar") are removed before parsing. Instrument credits are a graph-features topic, and keeping them out makes this a clean test of sound descriptions.
- **Served in the API and the frontend picker** for hand testing. No grading tooling in this build: a scripted evaluation can be added later if wanted.
- **Extraction runs at build time on every build**, not cached in the database, because the rules will keep being tuned.

## Scope

### 1. Extraction module: `backend/src/crate_backend/recommend/sound_phrases.py`

Pure functions in the style of `text_cleaning.py`:

- **`prose_only(text) -> str`:** the text without credit lines. It reuses `_CREDIT_LINE` from `text_cleaning.py`; a matching line counts as a credit only when it is at most 160 characters, since longer lines are prose that happens to contain a dash.
- **`extract(doc) -> list[str]`:** the sound phrases of one spaCy-parsed text. Phrases are normalized with `normalize_term` (so *pop-punk* becomes *pop punk*, matching tag spelling) and deduplicated in first-seen order.
- **`extract_all(texts, nlp, batch_size=...) -> list[list[str]]`:** runs `nlp.pipe` over all texts and calls `extract` on each.

Extraction rules:

1. **Anchors.** A token is an anchor when it is a NOUN whose lemma is in one of two lists:
   - `SPECIFIC_NOUNS` (e.g. sound, guitar, vocal, drum, bass, beat, riff, production, groove, melody, synth, piano, string, horn, rhythm, tempo, texture, atmosphere, mood, tone, arrangement, instrumentation, lyric, chorus, hook, sample, feel, timbre, distortion, reverb, ballad) emit `"<descriptor> <noun>"`.
   - `GENERIC_NOUNS` (e.g. song, track, album, record, music, style, solo, band, group, duo, musician, singer, rapper, artist, songwriter, producer) emit `"<descriptor>"` alone.

   The pronoun *it* also counts as a generic anchor when its head verb is a describing verb.
2. **Descriptors** of an anchor, each taken together with its `conj` chain ("lush and spacious"):
   - `amod` children of the anchor;
   - `compound` children of a specific anchor, and NOUN `compound` children of a generic anchor;
   - `acomp` children of a linking-verb head (be, sound, feel, seem, become, remain, appear) when the anchor is its subject;
   - for a describing-verb head (call, describe, label, deem, consider, dub, characterize, term) with the anchor as object or passive subject: ADJ `oprd`/`acomp`/`xcomp`/`ccomp` children, and *as* + object (an ADJ object, or the object's `amod` children).
3. **Multiword descriptors:**
   - Hyphenated words written without spaces are rebuilt whole (*electro-industrial*, *lo-fi*).
   - A descriptor's own `compound` children are prefixed (*acid jazz*, *hip hop*).
4. **Dropped:**
   - anchors or heads with a `neg` child, or with *no* as determiner;
   - descriptor tokens that are numbers, or that spaCy tags as a named entity of type NORP, GPE, LOC, ORG, PERSON, DATE, TIME, ORDINAL, CARDINAL, MONEY, PERCENT, QUANTITY, WORK_OF_ART, EVENT, FAC, PRODUCT or LANGUAGE;
   - descriptors that aren't letters and hyphens, or are shorter than 3 characters;
   - descriptors any of whose hyphen parts is in `IGNORED_WORDS`. This list holds the probe round-2 list plus its leftovers: opening, closing, earlier, subsequent, latter, breakthrough, signature, executive, vinyl, concept, biggest, strongest, able, unable, potential, future, support, milestone, affair.

Every list and verb set is a commented module-level constant.

### 2. Dependency

- A new `phrases` dependency group in `backend/pyproject.toml`: `spacy==3.8.7` and `en_core_web_sm` 3.8.0 from its GitHub release wheel URL, the exact versions the probes used.
- The `dev` group includes `phrases`, so tests always run against the real parser.
- The API never imports spaCy; only the build script's `--sound-phrases` path does.

### 3. TF-IDF model: `recommend/tfidf.py`

- **`build_model(..., phrases: list[list[str]] | None = None)`:** when given, the second block comes from a new `_phrase_block(docs, phrases)` instead of `_text_block`. The tag block is unchanged.
- **`_phrase_block`:**
  - each phrase is one term (no splitting into words, no word pairs, no stop words);
  - binary term frequency (a phrase counts once per album);
  - smoothed IDF, L2 normalization;
  - `min_df=2`, `max_df=0.5`;
  - rows are placed at their albums' positions as `_text_block` does.
- **`TfidfModel` is unchanged.** `text_terms` holds phrases, `text_matrix` the phrase vectors, and `has_text` means "has at least one phrase". `recommend()`, `_group_scores`, the α blend (default 0.6) and `_top_terms` explanations need no changes.
- **Metadata:**
  - `"text_source"`: `"sound_phrases"` or `"article"`.
  - For phrase builds, also: `"spacy_version"`, `"spacy_model"` (name and version) and `"phrase_vectorizer"` (min_df, max_df).

### 4. Build script: `scripts/build_tfidf_model.py`

- **New flag:** `--sound-phrases`. The pipeline is `load_album_docs` → `prose_only` → `spacy.load("en_core_web_sm")` → `extract_all` → `build_model(phrases=...)`.
- **Missing dependency:** spaCy is imported inside the flag's code path. If it isn't installed, the script exits with `sound phrases need spaCy. Run: uv sync --group phrases`.
- **Output path:** a new setting, `tfidf_phrases_model_path` (default `<repo>/models/tfidf-phrases.joblib`), used when `--sound-phrases` is set and `--out` isn't.
- **Flag combinations:** `--no-bigrams` and `--max-features` with `--sound-phrases` are argument errors. `--no-reception` and `--alpha` still apply.
- **Printed summary:**
  - albums with phrases (count and %);
  - distinct phrases extracted and the count kept after min_df/max_df;
  - median phrases per album with phrases;
  - the 25 most common kept phrases;
  - parse time;
  - plus the existing file, size and time lines.
- **Command:** `uv run --group phrases python -m crate_backend.scripts.build_tfidf_model --sound-phrases`

### 5. API

- **`recommend/model_store.py`:** `get_tfidf_phrases_model()`, the same contract as `get_tfidf_model()` (loaded once and kept; `None` while the file is missing; restart after a rebuild). Both share one helper keyed by path.
- **`api/routes/recommendations.py`:**
  - `approach: Literal["overlap", "tfidf", "phrases", "embeddings"]`, with the default still `"overlap"`;
  - the loader is chosen from a map of approach → loader;
  - a missing phrase model returns 503 with detail `"Sound-phrase model not built"`;
  - `phrases` ranks through the same TF-IDF code path as `tfidf`, so phrases arrive in `shared_text_terms`;
  - the response schema is unchanged.

### 6. Frontend: `frontend/app/page.tsx`

- `APPROACHES` gains `{ value: 'phrases', label: 'TF-IDF (tags + sound phrases)' }`.
- The text-explanation line reads **"Sounds alike: …"** when the results came from `phrases`, and keeps **"Described alike: …"** for `tfidf`.
- **Unchanged:** a missing model still shows the generic "Recommendations unavailable" error. The proxy maps every non-404/422 error to that message for all approaches, and changing it is out of scope.

## Testing

Test-first for all backend work.

- **`tests/test_sound_phrases.py` (new, real parser).** One test per rule, each asserting the exact output of a short sentence:
  - modifiers with `conj` partners ("jangly guitars and breathy vocals");
  - a generic noun keeping only its descriptor ("an industrial band");
  - a linking verb ("the sound is warm and spacious");
  - a describing verb ("critics called the album ferocious");
  - hyphen rebuilding ("a lo-fi production" → *lo fi production*);
  - a two-word genre ("an acid jazz record" → *acid jazz*);
  - negation ("no ska", "lacks melody");
  - names, places and ordinals ("the second album by the Canadian band");
  - the ignore list ("the best-selling opening track");
  - `prose_only` removing credit lines;
  - deduplication within an album.
- **`tests/test_recommend_tfidf.py` (hand-made phrase lists, no spaCy):**
  - phrases are whole terms;
  - `min_df` drops phrases found in only one album;
  - albums without phrases have `has_text=False` and score on tags alone;
  - shared phrases are the explanation;
  - `text_source` is recorded in the metadata.
- **`tests/test_build_tfidf_model_script.py`:** `--sound-phrases` parses, and the invalid flag combinations are rejected.
- **`tests/test_tfidf_model_store.py`:** the phrase loader uses its own setting and returns `None` for a missing file.
- **`tests/test_recommendations_api.py`:**
  - `approach: "phrases"` ranks from the phrase model and explains with phrases;
  - it returns 503 without a model;
  - the default approach is still `overlap`.
- **Frontend:** `oxlint` and a type check. Then the app is run by hand to confirm the picker switches to `phrases` and shows "Sounds alike".
- **Final checks:** the full backend suite and ruff pass. A real full-catalog build's summary is compared with probe round 2 (share of albums with phrases, top phrases) before the work is reported done.

## Not in scope

- A grading packet, an LLM-grading tool, or an evaluation variant. The owner tests by hand; a scripted evaluation can be specified later.
- Credit-line phrases (instrument credits).
- Caching extracted phrases in the database.
- Changing the default approach, or the frontend's error message for an unbuilt model.
- Combining phrases with whole-article text, or with embeddings.

## Risks

- **Low ceiling.** Probe round 2 found a median of 4 phrases per album beyond the tags, and 50/300 sampled albums got none. About half the catalog has no article. Expect differences from `tfidf` mainly for well-documented albums.
- **Popularity skew.** Texture words come mostly from long articles about popular albums.
- **Parser drift.** Exact-output tests can break on spaCy or model upgrades; the versions are pinned for that reason.
- **Rule maintenance.** The noun and ignore lists are hand-curated and will need tuning as you test in the app.
