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
