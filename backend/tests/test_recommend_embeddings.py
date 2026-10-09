import uuid

import numpy as np

from crate_backend.recommend.embeddings import EmbeddingModel, recommend

# A row is (name, tag vector, text vector or None, term votes). Vectors are
# 2-D so cosines are easy to reason about; the helper normalizes them.


def aid(name: str) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_URL, name)


def unit(vec) -> np.ndarray:
    v = np.asarray(vec, dtype=np.float32)
    n = np.linalg.norm(v)
    return v / n if n > 0 else v


def make_model(*rows, alpha: float = 0.6) -> EmbeddingModel:
    names = [r[0] for r in rows]
    return EmbeddingModel(
        album_ids=[aid(n) for n in names],
        titles=names,
        tag_vectors=np.stack([unit(r[1]) for r in rows]),
        text_vectors=np.stack(
            [unit(r[2]) if r[2] is not None else np.zeros(2, np.float32) for r in rows]
        ),
        has_text=np.array([r[2] is not None for r in rows]),
        term_votes=[r[3] if len(r) > 3 else {} for r in rows],
        metadata={"alpha": alpha, "model_version": "test"},
    )


def titles(model, results) -> list[str]:
    return [model.titles[model.row_of[r.album_id]] for r in results]


def test_the_closer_vector_ranks_first():
    model = make_model(
        ("Seed", [1, 0], None),
        ("Near", [0.9, 0.1], None),
        ("Far", [0.5, 0.5], None),
    )

    results = recommend(model, [aid("Seed")], 10)

    assert titles(model, results) == ["Near", "Far"]


def test_albums_without_text_are_compared_on_tags_alone():
    model = make_model(
        ("Seed", [1, 0], [1, 0]),
        ("NoText", [1, 1], None),
    )

    [result] = recommend(model, [aid("Seed")], 10)

    assert result.score == round(2**-0.5, 6)


def test_albums_with_text_on_both_sides_blend_tag_and_text_cosines():
    model = make_model(
        ("Seed", [1, 0], [1, 0]),
        ("Both", [1, 1], [0, 1]),  # tag cos 0.7071, text cos 0
    )

    [default] = recommend(model, [aid("Seed")], 10)
    [text_heavy] = recommend(model, [aid("Seed")], 10, alpha=0.2)

    assert default.score == round(0.6 * 2**-0.5, 6)
    assert text_heavy.score == round(0.2 * 2**-0.5, 6)


def test_group_scores_sum_over_seeds_and_seeds_are_never_returned():
    model = make_model(
        ("Seed1", [1, 0], None),
        ("Seed2", [0, 1], None),
        ("Between", [1, 1], None),
        ("OnlyOne", [1, 0.2], None),
    )

    results = recommend(model, [aid("Seed1"), aid("Seed2")], 10)

    assert titles(model, results) == ["Between", "OnlyOne"]
    assert all(r.album_id not in (aid("Seed1"), aid("Seed2")) for r in results)


def test_candidates_pointing_away_from_the_seeds_are_excluded():
    model = make_model(
        ("Seed", [1, 0], None),
        ("Opposite", [-1, 0], None),
        ("Match", [1, 1], None),
    )

    assert titles(model, recommend(model, [aid("Seed")], 10)) == ["Match"]


def test_ties_break_by_title_then_the_limit_applies():
    model = make_model(
        ("Seed", [1, 0], None),
        ("Zulu", [1, 1], None),
        ("Alpha", [1, 1], None),
        ("Mike", [1, 1], None),
    )

    assert titles(model, recommend(model, [aid("Seed")], 10)) == ["Alpha", "Mike", "Zulu"]
    assert titles(model, recommend(model, [aid("Seed")], 2)) == ["Alpha", "Mike"]


def test_seeds_missing_from_the_model_contribute_nothing():
    model = make_model(("Seed", [1, 0], None), ("Match", [1, 1], None))

    with_unknown = recommend(model, [aid("Seed"), uuid.uuid4()], 10)

    assert titles(model, with_unknown) == ["Match"]
    assert recommend(model, [uuid.uuid4()], 10) == []


def test_shared_terms_are_ranked_by_summed_seed_votes_times_candidate_votes():
    model = make_model(
        ("Seed1", [1, 0], None, {"jazz": 5, "bop": 1}),
        ("Seed2", [1, 0.1], None, {"jazz": 5, "modal": 2}),
        ("Match", [1, 0.2], None, {"jazz": 1, "modal": 3, "bop": 1, "polka": 9}),
    )

    result = next(
        r for r in recommend(model, [aid("Seed1"), aid("Seed2")], 10) if r.album_id == aid("Match")
    )

    # jazz 10*1=10, modal 2*3=6, bop 1*1=1; polka is on no seed.
    assert result.shared_terms == ["jazz", "modal", "bop"]


def test_shared_terms_are_capped_at_five():
    terms = {f"t{i}": 1 for i in range(8)}
    model = make_model(("Seed", [1, 0], None, terms), ("Match", [1, 0.1], None, terms))

    [result] = recommend(model, [aid("Seed")], 10)

    assert len(result.shared_terms) == 5
    assert result.shared_terms == sorted(result.shared_terms)
