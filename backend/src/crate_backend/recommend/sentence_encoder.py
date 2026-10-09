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
