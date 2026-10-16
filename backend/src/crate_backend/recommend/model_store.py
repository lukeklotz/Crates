"""The API process's copies of the model files: TF-IDF (Phase 4, Milestone 2),
sound-phrase TF-IDF, and sentence embeddings (Phase 5a)."""

from pathlib import Path

from crate_backend.core.config import get_settings
from crate_backend.recommend import embeddings
from crate_backend.recommend.tfidf import TfidfModel, load_model

_loaded: dict[Path, TfidfModel] = {}


def get_tfidf_model() -> TfidfModel | None:
    """The model at settings.tfidf_model_path, loaded on first use and kept
    for the life of the process. None while the file doesn't exist. That
    answer isn't cached, so a first build needs no restart; a rebuild of an
    already-loaded model does."""
    return _load_tfidf(Path(get_settings().tfidf_model_path))


def get_tfidf_phrases_model() -> TfidfModel | None:
    """The sound-phrase model at settings.tfidf_phrases_model_path, with the
    same loading rules as get_tfidf_model."""
    return _load_tfidf(Path(get_settings().tfidf_phrases_model_path))


def _load_tfidf(path: Path) -> TfidfModel | None:
    if path not in _loaded:
        if not path.exists():
            return None
        _loaded[path] = load_model(path)
    return _loaded[path]


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
