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

from crate_backend.recommend.ranking import rank_rows
from crate_backend.recommend.tfidf import DEFAULT_ALPHA, TOP_TERMS, AlbumDoc

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
