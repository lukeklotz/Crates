import uuid

import numpy as np

from crate_backend.recommend.ranking import rank_rows


def ids(n: int) -> list[uuid.UUID]:
    return [uuid.UUID(int=i + 1) for i in range(n)]


def test_orders_by_score_then_title_then_id():
    titles = ["b", "a", "a", "c"]
    album_ids = ids(4)
    scores = np.array([0.5, 0.5, 0.5, 0.9])

    rows = rank_rows(titles, album_ids, scores, seed_rows=[], limit=10)

    # 0.9 first; then the 0.5 ties by title ("a" before "b"), then by id.
    assert rows == [3, 1, 2, 0]


def test_excludes_seeds_and_non_positive_scores():
    titles = ["seed", "zero", "negative", "match"]
    scores = np.array([0.9, 0.0, -0.2, 0.4])

    rows = rank_rows(titles, ids(4), scores, seed_rows=[0], limit=10)

    assert rows == [3]


def test_limit_keeps_ties_for_the_tiebreak_to_decide():
    titles = ["top", "zeta", "alpha", "mid"]
    scores = np.array([0.9, 0.5, 0.5, 0.5])

    rows = rank_rows(titles, ids(4), scores, seed_rows=[], limit=2)

    assert rows == [0, 2]  # "alpha" beats "zeta" and "mid" for the last slot


def test_does_not_modify_the_scores_it_is_given():
    scores = np.array([0.9, 0.4])

    rank_rows(["a", "b"], ids(2), scores, seed_rows=[0], limit=5)

    assert scores.tolist() == [0.9, 0.4]
