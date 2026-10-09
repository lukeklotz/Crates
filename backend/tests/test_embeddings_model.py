import uuid

import numpy as np

from crate_backend.recommend.embeddings import (
    CHUNK_WORDS,
    MIN_TAIL_WORDS,
    TAG_TERMS,
    build_model,
    chunk_text,
    load_model,
    save_model,
    tag_string,
)
from crate_backend.recommend.tfidf import AlbumDoc
from tests.fakes import FakeEncoder


def words(n: int, prefix: str = "w") -> str:
    return " ".join(f"{prefix}{i}" for i in range(n))


def doc(name: str, terms: dict[str, int], text: str = "") -> AlbumDoc:
    return AlbumDoc(
        album_id=uuid.uuid5(uuid.NAMESPACE_URL, name), title=name, term_votes=terms, text=text
    )


def test_constants_match_the_spec():
    assert (CHUNK_WORDS, MIN_TAIL_WORDS, TAG_TERMS) == (250, 50, 20)


def test_chunks_are_full_windows_with_a_short_remainder_chunk():
    chunks = chunk_text(words(600))

    assert [len(c.split()) for c in chunks] == [250, 250, 100]


def test_a_tiny_tail_is_merged_into_the_previous_chunk():
    chunks = chunk_text(words(520))  # 250 + 250 + 20

    assert [len(c.split()) for c in chunks] == [250, 270]


def test_text_shorter_than_one_chunk_is_one_chunk_even_if_tiny():
    assert [len(c.split()) for c in chunk_text(words(100))] == [100]
    assert [len(c.split()) for c in chunk_text(words(10))] == [10]


def test_empty_or_whitespace_text_has_no_chunks():
    assert chunk_text("") == []
    assert chunk_text("   \n\t  ") == []


def test_tag_string_orders_by_votes_then_name_and_caps_at_the_limit():
    terms = {"rock": 3, "jazz": 9, "blues": 3, "folk": 1}

    assert tag_string(terms) == "jazz, blues, rock, folk"
    assert tag_string(terms, limit=2) == "jazz, blues"
    many = {f"t{i:02d}": 100 - i for i in range(30)}
    assert tag_string(many).count(",") == TAG_TERMS - 1


def test_text_vector_is_the_renormalized_mean_of_its_chunks():
    encoder = FakeEncoder({"a b": [1, 0], "c d": [0, 1], "jazz": [1, 1]})

    model = build_model(
        [doc("Album", {"jazz": 1}, text="a b c d")], encoder, chunk_words=2, min_tail_words=1
    )

    np.testing.assert_allclose(model.text_vectors[0], [2**-0.5, 2**-0.5], rtol=1e-6)
    assert model.has_text.tolist() == [True]
    np.testing.assert_allclose(model.tag_vectors[0], [2**-0.5, 2**-0.5], rtol=1e-6)


def test_albums_without_usable_text_get_a_zero_row_and_no_text_flag():
    encoder = FakeEncoder(dim=4)
    docs = [
        doc("Has", {"jazz": 1}, text=words(30)),
        doc("Empty", {"jazz": 1}, text=""),
        doc("Blank", {"jazz": 1}, text="  \n "),
    ]

    model = build_model(docs, encoder)

    assert model.has_text.tolist() == [True, False, False]
    assert not model.text_vectors[1].any() and not model.text_vectors[2].any()
    assert model.metadata["n_with_text"] == 1
    assert model.metadata["n_chunks"] == 1


def test_metadata_records_the_build_and_the_encoder():
    encoder = FakeEncoder(dim=4)

    model = build_model(
        [doc("A", {"jazz": 1}), doc("B", {"rock": 1})],
        encoder,
        alpha=0.5,
        extra_metadata={"catalog_source": "test dump"},
    )

    meta = model.metadata
    assert meta["alpha"] == 0.5
    assert meta["n_albums"] == 2
    assert meta["embedding_dim"] == 4
    assert meta["chunk_words"] == 250 and meta["min_tail_words"] == 50
    assert meta["tag_terms_per_album"] == 20
    assert meta["encoder_name"] == "fake"
    assert meta["catalog_source"] == "test dump"
    assert meta["model_version"]  # ISO 8601 build time


def test_the_encoder_is_called_once_for_tags_and_once_for_all_chunks():
    encoder = FakeEncoder(dim=4)
    docs = [doc("A", {"jazz": 1}, text=words(30)), doc("B", {"rock": 1}, text=words(30, "x"))]

    build_model(docs, encoder)

    assert len(encoder.calls) == 2
    assert encoder.calls[0] == ["jazz", "rock"]
    assert len(encoder.calls[1]) == 2


def test_albums_without_terms_get_a_zero_tag_row_and_are_not_encoded():
    encoder = FakeEncoder(dim=4)
    docs = [doc("Tagged", {"jazz": 1}), doc("Untagged", {})]

    model = build_model(docs, encoder)

    assert encoder.calls[0] == ["jazz"]
    assert model.tag_vectors[0].any()
    assert not model.tag_vectors[1].any()


def test_the_build_is_deterministic_apart_from_the_build_time():
    docs = [
        doc("A", {"jazz": 2, "bop": 2}, text=words(300)),
        doc("B", {"rock": 1}, text=words(40, "x")),
        doc("C", {"folk": 1}),
    ]

    first = build_model(docs, FakeEncoder(dim=8))
    second = build_model(docs, FakeEncoder(dim=8))

    np.testing.assert_array_equal(first.tag_vectors, second.tag_vectors)
    np.testing.assert_array_equal(first.text_vectors, second.text_vectors)
    np.testing.assert_array_equal(first.has_text, second.has_text)
    assert first.term_votes == second.term_votes
    second.metadata["model_version"] = first.metadata["model_version"]
    assert first.metadata == second.metadata


def test_save_then_load_round_trips_everything(tmp_path):
    encoder = FakeEncoder(dim=4)
    docs = [doc("A", {"jazz": 2, "bop": 1}, text=words(30)), doc("B", {"rock": 1})]
    model = build_model(docs, encoder)
    path = tmp_path / "models" / "embeddings.joblib"

    save_model(model, path)
    loaded = load_model(path)

    assert loaded.album_ids == model.album_ids
    assert loaded.titles == model.titles
    np.testing.assert_array_equal(loaded.tag_vectors, model.tag_vectors)
    np.testing.assert_array_equal(loaded.text_vectors, model.text_vectors)
    np.testing.assert_array_equal(loaded.has_text, model.has_text)
    assert loaded.term_votes == model.term_votes
    assert loaded.metadata == model.metadata
    assert loaded.row_of == model.row_of
    assert not path.with_suffix(".tmp").exists()
