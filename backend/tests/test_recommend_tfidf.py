import uuid
from datetime import datetime

import numpy as np
import pytest
import sklearn

from crate_backend.recommend.tfidf import (
    AlbumDoc,
    build_model,
    load_model,
    recommend,
    save_model,
)

# Tiny catalogs can't satisfy the production min_df=2 / max_df=0.5 text
# pruning, so tests keep every word.
KEEP_ALL_WORDS = {"min_df": 1, "max_df": 1.0}


def album(name: str, *terms: str, votes: dict[str, int] | None = None, text: str = "") -> AlbumDoc:
    return AlbumDoc(
        album_id=uuid.uuid5(uuid.NAMESPACE_URL, name),
        title=name,
        term_votes={term: 1 for term in terms} | (votes or {}),
        text=text,
    )


def model_of(*docs: AlbumDoc, **params):
    return build_model(list(docs), **(KEEP_ALL_WORDS | params))


def ranked_titles(model, results) -> list[str]:
    return [model.titles[model.row_of[r.album_id]] for r in results]


def scores(results) -> dict[uuid.UUID, float]:
    return {r.album_id: r.score for r in results}


def cosine(matrix, model, a: AlbumDoc, b: AlbumDoc) -> float:
    return (matrix[model.row_of[a.album_id]] @ matrix[model.row_of[b.album_id]].T)[0, 0]


def test_rare_shared_tag_outranks_common_shared_tag():
    seed = album("Seed", "rock", "glitch")
    model = model_of(
        seed,
        album("Common", "rock"),
        album("Rare", "glitch"),
        *(album(f"Filler {i}", "rock") for i in range(5)),
    )

    results = recommend(model, [seed.album_id], 20)

    assert ranked_titles(model, results)[0] == "Rare"


def test_higher_voted_shared_tag_outweighs_lower_voted_one():
    seed = album("Seed", votes={"ambient": 1, "drone": 20})
    model = model_of(seed, album("Ambient", "ambient"), album("Drone", "drone"))

    results = recommend(model, [seed.album_id], 20)

    assert ranked_titles(model, results) == ["Drone", "Ambient"]


def test_zero_votes_count_as_one():
    zero = model_of(album("Seed", votes={"jazz": 0, "funk": 1}), album("Other", "jazz"))
    one = model_of(album("Seed", votes={"jazz": 1, "funk": 1}), album("Other", "jazz"))

    np.testing.assert_allclose(zero.tag_matrix.toarray(), one.tag_matrix.toarray())


def test_text_counts_only_when_both_albums_have_it():
    seed = album("Seed", "jazz", "modal", text="spiritual modal saxophone")
    with_text = album("With Text", "jazz", text="modal saxophone suite")
    without = album("Without Text", "jazz", "modal")
    model = model_of(seed, with_text, without)

    blended = scores(recommend(model, [seed.album_id], 20))
    tags_only = scores(recommend(model, [seed.album_id], 20, alpha=1.0))

    assert blended[without.album_id] == pytest.approx(
        cosine(model.tag_matrix, model, seed, without), abs=1e-9
    )
    assert blended[with_text.album_id] == pytest.approx(
        0.6 * cosine(model.tag_matrix, model, seed, with_text)
        + 0.4 * cosine(model.text_matrix, model, seed, with_text),
        abs=1e-9,
    )
    assert tags_only[with_text.album_id] == pytest.approx(
        cosine(model.tag_matrix, model, seed, with_text), abs=1e-9
    )


def test_text_of_only_stopwords_counts_as_no_text():
    seed = album("Seed", "jazz", text="spiritual saxophone")
    blank = album("Blank", "jazz", text="the and of it")
    model = model_of(seed, blank)

    [result] = recommend(model, [seed.album_id], 20)

    assert not model.has_text[model.row_of[blank.album_id]]
    assert model.metadata["n_with_text"] == 1
    assert result.score == pytest.approx(1.0)


def test_catalog_without_any_text_scores_on_tags():
    seed = album("Seed", "jazz")
    model = model_of(seed, album("Other", "jazz"))

    [result] = recommend(model, [seed.album_id], 20)

    assert model.text_matrix.shape == (2, 0)
    assert result.score == pytest.approx(1.0)


def test_group_score_sums_each_seeds_similarity_and_excludes_seeds():
    a = album("Seed A", "ambient", "drone")
    b = album("Seed B", "techno", "acid")
    both = album("Both", "ambient", "techno")
    model = model_of(a, b, both, album("Neither", "polka"))

    alone_a = scores(recommend(model, [a.album_id], 20))
    alone_b = scores(recommend(model, [b.album_id], 20))
    together = scores(recommend(model, [a.album_id, b.album_id], 20))

    assert together[both.album_id] == pytest.approx(
        alone_a[both.album_id] + alone_b[both.album_id], abs=1e-8
    )
    assert set(together) == {both.album_id}


def test_ties_break_by_title_then_album_id():
    seed = album("Seed", "jazz")
    twins = [
        AlbumDoc(album_id=uuid.UUID(int=n), title="Same", term_votes={"jazz": 1}) for n in (2, 1)
    ]
    alpha, beta = album("Alpha", "jazz"), album("Beta", "jazz")
    model = model_of(seed, beta, alpha, *twins)

    results = recommend(model, [seed.album_id], 20)

    assert [r.album_id for r in results] == [
        alpha.album_id,
        beta.album_id,
        uuid.UUID(int=1),
        uuid.UUID(int=2),
    ]


def test_limit_keeps_tie_order_at_the_cut():
    seed = album("Seed", "jazz")
    model = model_of(seed, *(album(name, "jazz") for name in ["E", "C", "A", "D", "B"]))

    assert ranked_titles(model, recommend(model, [seed.album_id], 2)) == ["A", "B"]


def test_seeds_missing_from_the_model_are_ignored():
    seed, other = album("Seed", "jazz"), album("Other", "jazz")
    model = model_of(seed, other)
    unknown = uuid.uuid4()

    assert [r.album_id for r in recommend(model, [seed.album_id, unknown], 20)] == [other.album_id]
    assert recommend(model, [unknown], 20) == []


def test_shared_terms_are_ordered_by_contribution():
    seed = album("Seed", "rock", "glitch", "idm")
    candidate = album("Candidate", "rock", "glitch", "idm")
    model = model_of(
        seed,
        candidate,
        *(album(f"Rock {i}", "rock") for i in range(4)),
        album("IDM Fan", "idm"),
    )

    first = recommend(model, [seed.album_id], 20)[0]

    assert first.album_id == candidate.album_id
    # glitch is on 2 albums, idm on 3, rock on 6: rarer terms contribute more.
    assert first.shared_terms == ["glitch", "idm", "rock"]


def test_explanations_are_capped_at_five_terms():
    terms = [f"t{i}" for i in range(8)]
    seed = album("Seed", *terms)

    [result] = recommend(model_of(seed, album("Candidate", *terms)), [seed.album_id], 20)

    # Equal contributions fall back to alphabetical order.
    assert result.shared_terms == ["t0", "t1", "t2", "t3", "t4"]


def test_shared_text_terms_rank_distinctive_shared_words_first():
    seed = album("Seed", "jazz", text="modal saxophone saxophone suite")
    candidate = album("Candidate", "jazz", text="modal saxophone trumpet")
    model = model_of(
        seed, candidate, album("Other", "jazz", text="modal piano"), ngram_range=(1, 1)
    )

    result = next(
        r for r in recommend(model, [seed.album_id], 20) if r.album_id == candidate.album_id
    )

    assert result.shared_text_terms == ["saxophone", "modal"]


def test_shared_text_terms_empty_when_candidate_has_no_text():
    seed = album("Seed", "jazz", text="modal saxophone")
    candidate = album("Candidate", "jazz")
    model = model_of(seed, candidate, album("Other", "polka", text="modal accordion"))

    result = next(
        r for r in recommend(model, [seed.album_id], 20) if r.album_id == candidate.album_id
    )

    assert result.shared_terms == ["jazz"]
    assert result.shared_text_terms == []


def test_saved_model_loads_with_identical_scores(tmp_path):
    seed = album("Seed", "jazz", "modal", text="spiritual modal saxophone")
    model = model_of(
        seed,
        album("With Text", "jazz", text="modal saxophone suite"),
        album("Without Text", "modal"),
    )
    path = tmp_path / "nested" / "tfidf.joblib"

    save_model(model, path)
    loaded = load_model(path)

    assert recommend(loaded, [seed.album_id], 20) == recommend(model, [seed.album_id], 20)
    assert loaded.metadata == model.metadata
    assert not path.with_suffix(".tmp").exists()


def test_metadata_records_how_the_model_was_built():
    model = build_model(
        [album("A", "jazz", text="modal saxophone"), album("B", "jazz")],
        alpha=0.7,
        min_df=1,
        max_df=1.0,
        extra_metadata={"catalog_source": "test dump"},
    )

    metadata = model.metadata
    assert metadata["alpha"] == 0.7
    assert metadata["n_albums"] == 2
    assert metadata["n_with_text"] == 1
    assert metadata["catalog_source"] == "test dump"
    assert metadata["text_vectorizer"]["ngram_range"] == [1, 2]
    assert metadata["sklearn_version"] == sklearn.__version__
    datetime.fromisoformat(metadata["model_version"])


def test_phrases_are_whole_terms():
    model = model_of(
        album("A", "rock"),
        album("B", "rock"),
        phrases=[["crunchy guitars"], ["crunchy guitars", "warm sound"]],
    )

    assert sorted(model.text_terms) == ["crunchy guitars", "warm sound"]


def test_a_phrase_in_only_one_album_is_dropped_by_min_df():
    model = build_model(
        [album("A", "rock"), album("B", "rock")],
        phrases=[["crunchy guitars", "warm sound"], ["crunchy guitars"]],
        min_df=2,
        max_df=1.0,
    )

    assert list(model.text_terms) == ["crunchy guitars"]


def test_albums_without_phrases_score_on_tags_alone():
    seed = album("Seed", "jazz")
    match = album("Match", "jazz")
    for phrases in ([["warm sound"], []], [[], ["warm sound"]]):
        model = model_of(seed, match, phrases=phrases)

        [result] = recommend(model, [seed.album_id], 5)

        assert result.score == pytest.approx(1.0)
        assert result.shared_text_terms == []


def test_shared_phrases_explain_the_match():
    seed = album("Seed", "jazz")
    model = model_of(
        seed,
        album("Match", "jazz"),
        album("Other", "jazz"),
        phrases=[["warm sound", "chunky groove"], ["chunky groove"], ["warm sound"]],
    )

    results = {r.album_id: r for r in recommend(model, [seed.album_id], 5)}

    assert results[album("Match").album_id].shared_text_terms == ["chunky groove"]
    assert results[album("Other").album_id].shared_text_terms == ["warm sound"]


def test_metadata_records_the_text_source():
    docs = [album("A", "jazz", text="modal"), album("B", "jazz", text="modal")]

    article = model_of(*docs)
    phrase = model_of(*docs, phrases=[["warm sound"], ["warm sound"]])

    assert article.metadata["text_source"] == "article"
    assert "text_vectorizer" in article.metadata
    assert phrase.metadata["text_source"] == "sound_phrases"
    assert phrase.metadata["phrase_vectorizer"] == {"min_df": 1, "max_df": 1.0}
    assert "text_vectorizer" not in phrase.metadata


def test_phrases_replace_the_article_text():
    model = model_of(
        album("A", "jazz", text="modal saxophone"),
        album("B", "jazz", text="modal saxophone"),
        phrases=[["warm sound"], ["warm sound"]],
    )

    assert list(model.text_terms) == ["warm sound"]


def test_misaligned_phrases_are_rejected():
    with pytest.raises(ValueError, match="2 albums"):
        model_of(album("A", "jazz"), album("B", "jazz"), phrases=[["warm sound"]])


def test_no_phrases_at_all_gives_a_tags_only_model():
    seed = album("Seed", "jazz")
    model = model_of(seed, album("Match", "jazz"), phrases=[[], []])

    assert not model.has_text.any()
    assert len(model.text_terms) == 0
    assert len(recommend(model, [seed.album_id], 5)) == 1


def test_phrases_all_pruned_by_document_frequency_give_a_tags_only_model():
    seed = album("Seed", "jazz")
    model = build_model(
        [seed, album("Match", "jazz")],
        phrases=[["warm sound"], ["chunky groove"]],
        min_df=2,
        max_df=1.0,
    )

    assert not model.has_text.any()
    assert len(recommend(model, [seed.album_id], 5)) == 1
