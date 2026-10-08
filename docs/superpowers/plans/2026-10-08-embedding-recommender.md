# Sentence-Embedding Recommender (Phase 5a) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Embed each album's tags and Wikipedia text with a pretrained sentence encoder, serve the result as `approach: "embeddings"`, and add two evaluation variants so it can be scored against overlap and TF-IDF on the answer key.

**Architecture:** A new `recommend/embeddings.py` mirrors `recommend/tfidf.py`: pure functions over an in-memory `EmbeddingModel` (two unit-vector matrices, a has-text mask, each album's term votes, metadata), saved as one joblib file and loaded once per API process. The encoder is a small `Encoder` protocol so tests use a fake and only the build script needs `torch`. Ranking is extracted into `recommend/ranking.py` and shared with TF-IDF.

**Tech Stack:** Python 3.12, numpy, joblib, FastAPI, SQLAlchemy (existing); `sentence-transformers` (new, optional dependency group `embeddings`); pytest.

**Spec:** `docs/superpowers/specs/2026-10-08-embedding-recommender-design.md` (read it first; it explains why each choice was made). Existing patterns to follow: `recommend/tfidf.py`, `recommend/model_store.py`, `scripts/build_tfidf_model.py`, `evaluation/variants.py`.

## Global Constraints

Copied from the spec; every task includes these.

- Encoder: `BAAI/bge-small-en-v1.5` pinned to Hugging Face commit `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, 384 dimensions, 512-token limit. No BGE query-instruction prefix: every text is embedded as is.
- Chunks: **250 words** (whitespace windows, no overlap); a final window shorter than **50 words** is merged into the previous one.
- Tag string: the album's normalized genre/tag terms ordered by vote count descending, top **20**, joined with `", "`. An album with no terms gets a zero tag row and is never encoded (the real encoder would give `""` a non-zero vector shared by every untagged album; TF-IDF gives such albums an empty row). None of today's 25,000 albums is untagged, so this is a guard.
- Text vector: mean of the album's chunk vectors, re-normalized to unit length; albums with no cleaned text get a zero row and `has_text = False`.
- Similarity: `tag_cos` if either album has no text vector, else `α·tag_cos + (1 − α)·text_cos`, `α = 0.6` by default. Group score = sum over seeds; seeds are never returned; candidates must score `> 0`; ties break by title then album id.
- `shared_terms`: candidate terms that also appear on a seed, ranked by Σ over seeds of (seed votes × candidate votes), top 5. `shared_text_terms` is always `[]` for this approach.
- API: `approach` accepts `"overlap" | "tfidf" | "embeddings"`; the default stays `"overlap"`. Missing model file → `503 {"detail": "Embedding model not built"}`. No seed in the model → empty results with `reason: "seeds_not_in_model"`. Existing 404/422/`seeds_have_no_terms` behaviour is unchanged.
- The API process and the test suite must not import `torch` or `sentence-transformers`. Only `recommend/sentence_encoder.py` imports them, lazily, and only the build script imports that module.
- Model file: `settings.embeddings_model_path` (env `CRATE_EMBEDDINGS_MODEL_PATH`, default `<repo>/models/embeddings.joblib`), written to a temp file then renamed.
- No frontend changes. Do not make embeddings the default approach.
- Work on `main`, no branches or worktrees. Do not push.
- End every commit message with the trailer line `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` (pass it as a second `-m`).
- Tests run from `backend/` with `uv run pytest`. Format/lint with `uv run ruff check . && uv run ruff format --check .`.

## Review Focus

Failure modes the spec implies that a reader would expect to behave sensibly. Each has a test in the task that owns the code.

1. An album whose article cleans to empty or whitespace: zero text row, `has_text False`, scored on tags only (Task 2).
2. An article shorter than one chunk or with a tiny tail: one chunk / tail merged, never an empty or 3-word chunk (Task 2).
3. Candidates with a negative cosine to the seeds must not appear (Task 3).
4. A request mixing a known seed with an unknown one still uses the known seed; all-unknown gives an empty list, not an error (Task 3, Task 5).
5. Building without `sentence-transformers` installed exits with the install command, not a traceback (Task 4).
6. An album with no genre/tag terms gets a zero tag row, so it never matches on tags (Task 2).

---

## File Structure

- Create `backend/src/crate_backend/recommend/ranking.py`: `rank_rows`, the ordering/limit rule shared by TF-IDF and embeddings.
- Modify `backend/src/crate_backend/recommend/tfidf.py`: `_rank` delegates to `rank_rows`.
- Create `backend/src/crate_backend/recommend/embeddings.py`: `Encoder` protocol, `chunk_text`, `tag_string`, `EmbeddingModel`, `build_model`, `recommend`, `save_model`, `load_model`.
- Create `backend/src/crate_backend/recommend/sentence_encoder.py`: `SentenceTransformerEncoder`, `EncoderUnavailable` (the only module that touches `sentence-transformers`).
- Create `backend/src/crate_backend/scripts/build_embedding_model.py`: the build command.
- Modify `backend/src/crate_backend/recommend/model_store.py`: `get_embedding_model`.
- Modify `backend/src/crate_backend/core/config.py`: `embeddings_model_path`.
- Modify `backend/src/crate_backend/api/routes/recommendations.py`: the `embeddings` approach.
- Modify `backend/src/crate_backend/evaluation/variants.py` and `evaluation/score.py`: two variants, model loading, model versions in the report.
- Modify `backend/pyproject.toml`: dependency group `embeddings`.
- Create tests: `tests/fakes.py` (shared `FakeEncoder`), `tests/test_ranking.py`, `tests/test_embeddings_model.py`, `tests/test_recommend_embeddings.py`, `tests/test_sentence_encoder.py`, `tests/test_build_embedding_model_script.py`, `tests/test_embedding_model_store.py`. Extend `tests/test_config.py`, `tests/test_recommendations_api.py`, `tests/test_eval_variants_pool.py`, `tests/test_eval_score.py` (only if it asserts the variant count).
- Modify `docs/recommendation-systems.md` and the spec (Task 7).

---

### Task 1: Shared ranking function

**Files:**
- Create: `backend/src/crate_backend/recommend/ranking.py`
- Modify: `backend/src/crate_backend/recommend/tfidf.py` (the `_rank` function)
- Test: `backend/tests/test_ranking.py`

**Interfaces:**
- Produces: `rank_rows(titles: list[str], album_ids: list[uuid.UUID], rounded: np.ndarray, seed_rows: list[int], limit: int) -> list[int]` — row indexes ordered by `rounded` descending, then title, then `str(album_id)`; seed rows and rows with `rounded <= 0` are excluded; at most `limit` rows.

- [ ] **Step 1: Write the failing test**

Create `backend/tests/test_ranking.py`:

```python
import uuid

import numpy as np

from crate_backend.recommend.ranking import rank_rows


def ids(n: int) -> list[uuid.UUID]:
    return [uuid.UUID(int=i + 1) for i in range(n)]


def test_orders_by_score_then_title_then_id():
    titles = ["b", "a", "a", "c"]
    album_ids = ids(4)
    scores = np.array([0.5, 0.5, 0.5, 0.9])

    rows = rank_rows(titles, album_ids, scores, seed_rows=[], limit=10)

    # 0.9 first; then the 0.5 ties by title ("a" before "b"), then by id.
    assert rows == [3, 1, 2, 0]


def test_excludes_seeds_and_non_positive_scores():
    titles = ["seed", "zero", "negative", "match"]
    scores = np.array([0.9, 0.0, -0.2, 0.4])

    rows = rank_rows(titles, ids(4), scores, seed_rows=[0], limit=10)

    assert rows == [3]


def test_limit_keeps_ties_for_the_tiebreak_to_decide():
    titles = ["top", "zeta", "alpha", "mid"]
    scores = np.array([0.9, 0.5, 0.5, 0.5])

    rows = rank_rows(titles, ids(4), scores, seed_rows=[], limit=2)

    assert rows == [0, 2]  # "alpha" beats "zeta" and "mid" for the last slot


def test_does_not_modify_the_scores_it_is_given():
    scores = np.array([0.9, 0.4])

    rank_rows(["a", "b"], ids(2), scores, seed_rows=[0], limit=5)

    assert scores.tolist() == [0.9, 0.4]
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd backend && uv run pytest tests/test_ranking.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.recommend.ranking'`

- [ ] **Step 3: Write `ranking.py`**

```python
"""Ordering rule shared by the TF-IDF and embedding recommenders."""

import uuid

import numpy as np


def rank_rows(
    titles: list[str],
    album_ids: list[uuid.UUID],
    rounded: np.ndarray,
    seed_rows: list[int],
    limit: int,
) -> list[int]:
    """Rows ordered by rounded score desc, then title, then album id. Seeds
    and rows scoring 0 or less are never returned."""
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
        key=lambda row: (-rounded[row], titles[row], str(album_ids[row])),
    )
    return ordered[:limit]
```

- [ ] **Step 4: Make `tfidf._rank` delegate**

In `backend/src/crate_backend/recommend/tfidf.py`, add `from crate_backend.recommend.ranking import rank_rows` with the other imports and replace the body of `_rank` (keep its signature and docstring first line):

```python
def _rank(model: TfidfModel, rounded: np.ndarray, seed_rows: list[int], limit: int) -> list[int]:
    """Rows ordered by rounded score desc, then title, then album id."""
    return rank_rows(model.titles, model.album_ids, rounded, seed_rows, limit)
```

- [ ] **Step 5: Run the new and the existing TF-IDF tests**

Run: `cd backend && uv run pytest tests/test_ranking.py tests/test_recommend_tfidf.py tests/test_recommendations_api.py tests/test_eval_variants_pool.py -v`
Expected: all PASS (the existing TF-IDF ordering tests prove the refactor kept behaviour).

- [ ] **Step 6: Commit**

```bash
git add backend/src/crate_backend/recommend/ranking.py backend/src/crate_backend/recommend/tfidf.py backend/tests/test_ranking.py
git commit -m "refactor: share the ranking rule between recommenders" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Embedding model: chunking, build, save and load

**Files:**
- Create: `backend/src/crate_backend/recommend/embeddings.py`
- Create: `backend/tests/fakes.py`
- Modify: `backend/src/crate_backend/core/config.py` (add the setting)
- Modify: `backend/tests/test_config.py`
- Modify: `backend/pyproject.toml` (dependency group)
- Test: `backend/tests/test_embeddings_model.py`

**Interfaces:**
- Consumes: `AlbumDoc(album_id, title, term_votes, text)` and `DEFAULT_ALPHA`, `TOP_TERMS` from `crate_backend.recommend.tfidf`.
- Produces (all in `crate_backend.recommend.embeddings`):
  - `CHUNK_WORDS = 250`, `MIN_TAIL_WORDS = 50`, `TAG_TERMS = 20`
  - `class Encoder(Protocol)`: `encode(self, texts: list[str]) -> np.ndarray` (rows unit length, float32, one per text) and property `info -> dict[str, Any]`, read **after** encoding.
  - `chunk_text(text: str, chunk_words: int = CHUNK_WORDS, min_tail_words: int = MIN_TAIL_WORDS) -> list[str]`
  - `tag_string(term_votes: dict[str, int], limit: int = TAG_TERMS) -> str`
  - `@dataclass EmbeddingModel`: `album_ids: list[uuid.UUID]`, `titles: list[str]`, `tag_vectors: np.ndarray`, `text_vectors: np.ndarray`, `has_text: np.ndarray`, `term_votes: list[dict[str, int]]`, `metadata: dict[str, Any]`, and `row_of: dict[uuid.UUID, int]` (init=False, built in `__post_init__`)
  - `build_model(docs: list[AlbumDoc], encoder: Encoder, *, alpha: float = DEFAULT_ALPHA, chunk_words: int = CHUNK_WORDS, min_tail_words: int = MIN_TAIL_WORDS, extra_metadata: dict[str, Any] | None = None) -> EmbeddingModel`
  - `save_model(model: EmbeddingModel, path: Path) -> None`, `load_model(path: Path) -> EmbeddingModel`
  - Metadata keys: `model_version`, `alpha`, `chunk_words`, `min_tail_words`, `tag_terms_per_album`, `embedding_dim`, `n_albums`, `n_with_text`, `n_chunks`, plus everything in `encoder.info` and `extra_metadata`.
- Produces (tests): `tests.fakes.FakeEncoder(table: dict[str, list[float]] | None = None, dim: int = 16)`.

- [ ] **Step 1: Add the setting and the dependency group**

In `backend/src/crate_backend/core/config.py`, after the `tfidf_model_path` line add:

```python

    # Sentence-embedding recommender model file (Phase 5a), written by
    # scripts/build_embedding_model.py and read by the API on first use.
    embeddings_model_path: str = str(_REPO_ROOT / "models" / "embeddings.joblib")
```

In `backend/pyproject.toml`, under `[dependency-groups]` add after `dev`:

```toml
# Only the embedding build script needs these (torch is a large download);
# the API and the tests never import them.
embeddings = [
    "sentence-transformers>=3.0.0",
]
```

Append to `backend/tests/test_config.py`:

```python
def test_embeddings_model_path_defaults_to_repo_models_dir():
    settings = Settings(_env_file=None)
    assert settings.embeddings_model_path.endswith("/models/embeddings.joblib")


def test_embeddings_model_path_reads_from_env(monkeypatch):
    monkeypatch.setenv("CRATE_EMBEDDINGS_MODEL_PATH", "/tmp/elsewhere-emb.joblib")
    settings = Settings(_env_file=None)
    assert settings.embeddings_model_path == "/tmp/elsewhere-emb.joblib"
```

(Check the top of `test_config.py` for how `Settings` is imported and match it; the existing tfidf tests are the template.)

- [ ] **Step 2: Write the shared fake encoder**

Create `backend/tests/fakes.py`:

```python
"""Test doubles shared by the embedding tests."""

import hashlib
from typing import Any

import numpy as np


class FakeEncoder:
    """Deterministic stand-in for the sentence encoder.

    Texts in `table` get exactly that vector (normalized). Any other text
    gets a bag-of-hashed-words vector, so texts sharing words land near
    each other. Records every `encode` call in `calls`.
    """

    def __init__(self, table: dict[str, list[float]] | None = None, dim: int = 16) -> None:
        self.table = {text: np.asarray(vec, dtype=np.float64) for text, vec in (table or {}).items()}
        self.dim = len(next(iter(self.table.values()))) if self.table else dim
        self.calls: list[list[str]] = []

    def encode(self, texts: list[str]) -> np.ndarray:
        self.calls.append(list(texts))
        if not texts:
            return np.zeros((0, self.dim), dtype=np.float32)
        return np.stack([self._unit(self._raw(text)) for text in texts]).astype(np.float32)

    @property
    def info(self) -> dict[str, Any]:
        return {"encoder_name": "fake", "encoder_revision": "0"}

    def _raw(self, text: str) -> np.ndarray:
        if text in self.table:
            return self.table[text]
        vector = np.zeros(self.dim)
        for word in text.lower().replace(",", " ").split():
            digest = hashlib.md5(word.encode()).digest()
            vector[int.from_bytes(digest[:4], "big") % self.dim] += 1.0
        return vector

    @staticmethod
    def _unit(vector: np.ndarray) -> np.ndarray:
        norm = np.linalg.norm(vector)
        return vector / norm if norm > 0 else vector
```

- [ ] **Step 3: Write the failing tests**

Create `backend/tests/test_embeddings_model.py`:

```python
import uuid

import numpy as np

from crate_backend.recommend.embeddings import (
    CHUNK_WORDS,
    MIN_TAIL_WORDS,
    TAG_TERMS,
    build_model,
    chunk_text,
    load_model,
    save_model,
    tag_string,
)
from crate_backend.recommend.tfidf import AlbumDoc
from tests.fakes import FakeEncoder


def words(n: int, prefix: str = "w") -> str:
    return " ".join(f"{prefix}{i}" for i in range(n))


def doc(name: str, terms: dict[str, int], text: str = "") -> AlbumDoc:
    return AlbumDoc(
        album_id=uuid.uuid5(uuid.NAMESPACE_URL, name), title=name, term_votes=terms, text=text
    )


def test_constants_match_the_spec():
    assert (CHUNK_WORDS, MIN_TAIL_WORDS, TAG_TERMS) == (250, 50, 20)


def test_chunks_are_full_windows_with_a_short_remainder_chunk():
    chunks = chunk_text(words(600))

    assert [len(c.split()) for c in chunks] == [250, 250, 100]


def test_a_tiny_tail_is_merged_into_the_previous_chunk():
    chunks = chunk_text(words(520))  # 250 + 250 + 20

    assert [len(c.split()) for c in chunks] == [250, 270]


def test_text_shorter_than_one_chunk_is_one_chunk_even_if_tiny():
    assert [len(c.split()) for c in chunk_text(words(100))] == [100]
    assert [len(c.split()) for c in chunk_text(words(10))] == [10]


def test_empty_or_whitespace_text_has_no_chunks():
    assert chunk_text("") == []
    assert chunk_text("   \n\t  ") == []


def test_tag_string_orders_by_votes_then_name_and_caps_at_the_limit():
    terms = {"rock": 3, "jazz": 9, "blues": 3, "folk": 1}

    assert tag_string(terms) == "jazz, blues, rock, folk"
    assert tag_string(terms, limit=2) == "jazz, blues"
    many = {f"t{i:02d}": 100 - i for i in range(30)}
    assert tag_string(many).count(",") == TAG_TERMS - 1


def test_text_vector_is_the_renormalized_mean_of_its_chunks():
    encoder = FakeEncoder({"a b": [1, 0], "c d": [0, 1], "jazz": [1, 1]})

    model = build_model(
        [doc("Album", {"jazz": 1}, text="a b c d")], encoder, chunk_words=2, min_tail_words=1
    )

    np.testing.assert_allclose(model.text_vectors[0], [2**-0.5, 2**-0.5], rtol=1e-6)
    assert model.has_text.tolist() == [True]
    np.testing.assert_allclose(model.tag_vectors[0], [2**-0.5, 2**-0.5], rtol=1e-6)


def test_albums_without_usable_text_get_a_zero_row_and_no_text_flag():
    encoder = FakeEncoder(dim=4)
    docs = [
        doc("Has", {"jazz": 1}, text=words(30)),
        doc("Empty", {"jazz": 1}, text=""),
        doc("Blank", {"jazz": 1}, text="  \n "),
    ]

    model = build_model(docs, encoder)

    assert model.has_text.tolist() == [True, False, False]
    assert not model.text_vectors[1].any() and not model.text_vectors[2].any()
    assert model.metadata["n_with_text"] == 1
    assert model.metadata["n_chunks"] == 1


def test_metadata_records_the_build_and_the_encoder():
    encoder = FakeEncoder(dim=4)

    model = build_model(
        [doc("A", {"jazz": 1}), doc("B", {"rock": 1})],
        encoder,
        alpha=0.5,
        extra_metadata={"catalog_source": "test dump"},
    )

    meta = model.metadata
    assert meta["alpha"] == 0.5
    assert meta["n_albums"] == 2
    assert meta["embedding_dim"] == 4
    assert meta["chunk_words"] == 250 and meta["min_tail_words"] == 50
    assert meta["tag_terms_per_album"] == 20
    assert meta["encoder_name"] == "fake"
    assert meta["catalog_source"] == "test dump"
    assert meta["model_version"]  # ISO 8601 build time


def test_the_encoder_is_called_once_for_tags_and_once_for_all_chunks():
    encoder = FakeEncoder(dim=4)
    docs = [doc("A", {"jazz": 1}, text=words(30)), doc("B", {"rock": 1}, text=words(30, "x"))]

    build_model(docs, encoder)

    assert len(encoder.calls) == 2
    assert encoder.calls[0] == ["jazz", "rock"]
    assert len(encoder.calls[1]) == 2


def test_albums_without_terms_get_a_zero_tag_row_and_are_not_encoded():
    encoder = FakeEncoder(dim=4)
    docs = [doc("Tagged", {"jazz": 1}), doc("Untagged", {})]

    model = build_model(docs, encoder)

    assert encoder.calls[0] == ["jazz"]
    assert model.tag_vectors[0].any()
    assert not model.tag_vectors[1].any()


def test_the_build_is_deterministic_apart_from_the_build_time():
    docs = [
        doc("A", {"jazz": 2, "bop": 2}, text=words(300)),
        doc("B", {"rock": 1}, text=words(40, "x")),
        doc("C", {"folk": 1}),
    ]

    first = build_model(docs, FakeEncoder(dim=8))
    second = build_model(docs, FakeEncoder(dim=8))

    np.testing.assert_array_equal(first.tag_vectors, second.tag_vectors)
    np.testing.assert_array_equal(first.text_vectors, second.text_vectors)
    np.testing.assert_array_equal(first.has_text, second.has_text)
    assert first.term_votes == second.term_votes
    second.metadata["model_version"] = first.metadata["model_version"]
    assert first.metadata == second.metadata


def test_save_then_load_round_trips_everything(tmp_path):
    encoder = FakeEncoder(dim=4)
    docs = [doc("A", {"jazz": 2, "bop": 1}, text=words(30)), doc("B", {"rock": 1})]
    model = build_model(docs, encoder)
    path = tmp_path / "models" / "embeddings.joblib"

    save_model(model, path)
    loaded = load_model(path)

    assert loaded.album_ids == model.album_ids
    assert loaded.titles == model.titles
    np.testing.assert_array_equal(loaded.tag_vectors, model.tag_vectors)
    np.testing.assert_array_equal(loaded.text_vectors, model.text_vectors)
    np.testing.assert_array_equal(loaded.has_text, model.has_text)
    assert loaded.term_votes == model.term_votes
    assert loaded.metadata == model.metadata
    assert loaded.row_of == model.row_of
    assert not path.with_suffix(".tmp").exists()
```

- [ ] **Step 4: Run the tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_embeddings_model.py tests/test_config.py -v`
Expected: `test_embeddings_model.py` FAILS at import (`ModuleNotFoundError: crate_backend.recommend.embeddings`); the new config tests pass already or fail only if the setting is missing.

- [ ] **Step 5: Write `embeddings.py` (build half)**

Create `backend/src/crate_backend/recommend/embeddings.py`. This task writes everything except `recommend` (Task 3 appends it):

```python
"""Sentence-embedding recommender (Phase 5a): pure functions over in-memory
data, no database and no torch.

Each album gets two unit vectors from a pretrained sentence encoder. The tag
vector embeds the album's top genre/tag terms as one line. The text vector
is the mean of the embeddings of its cleaned Wikipedia article, split into
chunks because encoders read only a few hundred tokens; it is zero for
albums without text. Similarity blends the two cosines only when both albums
have text, exactly as the TF-IDF recommender does.

Design: docs/superpowers/specs/2026-10-08-embedding-recommender-design.md
"""

import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Protocol

import joblib
import numpy as np

from crate_backend.recommend.tfidf import DEFAULT_ALPHA, AlbumDoc

CHUNK_WORDS = 250
MIN_TAIL_WORDS = 50
TAG_TERMS = 20


class Encoder(Protocol):
    def encode(self, texts: list[str]) -> np.ndarray:
        """One unit-length float32 row per text."""
        ...

    @property
    def info(self) -> dict[str, Any]:
        """Facts about the encoder for the model metadata; read after encoding."""
        ...


@dataclass
class EmbeddingModel:
    album_ids: list[uuid.UUID]
    titles: list[str]
    # Albums x dim, rows unit length.
    tag_vectors: np.ndarray
    # Albums x dim, rows unit length; all zero for albums without text.
    text_vectors: np.ndarray
    has_text: np.ndarray
    # Each album's normalized term -> vote count, for explanations.
    term_votes: list[dict[str, int]]
    metadata: dict[str, Any]
    row_of: dict[uuid.UUID, int] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.row_of = {album_id: row for row, album_id in enumerate(self.album_ids)}


def chunk_text(
    text: str, chunk_words: int = CHUNK_WORDS, min_tail_words: int = MIN_TAIL_WORDS
) -> list[str]:
    """Split on whitespace into windows of `chunk_words` words. A last window
    shorter than `min_tail_words` joins the one before it, so no chunk is a
    few stray words. No usable text gives no chunks."""
    words = text.split()
    if not words:
        return []
    windows = [words[i : i + chunk_words] for i in range(0, len(words), chunk_words)]
    if len(windows) > 1 and len(windows[-1]) < min_tail_words:
        tail = windows.pop()
        windows[-1] = windows[-1] + tail
    return [" ".join(window) for window in windows]


def tag_string(term_votes: dict[str, int], limit: int = TAG_TERMS) -> str:
    """The album's top terms by votes (ties alphabetical) as one line."""
    ranked = sorted(term_votes.items(), key=lambda item: (-item[1], item[0]))
    return ", ".join(term for term, _ in ranked[:limit])


def _unit_rows(vectors: np.ndarray) -> np.ndarray:
    vectors = np.asarray(vectors, dtype=np.float32)
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return np.divide(vectors, norms, out=np.zeros_like(vectors), where=norms > 0)


def build_model(
    docs: list[AlbumDoc],
    encoder: Encoder,
    *,
    alpha: float = DEFAULT_ALPHA,
    chunk_words: int = CHUNK_WORDS,
    min_tail_words: int = MIN_TAIL_WORDS,
    extra_metadata: dict[str, Any] | None = None,
) -> EmbeddingModel:
    # Untagged albums keep a zero tag row: encoding "" would give them all
    # the same non-zero vector, so they would match each other and anything.
    tag_texts = [tag_string(doc.term_votes) for doc in docs]
    tagged = [row for row, text in enumerate(tag_texts) if text]
    encoded_tags = _unit_rows(encoder.encode([tag_texts[row] for row in tagged]))
    tag_vectors = np.zeros((len(docs), encoded_tags.shape[1]), dtype=np.float32)
    tag_vectors[tagged] = encoded_tags

    chunks: list[str] = []
    owners: list[int] = []
    for row, doc in enumerate(docs):
        for chunk in chunk_text(doc.text, chunk_words, min_tail_words):
            chunks.append(chunk)
            owners.append(row)

    text_vectors = np.zeros_like(tag_vectors)
    if chunks:
        # Summing then normalizing gives the same direction as the mean.
        np.add.at(text_vectors, owners, _unit_rows(encoder.encode(chunks)))
    norms = np.linalg.norm(text_vectors, axis=1)
    has_text = norms > 0
    text_vectors[has_text] /= norms[has_text, None]

    metadata = {
        "model_version": datetime.now(UTC).isoformat(timespec="seconds"),
        "alpha": alpha,
        "chunk_words": chunk_words,
        "min_tail_words": min_tail_words,
        "tag_terms_per_album": TAG_TERMS,
        "embedding_dim": int(tag_vectors.shape[1]),
        "n_albums": len(docs),
        "n_with_text": int(has_text.sum()),
        "n_chunks": len(chunks),
        **encoder.info,
        **(extra_metadata or {}),
    }
    return EmbeddingModel(
        album_ids=[doc.album_id for doc in docs],
        titles=[doc.title for doc in docs],
        tag_vectors=tag_vectors,
        text_vectors=text_vectors,
        has_text=has_text,
        term_votes=[dict(doc.term_votes) for doc in docs],
        metadata=metadata,
    )


def save_model(model: EmbeddingModel, path: Path) -> None:
    """Write the model as one joblib file. Written to a temp file and renamed
    so a process loading the path never sees a half-written file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    joblib.dump(
        {
            "album_ids": model.album_ids,
            "titles": model.titles,
            "tag_vectors": model.tag_vectors,
            "text_vectors": model.text_vectors,
            "has_text": model.has_text,
            "term_votes": model.term_votes,
            "metadata": model.metadata,
        },
        temp,
    )
    temp.replace(path)


def load_model(path: Path) -> EmbeddingModel:
    return EmbeddingModel(**joblib.load(path))
```

- [ ] **Step 6: Run the tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_embeddings_model.py tests/test_config.py -v`
Expected: all PASS.

- [ ] **Step 7: Lint and commit**

```bash
cd backend && uv lock && uv run ruff check . && uv run ruff format --check .
git add backend/src/crate_backend/recommend/embeddings.py backend/src/crate_backend/core/config.py backend/pyproject.toml backend/uv.lock backend/tests/fakes.py backend/tests/test_embeddings_model.py backend/tests/test_config.py
git commit -m "feat: build and store sentence-embedding models" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

If `ruff format --check` fails, run `uv run ruff format .` on the files you touched and include them in the commit. `uv.lock` grows (it now resolves `torch` for every platform); that is expected. The Dockerfile's `uv sync --frozen --no-dev` installs only the default dependencies, so the API image doesn't get `torch`.

---

### Task 3: Scoring and explanations

**Files:**
- Modify: `backend/src/crate_backend/recommend/embeddings.py` (append `recommend` and helpers)
- Test: `backend/tests/test_recommend_embeddings.py`

**Interfaces:**
- Consumes: `EmbeddingModel`, `rank_rows` (Task 1), `TOP_TERMS` from `crate_backend.recommend.tfidf`.
- Produces: `@dataclass(frozen=True) EmbeddingRecommendation(album_id: uuid.UUID, score: float, shared_terms: list[str])` and `recommend(model: EmbeddingModel, seed_ids: list[uuid.UUID], limit: int, *, alpha: float | None = None) -> list[EmbeddingRecommendation]`. Scores are rounded to **6** decimals (float32 precision) before ranking.

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_recommend_embeddings.py`:

```python
import uuid

import numpy as np

from crate_backend.recommend.embeddings import EmbeddingModel, recommend

# A row is (name, tag vector, text vector or None, term votes). Vectors are
# 2-D so cosines are easy to reason about; the helper normalizes them.


def aid(name: str) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_URL, name)


def unit(vec) -> np.ndarray:
    v = np.asarray(vec, dtype=np.float32)
    n = np.linalg.norm(v)
    return v / n if n > 0 else v


def make_model(*rows, alpha: float = 0.6) -> EmbeddingModel:
    names = [r[0] for r in rows]
    return EmbeddingModel(
        album_ids=[aid(n) for n in names],
        titles=names,
        tag_vectors=np.stack([unit(r[1]) for r in rows]),
        text_vectors=np.stack([unit(r[2]) if r[2] is not None else np.zeros(2, np.float32) for r in rows]),
        has_text=np.array([r[2] is not None for r in rows]),
        term_votes=[r[3] if len(r) > 3 else {} for r in rows],
        metadata={"alpha": alpha, "model_version": "test"},
    )


def titles(model, results) -> list[str]:
    return [model.titles[model.row_of[r.album_id]] for r in results]


def test_the_closer_vector_ranks_first():
    model = make_model(
        ("Seed", [1, 0], None),
        ("Near", [0.9, 0.1], None),
        ("Far", [0.5, 0.5], None),
    )

    results = recommend(model, [aid("Seed")], 10)

    assert titles(model, results) == ["Near", "Far"]


def test_albums_without_text_are_compared_on_tags_alone():
    model = make_model(
        ("Seed", [1, 0], [1, 0]),
        ("NoText", [1, 1], None),
    )

    [result] = recommend(model, [aid("Seed")], 10)

    assert result.score == round(2**-0.5, 6)


def test_albums_with_text_on_both_sides_blend_tag_and_text_cosines():
    model = make_model(
        ("Seed", [1, 0], [1, 0]),
        ("Both", [1, 1], [0, 1]),  # tag cos 0.7071, text cos 0
    )

    [default] = recommend(model, [aid("Seed")], 10)
    [text_heavy] = recommend(model, [aid("Seed")], 10, alpha=0.2)

    assert default.score == round(0.6 * 2**-0.5, 6)
    assert text_heavy.score == round(0.2 * 2**-0.5, 6)


def test_group_scores_sum_over_seeds_and_seeds_are_never_returned():
    model = make_model(
        ("Seed1", [1, 0], None),
        ("Seed2", [0, 1], None),
        ("Between", [1, 1], None),
        ("OnlyOne", [1, 0.2], None),
    )

    results = recommend(model, [aid("Seed1"), aid("Seed2")], 10)

    assert titles(model, results) == ["Between", "OnlyOne"]
    assert all(r.album_id not in (aid("Seed1"), aid("Seed2")) for r in results)


def test_candidates_pointing_away_from_the_seeds_are_excluded():
    model = make_model(
        ("Seed", [1, 0], None),
        ("Opposite", [-1, 0], None),
        ("Match", [1, 1], None),
    )

    assert titles(model, recommend(model, [aid("Seed")], 10)) == ["Match"]


def test_ties_break_by_title_then_the_limit_applies():
    model = make_model(
        ("Seed", [1, 0], None),
        ("Zulu", [1, 1], None),
        ("Alpha", [1, 1], None),
        ("Mike", [1, 1], None),
    )

    assert titles(model, recommend(model, [aid("Seed")], 10)) == ["Alpha", "Mike", "Zulu"]
    assert titles(model, recommend(model, [aid("Seed")], 2)) == ["Alpha", "Mike"]


def test_seeds_missing_from_the_model_contribute_nothing():
    model = make_model(("Seed", [1, 0], None), ("Match", [1, 1], None))

    with_unknown = recommend(model, [aid("Seed"), uuid.uuid4()], 10)

    assert titles(model, with_unknown) == ["Match"]
    assert recommend(model, [uuid.uuid4()], 10) == []


def test_shared_terms_are_ranked_by_summed_seed_votes_times_candidate_votes():
    model = make_model(
        ("Seed1", [1, 0], None, {"jazz": 5, "bop": 1}),
        ("Seed2", [1, 0.1], None, {"jazz": 5, "modal": 2}),
        ("Match", [1, 0.2], None, {"jazz": 1, "modal": 3, "bop": 1, "polka": 9}),
    )

    result = next(r for r in recommend(model, [aid("Seed1"), aid("Seed2")], 10) if r.album_id == aid("Match"))

    # jazz 10*1=10, modal 2*3=6, bop 1*1=1; polka is on no seed.
    assert result.shared_terms == ["jazz", "modal", "bop"]


def test_shared_terms_are_capped_at_five():
    terms = {f"t{i}": 1 for i in range(8)}
    model = make_model(("Seed", [1, 0], None, terms), ("Match", [1, 0.1], None, terms))

    [result] = recommend(model, [aid("Seed")], 10)

    assert len(result.shared_terms) == 5
    assert result.shared_terms == sorted(result.shared_terms)
```

- [ ] **Step 2: Run to verify failure**

Run: `cd backend && uv run pytest tests/test_recommend_embeddings.py -v`
Expected: FAIL with `ImportError: cannot import name 'recommend'`.

- [ ] **Step 3: Append the implementation to `embeddings.py`**

Add `from crate_backend.recommend.ranking import rank_rows` and change the tfidf import line to `from crate_backend.recommend.tfidf import DEFAULT_ALPHA, TOP_TERMS, AlbumDoc`, then append:

```python

# Cosines of float32 vectors are exact to about 1e-7, so scores that should
# tie are rounded to 6 decimals (TF-IDF's float64 scores use 9).
SCORE_DECIMALS = 6


@dataclass(frozen=True)
class EmbeddingRecommendation:
    album_id: uuid.UUID
    score: float
    shared_terms: list[str]


def recommend(
    model: EmbeddingModel,
    seed_ids: list[uuid.UUID],
    limit: int,
    *,
    alpha: float | None = None,
) -> list[EmbeddingRecommendation]:
    """Rank model albums related to the seeds. Seeds missing from the model
    (added to the catalog after the build) contribute nothing; seeds are
    never returned."""
    seed_rows = sorted({model.row_of[s] for s in seed_ids if s in model.row_of})
    if not seed_rows:
        return []
    scores = _group_scores(model, seed_rows, model.metadata["alpha"] if alpha is None else alpha)
    rounded = np.round(scores, SCORE_DECIMALS)
    seed_votes = _seed_votes(model, seed_rows)
    return [
        EmbeddingRecommendation(
            album_id=model.album_ids[row],
            score=float(rounded[row]),
            shared_terms=_shared_terms(model.term_votes[row], seed_votes),
        )
        for row in rank_rows(model.titles, model.album_ids, rounded, seed_rows, limit)
    ]


def _cosines(vectors: np.ndarray, seed_rows: list[int]) -> np.ndarray:
    """Cosine of every album with each seed, shape (seeds, albums). Rows are
    unit length, so dot products are cosines."""
    return (vectors @ vectors[seed_rows].T).T.astype(np.float64)


def _group_scores(model: EmbeddingModel, seed_rows: list[int], alpha: float) -> np.ndarray:
    tag = _cosines(model.tag_vectors, seed_rows)
    text = _cosines(model.text_vectors, seed_rows)
    both_have_text = model.has_text[seed_rows][:, None] & model.has_text[None, :]
    return np.where(both_have_text, alpha * tag + (1 - alpha) * text, tag).sum(axis=0)


def _seed_votes(model: EmbeddingModel, seed_rows: list[int]) -> dict[str, int]:
    votes: dict[str, int] = {}
    for row in seed_rows:
        for term, count in model.term_votes[row].items():
            votes[term] = votes.get(term, 0) + count
    return votes


def _shared_terms(candidate_votes: dict[str, int], seed_votes: dict[str, int]) -> list[str]:
    """The candidate's terms that a seed also has, strongest first: summed
    seed votes times the candidate's own votes, ties alphabetical."""
    ranked = sorted(
        (-seed_votes[term] * count, term)
        for term, count in candidate_votes.items()
        if term in seed_votes
    )
    return [term for _, term in ranked[:TOP_TERMS]]
```

- [ ] **Step 4: Run to verify they pass**

Run: `cd backend && uv run pytest tests/test_recommend_embeddings.py tests/test_embeddings_model.py -v`
Expected: all PASS.

- [ ] **Step 5: Lint and commit**

```bash
cd backend && uv run ruff format . && uv run ruff check .
git add backend/src/crate_backend/recommend/embeddings.py backend/tests/test_recommend_embeddings.py
git commit -m "feat: rank albums by embedding similarity with shared-term explanations" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

(`ruff format .` may touch files outside this task; run `git status` and add only the files you changed.)

---

### Task 4: The real encoder and the build script

**Files:**
- Create: `backend/src/crate_backend/recommend/sentence_encoder.py`
- Create: `backend/src/crate_backend/scripts/build_embedding_model.py`
- Test: `backend/tests/test_sentence_encoder.py`, `backend/tests/test_build_embedding_model_script.py`

**Interfaces:**
- Consumes: `load_album_docs(session, *, drop_reception, drop_personnel, only)` and `_catalog_source()` and `_megabytes()` from `crate_backend.scripts.build_tfidf_model`; `build_model`, `save_model` from `embeddings`.
- Produces:
  - `class EncoderUnavailable(Exception)`; `MODEL_NAME = "BAAI/bge-small-en-v1.5"`; `MODEL_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"`; `MAX_SEQ_LENGTH = 512`
  - `class SentenceTransformerEncoder(name: str = MODEL_NAME, *, revision: str = MODEL_REVISION, device: str = "cpu", batch_size: int = 64)` implementing `Encoder`; `info` returns `encoder_name`, `encoder_revision` (the pinned revision the weights were loaded at), `max_seq_length`, `n_truncated_inputs`, `sentence_transformers_version`, `torch_version`. Raises `EncoderUnavailable` (message contains `uv sync --group embeddings`) if the libraries are missing.
  - Script: `parse_args(argv)` with `--alpha`, `--no-reception`, `--no-personnel`, `--device`, `--batch-size`, `--out`; `async def build(args, encoder=None)`.

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_sentence_encoder.py`:

```python
import sys

import pytest

from crate_backend.recommend.sentence_encoder import (
    MAX_SEQ_LENGTH,
    MODEL_NAME,
    MODEL_REVISION,
    EncoderUnavailable,
    SentenceTransformerEncoder,
)


def test_the_chosen_encoder_and_window_match_the_spec():
    assert MODEL_NAME == "BAAI/bge-small-en-v1.5"
    assert MODEL_REVISION == "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
    assert MAX_SEQ_LENGTH == 512


def test_missing_libraries_give_the_install_command(monkeypatch):
    monkeypatch.setitem(sys.modules, "sentence_transformers", None)

    with pytest.raises(EncoderUnavailable, match="uv sync --group embeddings"):
        SentenceTransformerEncoder()
```

Create `backend/tests/test_build_embedding_model_script.py`:

```python
import pytest

from crate_backend.scripts.build_embedding_model import parse_args


def test_defaults():
    args = parse_args([])

    assert args.alpha == 0.6
    assert args.device == "cpu"
    assert args.batch_size == 64
    assert args.out is None
    assert not args.no_reception and not args.no_personnel


def test_flags_are_read(tmp_path):
    args = parse_args(
        ["--alpha", "0.4", "--no-reception", "--no-personnel", "--device", "mps",
         "--batch-size", "16", "--out", str(tmp_path / "x.joblib")]
    )

    assert (args.alpha, args.device, args.batch_size) == (0.4, "mps", 16)
    assert args.no_reception and args.no_personnel
    assert args.out == tmp_path / "x.joblib"


def test_alpha_outside_zero_one_is_rejected():
    with pytest.raises(SystemExit):
        parse_args(["--alpha", "1.5"])
```

- [ ] **Step 2: Run to verify failure**

Run: `cd backend && uv run pytest tests/test_sentence_encoder.py tests/test_build_embedding_model_script.py -v`
Expected: FAIL with `ModuleNotFoundError`.

- [ ] **Step 3: Write `sentence_encoder.py`**

```python
"""The real sentence encoder (Phase 5a). The only module that imports
sentence-transformers / torch, and only the build script imports this one,
so the API and the tests never need them.

Install with: uv sync --group embeddings
"""

from typing import Any

import numpy as np

MODEL_NAME = "BAAI/bge-small-en-v1.5"
# The Hugging Face commit the weights are loaded at, pinned so a rebuild
# uses the same weights and the metadata names them exactly.
MODEL_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
# The model's own limit. Set explicitly so a library default can't change it.
MAX_SEQ_LENGTH = 512
# Texts tokenized at a time when counting truncation, so the token ids of
# all ~50,000 chunks are never held in memory at once.
_LENGTH_BATCH = 1000


class EncoderUnavailable(Exception):
    pass


class SentenceTransformerEncoder:
    def __init__(
        self,
        name: str = MODEL_NAME,
        *,
        revision: str = MODEL_REVISION,
        device: str = "cpu",
        batch_size: int = 64,
    ):
        try:
            import sentence_transformers
            import torch
        except ImportError as error:
            raise EncoderUnavailable(
                "sentence-transformers is not installed. Run: uv sync --group embeddings"
            ) from error
        self._name = name
        self._revision = revision
        self._batch_size = batch_size
        self._model = sentence_transformers.SentenceTransformer(
            name, revision=revision, device=device
        )
        self._model.max_seq_length = MAX_SEQ_LENGTH
        self._versions = {
            "sentence_transformers_version": sentence_transformers.__version__,
            "torch_version": torch.__version__,
        }
        self._truncated = 0

    def encode(self, texts: list[str]) -> np.ndarray:
        # Count inputs the model would silently cut off, so a chunk size that
        # is too big shows up in the metadata instead of degrading quality.
        # Only the lengths are kept, one batch at a time.
        for start in range(0, len(texts), _LENGTH_BATCH):
            batch = texts[start : start + _LENGTH_BATCH]
            lengths = self._model.tokenizer(batch, truncation=False, return_length=True)["length"]
            self._truncated += sum(n > MAX_SEQ_LENGTH for n in lengths)
        vectors = self._model.encode(
            texts,
            batch_size=self._batch_size,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=True,
        )
        return vectors.astype(np.float32)

    @property
    def info(self) -> dict[str, Any]:
        return {
            "encoder_name": self._name,
            "encoder_revision": self._revision,
            "max_seq_length": MAX_SEQ_LENGTH,
            "n_truncated_inputs": self._truncated,
            **self._versions,
        }
```

- [ ] **Step 4: Write `build_embedding_model.py`**

```python
"""Build the sentence-embedding recommender model file (Phase 5a).

Design: docs/superpowers/specs/2026-10-08-embedding-recommender-design.md

Run with: uv run --group embeddings python -m crate_backend.scripts.build_embedding_model
          [--alpha 0.6] [--no-reception] [--no-personnel] [--device cpu|mps]
          [--batch-size 64] [--out PATH]

Reads the same album documents as the TF-IDF build (genre/tag votes and the
cleaned Wikipedia text), embeds them with bge-small-en-v1.5 and writes one
joblib file (default: settings.embeddings_model_path). The API loads that
file on its first embeddings request and keeps it until restart, so restart
the backend after rebuilding. The first run downloads the encoder (~130 MB).
"""

import argparse
import asyncio
import time
from pathlib import Path

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.recommend.embeddings import (
    Encoder,
    build_model,
    save_model,
)
from crate_backend.recommend.sentence_encoder import EncoderUnavailable, SentenceTransformerEncoder
from crate_backend.recommend.tfidf import DEFAULT_ALPHA
from crate_backend.scripts.build_tfidf_model import _catalog_source, _megabytes, load_album_docs


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the sentence-embedding model file.")
    parser.add_argument(
        "--alpha", type=float, default=DEFAULT_ALPHA, help="tag weight in the blend, 0–1"
    )
    parser.add_argument(
        "--no-reception", action="store_true", help="drop Reception sections from articles"
    )
    parser.add_argument(
        "--no-personnel", action="store_true", help="drop Personnel/Credits sections"
    )
    parser.add_argument("--device", default="cpu", help="cpu or mps (Apple GPU)")
    parser.add_argument("--batch-size", type=int, default=64, help="texts per encoder batch")
    parser.add_argument("--out", type=Path, default=None, help="model file to write")
    args = parser.parse_args(argv)
    if not 0 <= args.alpha <= 1:
        parser.error("--alpha must be between 0 and 1")
    return args


async def build(args: argparse.Namespace, encoder: Encoder | None = None) -> None:
    out = args.out or Path(get_settings().embeddings_model_path)
    started = time.perf_counter()
    async with async_session_factory() as session:
        docs = await load_album_docs(
            session, drop_reception=args.no_reception, drop_personnel=args.no_personnel
        )
    loaded = time.perf_counter()

    # Created before the encode timer starts: the first run downloads the
    # weights, which would otherwise count as encoding time.
    if encoder is None:
        encoder = SentenceTransformerEncoder(device=args.device, batch_size=args.batch_size)
    ready = time.perf_counter()
    model = build_model(
        docs,
        encoder,
        alpha=args.alpha,
        extra_metadata={
            "catalog_source": _catalog_source(),
            "drop_reception": args.no_reception,
            "drop_personnel": args.no_personnel,
        },
    )
    encoded = time.perf_counter()
    save_model(model, out)
    saved = time.perf_counter()

    meta = model.metadata
    n_albums, n_text = meta["n_albums"], meta["n_with_text"]
    # Tag strings are encoded too, so the rate is over every encoded text.
    n_texts = n_albums + meta["n_chunks"]
    matrix_bytes = model.tag_vectors.nbytes + model.text_vectors.nbytes
    print(f"Albums:          {n_albums:,} ({n_text:,} with text, {100 * n_text / n_albums:.0f}%)")
    print(f"Chunks embedded: {meta['n_chunks']:,}")
    print(f"Encode rate:     {n_texts / (encoded - ready):.0f} texts/s (tag lines + chunks)")
    print(f"Encoder:         {meta['encoder_name']} @ {meta['encoder_revision']}")
    print(f"Vectors:         {meta['embedding_dim']} dims, {_megabytes(matrix_bytes)} in memory")
    print(f"File:            {out} ({_megabytes(out.stat().st_size)})")
    print(
        f"Time:            load {loaded - started:.1f}s, encoder setup {ready - loaded:.1f}s, "
        f"encode {encoded - ready:.1f}s, save {saved - encoded:.1f}s"
    )
    print(f"Model version:   {meta['model_version']}")
    if meta.get("n_truncated_inputs"):
        print(
            f"Warning: {meta['n_truncated_inputs']} inputs were longer than the encoder's "
            f"{meta['max_seq_length']}-token window and were cut off. Lower CHUNK_WORDS."
        )


def main() -> None:
    try:
        asyncio.run(build(parse_args()))
    except EncoderUnavailable as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()
```

Note: this deviates from the spec's "asserts no chunk exceeds 512" — it records `n_truncated_inputs` and warns instead, so one oddly tokenized chunk can't fail a ten-minute build. Task 7 updates the spec.

- [ ] **Step 5: Run to verify they pass**

Run: `cd backend && uv run pytest tests/test_sentence_encoder.py tests/test_build_embedding_model_script.py -v`
Expected: all PASS (no `torch` needed: the missing-library test sets `sys.modules["sentence_transformers"] = None`, which makes the import fail even when the package is installed).

- [ ] **Step 6: Lint and commit**

```bash
cd backend && uv run ruff format src/crate_backend/recommend/sentence_encoder.py src/crate_backend/scripts/build_embedding_model.py tests/test_sentence_encoder.py tests/test_build_embedding_model_script.py && uv run ruff check .
git add backend/src/crate_backend/recommend/sentence_encoder.py backend/src/crate_backend/scripts/build_embedding_model.py backend/tests/test_sentence_encoder.py backend/tests/test_build_embedding_model_script.py
git commit -m "feat: add the bge-small encoder and the embedding model build script" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Model store and API

**Files:**
- Modify: `backend/src/crate_backend/recommend/model_store.py`
- Modify: `backend/src/crate_backend/api/routes/recommendations.py`
- Test: `backend/tests/test_embedding_model_store.py` (new), `backend/tests/test_recommendations_api.py` (extend)

**Interfaces:**
- Consumes: `EmbeddingModel`, `load_model`, `recommend` from `embeddings` (Tasks 2–3).
- Produces: `model_store.get_embedding_model() -> EmbeddingModel | None` (cached per path in `model_store._loaded_embeddings`; `None` is not cached); request `approach: Literal["overlap", "tfidf", "embeddings"]`.

- [ ] **Step 1: Write the failing store tests**

Create `backend/tests/test_embedding_model_store.py`:

```python
import uuid

import pytest

from crate_backend.core.config import get_settings
from crate_backend.recommend import model_store
from crate_backend.recommend.embeddings import build_model, save_model
from crate_backend.recommend.tfidf import AlbumDoc
from tests.fakes import FakeEncoder


@pytest.fixture
def model_path(tmp_path, monkeypatch):
    path = tmp_path / "embeddings.joblib"
    monkeypatch.setattr(get_settings(), "embeddings_model_path", str(path))
    monkeypatch.setattr(model_store, "_loaded_embeddings", {})
    return path


def _tiny_model():
    docs = [
        AlbumDoc(album_id=uuid.uuid4(), title="A", term_votes={"jazz": 1}),
        AlbumDoc(album_id=uuid.uuid4(), title="B", term_votes={"jazz": 1}),
    ]
    return build_model(docs, FakeEncoder(dim=4))


def test_missing_file_gives_none_and_is_picked_up_once_built(model_path):
    assert model_store.get_embedding_model() is None

    model = _tiny_model()
    save_model(model, model_path)
    loaded = model_store.get_embedding_model()

    assert loaded is not None
    assert loaded.metadata == model.metadata


def test_model_is_loaded_once_per_process(model_path):
    save_model(_tiny_model(), model_path)

    assert model_store.get_embedding_model() is model_store.get_embedding_model()
```

- [ ] **Step 2: Write the failing API tests**

In `backend/tests/test_recommendations_api.py`, add imports `from crate_backend.recommend import embeddings` and `from tests.fakes import FakeEncoder`, then append:

```python
@pytest.fixture
def use_embedding_model(monkeypatch):
    """Serve the given model (or None: no model file built) for embeddings requests."""

    def use(model):
        monkeypatch.setattr(recommendations_route, "get_embedding_model", lambda: model)

    return use


def _embedding_model(*docs: AlbumDoc):
    return embeddings.build_model(list(docs), FakeEncoder(dim=8))


async def test_embeddings_rank_from_the_model_and_explain_with_shared_terms(
    client, db_session, use_embedding_model
):
    seed = await _album(db_session, "Seed", "a")
    match = await _album(db_session, "Match", release_year=1999)
    model = _embedding_model(_doc(seed, "jazz", "bop"), _doc(match, "jazz", "bop"))
    use_embedding_model(model)

    response = await _post(client, album_ids=[str(seed.id)], approach="embeddings")

    assert response.status_code == 200
    body = response.json()
    assert body["approach"] == "embeddings"
    assert body["model_version"] == model.metadata["model_version"]
    assert body["reason"] is None
    [result] = body["results"]
    assert result["id"] == str(match.id)
    assert result["release_year"] == 1999
    assert sorted(result["shared_terms"]) == ["bop", "jazz"]
    assert result["shared_text_terms"] == []


async def test_embeddings_without_a_built_model_is_503(client, db_session, use_embedding_model):
    seed = await _album(db_session, "Seed", "a")
    use_embedding_model(None)

    response = await _post(client, album_ids=[str(seed.id)], approach="embeddings")

    assert response.status_code == 503
    assert response.json() == {"detail": "Embedding model not built"}


async def test_embeddings_seeds_missing_from_the_model_explain_the_empty_result(
    client, db_session, use_embedding_model
):
    seed = await _album(db_session, "New Seed", "a")
    older = await _album(db_session, "Older Album", "b")
    model = _embedding_model(_doc(older, "jazz"))
    use_embedding_model(model)

    response = await _post(client, album_ids=[str(seed.id)], approach="embeddings")

    assert response.json() == {
        "approach": "embeddings",
        "model_version": model.metadata["model_version"],
        "results": [],
        "reason": "seeds_not_in_model",
    }


async def test_embeddings_seeds_without_terms_keep_their_reason(
    client, db_session, use_embedding_model
):
    seed = await _album(db_session, "Untagged Seed")
    other = await _album(db_session, "Tagged Album", "a")
    use_embedding_model(_embedding_model(_doc(seed), _doc(other, "jazz")))

    response = await _post(client, album_ids=[str(seed.id)], approach="embeddings")

    assert response.json()["reason"] == "seeds_have_no_terms"


async def test_embeddings_skip_albums_removed_since_the_build(
    client, db_session, use_embedding_model
):
    seed = await _album(db_session, "Seed", "a")
    kept = await _album(db_session, "Kept")
    gone = AlbumDoc(album_id=uuid.uuid4(), title="Gone", term_votes={"jazz": 1})
    use_embedding_model(_embedding_model(_doc(seed, "jazz"), _doc(kept, "jazz"), gone))

    response = await _post(client, album_ids=[str(seed.id)], approach="embeddings")

    assert [r["id"] for r in response.json()["results"]] == [str(kept.id)]


async def test_embeddings_use_the_known_seed_when_another_seed_is_unknown(
    client, db_session, use_embedding_model
):
    known = await _album(db_session, "Known", "a")
    newer = await _album(db_session, "Newer", "b")
    match = await _album(db_session, "Match")
    use_embedding_model(_embedding_model(_doc(known, "jazz"), _doc(match, "jazz")))

    response = await _post(
        client, album_ids=[str(known.id), str(newer.id)], approach="embeddings"
    )

    assert [r["id"] for r in response.json()["results"]] == [str(match.id)]


async def test_the_default_approach_is_still_overlap(client, db_session):
    seed = await _album(db_session, "Seed", "a")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.json()["approach"] == "overlap"
```

(`_doc`, `_album` and `_post` are the helpers already at the top of this file.)

- [ ] **Step 3: Run to verify failure**

Run: `cd backend && uv run pytest tests/test_embedding_model_store.py tests/test_recommendations_api.py -v`
Expected: store tests FAIL (`AttributeError: ... get_embedding_model`); new API tests FAIL (422 on `approach="embeddings"` or missing attribute `get_embedding_model`).

- [ ] **Step 4: Implement the store**

Append to `backend/src/crate_backend/recommend/model_store.py`, and add the imports at the top (`from crate_backend.recommend import embeddings`):

```python

_loaded_embeddings: dict[Path, embeddings.EmbeddingModel] = {}


def get_embedding_model() -> embeddings.EmbeddingModel | None:
    """The model at settings.embeddings_model_path, loaded on first use and
    kept for the life of the process. None while the file doesn't exist
    (not cached, so a first build needs no restart; a rebuild of an
    already-loaded model does)."""
    path = Path(get_settings().embeddings_model_path)
    if path not in _loaded_embeddings:
        if not path.exists():
            return None
        _loaded_embeddings[path] = embeddings.load_model(path)
    return _loaded_embeddings[path]
```

- [ ] **Step 5: Implement the route changes**

In `backend/src/crate_backend/api/routes/recommendations.py`:

1. Imports: change to `from crate_backend.recommend.model_store import get_embedding_model, get_tfidf_model` and add `from crate_backend.recommend.embeddings import recommend as recommend_by_embeddings`.
2. Request field and comment:

```python
    # "overlap" (Jaccard, Phase 3), "tfidf" (Phase 4) or "embeddings"
    # (Phase 5a). The default changes only once the evaluation answer key
    # picks a winner.
    approach: Literal["overlap", "tfidf", "embeddings"] = "overlap"
```
3. Replace the model-loading block:

```python
    model = None
    if request.approach != "overlap":
        # The first call reads the model file; keep that off the event loop.
        # Look the loader up here, not at import time, so tests can swap it.
        loader = get_tfidf_model if request.approach == "tfidf" else get_embedding_model
        model = await run_in_threadpool(loader)
        if model is None:
            name = "TF-IDF" if request.approach == "tfidf" else "Embedding"
            raise HTTPException(status_code=503, detail=f"{name} model not built")
    model_version = model.metadata["model_version"] if model else None
```
4. Replace the `else:` ranking branch:

```python
    else:
        if not any(seed_id in model.row_of for seed_id in seed_ids):
            return respond([], "seeds_not_in_model")
        if request.approach == "tfidf":
            ranked = [
                _Ranked(r.album_id, r.score, r.shared_terms, r.shared_text_terms)
                for r in recommend_by_tfidf(model, seed_ids, request.limit)
            ]
        else:
            ranked = [
                _Ranked(r.album_id, r.score, r.shared_terms, [])
                for r in recommend_by_embeddings(model, seed_ids, request.limit)
            ]
```
5. Update the `model_version` comment in `RecommendationResponse` to "Build time of the model file that answered; null for overlap."

- [ ] **Step 6: Run to verify they pass**

Run: `cd backend && uv run pytest tests/test_embedding_model_store.py tests/test_tfidf_model_store.py tests/test_recommendations_api.py -v`
Expected: all PASS (including every existing TF-IDF API test).

- [ ] **Step 7: Lint and commit**

```bash
cd backend && uv run ruff format src/crate_backend/recommend/model_store.py src/crate_backend/api/routes/recommendations.py tests/test_embedding_model_store.py tests/test_recommendations_api.py && uv run ruff check .
git add backend/src/crate_backend/recommend/model_store.py backend/src/crate_backend/api/routes/recommendations.py backend/tests/test_embedding_model_store.py backend/tests/test_recommendations_api.py
git commit -m "feat: serve embedding recommendations behind the approach switch" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Evaluation variants

**Files:**
- Modify: `backend/src/crate_backend/evaluation/variants.py`
- Modify: `backend/src/crate_backend/evaluation/score.py`
- Modify: `backend/tests/test_eval_variants_pool.py`
- Check: `backend/tests/test_eval_score.py` (update only if it asserts the core variant list)

**Interfaces:**
- Consumes: `embeddings.recommend`, `embeddings.load_model`, `EmbeddingModel` (Tasks 2–3).
- Produces: variants `embed-tags` (alpha 1.0) and `embed-tags+text` (alpha 0.6) with `approach == "embeddings"`; `CORE_VARIANTS == ("overlap", "tfidf-tags", "tfidf-tags+text", "embed-tags", "embed-tags+text")`; `embedding_model(variant) -> EmbeddingModel` (raises `ModelNotBuilt` naming `build_embedding_model`); `model_version(variant) -> str | None`.

- [ ] **Step 1: Update and add the tests**

In `backend/tests/test_eval_variants_pool.py`:

1. Add imports: `from crate_backend.recommend import embeddings` and `from tests.fakes import FakeEncoder`; add `embedding_model, model_version` to the `crate_backend.evaluation.variants` import list.
2. Extend the `model_path` fixture so both paths are set (replace the fixture):

```python
@pytest.fixture
def model_path(tmp_path, monkeypatch):
    path = tmp_path / "models" / "tfidf.joblib"
    monkeypatch.setattr(
        variants,
        "get_settings",
        lambda: Settings(
            _env_file=None,
            tfidf_model_path=str(path),
            embeddings_model_path=str(tmp_path / "models" / "embeddings.joblib"),
        ),
    )
    monkeypatch.setattr(variants, "_embedding_models", {})
    return path
```
3. Replace `test_core_variants_use_the_spec_alphas` with:

```python
def test_core_variants_use_the_spec_alphas():
    assert CORE_VARIANTS == (
        "overlap",
        "tfidf-tags",
        "tfidf-tags+text",
        "embed-tags",
        "embed-tags+text",
    )
    assert VARIANTS["overlap"].approach == "overlap"
    assert VARIANTS["tfidf-tags"].alpha == 1.0
    assert VARIANTS["tfidf-tags+text"].alpha == 0.6
    assert VARIANTS["embed-tags"].approach == "embeddings"
    assert VARIANTS["embed-tags"].alpha == 1.0
    assert VARIANTS["embed-tags+text"].approach == "embeddings"
    assert VARIANTS["embed-tags+text"].alpha == 0.6
```
4. Append:

```python
def test_embedding_variants_share_the_embeddings_model_file(model_path):
    expected = model_path.with_name("embeddings.joblib")
    assert VARIANTS["embed-tags"].model_path() == expected
    assert VARIANTS["embed-tags+text"].model_path() == expected


async def test_missing_embedding_model_names_the_build_command(model_path):
    with pytest.raises(ModelNotBuilt, match="build_embedding_model"):
        await top_k(VARIANTS["embed-tags"], None, S1)


async def test_embedding_variants_apply_their_alpha(model_path):
    table = {
        "rock": [1, 0],
        "polka": [0, 1],
        "glacial saxophone": [1, 0],
        "loud guitars": [0, 1],
    }
    docs = [
        AlbumDoc(S1, "Seed", {"rock": 1}, text="glacial saxophone"),
        AlbumDoc(A, "Tag Twin", {"rock": 1}, text="loud guitars"),
        AlbumDoc(B, "Text Twin", {"polka": 1}, text="glacial saxophone"),
    ]
    embeddings.save_model(
        embeddings.build_model(docs, FakeEncoder(table)), model_path.with_name("embeddings.joblib")
    )

    assert await top_k(VARIANTS["embed-tags"], None, S1) == [A]
    assert await top_k(VARIANTS["embed-tags+text"], None, S1) == [A, B]


async def test_model_version_reports_the_file_that_answered(model_path):
    embeddings.save_model(
        embeddings.build_model([AlbumDoc(S1, "Seed", {"rock": 1})], FakeEncoder(dim=4)),
        model_path.with_name("embeddings.joblib"),
    )

    assert model_version(VARIANTS["overlap"]) is None
    assert model_version(VARIANTS["embed-tags"]) == embedding_model(
        VARIANTS["embed-tags"]
    ).metadata["model_version"]
```

- [ ] **Step 2: Run to verify failure**

Run: `cd backend && uv run pytest tests/test_eval_variants_pool.py -v`
Expected: FAIL (ImportError on `embedding_model`/`model_version`).

- [ ] **Step 3: Implement in `variants.py`**

1. Import `from crate_backend.recommend import embeddings` (keep the existing `tfidf` imports).
2. `Variant.approach` comment → `# "overlap" | "tfidf" | "embeddings"`; the model-file comment → `# TF-IDF only.` stays; replace `model_path`:

```python
    def model_path(self) -> Path:
        if self.approach == "embeddings":
            return Path(get_settings().embeddings_model_path)
        default = Path(get_settings().tfidf_model_path)
        return default if self.model_file is None else default.with_name(self.model_file)
```
3. In `VARIANTS`, after `tfidf-tags+text` add:

```python
        Variant("embed-tags", "embeddings", alpha=1.0),
        Variant("embed-tags+text", "embeddings", alpha=0.6),
```
4. `CORE_VARIANTS = ("overlap", "tfidf-tags", "tfidf-tags+text", "embed-tags", "embed-tags+text")`
5. After `tfidf_model`, add:

```python
_embedding_models: dict[Path, embeddings.EmbeddingModel] = {}


def embedding_model(variant: Variant) -> embeddings.EmbeddingModel:
    path = variant.model_path()
    if path not in _embedding_models:
        if not path.exists():
            raise ModelNotBuilt(
                f"{variant.name}: no model at {path}. Build it with: uv sync --group "
                f"embeddings && uv run python -m crate_backend.scripts.build_embedding_model "
                f"--out {path}"
            )
        _embedding_models[path] = embeddings.load_model(path)
    return _embedding_models[path]


def model_version(variant: Variant) -> str | None:
    """Build time of the model file behind a variant; None for overlap."""
    if variant.approach == "tfidf":
        return tfidf_model(variant).metadata["model_version"]
    if variant.approach == "embeddings":
        return embedding_model(variant).metadata["model_version"]
    return None
```
6. In `top_k`, between the overlap branch and the TF-IDF lines, add:

```python
    if variant.approach == "embeddings":
        model = embedding_model(variant)
        return [r.album_id for r in embeddings.recommend(model, [seed_id], k, alpha=variant.alpha)]
```
7. Update the module docstring's first paragraph to mention that the embedding variants share one model file.

- [ ] **Step 4: Use `model_version` in `score.py`**

In the import list from `crate_backend.evaluation.variants` replace `tfidf_model` with `model_version` (remove it if nothing else uses it; check with grep), and replace the `model_versions = {...}` block with:

```python
    model_versions = {v.name: version for v in variants if (version := model_version(v))}
```
Update the argparse help strings in `score.py` and `pool.py` from `default: core three` to `default: the five core variants`, and the docstring line in `pool.py`'s module header if it says "three".

- [ ] **Step 5: Run the evaluation tests and the full suite**

Run: `cd backend && uv run pytest tests/test_eval_variants_pool.py tests/test_eval_score.py -v && uv run pytest -q`
Expected: all PASS. If `test_eval_score.py` asserts the old three-variant list, update it to the new tuple.

- [ ] **Step 6: Lint and commit**

```bash
cd backend && uv run ruff format src/crate_backend/evaluation tests/test_eval_variants_pool.py && uv run ruff check .
git add backend/src/crate_backend/evaluation backend/tests/test_eval_variants_pool.py backend/tests/test_eval_score.py
git commit -m "feat: add embedding variants to the evaluation harness" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: Build for real, measure, document

This task needs the owner at the checkpoint (they judge results by eye and grade the new pairs). Do the steps in order and stop where noted.

**Files:**
- Modify: `docs/recommendation-systems.md`
- Modify: `docs/superpowers/specs/2026-10-08-embedding-recommender-design.md` (reconcile five deviations)

- [ ] **Step 1: Install the encoder dependencies**

Run: `cd backend && uv sync --group embeddings`
Expected: installs `sentence-transformers` and `torch` (a large download). Then `uv run python -c "import sentence_transformers, torch; print(torch.__version__)"` prints a version. If this fails, stop and report; do not work around it.

- [ ] **Step 2: Build the model**

Run: `cd backend && /usr/bin/time -l uv run python -m crate_backend.scripts.build_embedding_model`
Expected: downloads bge-small on first run, shows a progress bar, then prints the summary (albums, chunks, encode rate, encoder + revision, vector size, file size, load/setup/encode/save seconds, model version). `/usr/bin/time -l` then prints `maximum resident set size` in bytes: that is the build's peak memory (Phase 4 recorded 724 MB for TF-IDF the same way). If the first run included the weights download, its setup time is not representative; the encode time and rate are. `Albums:` should show 25,000 with about 51% having text. If a `Warning: N inputs were longer…` line appears with N > 0, record N; if it is more than about 1% of chunks, lower `CHUNK_WORDS` to 200 in `embeddings.py`, update the Task 2 constant test, and rebuild. Copy the whole printed summary into your notes; Step 6 needs it.

- [ ] **Step 3: Check the API end to end**

Run the backend locally with `cd backend && uv run uvicorn crate_backend.main:app` (not docker-compose: the container doesn't mount `models/`, so it would answer 503), then post requests with a seed from `eval/seeds.json`:

```bash
curl -s localhost:8000/recommendations -H 'content-type: application/json' \
  -d '{"album_ids": ["<seed album_id>"], "limit": 5, "approach": "embeddings"}' | python -m json.tool
```
Expected: 5 results with `shared_terms` and `shared_text_terms: []`. Also time 1, 5 and 50 seeds (use 50 distinct album ids from the database) with `curl -w '%{time_total}\n' -o /dev/null -s`; record the three latencies.

- [ ] **Step 4: Checkpoint: look at results by eye with the owner**

For *A Love Supreme* and *Kid A* (search them in the catalog for their album ids), print the top 10 from `approach: "tfidf"` and `approach: "embeddings"` side by side with titles and artists. Show both lists to the owner and ask what they notice (e.g. artist-name crowding, albums without articles ranking too high or low). **Stop here until the owner has looked.**

- [ ] **Step 5: Pool, grade, score (owner does the grading)**

Run: `cd backend && uv run python -m crate_backend.evaluation.pool`
Expected: prints `N new pairs to grade…`; the spec estimates 20–40. Tell the owner the number and ask them to run `uv run python -m crate_backend.evaluation.grade`. **Stop until they say grading is done**, then run `uv run python -m crate_backend.evaluation.score` and read the report to the owner honestly: if any row has ⚠ (under-judged), say so and pool again instead of interpreting it.

- [ ] **Step 6: Document the approach**

Edit `docs/recommendation-systems.md`:

1. Summary table: change row 3 to `| 3 | Sentence embeddings (bge-small-en-v1.5) | 5a | **Built** <build date>, opt-in (approach: "embeddings"), not the default | Genre/tag line + chunk-averaged Wikipedia text, embedded by a pretrained encoder | <see Evaluation> |`.
2. Add a section "Approach 3: sentence embeddings" after the TF-IDF section, in the same style, covering: how it works (define "embedding", "chunk", "cosine" with a Crate example, e.g. "melancholic" and "sorrowful" landing close together); the exact build parameters from the model metadata; **measured** build time, encode rate, peak memory, file size, in-memory size and the three request latencies from Steps 2–3 (write the figures you measured; do not estimate or copy the spec's estimates); the explanation limitation (only shared tags are shown, no "Described alike"); that the "score > 0" filter removes almost nothing here, because a pretrained encoder gives even unrelated texts positive cosines, so nearly every album is a candidate and only the ordering matters; the spike finding on extra text sources (see the spec's decisions list); and "what went wrong" if anything did.
3. Evaluation section: change "Default: the three core variants" to the five core variants; add the new report's table (copy it from `eval/results/<date>.md`) and a short, honest reading of it with the per-quartile columns, including whether the spec's predicted risk (averaged text vectors favouring albums that have an article) showed up.
4. Add the build command and flags to the "Evaluation flags" / build documentation next to the TF-IDF ones.

- [ ] **Step 7: Reconcile the spec with what was built**

Edit `docs/superpowers/specs/2026-10-08-embedding-recommender-design.md`:
- Scores are rounded to **6** decimals for embeddings (float32), not 9 (the "Similarity" section's ordering sentence).
- The build **records `n_truncated_inputs` and warns** instead of asserting that no chunk exceeds 512 tokens ("Text chunks" bullet).
- "Scoring parity with TF-IDF" is covered by the shared `rank_rows` function and `tests/test_ranking.py`, not a duplicate parity test (Milestone 2 tests).
- The encoder is pinned to revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a` and `encoder_revision` records that pin ("Encoder" decision and the metadata bullet).
- "Every album has at least one term" is guarded rather than assumed: an untagged album gets a zero tag row ("Tag string" bullet).
- Change **Status** to "Implemented <date>; see docs/recommendation-systems.md for results."

- [ ] **Step 8: Run everything and commit**

```bash
cd backend && uv run pytest -q && uv run ruff check . && uv run ruff format --check .
git add docs/recommendation-systems.md docs/superpowers/specs/2026-10-08-embedding-recommender-design.md eval/results
git commit -m "docs: record the Phase 5a embedding recommender and its evaluation" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```
Do not add `eval/judgments.jsonl` or `docs/project-decisions.md` (both are gitignored on purpose). Do not push. Do not change the default approach; if the report shows embeddings beating both overlap and TF-IDF on NDCG@5 **and** winning more seeds than losing against TF-IDF, tell the owner and let them decide on a separate commit.

---

## Self-review notes

- **Spec coverage:** documents/chunking/tag string (T2), encoder + `torch` isolation + dependency group (T4), model file + metadata (T2/T4), scoring + explanations (T3), loader + API + errors (T5), variants + `CORE_VARIANTS` (T6), build/latency/size recording, by-eye checkpoint, grading, default rule and documentation (T7). The spec's "scoring parity" test and the "assert no chunk > 512" are replaced, and the encoder pin and untagged-album guard added, as noted in Task 7 Step 7. The spec's "build is deterministic" test is `test_the_build_is_deterministic_apart_from_the_build_time` (T2).
- **Signatures used across tasks:** `rank_rows` (T1→T3), `build_model(docs, encoder, ...)`, `save_model`/`load_model`, `recommend(model, seed_ids, limit, *, alpha)` (T2/T3→T5/T6), `get_embedding_model` (T5), `embedding_model`, `model_version` (T6). `EmbeddingRecommendation` has no `shared_text_terms`; the route passes `[]`.
- **Risks to watch while executing:** `tests.fakes` import path (works because `tests/` has `__init__.py`; if pytest cannot import it, move the file next to `conftest.py` helpers and adjust imports); the real encoder is only exercised in Task 7, so the first real build may surface tokenizer-call differences in `sentence_encoder.py` (adjust there, nothing else depends on its internals).
