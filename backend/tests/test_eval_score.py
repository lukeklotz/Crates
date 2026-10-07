import uuid
from datetime import date

import pytest

from crate_backend.evaluation.score import (
    AlbumFacts,
    build_report,
    judged_at_k,
    ndcg_at_k,
    pooled_recall_at_k,
)
from crate_backend.evaluation.store import Seed


def uid(name: str) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_URL, name)


S1, S2, A, B, C, D, X = (uid(n) for n in ("s1", "s2", "a", "b", "c", "d", "x"))


def test_ndcg_matches_a_hand_computed_example():
    # DCG = 3/log2(2) + 0 + 1/log2(4) = 3.5
    # IDCG from grades [2, 2, 1, 0] = 3 + 3/log2(3) + 1/log2(4) = 5.392789...
    grades = {A: 2, B: 0, C: 1, D: 2}

    assert ndcg_at_k([A, B, C], grades) == pytest.approx(0.649014792)


def test_ungraded_results_count_as_zero():
    # [X ungraded, A=2]: DCG = 3/log2(3); IDCG = 3.
    assert ndcg_at_k([X, A], {A: 2}) == pytest.approx(0.630929754)
    assert judged_at_k([X, A], {A: 2}) == 0.5


def test_perfect_ranking_scores_one_and_only_the_top_k_counts():
    grades = {A: 2, B: 1}

    assert ndcg_at_k([A, B], grades) == pytest.approx(1.0)
    assert ndcg_at_k([X, A], grades, k=1) == 0.0


def test_seed_with_no_relevant_candidate_is_undefined():
    assert ndcg_at_k([A, B], {A: 0, B: 0}) is None
    assert pooled_recall_at_k([A, B], {A: 0, B: 0}) is None
    assert ndcg_at_k([A], {}) is None


def test_pooled_recall_counts_grades_of_one_or_more():
    grades = {A: 2, B: 0, C: 1, D: 2}

    assert pooled_recall_at_k([A, B, C], grades) == pytest.approx(2 / 3)


def test_judged_at_k_of_no_results_is_one():
    assert judged_at_k([], {A: 2}) == 1.0


def test_report_rows_overall_and_per_quartile_and_flags_unjudged_results():
    seeds = [Seed(S1, "One", "X", "top"), Seed(S2, "Two", "Y", "bottom")]
    runs = {"good": {S1: [A], S2: [C]}, "new": {S1: [B], S2: [C]}}
    grades = {(S1, A): 2, (S2, C): 1}
    facts = {
        A: AlbumFacts(0.9, "x"),
        B: AlbumFacts(0.5, "y"),
        C: AlbumFacts(0.1, "z"),
    }

    report = build_report(
        seeds,
        runs,
        grades,
        facts,
        model_versions={"new": "2026-10-06T00:00:00+00:00"},
        today=date(2026, 10, 8),
    )

    assert "| good | all | 2/2 | 1.000 | 1.000 | 1.00 | 0.50 | 1.0 |" in report
    # B is ungraded: S1 scores 0, S2 scores 1.
    assert "| new | all | 2/2 | 0.500 | 0.500 | 0.50 ⚠ | 0.30 | 1.0 |" in report
    assert "| good | top | 1/1 | 1.000 |" in report
    assert "| new | bottom | 1/1 | 1.000 |" in report
    assert "| good | upper-mid | 0/0 | – | – | – | – | – |" in report
    assert "| good vs new | 1 | 0 | 1 |" in report
    assert "new: model 2026-10-06T00:00:00+00:00" in report
    assert report.startswith("# Evaluation results 2026-10-08")


def test_report_ignores_judgments_for_seeds_no_longer_in_the_seeds_file():
    seeds = [Seed(S1, "One", "X", "top")]
    runs = {"only": {S1: [A]}}
    grades = {(S1, A): 2, (S2, B): 2}

    report = build_report(seeds, runs, grades, {}, model_versions={}, today=date(2026, 10, 8))

    assert "Judgments: 1 for the current 1 seeds" in report
