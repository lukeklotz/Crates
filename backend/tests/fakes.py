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
        self.table = {
            text: np.asarray(vec, dtype=np.float64) for text, vec in (table or {}).items()
        }
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
