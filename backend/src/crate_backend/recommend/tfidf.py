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
from pathlib import Path
from typing import Any

import joblib
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
TOP_TERMS = 5

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
    # As in scikit-learn: an int is a document count, a float a proportion.
    min_df: float = 2,
    max_df: float = 0.5,
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
