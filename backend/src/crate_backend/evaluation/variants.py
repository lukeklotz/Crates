"""Named recommender configurations compared by the evaluation harness
(Phase 4, Milestone 3).

α is applied at scoring time, so tfidf-tags, tfidf-tags+text and the α
sweep share one model file. Variants that change the text block need
their own file, built with the flags in `build_flags`.
"""

import uuid
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.core.config import get_settings
from crate_backend.evaluation.store import Seed
from crate_backend.recommend.overlap import recommend_by_overlap
from crate_backend.recommend.tfidf import TfidfModel, load_model, recommend

TOP_K = 5


@dataclass(frozen=True)
class Variant:
    name: str
    approach: str  # "overlap" | "tfidf"
    # TF-IDF only. None means the default model file (settings.tfidf_model_path).
    model_file: str | None = None
    build_flags: tuple[str, ...] = ()
    alpha: float | None = None

    def model_path(self) -> Path:
        default = Path(get_settings().tfidf_model_path)
        return default if self.model_file is None else default.with_name(self.model_file)


def _file_variant(name: str, flag: str) -> Variant:
    return Variant(name, "tfidf", model_file=f"{name}.joblib", build_flags=(flag,), alpha=0.6)


VARIANTS = {
    v.name: v
    for v in (
        Variant("overlap", "overlap"),
        Variant("tfidf-tags", "tfidf", alpha=1.0),
        Variant("tfidf-tags+text", "tfidf", alpha=0.6),
        # Stretch variants (spec: grade only after the core is graded).
        Variant("tfidf-a0.4", "tfidf", alpha=0.4),
        Variant("tfidf-a0.8", "tfidf", alpha=0.8),
        _file_variant("tfidf-no-reception", "--no-reception"),
        _file_variant("tfidf-no-personnel", "--no-personnel"),
        _file_variant("tfidf-no-bigrams", "--no-bigrams"),
    )
}
CORE_VARIANTS = ("overlap", "tfidf-tags", "tfidf-tags+text")


def parse_variant_names(text: str | None) -> list[Variant]:
    names = CORE_VARIANTS if text is None else [n.strip() for n in text.split(",") if n.strip()]
    unknown = [name for name in names if name not in VARIANTS]
    if unknown:
        raise ValueError(f"Unknown variants {unknown}; known: {', '.join(VARIANTS)}")
    return [VARIANTS[name] for name in names]


class ModelNotBuilt(Exception):
    pass


_models: dict[Path, TfidfModel] = {}


def tfidf_model(variant: Variant) -> TfidfModel:
    path = variant.model_path()
    if path not in _models:
        if not path.exists():
            flags = " ".join(variant.build_flags)
            raise ModelNotBuilt(
                f"{variant.name}: no model at {path}. Build it with: uv run python -m "
                f"crate_backend.scripts.build_tfidf_model --out {path} {flags}".rstrip()
            )
        _models[path] = load_model(path)
    return _models[path]


async def top_k(
    variant: Variant, session: AsyncSession | None, seed_id: uuid.UUID, k: int = TOP_K
) -> list[uuid.UUID]:
    """The variant's top k album ids for a single-album seed. `session` is
    only used by overlap."""
    if variant.approach == "overlap":
        return [r.album_id for r in await recommend_by_overlap(session, [seed_id], k)]
    model = tfidf_model(variant)
    return [r.album_id for r in recommend(model, [seed_id], k, alpha=variant.alpha)]


async def run_variants(
    variants: Iterable[Variant], session: AsyncSession, seeds: list[Seed], k: int = TOP_K
) -> dict[str, dict[uuid.UUID, list[uuid.UUID]]]:
    """Variant name -> seed id -> ranked album ids."""
    runs: dict[str, dict[uuid.UUID, list[uuid.UUID]]] = {}
    for variant in variants:
        runs[variant.name] = {
            seed.album_id: await top_k(variant, session, seed.album_id, k) for seed in seeds
        }
    return runs
