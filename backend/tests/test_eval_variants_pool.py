import uuid

import pytest

from crate_backend.core.config import Settings
from crate_backend.evaluation import variants
from crate_backend.evaluation.pool import new_pairs
from crate_backend.evaluation.store import Seed
from crate_backend.evaluation.variants import (
    CORE_VARIANTS,
    VARIANTS,
    ModelNotBuilt,
    embedding_model,
    model_version,
    parse_variant_names,
    top_k,
)
from crate_backend.models.catalog import Album, AlbumTag, Tag
from crate_backend.recommend import embeddings
from crate_backend.recommend.tfidf import AlbumDoc, build_model, save_model
from tests.fakes import FakeEncoder


def uid(name: str) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_URL, name)


S1, S2, A, B, C, D = (uid(n) for n in ("s1", "s2", "a", "b", "c", "d"))


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


def test_parse_variant_names():
    assert [v.name for v in parse_variant_names(None)] == list(CORE_VARIANTS)
    assert [v.name for v in parse_variant_names("overlap, tfidf-a0.4")] == [
        "overlap",
        "tfidf-a0.4",
    ]
    with pytest.raises(ValueError, match="tfidf-tags\\+text"):
        parse_variant_names("overlap,nope")


def test_core_tfidf_variants_share_the_default_model_and_stretch_files_sit_beside_it(model_path):
    assert VARIANTS["tfidf-tags"].model_path() == model_path
    assert VARIANTS["tfidf-a0.8"].model_path() == model_path
    assert VARIANTS["tfidf-no-reception"].model_path() == model_path.with_name(
        "tfidf-no-reception.joblib"
    )


async def test_missing_model_names_the_build_command(model_path):
    with pytest.raises(ModelNotBuilt, match="--no-reception"):
        await top_k(VARIANTS["tfidf-no-reception"], None, S1)


async def test_tfidf_variants_apply_their_alpha(model_path):
    seed = AlbumDoc(S1, "Seed", {"rock": 1}, text="glacial saxophone")
    tag_twin = AlbumDoc(A, "Tag Twin", {"rock": 1}, text="loud guitars")
    text_twin = AlbumDoc(B, "Text Twin", {"polka": 1}, text="glacial saxophone")
    save_model(build_model([seed, tag_twin, text_twin], min_df=1, max_df=1.0), model_path)

    assert await top_k(VARIANTS["tfidf-tags"], None, S1) == [A]
    assert await top_k(VARIANTS["tfidf-tags+text"], None, S1) == [A, B]


async def test_overlap_variant_ranks_from_the_database(db_session):
    seed = Album(title="Zzfixture Pool Seed", artist_name="Fixture Artist")
    match = Album(title="Zzfixture Pool Match", artist_name="Fixture Artist")
    tag = Tag(name="zzfixture-pool-term")
    db_session.add_all([seed, match, tag])
    await db_session.flush()
    db_session.add_all([AlbumTag(album_id=a.id, tag_id=tag.id) for a in (seed, match)])
    await db_session.flush()

    assert await top_k(VARIANTS["overlap"], db_session, seed.id) == [match.id]


def test_new_pairs_dedupes_across_variants_and_skips_judged():
    seeds = [Seed(S1, "One", "X", "top"), Seed(S2, "Two", "Y", "bottom")]
    runs = {"a": {S1: [A, B], S2: [C]}, "b": {S1: [B, D], S2: []}}

    pairs = new_pairs(seeds, runs, judged={(S1, A): 2})

    assert pairs == [(S1, c) for c in sorted([B, D], key=str)] + [(S2, C)]


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
    assert (
        model_version(VARIANTS["embed-tags"])
        == embedding_model(VARIANTS["embed-tags"]).metadata["model_version"]
    )
