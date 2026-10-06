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
