# TF-IDF Recommender (Phase 4, Milestone 2) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a TF-IDF recommender beside the Jaccard overlap baseline. It is built offline into one model file, served from memory behind `POST /recommendations` `approach: "tfidf"`, and explains each result with shared tag terms and shared Wikipedia words. The milestone ends with a by-eye checkpoint on familiar seeds.

**Architecture:** `recommend/text_cleaning.py` prepares terms and article text. `recommend/tfidf.py` is pure in-memory code (no database): it builds two L2-normalized sparse matrices (a tag block and a text block), scores seeds by blended cosine similarity, explains results by per-term contribution, and saves/loads one joblib file. `scripts/build_tfidf_model.py` reads Postgres and writes the file. `recommend/model_store.py` loads it once per API process. The endpoint gains an `approach` switch whose default stays `overlap`.

**Tech Stack:** Python 3.12+, scikit-learn (new; brings numpy, scipy, joblib), SQLAlchemy 2 async + asyncpg, FastAPI, pytest + pytest-asyncio (auto mode), uv. Frontend: Next.js-style app (`frontend/app/page.tsx`), checked with `oxlint` and `tsc --noEmit`.

**Spec:** `docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md`, section "Milestone 2 — TF-IDF recommender". This plan implements only Milestone 2. Milestone 3 (evaluation harness) gets its own plan after the checkpoint.

## Deviations from the spec (each small; listed so a reviewer doesn't flag them)

1. **Drop list extended with heading variants seen in the real data** (scan of all 12,799 stored articles, 2026-10-06): `track listings`, `chart positions`, `charts and certifications`, `certifications and sales`, `sources`, `bibliography`, `further reading`. They are the same kinds of section the spec drops, just spelled differently.
1a. **Personnel is kept, filtered (owner decision, 2026-10-06).** `personnel`, `credits` and `credits and personnel` sections are no longer dropped. Inside them, only `Name – roles` lines with at least one musical or production role are kept. Lines whose roles are all crew roles (mastering, engineering, photography, design, art direction, artwork, illustration, layout, liner notes, cover) are dropped, as are lines that aren't credits ("Credits adapted from liner notes."). Why: credits link albums through shared musicians and producers (*A Love Supreme* → McCoy Tyner, Elvin Jones), which recovers some of the credits data Phase 2 never delivered. But the most-credited names across all articles are mastering engineers (Bob Ludwig on 226 albums, Ted Jensen 180, George Marino 148), and they would link unrelated albums. A `--no-personnel` build flag drops these sections entirely, so Milestone 3 can measure whether they help (new stretch variant `tfidf-no-personnel`).
2. **`--no-reception` drops every top-level section whose heading contains the word "reception"**, not one list entry. The data has `reception` (2,607 articles), `critical reception` (4,712), `release and reception`, `reception and legacy` and others; one entry would miss most of them. Default behaviour (Reception kept) is as specced.
3. **Model loader caches a loaded model, but not "file missing".** The spec says `functools.lru_cache`, which would cache `None` and force an API restart after the first build. Rebuilding an already-loaded model still needs a restart; that is documented.
4. **The model file stores term (feature-name) arrays, not fitted scikit-learn vectorizer objects.** Serving never vectorizes new text, so the vocabularies are all it needs. This also keeps scikit-learn's internal state out of the file.
5. **`--max-features` build flag** added so the spec's "cap at 100,000 if the model exceeds ~500 MB" fallback is a flag, not a code edit.
6. **`load_album_docs(..., only=...)`** takes an optional album-id filter so tests don't load the whole 25,000-album catalog.

## Global Constraints

- All backend commands run from `backend/` with `uv run ...`. Tests need the local Postgres from `.env`; the `db_session` fixture rolls back every test.
- The dev database holds the real 25,000-album catalog. Tests create their own albums and assert on those albums only, never on catalog-wide counts.
- `normalize_term`: Unicode NFKC, lowercase, `-` and `_` → space, `&` → `and`, collapse whitespace, strip. Each genre/tag name is one whole term.
- Tag block TF = `1 + ln(votes)`, votes of 0 treated as 1; duplicate normalized terms keep the **largest** vote count. IDF via `TfidfTransformer(norm="l2", smooth_idf=True, sublinear_tf=False)`.
- Text block: `TfidfVectorizer(stop_words=<sklearn English list + music-press list>, ngram_range=(1, 2), min_df=2, max_df=0.5, sublinear_tf=True)`, `max_features` unset by default. Artist names are **not** removed.
- Music-press stopwords (exact): album, albums, song, songs, track, tracks, record, records, recorded, recording, released, release, single, singles, chart, charts, billboard, band, label, lp, ep, version, edition, also, first, second, including.
- Spec drop list (exact): track listing, personnel, charts, weekly charts, year-end charts, certifications, release history, references, notes, external links, see also, accolades, awards, sales. Plus the variants in Deviation 1, **minus personnel** (Deviation 1a).
- Personnel/credits sections (`personnel`, `credits`, `credits and personnel`): keep only `Name – roles` lines with at least one role that isn't a crew role. `--no-personnel` drops the sections entirely.
- Similarity: `tag_cos` if either album has no text row, else `α·tag_cos + (1 − α)·text_cos`, **α = 0.6**. "Has a text row" means the row has at least one nonzero after vectorizing.
- Group score = sum over seeds. Candidates: all model albums except seeds, score > 0. Order: `round(score, 9)` desc, then title asc, then `str(album_id)` asc.
- Explanations: top **5** terms per block by contribution (Σ seed weight × candidate weight), ties by term asc.
- Setting `tfidf_model_path`, env `CRATE_TFIDF_MODEL_PATH`, default `<repo>/models/tfidf.joblib`; `/models/*.joblib` gitignored.
- Metadata keys: `model_version` (UTC build time, ISO 8601), `alpha`, `text_vectorizer`, `n_albums`, `n_with_text`, `catalog_source`, `sklearn_version`, `drop_reception`, `drop_personnel`.
- API: request `approach: "overlap" | "tfidf"`, default `"overlap"`. Response adds `approach`, `model_version` (null for overlap), per-result `shared_text_terms` (always `[]` for overlap). `503 {"detail": "TF-IDF model not built"}`; `reason: "seeds_not_in_model"`. Existing 404/422/`seeds_have_no_terms` unchanged.
- Wikipedia text is CC BY-SA: used as model features and single-word/phrase explanation terms only; no article text displayed.
- Ruff line length 100 (`uv run ruff check src tests`).
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Work directly on `main`; don't push.

## Review Focus

1. **Article text that vectorizes to nothing** (only stopwords, or only dropped sections): expected to count as "no text", so the album is compared on tags alone and not scored at 0.6 × tag. Pinned in Task 2 (`test_text_of_only_stopwords_counts_as_no_text`) and Task 1 (`test_clean_article_of_only_dropped_sections_is_empty`).
2. **An album deleted from the catalog after the model was built:** expected to be skipped in results, not to crash the endpoint with a `KeyError`. Pinned in Task 5 (`test_albums_removed_since_the_model_was_built_are_skipped`).
3. **API started before the model file exists, then the model is built:** expected to serve TF-IDF on the next request without a restart. Pinned in Task 5 (`test_missing_file_gives_none_and_is_picked_up_once_built`).
4. **Many candidates tied at the `limit` cut:** expected to still break ties by title, not by whatever order `np.partition` leaves. Pinned in Task 2 (`test_limit_keeps_tie_order_at_the_cut`).
5. **A group mixing seeds that are in the model with seeds added after the build:** expected to rank from the known seeds and ignore the rest. Pinned in Task 2 (`test_seeds_missing_from_the_model_are_ignored`) and Task 5 (`seeds_not_in_model` when none are known).

---

## File Structure

| File | Responsibility |
|---|---|
| `backend/src/crate_backend/recommend/text_cleaning.py` (create) | `normalize_term`, `merge_term_votes`, `clean_article`, `DROPPED_SECTIONS` |
| `backend/src/crate_backend/recommend/tfidf.py` (create) | `AlbumDoc`, `TfidfModel`, `build_model`, `recommend`, `save_model`, `load_model` |
| `backend/src/crate_backend/recommend/model_store.py` (create) | `get_tfidf_model()`: per-process cache of the model file |
| `backend/src/crate_backend/scripts/build_tfidf_model.py` (create) | `load_album_docs`, `parse_args`, CLI that writes the model file and prints stats |
| `backend/src/crate_backend/core/config.py`, `backend/.env.example` (modify) | `tfidf_model_path` setting |
| `backend/pyproject.toml`, `backend/uv.lock` (modify) | `scikit-learn` dependency |
| `.gitignore` (modify) | ignore `/models/*.joblib` |
| `backend/src/crate_backend/api/routes/recommendations.py` (modify) | `approach` switch, new response fields, 503, `seeds_not_in_model` |
| `frontend/app/page.tsx` (modify) | `shared_text_terms` type + "Described alike: …" line |
| `docs/recommendation-systems.md` (modify) | Section 2 (TF-IDF), summary table, API example fields |

Tests: `tests/test_text_cleaning.py`, `tests/test_recommend_tfidf.py`, `tests/test_build_tfidf_model_script.py`, `tests/test_tfidf_model_store.py` (create); `tests/test_config.py`, `tests/test_recommendations_api.py` (modify).

---

### Task 1: Term normalization and article cleaning

**Files:**
- Create: `backend/src/crate_backend/recommend/text_cleaning.py`
- Test: `backend/tests/test_text_cleaning.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `normalize_term(name: str) -> str`
  - `merge_term_votes(pairs: Iterable[tuple[str, int]]) -> dict[str, int]`: normalized term → largest vote count; names that normalize to `""` are skipped.
  - `clean_article(text: str, *, drop_reception: bool = False, drop_personnel: bool = False) -> str`: kept body text, heading lines removed, stripped.
  - `DROPPED_SECTIONS`, `PERSONNEL_SECTIONS: frozenset[str]`; `CREW_ROLE_WORDS: tuple[str, ...]`

- [ ] **Step 1: Write the failing tests**

`backend/tests/test_text_cleaning.py`:

```python
from crate_backend.recommend.text_cleaning import clean_article, merge_term_votes, normalize_term


def test_normalize_term_merges_spelling_variants():
    assert normalize_term("Post-Bop") == "post bop"
    assert normalize_term("post bop") == "post bop"
    assert normalize_term("  Drum_and_Bass ") == "drum and bass"
    assert normalize_term("R&B") == "r and b"
    # NFKC folds full-width letters into plain ones.
    assert normalize_term("ｊａｚｚ") == "jazz"


def test_merge_term_votes_keeps_largest_count_per_normalized_term():
    merged = merge_term_votes([("Post-Bop", 3), ("post bop", 5), ("jazz", 0), ("Jazz", 2)])

    assert merged == {"post bop": 5, "jazz": 2}


def test_merge_term_votes_skips_names_that_normalize_to_nothing():
    assert merge_term_votes([("-", 4), ("jazz", 1)]) == {"jazz": 1}


ARTICLE = """Kid A is the fourth studio album by Radiohead.
It features electronic textures.

== Background ==
Burned out after OK Computer, Yorke wrote on piano.

=== Recording ===
Sessions began in Paris.

== Track listing ==
Everything in Its Right Place – 4:11

=== Side two ===
Idioteque – 5:09

== Critical reception ==
Critics praised its glitch influences.

== Personnel ==
Credits adapted from liner notes.

=== Radiohead ===
Thom Yorke – vocals, piano
Nigel Godrich – production, mixing

=== Technical ===
Bob Ludwig – mastering
Stanley Donwood – artwork, cover design

== Charts & certifications ==
Number one in the UK.

== References =="""


def test_clean_article_drops_listed_sections_with_their_subsections():
    cleaned = clean_article(ARTICLE)

    assert "fourth studio album" in cleaned  # lead
    assert "Burned out" in cleaned and "Paris" in cleaned  # kept section and its subsection
    assert "glitch influences" in cleaned  # Reception is kept by default
    assert "4:11" not in cleaned and "Idioteque" not in cleaned  # dropped, with subsection
    assert "Number one" not in cleaned  # "&" heading normalizes to a dropped one
    assert "==" not in cleaned  # heading lines themselves are removed


def test_clean_article_keeps_only_musical_credits():
    cleaned = clean_article(ARTICLE)

    assert "Thom Yorke – vocals, piano" in cleaned
    assert "Nigel Godrich – production, mixing" in cleaned
    assert "Bob Ludwig" not in cleaned  # mastering only
    assert "Stanley Donwood" not in cleaned  # artwork and design only
    assert "adapted from liner notes" not in cleaned  # not a credit line


def test_credit_with_any_musical_role_is_kept():
    article = (
        "== Credits and personnel ==\n"
        "Bob Thiele – production and cover photo\n"
        "Rudy Van Gelder – engineering and mastering\n"
        "George Gray / Viceroy – cover design"
    )

    assert clean_article(article) == "Bob Thiele – production and cover photo"


def test_clean_article_can_drop_reception_sections():
    cleaned = clean_article(ARTICLE, drop_reception=True)

    assert "glitch influences" not in cleaned
    assert "Burned out" in cleaned


def test_clean_article_can_drop_personnel_sections():
    cleaned = clean_article(ARTICLE, drop_personnel=True)

    assert "Thom Yorke" not in cleaned and "Nigel Godrich" not in cleaned
    assert "Burned out" in cleaned and "glitch influences" in cleaned


def test_clean_article_of_only_dropped_sections_is_empty():
    article = "== Track listing ==\nSong – 3:00\n\n== Personnel ==\nSomeone – mastering"

    assert clean_article(article) == ""
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_text_cleaning.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.recommend.text_cleaning'`

- [ ] **Step 3: Write the implementation**

`backend/src/crate_backend/recommend/text_cleaning.py`:

```python
"""Prepare genre/tag terms and Wikipedia article text for the TF-IDF
recommender (Phase 4, Milestone 2).

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md
"""

import re
import unicodedata
from collections.abc import Iterable

# Top-level sections that list facts (tracks, chart positions) or point
# elsewhere instead of describing the music. Matched against the normalized
# heading; subsections go with their parent. The spec's list plus spelling
# variants found in the stored articles (2026-10-06).
DROPPED_SECTIONS = frozenset(
    {
        "track listing",
        "track listings",
        "charts",
        "weekly charts",
        "year end charts",
        "chart positions",
        "charts and certifications",
        "certifications",
        "certifications and sales",
        "release history",
        "references",
        "notes",
        "sources",
        "bibliography",
        "further reading",
        "external links",
        "see also",
        "accolades",
        "awards",
        "sales",
    }
)

# Credits sections: shared musicians and producers link albums, so these are
# kept, but only their "Name – roles" lines with a musical or production role.
PERSONNEL_SECTIONS = frozenset({"personnel", "credits", "credits and personnel"})

# Crew roles that say nothing about the music. The most-credited names in the
# stored articles are mastering engineers (Bob Ludwig on 226 albums), which
# would otherwise link unrelated albums. Matched as substrings of each role.
CREW_ROLE_WORDS = (
    "master",
    "engineer",
    "photo",
    "design",
    "art direction",
    "artwork",
    "illustration",
    "layout",
    "liner notes",
    "cover",
)

# "== Heading ==" (top level) or deeper "=== Subheading ===".
_HEADING = re.compile(r"^(={2,})\s*(.*?)\s*\1\s*$")
# "Name – role, role and role" (en dash, em dash or spaced hyphen).
_CREDIT_LINE = re.compile(r"^(.+?)\s[–—-]\s(.+)$")
_ROLE_SEPARATORS = re.compile(r",|;|&|\band\b")


def normalize_term(name: str) -> str:
    """One spelling per term: "Post-Bop" and "post bop" become "post bop"."""
    name = unicodedata.normalize("NFKC", name).lower()
    name = name.replace("-", " ").replace("_", " ").replace("&", " and ")
    return " ".join(name.split())


def merge_term_votes(pairs: Iterable[tuple[str, int]]) -> dict[str, int]:
    """Normalize (name, vote count) pairs from an album's genres and tags.
    When several names normalize to the same term, the largest count wins."""
    merged: dict[str, int] = {}
    for name, votes in pairs:
        term = normalize_term(name)
        if term:
            merged[term] = max(votes, merged.get(term, votes))
    return merged


def clean_article(
    text: str, *, drop_reception: bool = False, drop_personnel: bool = False
) -> str:
    """Article body text without the dropped sections, crew-only credit lines
    or any heading lines. The flags are evaluation variants:
    `drop_reception` drops every top-level section whose heading contains
    the word "reception"; `drop_personnel` drops credits sections entirely."""
    kept: list[str] = []
    section = "keep"
    for line in text.splitlines():
        match = _HEADING.match(line)
        if match is None:
            if section == "keep" or (section == "credits" and _is_musical_credit(line)):
                kept.append(line)
            continue
        if len(match.group(1)) == 2:
            section = _section_kind(
                normalize_term(match.group(2)), drop_reception, drop_personnel
            )
    return "\n".join(kept).strip()


def _section_kind(heading: str, drop_reception: bool, drop_personnel: bool) -> str:
    """"keep", "drop", or "credits" (keep musical credit lines only)."""
    if heading in DROPPED_SECTIONS or (drop_reception and "reception" in heading.split()):
        return "drop"
    if heading in PERSONNEL_SECTIONS:
        return "drop" if drop_personnel else "credits"
    return "keep"


def _is_musical_credit(line: str) -> bool:
    """A "Name – roles" line with at least one role that isn't crew work.
    Other lines in credits sections ("Credits adapted from liner notes.")
    are boilerplate and dropped."""
    match = _CREDIT_LINE.match(line.strip())
    if match is None:
        return False
    roles = [r.strip().lower() for r in _ROLE_SEPARATORS.split(match.group(2)) if r.strip()]
    return any(not any(word in role for word in CREW_ROLE_WORDS) for role in roles)
```

Note: `normalize_term` turns "year-end charts" into "year end charts", which is why the set holds that spelling. Producers and mixers are deliberately *not* crew: a shared producer (Nigel Godrich, Rick Rubin) is a real taste signal.

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_text_cleaning.py -v && uv run ruff check src tests`
Expected: 9 passed; ruff clean.

- [ ] **Step 5: Commit**

```bash
git add backend/src/crate_backend/recommend/text_cleaning.py backend/tests/test_text_cleaning.py
git commit -m "feat: normalize genre/tag terms and strip non-descriptive article sections

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Build the TF-IDF model and rank by blended similarity

**Files:**
- Modify: `backend/pyproject.toml`, `backend/uv.lock` (via `uv add`)
- Create: `backend/src/crate_backend/recommend/tfidf.py`
- Test: `backend/tests/test_recommend_tfidf.py`

**Interfaces:**
- Consumes: nothing from Task 1 directly (callers pass already-cleaned text and normalized terms).
- Produces:
  - `AlbumDoc(album_id: uuid.UUID, title: str, term_votes: dict[str, int], text: str = "")` (frozen dataclass)
  - `TfidfModel` dataclass with fields `album_ids: list[uuid.UUID]`, `titles: list[str]`, `tag_terms: np.ndarray`, `tag_matrix: sparse.csr_matrix`, `text_terms: np.ndarray`, `text_matrix: sparse.csr_matrix`, `has_text: np.ndarray` (bool), `metadata: dict[str, Any]`, and derived `row_of: dict[uuid.UUID, int]`.
  - `build_model(docs: list[AlbumDoc], *, alpha: float = DEFAULT_ALPHA, ngram_range: tuple[int, int] = (1, 2), min_df: int | float = 2, max_df: int | float = 0.5, max_features: int | None = None, extra_metadata: dict[str, Any] | None = None) -> TfidfModel`
  - `TfidfRecommendation(album_id: uuid.UUID, score: float, shared_terms: list[str], shared_text_terms: list[str])` (frozen dataclass)
  - `recommend(model: TfidfModel, seed_ids: list[uuid.UUID], limit: int, *, alpha: float | None = None) -> list[TfidfRecommendation]`. In this task `shared_terms` and `shared_text_terms` are returned as `[]`; Task 3 fills them.
  - `DEFAULT_ALPHA = 0.6`

- [ ] **Step 1: Add the dependency**

Run: `cd backend && uv add scikit-learn`
Expected: `pyproject.toml` gains `"scikit-learn>=…"`; `uv.lock` updates. (scikit-learn 1.9.x was current on 2026-10-06.)

- [ ] **Step 2: Write the failing tests**

`backend/tests/test_recommend_tfidf.py`:

```python
import uuid

import numpy as np
import pytest

from crate_backend.recommend.tfidf import AlbumDoc, build_model, recommend

# Tiny catalogs can't satisfy the production min_df=2 / max_df=0.5 text
# pruning, so tests keep every word.
KEEP_ALL_WORDS = {"min_df": 1, "max_df": 1.0}


def album(name: str, *terms: str, votes: dict[str, int] | None = None, text: str = "") -> AlbumDoc:
    return AlbumDoc(
        album_id=uuid.uuid5(uuid.NAMESPACE_URL, name),
        title=name,
        term_votes={term: 1 for term in terms} | (votes or {}),
        text=text,
    )


def model_of(*docs: AlbumDoc, **params):
    return build_model(list(docs), **(KEEP_ALL_WORDS | params))


def ranked_titles(model, results) -> list[str]:
    return [model.titles[model.row_of[r.album_id]] for r in results]


def scores(results) -> dict[uuid.UUID, float]:
    return {r.album_id: r.score for r in results}


def cosine(matrix, model, a: AlbumDoc, b: AlbumDoc) -> float:
    return (matrix[model.row_of[a.album_id]] @ matrix[model.row_of[b.album_id]].T)[0, 0]


def test_rare_shared_tag_outranks_common_shared_tag():
    seed = album("Seed", "rock", "glitch")
    model = model_of(
        seed,
        album("Common", "rock"),
        album("Rare", "glitch"),
        *(album(f"Filler {i}", "rock") for i in range(5)),
    )

    results = recommend(model, [seed.album_id], 20)

    assert ranked_titles(model, results)[0] == "Rare"


def test_higher_voted_shared_tag_outweighs_lower_voted_one():
    seed = album("Seed", votes={"ambient": 1, "drone": 20})
    model = model_of(seed, album("Ambient", "ambient"), album("Drone", "drone"))

    results = recommend(model, [seed.album_id], 20)

    assert ranked_titles(model, results) == ["Drone", "Ambient"]


def test_zero_votes_count_as_one():
    zero = model_of(album("Seed", votes={"jazz": 0, "funk": 1}), album("Other", "jazz"))
    one = model_of(album("Seed", votes={"jazz": 1, "funk": 1}), album("Other", "jazz"))

    np.testing.assert_allclose(zero.tag_matrix.toarray(), one.tag_matrix.toarray())


def test_text_counts_only_when_both_albums_have_it():
    seed = album("Seed", "jazz", "modal", text="spiritual modal saxophone")
    with_text = album("With Text", "jazz", text="modal saxophone suite")
    without = album("Without Text", "jazz", "modal")
    model = model_of(seed, with_text, without)

    blended = scores(recommend(model, [seed.album_id], 20))
    tags_only = scores(recommend(model, [seed.album_id], 20, alpha=1.0))

    assert blended[without.album_id] == pytest.approx(
        cosine(model.tag_matrix, model, seed, without), abs=1e-9
    )
    assert blended[with_text.album_id] == pytest.approx(
        0.6 * cosine(model.tag_matrix, model, seed, with_text)
        + 0.4 * cosine(model.text_matrix, model, seed, with_text),
        abs=1e-9,
    )
    assert tags_only[with_text.album_id] == pytest.approx(
        cosine(model.tag_matrix, model, seed, with_text), abs=1e-9
    )


def test_text_of_only_stopwords_counts_as_no_text():
    seed = album("Seed", "jazz", text="spiritual saxophone")
    blank = album("Blank", "jazz", text="the and of it")
    model = model_of(seed, blank)

    [result] = recommend(model, [seed.album_id], 20)

    assert not model.has_text[model.row_of[blank.album_id]]
    assert model.metadata["n_with_text"] == 1
    assert result.score == pytest.approx(1.0)


def test_catalog_without_any_text_scores_on_tags():
    seed = album("Seed", "jazz")
    model = model_of(seed, album("Other", "jazz"))

    [result] = recommend(model, [seed.album_id], 20)

    assert model.text_matrix.shape == (2, 0)
    assert result.score == pytest.approx(1.0)


def test_group_score_sums_each_seeds_similarity_and_excludes_seeds():
    a = album("Seed A", "ambient", "drone")
    b = album("Seed B", "techno", "acid")
    both = album("Both", "ambient", "techno")
    model = model_of(a, b, both, album("Neither", "polka"))

    alone_a = scores(recommend(model, [a.album_id], 20))
    alone_b = scores(recommend(model, [b.album_id], 20))
    together = scores(recommend(model, [a.album_id, b.album_id], 20))

    assert together[both.album_id] == pytest.approx(
        alone_a[both.album_id] + alone_b[both.album_id], abs=1e-8
    )
    assert set(together) == {both.album_id}


def test_ties_break_by_title_then_album_id():
    seed = album("Seed", "jazz")
    twins = [
        AlbumDoc(album_id=uuid.UUID(int=n), title="Same", term_votes={"jazz": 1}) for n in (2, 1)
    ]
    alpha, beta = album("Alpha", "jazz"), album("Beta", "jazz")
    model = model_of(seed, beta, alpha, *twins)

    results = recommend(model, [seed.album_id], 20)

    assert [r.album_id for r in results] == [
        alpha.album_id,
        beta.album_id,
        uuid.UUID(int=1),
        uuid.UUID(int=2),
    ]


def test_limit_keeps_tie_order_at_the_cut():
    seed = album("Seed", "jazz")
    model = model_of(seed, *(album(name, "jazz") for name in ["E", "C", "A", "D", "B"]))

    assert ranked_titles(model, recommend(model, [seed.album_id], 2)) == ["A", "B"]


def test_seeds_missing_from_the_model_are_ignored():
    seed, other = album("Seed", "jazz"), album("Other", "jazz")
    model = model_of(seed, other)
    unknown = uuid.uuid4()

    assert [r.album_id for r in recommend(model, [seed.album_id, unknown], 20)] == [
        other.album_id
    ]
    assert recommend(model, [unknown], 20) == []
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_recommend_tfidf.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.recommend.tfidf'`

- [ ] **Step 4: Write the implementation**

`backend/src/crate_backend/recommend/tfidf.py`:

```python
"""TF-IDF recommender (Phase 4, Milestone 2): pure functions over in-memory
data, no database.

Each album gets two L2-normalized TF-IDF rows. The tag row holds genre and
tag names as whole terms, weighted by MusicBrainz votes and by rarity. The
text row, present only for albums with article text, holds words and
two-word phrases. Similarity blends the two cosines only when both albums
have text, so albums without an article are compared on tags alone rather
than penalized.

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md
"""

import math
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

import numpy as np
import sklearn
from scipy import sparse
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import (
    ENGLISH_STOP_WORDS,
    TfidfTransformer,
    TfidfVectorizer,
)

DEFAULT_ALPHA = 0.6

# Words music writing uses about every album, so they say nothing about
# what one sounds like. Added to scikit-learn's English stop words.
MUSIC_PRESS_STOPWORDS = frozenset(
    {
        "album", "albums", "song", "songs", "track", "tracks", "record", "records",
        "recorded", "recording", "released", "release", "single", "singles", "chart",
        "charts", "billboard", "band", "label", "lp", "ep", "version", "edition", "also",
        "first", "second", "including",
    }
)  # fmt: skip


@dataclass(frozen=True)
class AlbumDoc:
    album_id: uuid.UUID
    title: str
    # Normalized genre/tag term -> MusicBrainz vote count.
    term_votes: dict[str, int]
    # Article text after clean_article; empty when the album has none.
    text: str = ""


@dataclass
class TfidfModel:
    album_ids: list[uuid.UUID]
    titles: list[str]
    tag_terms: np.ndarray
    # Albums x tag terms, rows L2-normalized.
    tag_matrix: sparse.csr_matrix
    text_terms: np.ndarray
    # Albums x text terms, rows L2-normalized; all-zero for albums without text.
    text_matrix: sparse.csr_matrix
    has_text: np.ndarray
    metadata: dict[str, Any]
    row_of: dict[uuid.UUID, int] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.row_of = {album_id: row for row, album_id in enumerate(self.album_ids)}


@dataclass(frozen=True)
class TfidfRecommendation:
    album_id: uuid.UUID
    score: float
    shared_terms: list[str]
    shared_text_terms: list[str]


def build_model(
    docs: list[AlbumDoc],
    *,
    alpha: float = DEFAULT_ALPHA,
    ngram_range: tuple[int, int] = (1, 2),
    min_df: int | float = 2,
    max_df: int | float = 0.5,
    max_features: int | None = None,
    extra_metadata: dict[str, Any] | None = None,
) -> TfidfModel:
    text_params = {
        "ngram_range": ngram_range,
        "min_df": min_df,
        "max_df": max_df,
        "max_features": max_features,
    }
    tag_terms, tag_matrix = _tag_block(docs)
    text_terms, text_matrix = _text_block(docs, text_params)
    # A row that vectorized to nothing (only stop words) is no text at all.
    has_text = np.diff(text_matrix.indptr) > 0
    metadata = {
        "model_version": datetime.now(UTC).isoformat(timespec="seconds"),
        "alpha": alpha,
        "text_vectorizer": {**text_params, "ngram_range": list(ngram_range)},
        "n_albums": len(docs),
        "n_with_text": int(has_text.sum()),
        "sklearn_version": sklearn.__version__,
        **(extra_metadata or {}),
    }
    return TfidfModel(
        album_ids=[doc.album_id for doc in docs],
        titles=[doc.title for doc in docs],
        tag_terms=tag_terms,
        tag_matrix=tag_matrix,
        text_terms=text_terms,
        text_matrix=text_matrix,
        has_text=has_text,
        metadata=metadata,
    )


def _tag_block(docs: list[AlbumDoc]) -> tuple[np.ndarray, sparse.csr_matrix]:
    """TF = 1 + ln(votes), so ten votes count about three times one vote
    rather than ten times; then smoothed IDF and L2 normalization."""
    vectorizer = DictVectorizer(sort=True)
    tf = vectorizer.fit_transform(
        {term: 1 + math.log(max(votes, 1)) for term, votes in doc.term_votes.items()}
        for doc in docs
    )
    tfidf = TfidfTransformer(norm="l2", smooth_idf=True, sublinear_tf=False).fit_transform(tf)
    return vectorizer.get_feature_names_out(), sparse.csr_matrix(tfidf)


def _text_block(
    docs: list[AlbumDoc], params: dict[str, Any]
) -> tuple[np.ndarray, sparse.csr_matrix]:
    rows = [i for i, doc in enumerate(docs) if doc.text.strip()]
    if not rows:
        return np.array([], dtype=object), sparse.csr_matrix((len(docs), 0))
    vectorizer = TfidfVectorizer(
        stop_words=sorted(ENGLISH_STOP_WORDS | MUSIC_PRESS_STOPWORDS),
        sublinear_tf=True,
        **params,
    )
    fitted = vectorizer.fit_transform(docs[i].text for i in rows)
    # Place the fitted rows at their albums' positions; other rows stay empty.
    placement = sparse.csr_matrix(
        (np.ones(len(rows)), (rows, range(len(rows)))), shape=(len(docs), len(rows))
    )
    return vectorizer.get_feature_names_out(), sparse.csr_matrix(placement @ fitted)


def recommend(
    model: TfidfModel, seed_ids: list[uuid.UUID], limit: int, *, alpha: float | None = None
) -> list[TfidfRecommendation]:
    """Rank model albums related to the seeds. Seeds missing from the model
    (added to the catalog after the build) contribute nothing; seeds are
    never returned."""
    seed_rows = sorted({model.row_of[s] for s in seed_ids if s in model.row_of})
    if not seed_rows:
        return []
    scores = _group_scores(model, seed_rows, model.metadata["alpha"] if alpha is None else alpha)
    rounded = np.round(scores, 9)
    return [
        TfidfRecommendation(
            album_id=model.album_ids[row],
            score=float(rounded[row]),
            shared_terms=[],
            shared_text_terms=[],
        )
        for row in _rank(model, rounded, seed_rows, limit)
    ]


def _cosines(matrix: sparse.csr_matrix, seed_rows: list[int]) -> np.ndarray:
    """Cosine of every album with each seed, shape (seeds, albums). Rows are
    L2-normalized, so dot products are cosines. Multiplying the full matrix
    by the few seed rows avoids transposing the full matrix per request."""
    return (matrix @ matrix[seed_rows].T).T.toarray()


def _group_scores(model: TfidfModel, seed_rows: list[int], alpha: float) -> np.ndarray:
    tag = _cosines(model.tag_matrix, seed_rows)
    text = _cosines(model.text_matrix, seed_rows)
    both_have_text = model.has_text[seed_rows][:, None] & model.has_text[None, :]
    return np.where(both_have_text, alpha * tag + (1 - alpha) * text, tag).sum(axis=0)


def _rank(model: TfidfModel, rounded: np.ndarray, seed_rows: list[int], limit: int) -> list[int]:
    """Rows ordered by rounded score desc, then title, then album id."""
    rounded = rounded.copy()
    rounded[seed_rows] = 0.0
    candidates = np.flatnonzero(rounded > 0)
    if len(candidates) > limit:
        # Keep everything tied with the limit-th score so the title/id
        # tie-break, not np.partition, decides who makes the cut.
        cutoff = np.partition(rounded[candidates], -limit)[-limit]
        candidates = candidates[rounded[candidates] >= cutoff]
    ordered = sorted(
        (int(row) for row in candidates),
        key=lambda row: (-rounded[row], model.titles[row], str(model.album_ids[row])),
    )
    return ordered[:limit]
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_recommend_tfidf.py -v && uv run ruff check src tests`
Expected: 10 passed; ruff clean.

- [ ] **Step 6: Commit**

```bash
git add backend/pyproject.toml backend/uv.lock backend/src/crate_backend/recommend/tfidf.py backend/tests/test_recommend_tfidf.py
git commit -m "feat: build TF-IDF tag and text blocks and rank by blended cosine

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Explanations and model save/load

**Files:**
- Modify: `backend/src/crate_backend/recommend/tfidf.py`
- Test: `backend/tests/test_recommend_tfidf.py` (append)

**Interfaces:**
- Consumes: Task 2's `TfidfModel`, `recommend`, `build_model`.
- Produces:
  - `recommend(...)` now fills `shared_terms` (top 5 tag terms) and `shared_text_terms` (top 5 text terms) by contribution.
  - `TOP_TERMS = 5`
  - `save_model(model: TfidfModel, path: Path) -> None`: creates parent dirs; writes atomically (temp file, then rename).
  - `load_model(path: Path) -> TfidfModel`

- [ ] **Step 1: Write the failing tests** (append to `backend/tests/test_recommend_tfidf.py`, and add `from datetime import datetime`, `import sklearn` and `save_model, load_model` to the imports)

```python
def test_shared_terms_are_ordered_by_contribution():
    seed = album("Seed", "rock", "glitch", "idm")
    candidate = album("Candidate", "rock", "glitch", "idm")
    model = model_of(
        seed,
        candidate,
        *(album(f"Rock {i}", "rock") for i in range(4)),
        album("IDM Fan", "idm"),
    )

    first = recommend(model, [seed.album_id], 20)[0]

    assert first.album_id == candidate.album_id
    # glitch is on 2 albums, idm on 3, rock on 6: rarer terms contribute more.
    assert first.shared_terms == ["glitch", "idm", "rock"]


def test_explanations_are_capped_at_five_terms():
    terms = [f"t{i}" for i in range(8)]
    seed = album("Seed", *terms)

    [result] = recommend(model_of(seed, album("Candidate", *terms)), [seed.album_id], 20)

    # Equal contributions fall back to alphabetical order.
    assert result.shared_terms == ["t0", "t1", "t2", "t3", "t4"]


def test_shared_text_terms_rank_distinctive_shared_words_first():
    seed = album("Seed", "jazz", text="modal saxophone saxophone suite")
    candidate = album("Candidate", "jazz", text="modal saxophone trumpet")
    model = model_of(
        seed, candidate, album("Other", "jazz", text="modal piano"), ngram_range=(1, 1)
    )

    result = next(
        r for r in recommend(model, [seed.album_id], 20) if r.album_id == candidate.album_id
    )

    assert result.shared_text_terms == ["saxophone", "modal"]


def test_shared_text_terms_empty_when_candidate_has_no_text():
    seed = album("Seed", "jazz", text="modal saxophone")
    candidate = album("Candidate", "jazz")
    model = model_of(seed, candidate, album("Other", "polka", text="modal accordion"))

    result = next(
        r for r in recommend(model, [seed.album_id], 20) if r.album_id == candidate.album_id
    )

    assert result.shared_terms == ["jazz"]
    assert result.shared_text_terms == []


def test_saved_model_loads_with_identical_scores(tmp_path):
    seed = album("Seed", "jazz", "modal", text="spiritual modal saxophone")
    model = model_of(
        seed,
        album("With Text", "jazz", text="modal saxophone suite"),
        album("Without Text", "modal"),
    )
    path = tmp_path / "nested" / "tfidf.joblib"

    save_model(model, path)
    loaded = load_model(path)

    assert recommend(loaded, [seed.album_id], 20) == recommend(model, [seed.album_id], 20)
    assert loaded.metadata == model.metadata
    assert not path.with_suffix(".tmp").exists()


def test_metadata_records_how_the_model_was_built():
    model = build_model(
        [album("A", "jazz", text="modal saxophone"), album("B", "jazz")],
        alpha=0.7,
        min_df=1,
        max_df=1.0,
        extra_metadata={"catalog_source": "test dump"},
    )

    metadata = model.metadata
    assert metadata["alpha"] == 0.7
    assert metadata["n_albums"] == 2
    assert metadata["n_with_text"] == 1
    assert metadata["catalog_source"] == "test dump"
    assert metadata["text_vectorizer"]["ngram_range"] == [1, 2]
    assert metadata["sklearn_version"] == sklearn.__version__
    datetime.fromisoformat(metadata["model_version"])
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_recommend_tfidf.py -v`
Expected: ImportError on `save_model`/`load_model` (the whole module fails to collect). Once imports exist, the explanation tests fail with `[] != [...]`.

- [ ] **Step 3: Implement explanations and save/load**

In `tfidf.py`, add `from pathlib import Path` and `import joblib` to the imports, add `TOP_TERMS = 5` under `DEFAULT_ALPHA`, and replace `recommend` with:

```python
def recommend(
    model: TfidfModel, seed_ids: list[uuid.UUID], limit: int, *, alpha: float | None = None
) -> list[TfidfRecommendation]:
    """Rank model albums related to the seeds. Seeds missing from the model
    (added to the catalog after the build) contribute nothing; seeds are
    never returned."""
    seed_rows = sorted({model.row_of[s] for s in seed_ids if s in model.row_of})
    if not seed_rows:
        return []
    scores = _group_scores(model, seed_rows, model.metadata["alpha"] if alpha is None else alpha)
    rounded = np.round(scores, 9)
    tag_seed_weights = _seed_weights(model.tag_matrix, seed_rows)
    text_seed_weights = _seed_weights(model.text_matrix, seed_rows)
    return [
        TfidfRecommendation(
            album_id=model.album_ids[row],
            score=float(rounded[row]),
            shared_terms=_top_terms(model.tag_matrix, model.tag_terms, row, tag_seed_weights),
            shared_text_terms=_top_terms(
                model.text_matrix, model.text_terms, row, text_seed_weights
            ),
        )
        for row in _rank(model, rounded, seed_rows, limit)
    ]
```

Add these after `_rank`:

```python
def _seed_weights(matrix: sparse.csr_matrix, seed_rows: list[int]) -> np.ndarray:
    """Each term's weight summed over the seeds (seeds without text add 0)."""
    return np.asarray(matrix[seed_rows].sum(axis=0)).ravel()


def _top_terms(
    matrix: sparse.csr_matrix, terms: np.ndarray, row: int, seed_weights: np.ndarray
) -> list[str]:
    """The album's terms that contribute most to its score: summed seed
    weight times the album's own weight, highest first, ties alphabetical."""
    start, end = matrix.indptr[row], matrix.indptr[row + 1]
    columns = matrix.indices[start:end]
    contributions = matrix.data[start:end] * seed_weights[columns]
    ranked = sorted(
        (-contribution, str(terms[column]))
        for contribution, column in zip(contributions, columns, strict=True)
        if contribution > 0
    )
    return [term for _, term in ranked[:TOP_TERMS]]


def save_model(model: TfidfModel, path: Path) -> None:
    """Write the model as one joblib file. Written to a temp file and renamed
    so a process loading the path never sees a half-written file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    joblib.dump(
        {
            "album_ids": model.album_ids,
            "titles": model.titles,
            "tag_terms": model.tag_terms,
            "tag_matrix": model.tag_matrix,
            "text_terms": model.text_terms,
            "text_matrix": model.text_matrix,
            "has_text": model.has_text,
            "metadata": model.metadata,
        },
        temp,
    )
    temp.replace(path)


def load_model(path: Path) -> TfidfModel:
    return TfidfModel(**joblib.load(path))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_recommend_tfidf.py -v && uv run ruff check src tests`
Expected: 16 passed; ruff clean.

- [ ] **Step 5: Commit**

```bash
git add backend/src/crate_backend/recommend/tfidf.py backend/tests/test_recommend_tfidf.py
git commit -m "feat: explain TF-IDF results by term contribution and save/load the model

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: Model path setting and the build script

**Files:**
- Modify: `backend/src/crate_backend/core/config.py`, `backend/.env.example`, `.gitignore`
- Create: `backend/src/crate_backend/scripts/build_tfidf_model.py`
- Test: `backend/tests/test_config.py` (append), `backend/tests/test_build_tfidf_model_script.py` (create)

**Interfaces:**
- Consumes: `merge_term_votes`, `clean_article` (Task 1); `AlbumDoc`, `build_model`, `save_model`, `DEFAULT_ALPHA` (Tasks 2–3); `read_dump_metadata` from `musicbrainz/dump_reader.py`.
- Produces:
  - `Settings.tfidf_model_path: str` (env `CRATE_TFIDF_MODEL_PATH`)
  - `load_album_docs(session: AsyncSession, *, drop_reception: bool = False, drop_personnel: bool = False, only: list[uuid.UUID] | None = None) -> list[AlbumDoc]`, ordered by album id
  - `parse_args(argv: list[str] | None = None) -> argparse.Namespace` with `alpha: float`, `no_bigrams: bool`, `no_reception: bool`, `no_personnel: bool`, `max_features: int | None`, `out: Path | None`

- [ ] **Step 1: Write the failing tests**

Append to `backend/tests/test_config.py`:

```python
def test_tfidf_model_path_defaults_to_repo_models_dir():
    settings = Settings(_env_file=None)
    assert settings.tfidf_model_path.endswith("/models/tfidf.joblib")


def test_tfidf_model_path_reads_from_env(monkeypatch):
    monkeypatch.setenv("CRATE_TFIDF_MODEL_PATH", "/tmp/elsewhere.joblib")
    settings = Settings(_env_file=None)
    assert settings.tfidf_model_path == "/tmp/elsewhere.joblib"
```

`backend/tests/test_build_tfidf_model_script.py`:

```python
import uuid
from datetime import UTC, datetime

import pytest

from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.scripts.build_tfidf_model import load_album_docs, parse_args

ARTICLE = (
    "Lead about modal saxophone.\n\n"
    "== Critical reception ==\nCritics loved it.\n\n"
    "== Personnel ==\nElvin Jones – drums\n\n"
    "== Track listing ==\nSong – 3:00"
)


async def _fixture_albums(db_session) -> tuple[Album, Album]:
    album = Album(title="Fixture Build Album", artist_name="Fixture Artist")
    bare = Album(title="Fixture Bare Album", artist_name="Fixture Artist")
    genre = Genre(musicbrainz_id=str(uuid.uuid4()), name="Zzfixture-Build-Post-Bop")
    tag = Tag(name="zzfixture build post bop")
    db_session.add_all([album, bare, genre, tag])
    await db_session.flush()
    now = datetime.now(UTC)
    db_session.add_all(
        [
            AlbumGenre(album_id=album.id, genre_id=genre.id, count=3),
            AlbumTag(album_id=album.id, tag_id=tag.id, count=5),
            AlbumText(album_id=album.id, source=WIKIPEDIA_SOURCE, text=ARTICLE, fetched_at=now),
            AlbumText(album_id=bare.id, source=WIKIPEDIA_SOURCE, text=None, fetched_at=now),
        ]
    )
    await db_session.flush()
    return album, bare


async def test_load_album_docs_merges_votes_and_cleans_text(db_session):
    album, bare = await _fixture_albums(db_session)

    docs = {d.album_id: d for d in await load_album_docs(db_session, only=[album.id, bare.id])}

    assert set(docs) == {album.id, bare.id}
    assert docs[album.id].title == "Fixture Build Album"
    assert docs[album.id].term_votes == {"zzfixture build post bop": 5}
    assert docs[album.id].text == (
        "Lead about modal saxophone.\n\nCritics loved it.\n\nElvin Jones – drums"
    )
    assert docs[bare.id].term_votes == {}
    assert docs[bare.id].text == ""


async def test_load_album_docs_can_drop_reception_and_personnel(db_session):
    album, _ = await _fixture_albums(db_session)

    [doc] = await load_album_docs(
        db_session, drop_reception=True, drop_personnel=True, only=[album.id]
    )

    assert doc.text == "Lead about modal saxophone."


def test_parse_args_defaults():
    args = parse_args([])

    assert args.alpha == 0.6
    assert not args.no_bigrams and not args.no_reception and not args.no_personnel
    assert args.max_features is None and args.out is None


@pytest.mark.parametrize("alpha", ["-0.1", "1.5"])
def test_parse_args_rejects_alpha_outside_zero_to_one(alpha):
    with pytest.raises(SystemExit):
        parse_args(["--alpha", alpha])
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_config.py tests/test_build_tfidf_model_script.py -v`
Expected: `AttributeError: 'Settings' object has no attribute 'tfidf_model_path'` and `ModuleNotFoundError: No module named 'crate_backend.scripts.build_tfidf_model'`.

- [ ] **Step 3: Add the setting, env example and gitignore entry**

In `backend/src/crate_backend/core/config.py`, after `wikimedia_contact_email`:

```python

    # TF-IDF recommender model file (Phase 4), written by
    # scripts/build_tfidf_model.py and read by the API on first use.
    tfidf_model_path: str = str(_REPO_ROOT / "models" / "tfidf.joblib")
```

Append to `backend/.env.example`:

```
# TF-IDF model file written by scripts/build_tfidf_model.py. Defaults to
# <repo>/models/tfidf.joblib.
# CRATE_TFIDF_MODEL_PATH=
```

Append to the repo-root `.gitignore`, after the Python block:

```
# Built recommender models (rebuild with scripts/build_tfidf_model.py)
/models/*.joblib
/models/*.tmp
```

- [ ] **Step 4: Write the build script**

`backend/src/crate_backend/scripts/build_tfidf_model.py`:

```python
"""Build the TF-IDF recommender model file from the catalog (Phase 4,
Milestone 2).

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md

Run with: uv run python -m crate_backend.scripts.build_tfidf_model
          [--alpha 0.6] [--no-bigrams] [--no-reception] [--no-personnel]
          [--max-features N] [--out PATH]

Reads every album's genre/tag votes and stored Wikipedia text, fits the
model and writes one joblib file (default: settings.tfidf_model_path). The
API loads that file on its first tfidf request and keeps it until restart,
so restart the backend after rebuilding. Evaluation variants are separate
files built with --out.
"""

import argparse
import asyncio
import time
import uuid
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.musicbrainz.dump_reader import read_dump_metadata
from crate_backend.recommend.text_cleaning import clean_article, merge_term_votes
from crate_backend.recommend.tfidf import DEFAULT_ALPHA, AlbumDoc, build_model, save_model

# The spec's fallback: past this in-memory size, rebuild with
# --max-features 100000 and record the change.
_LARGE_MODEL_BYTES = 500 * 1024 * 1024


async def load_album_docs(
    session: AsyncSession,
    *,
    drop_reception: bool = False,
    drop_personnel: bool = False,
    only: list[uuid.UUID] | None = None,
) -> list[AlbumDoc]:
    """One AlbumDoc per album, ordered by id so builds are reproducible.
    `only` restricts loading to those albums (for tests)."""

    def restrict(query, album_id_column):
        return query if only is None else query.where(album_id_column.in_(only))

    albums = (
        await session.execute(restrict(select(Album.id, Album.title), Album.id).order_by(Album.id))
    ).all()

    pairs: dict[uuid.UUID, list[tuple[str, int]]] = {}
    genre_votes = select(AlbumGenre.album_id, Genre.name, AlbumGenre.count).join(
        Genre, Genre.id == AlbumGenre.genre_id
    )
    tag_votes = select(AlbumTag.album_id, Tag.name, AlbumTag.count).join(
        Tag, Tag.id == AlbumTag.tag_id
    )
    for query, column in ((genre_votes, AlbumGenre.album_id), (tag_votes, AlbumTag.album_id)):
        for album_id, name, votes in await session.execute(restrict(query, column)):
            pairs.setdefault(album_id, []).append((name, votes))

    texts = dict(
        (
            await session.execute(
                restrict(
                    select(AlbumText.album_id, AlbumText.text).where(
                        AlbumText.source == WIKIPEDIA_SOURCE, AlbumText.text.is_not(None)
                    ),
                    AlbumText.album_id,
                )
            )
        ).all()
    )

    return [
        AlbumDoc(
            album_id=album_id,
            title=title,
            term_votes=merge_term_votes(pairs.get(album_id, [])),
            text=clean_article(
                texts[album_id], drop_reception=drop_reception, drop_personnel=drop_personnel
            )
            if album_id in texts
            else "",
        )
        for album_id, title in albums
    ]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the TF-IDF recommender model file.")
    parser.add_argument(
        "--alpha", type=float, default=DEFAULT_ALPHA, help="tag weight in the blend, 0–1"
    )
    parser.add_argument("--no-bigrams", action="store_true", help="single words only")
    parser.add_argument(
        "--no-reception", action="store_true", help="drop Reception sections from articles"
    )
    parser.add_argument(
        "--no-personnel", action="store_true", help="drop Personnel/Credits sections"
    )
    parser.add_argument("--max-features", type=int, default=None, help="cap the text vocabulary")
    parser.add_argument("--out", type=Path, default=None, help="model file to write")
    args = parser.parse_args(argv)
    if not 0 <= args.alpha <= 1:
        parser.error("--alpha must be between 0 and 1")
    return args


def _catalog_source() -> str:
    archive = Path(get_settings().musicbrainz_dump_dir) / "release-group.tar.xz"
    if not archive.exists():
        return "MusicBrainz dump (unknown date)"
    return f"MusicBrainz dump {read_dump_metadata(archive).get('TIMESTAMP', '(unknown date)')}"


def _megabytes(n_bytes: int) -> str:
    return f"{n_bytes / 1024 / 1024:.0f} MB"


async def build(args: argparse.Namespace) -> None:
    out = args.out or Path(get_settings().tfidf_model_path)
    started = time.perf_counter()
    async with async_session_factory() as session:
        docs = await load_album_docs(
            session, drop_reception=args.no_reception, drop_personnel=args.no_personnel
        )
    loaded = time.perf_counter()

    model = build_model(
        docs,
        alpha=args.alpha,
        ngram_range=(1, 1) if args.no_bigrams else (1, 2),
        max_features=args.max_features,
        extra_metadata={
            "catalog_source": _catalog_source(),
            "drop_reception": args.no_reception,
            "drop_personnel": args.no_personnel,
        },
    )
    fitted = time.perf_counter()
    save_model(model, out)
    saved = time.perf_counter()

    matrix_bytes = sum(
        m.data.nbytes + m.indices.nbytes + m.indptr.nbytes
        for m in (model.tag_matrix, model.text_matrix)
    )
    n_albums, n_text = model.metadata["n_albums"], model.metadata["n_with_text"]
    print(f"Albums:          {n_albums:,} ({n_text:,} with text, {100 * n_text / n_albums:.0f}%)")
    print(f"Tag terms:       {len(model.tag_terms):,}")
    print(f"Text terms:      {len(model.text_terms):,}")
    print(f"Nonzeros:        {model.tag_matrix.nnz:,} tag, {model.text_matrix.nnz:,} text")
    print(f"Matrices:        {_megabytes(matrix_bytes)} in memory")
    print(f"File:            {out} ({_megabytes(out.stat().st_size)})")
    print(
        f"Time:            load {loaded - started:.1f}s, fit {fitted - loaded:.1f}s, "
        f"save {saved - fitted:.1f}s"
    )
    print(f"Model version:   {model.metadata['model_version']}")
    if matrix_bytes > _LARGE_MODEL_BYTES and args.max_features is None:
        print("Model exceeds 500 MB: rebuild with --max-features 100000 and record the change.")


def main() -> None:
    asyncio.run(build(parse_args()))


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_config.py tests/test_build_tfidf_model_script.py -v && uv run ruff check src tests`
Expected: all pass; ruff clean.

- [ ] **Step 6: Commit**

```bash
git add .gitignore backend/.env.example backend/src/crate_backend/core/config.py backend/src/crate_backend/scripts/build_tfidf_model.py backend/tests/test_config.py backend/tests/test_build_tfidf_model_script.py
git commit -m "feat: add TF-IDF model path setting and catalog build script

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Serve TF-IDF behind the `approach` switch

**Files:**
- Create: `backend/src/crate_backend/recommend/model_store.py`
- Modify: `backend/src/crate_backend/api/routes/recommendations.py`
- Test: `backend/tests/test_tfidf_model_store.py` (create), `backend/tests/test_recommendations_api.py` (modify)

**Interfaces:**
- Consumes: `load_model`, `recommend`, `TfidfModel`, `AlbumDoc`, `build_model`, `save_model` (Tasks 2–3); `Settings.tfidf_model_path` (Task 4).
- Produces:
  - `model_store.get_tfidf_model() -> TfidfModel | None`
  - The API contract in Global Constraints.

- [ ] **Step 1: Write the failing model-store tests**

`backend/tests/test_tfidf_model_store.py`:

```python
import uuid

import pytest

from crate_backend.core.config import get_settings
from crate_backend.recommend import model_store
from crate_backend.recommend.tfidf import AlbumDoc, build_model, save_model


@pytest.fixture
def model_path(tmp_path, monkeypatch):
    path = tmp_path / "tfidf.joblib"
    monkeypatch.setattr(get_settings(), "tfidf_model_path", str(path))
    monkeypatch.setattr(model_store, "_loaded", {})
    return path


def _tiny_model():
    return build_model(
        [
            AlbumDoc(album_id=uuid.uuid4(), title="A", term_votes={"jazz": 1}),
            AlbumDoc(album_id=uuid.uuid4(), title="B", term_votes={"jazz": 1}),
        ],
        min_df=1,
        max_df=1.0,
    )


def test_missing_file_gives_none_and_is_picked_up_once_built(model_path):
    assert model_store.get_tfidf_model() is None

    model = _tiny_model()
    save_model(model, model_path)
    loaded = model_store.get_tfidf_model()

    assert loaded is not None
    assert loaded.metadata == model.metadata


def test_model_is_loaded_once_per_process(model_path):
    save_model(_tiny_model(), model_path)

    assert model_store.get_tfidf_model() is model_store.get_tfidf_model()
```

- [ ] **Step 2: Write the failing API tests**

In `backend/tests/test_recommendations_api.py`:

Add imports:

```python
from crate_backend.api.routes import recommendations as recommendations_route
from crate_backend.recommend.tfidf import AlbumDoc, build_model
```

Add helpers after `_post`:

```python
@pytest.fixture
def use_model(monkeypatch):
    """Serve the given model (or None: no model file built) for tfidf requests."""

    def use(model):
        monkeypatch.setattr(recommendations_route, "get_tfidf_model", lambda: model)

    return use


def _doc(album: Album, *terms: str, text: str = "") -> AlbumDoc:
    return AlbumDoc(
        album_id=album.id, title=album.title, term_votes={t: 1 for t in terms}, text=text
    )


def _model(*docs: AlbumDoc):
    return build_model(list(docs), min_df=1, max_df=1.0)
```

Update `test_returns_ranked_albums_with_shared_terms`: after `assert body["reason"] is None` add `assert body["approach"] == "overlap"` and `assert body["model_version"] is None`, and add `"shared_text_terms": [],` after `"shared_terms": [...]` in the expected result dict.

Update the expected bodies in `test_seeds_without_terms_explain_the_empty_result` and `test_tagged_seed_with_no_matches_has_no_reason` to:

```python
    assert response.json() == {
        "approach": "overlap",
        "model_version": None,
        "results": [],
        "reason": "seeds_have_no_terms",  # and `None` in the second test
    }
```

Add `{"album_ids": [str(uuid.uuid4())], "approach": "bogus"},` to the `test_invalid_input_is_422` parametrize list.

Append:

```python
async def test_tfidf_ranks_from_the_model_and_explains_with_text(client, db_session, use_model):
    seed = await _album(db_session, "Seed", "a")
    match = await _album(db_session, "Match", release_year=1999)
    model = _model(
        _doc(seed, "jazz", text="modal saxophone"),
        _doc(match, "jazz", text="modal saxophone suite"),
    )
    use_model(model)

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.status_code == 200
    body = response.json()
    assert body["approach"] == "tfidf"
    assert body["model_version"] == model.metadata["model_version"]
    assert body["reason"] is None
    [result] = body["results"]
    assert result["id"] == str(match.id)
    assert result["title"] == "Match"
    assert result["release_year"] == 1999
    assert result["shared_terms"] == ["jazz"]
    assert sorted(result["shared_text_terms"]) == ["modal", "modal saxophone", "saxophone"]


async def test_tfidf_without_a_built_model_is_503(client, db_session, use_model):
    seed = await _album(db_session, "Seed", "a")
    use_model(None)

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.status_code == 503
    assert response.json() == {"detail": "TF-IDF model not built"}


async def test_overlap_works_without_a_built_model(client, db_session, use_model):
    seed = await _album(db_session, "Seed", "a")
    use_model(None)

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.status_code == 200


async def test_seeds_missing_from_the_model_explain_the_empty_result(
    client, db_session, use_model
):
    seed = await _album(db_session, "New Seed", "a")
    older = await _album(db_session, "Older Album", "b")
    model = _model(_doc(older, "jazz"))
    use_model(model)

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.json() == {
        "approach": "tfidf",
        "model_version": model.metadata["model_version"],
        "results": [],
        "reason": "seeds_not_in_model",
    }


async def test_tfidf_seeds_without_terms_keep_their_reason(client, db_session, use_model):
    seed = await _album(db_session, "Untagged Seed")
    other = await _album(db_session, "Tagged Album", "a")
    # A model needs at least one term in the catalog to fit.
    use_model(_model(_doc(seed), _doc(other, "jazz")))

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.json()["reason"] == "seeds_have_no_terms"


async def test_albums_removed_since_the_model_was_built_are_skipped(
    client, db_session, use_model
):
    seed = await _album(db_session, "Seed", "a")
    kept = await _album(db_session, "Kept")
    gone = AlbumDoc(album_id=uuid.uuid4(), title="Gone", term_votes={"jazz": 1})
    use_model(_model(_doc(seed, "jazz"), _doc(kept, "jazz"), gone))

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.status_code == 200
    assert [r["id"] for r in response.json()["results"]] == [str(kept.id)]
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_tfidf_model_store.py tests/test_recommendations_api.py -v`
Expected: `ModuleNotFoundError: No module named 'crate_backend.recommend.model_store'`; the API module fails to collect on `recommendations_route.get_tfidf_model` / missing fields.

- [ ] **Step 4: Write the model store**

`backend/src/crate_backend/recommend/model_store.py`:

```python
"""The API process's copy of the TF-IDF model file (Phase 4, Milestone 2)."""

from pathlib import Path

from crate_backend.core.config import get_settings
from crate_backend.recommend.tfidf import TfidfModel, load_model

_loaded: dict[Path, TfidfModel] = {}


def get_tfidf_model() -> TfidfModel | None:
    """The model at settings.tfidf_model_path, loaded on first use and kept
    for the life of the process. None while the file doesn't exist. That
    answer isn't cached, so a first build needs no restart; a rebuild of an
    already-loaded model does."""
    path = Path(get_settings().tfidf_model_path)
    if path not in _loaded:
        if not path.exists():
            return None
        _loaded[path] = load_model(path)
    return _loaded[path]
```

- [ ] **Step 5: Update the endpoint**

Replace `backend/src/crate_backend/api/routes/recommendations.py` with:

```python
import uuid
from typing import Literal, NamedTuple

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.concurrency import run_in_threadpool

from crate_backend.db.session import get_session
from crate_backend.models.catalog import Album
from crate_backend.recommend.model_store import get_tfidf_model
from crate_backend.recommend.overlap import recommend_by_overlap, seeds_have_terms
from crate_backend.recommend.tfidf import recommend as recommend_by_tfidf

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


class RecommendationRequest(BaseModel):
    album_ids: list[uuid.UUID] = Field(min_length=1, max_length=50)
    limit: int = Field(default=20, ge=1, le=50)
    # "overlap" (Jaccard, Phase 3) or "tfidf" (Phase 4). The default changes
    # only once the evaluation answer key picks a winner.
    approach: Literal["overlap", "tfidf"] = "overlap"


class RecommendedAlbum(BaseModel):
    id: str
    title: str
    artist_name: str | None
    release_year: int | None
    cover_art_url: str | None
    score: float
    shared_terms: list[str]
    # Article words/phrases behind the match; always empty for overlap.
    shared_text_terms: list[str]


class RecommendationResponse(BaseModel):
    approach: str
    # Build time of the TF-IDF model file that answered; null for overlap.
    model_version: str | None
    results: list[RecommendedAlbum]
    reason: str | None


class _Ranked(NamedTuple):
    album_id: uuid.UUID
    score: float
    shared_terms: list[str]
    shared_text_terms: list[str]


@router.post("", response_model=RecommendationResponse)
async def recommend(
    request: RecommendationRequest, session: AsyncSession = Depends(get_session)
) -> RecommendationResponse:
    """Albums related to a group's seed albums."""
    seed_ids = list(dict.fromkeys(request.album_ids))
    found = set(await session.scalars(select(Album.id).where(Album.id.in_(seed_ids))))
    missing = [str(album_id) for album_id in seed_ids if album_id not in found]
    if missing:
        raise HTTPException(
            status_code=404, detail={"message": "Unknown album ids", "missing": missing}
        )

    model = None
    if request.approach == "tfidf":
        # The first call reads the model file; keep that off the event loop.
        model = await run_in_threadpool(get_tfidf_model)
        if model is None:
            raise HTTPException(status_code=503, detail="TF-IDF model not built")
    model_version = model.metadata["model_version"] if model else None

    def respond(results: list[RecommendedAlbum], reason: str | None) -> RecommendationResponse:
        return RecommendationResponse(
            approach=request.approach, model_version=model_version, results=results, reason=reason
        )

    if not await seeds_have_terms(session, seed_ids):
        return respond([], "seeds_have_no_terms")

    if model is None:
        ranked = [
            _Ranked(r.album_id, r.score, r.shared_terms, [])
            for r in await recommend_by_overlap(session, seed_ids, request.limit)
        ]
    else:
        if not any(seed_id in model.row_of for seed_id in seed_ids):
            return respond([], "seeds_not_in_model")
        ranked = [
            _Ranked(r.album_id, r.score, r.shared_terms, r.shared_text_terms)
            for r in recommend_by_tfidf(model, seed_ids, request.limit)
        ]

    albums = {
        album.id: album
        for album in await session.scalars(
            select(Album).where(Album.id.in_([r.album_id for r in ranked]))
        )
    }
    return respond(
        [
            RecommendedAlbum(
                id=str(r.album_id),
                title=albums[r.album_id].title,
                artist_name=albums[r.album_id].artist_name,
                release_year=albums[r.album_id].release_year,
                cover_art_url=albums[r.album_id].cover_art_url,
                score=r.score,
                shared_terms=r.shared_terms,
                shared_text_terms=r.shared_text_terms,
            )
            for r in ranked
            # A model built before an album left the catalog can still rank it.
            if r.album_id in albums
        ],
        None,
    )
```

- [ ] **Step 6: Run the tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_tfidf_model_store.py tests/test_recommendations_api.py tests/test_recommend_overlap.py -v && uv run ruff check src tests`
Expected: all pass; ruff clean.

- [ ] **Step 7: Commit**

```bash
git add backend/src/crate_backend/recommend/model_store.py backend/src/crate_backend/api/routes/recommendations.py backend/tests/test_tfidf_model_store.py backend/tests/test_recommendations_api.py
git commit -m "feat: serve TF-IDF recommendations behind an approach switch

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: "Described alike" line in the group panel

**Files:**
- Modify: `frontend/app/page.tsx` (type `Recommendation` near line 51; result markup near line 950)

**Interfaces:**
- Consumes: the response field `shared_text_terms: string[]` (Task 5).
- Produces: UI only. The panel still sends no `approach`, so it gets the default (`overlap`), where `shared_text_terms` is always `[]` and the new line stays hidden until the default changes.

- [ ] **Step 1: Add the field to the type**

In `type Recommendation`, after `shared_terms: string[];`:

```ts
  shared_text_terms: string[];
```

- [ ] **Step 2: Render the line under "Shares"**

Replace:

```tsx
                          <small className="rec-terms">
                            Shares: {r.shared_terms.join(', ')}
                          </small>
```

with:

```tsx
                          <small className="rec-terms">
                            Shares: {r.shared_terms.join(', ')}
                          </small>
                          {r.shared_text_terms.length > 0 && (
                            <small className="rec-terms">
                              Described alike: {r.shared_text_terms.join(', ')}
                            </small>
                          )}
```

(`.rec-result small` is already `display: block` with a 5px top margin, so the two lines stack without new CSS.)

- [ ] **Step 3: Lint and type-check**

Run: `cd frontend && npx oxlint && npx tsc --noEmit`
Expected: no errors.

- [ ] **Step 4: Commit**

```bash
git add frontend/app/page.tsx
git commit -m "feat: show shared article terms as 'Described alike' in the group panel

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: Build the real model, measure, document, checkpoint

**Files:**
- Modify: `docs/recommendation-systems.md`

**Interfaces:**
- Consumes: everything above.
- Produces: `models/tfidf.joblib` (gitignored), recorded measurements, docs section 2.

- [ ] **Step 1: Full test suite and lint**

Run: `cd backend && uv run pytest -q && uv run ruff check src tests`
Expected: all pass. If anything fails, stop and fix before building.

- [ ] **Step 2: Build the real model**

Run: `cd backend && /usr/bin/time -l uv run python -m crate_backend.scripts.build_tfidf_model`
Expected: about 1–3 minutes. Record the printed stats and the "maximum resident set size" line (peak memory). If it prints the 500 MB warning, rebuild with `--max-features 100000` and record that too.

- [ ] **Step 3: Measure load time, in-memory size and per-request latency**

```bash
cd backend && uv run python - <<'EOF'
import random, resource, time
from pathlib import Path
from crate_backend.core.config import get_settings
from crate_backend.recommend.tfidf import load_model, recommend

before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
t = time.perf_counter()
model = load_model(Path(get_settings().tfidf_model_path))
print(f"load {time.perf_counter() - t:.2f}s")
after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(f"peak RSS growth {(after - before) / 1024 / 1024:.0f} MB")  # macOS reports bytes
rng = random.Random(0)
for n in (1, 5, 50):
    seeds = rng.sample(model.album_ids, n)
    times = []
    for _ in range(5):
        t = time.perf_counter()
        recommend(model, seeds, 20)
        times.append(time.perf_counter() - t)
    print(f"{n} seeds: {min(times) * 1000:.0f}–{max(times) * 1000:.0f} ms")
EOF
```

- [ ] **Step 4: Look at results for familiar seeds**

```bash
cd backend && uv run python - <<'EOF'
import asyncio
from pathlib import Path
from sqlalchemy import select
from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.models.catalog import Album
from crate_backend.recommend.tfidf import load_model, recommend

SEEDS = [("A Love Supreme", "John Coltrane"), ("Kid A", "Radiohead")]

async def main():
    model = load_model(Path(get_settings().tfidf_model_path))
    async with async_session_factory() as session:
        for title, artist in SEEDS:
            seed = await session.scalar(
                select(Album).where(Album.title == title, Album.artist_name == artist)
            )
            has_text = bool(model.has_text[model.row_of[seed.id]])
            print(f"\n=== {title} ({artist}), has article text: {has_text}")
            for r in recommend(model, [seed.id], 10):
                album = await session.get(Album, r.album_id)
                print(f"{r.score:.3f}  {album.title} / {album.artist_name}")
                print(f"       shares: {', '.join(r.shared_terms)}")
                print(f"       described alike: {', '.join(r.shared_text_terms)}")

asyncio.run(main())
EOF
```

Also smoke-test the live endpoint: start the backend (`uv run uvicorn crate_backend.main:app`), then `curl -s localhost:8000/recommendations -H 'content-type: application/json' -d '{"album_ids":["<A Love Supreme id>"],"approach":"tfidf","limit":5}'`. Expect `"approach":"tfidf"` and a non-null `model_version`.

Note while looking: same-artist crowding (artist names and band members' credits stay in the text), whether credited musicians/producers show up in "described alike" and look sensible, and whether results with articles seem pushed below results without them (the text-vs-tag scale risk). Report both at the checkpoint; don't fix them in this milestone.

- [ ] **Step 5: Update `docs/recommendation-systems.md`**

1. Summary table row 2: Status **Built YYYY-MM-DD (opt-in, `approach: "tfidf"`); not the default**; Signal used "Genre/tag votes + Wikipedia text, weighted by rarity"; Evaluated? "Pending (Milestone 3)".
2. Approach 1's API example: add `"approach": "overlap", "model_version": null` to the response and `"shared_text_terms": []` to the result. Add a bullet: `approach`: `"overlap"` (default) or `"tfidf"`.
3. Replace the short "2. TF-IDF text similarity (Phase 4)" note under Planned approaches with a full `## 2. TF-IDF text similarity` section placed after section 1, following "Adding a new approach":
   - **Status / Spec / Code:** status line; spec path; `recommend/text_cleaning.py`, `recommend/tfidf.py`, `recommend/model_store.py`, `scripts/build_tfidf_model.py`, endpoint.
   - **How it works:** the two blocks (tag TF = 1 + ln votes, smoothed IDF; text words + two-word phrases with English and music-press stop words, min_df 2, max_df 0.5), the dropped article sections, the Personnel/Credits filter (musical and production credits kept, crew-only lines dropped), the α = 0.6 blend only when both albums have text, summing over seeds, ordering, and explanations by contribution. Mention that "post bop"/"post-bop" are now one term.
   - **Worked example:** *A Love Supreme* top 3 with scores, shared terms and "described alike" terms from Step 4.
   - **Building the model:** the command, flags (`--alpha`, `--no-bigrams`, `--no-reception`, `--no-personnel`, `--max-features`, `--out`), where the file goes, "restart the API after a rebuild".
   - **API:** the `approach` field, `model_version`, `shared_text_terms`, the 503 and `seeds_not_in_model`.
   - **Performance:** the Step 2–3 numbers (build time, peak memory, file size, in-memory size, load time, latency for 1/5/50 seeds), dated.
   - **Known limitations:** text cosines run lower than tag cosines, so the blend may favour albums without articles (measured in Milestone 3); article coverage is 96% of the top popularity quartile vs 9% of the bottom; artist names are kept, so same-artist albums can crowd results; the model is a snapshot (albums added later can't be seeds or results until a rebuild; a rebuild needs an API restart); not yet evaluated.

- [ ] **Step 6: Commit**

```bash
git add docs/recommendation-systems.md
git commit -m "docs: document the TF-IDF recommender with measured build and latency

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

- [ ] **Step 7: Checkpoint with the owner**

Show: the Step 2–3 numbers, the Step 4 output for *A Love Supreme* and *Kid A* (plus any seeds the owner asks for), and the two things to watch (same-artist crowding, articles vs. no articles). Wait for the owner's go-ahead before starting Milestone 3.
