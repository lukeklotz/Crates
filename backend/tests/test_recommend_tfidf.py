import uuid

import numpy as np
import pytest

from crate_backend.recommend.tfidf import AlbumDoc, build_model, recommend

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
