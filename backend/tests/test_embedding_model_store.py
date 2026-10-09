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
