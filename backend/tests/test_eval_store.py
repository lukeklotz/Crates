import json
import uuid
from datetime import UTC, datetime

import pytest

from crate_backend.evaluation.store import (
    Seed,
    append_line,
    judgment_line,
    load_judgments,
    load_pool,
    load_seeds,
    popularity_quartile,
    remove_line,
    save_pool,
    save_seeds,
)

A, B, C = (uuid.uuid5(uuid.NAMESPACE_URL, name) for name in ("a", "b", "c"))
AT = datetime(2026, 10, 7, 12, 0, tzinfo=UTC)


def test_seeds_round_trip_as_hand_editable_json(tmp_path):
    path = tmp_path / "eval" / "seeds.json"
    seeds = [Seed(A, "Kid A", "Radiohead", "top"), Seed(B, "Café Tacvba", None, "bottom")]

    save_seeds(seeds, path)

    assert load_seeds(path) == seeds
    assert json.loads(path.read_text())[0] == {
        "album_id": str(A),
        "title": "Kid A",
        "artist_name": "Radiohead",
        "popularity_quartile": "top",
    }
    assert "Café" in path.read_text()


@pytest.mark.parametrize(
    ("popularity", "quartile"),
    [
        (1.0, "top"),
        (0.75, "top"),
        (0.7499, "upper-mid"),
        (0.5, "upper-mid"),
        (0.25, "lower-mid"),
        (0.2499, "bottom"),
        (0.011, "bottom"),
    ],
)
def test_popularity_quartile(popularity, quartile):
    assert popularity_quartile(popularity) == quartile


def test_missing_judgments_file_means_no_judgments(tmp_path):
    assert load_judgments(tmp_path / "judgments.jsonl") == {}


def test_judgments_append_and_later_lines_win(tmp_path):
    path = tmp_path / "eval" / "judgments.jsonl"

    append_line(path, judgment_line(A, B, 2, AT))
    append_line(path, judgment_line(A, C, 0, AT))
    append_line(path, judgment_line(A, B, 1, AT))

    assert load_judgments(path) == {(A, B): 1, (A, C): 0}
    assert json.loads(path.read_text().splitlines()[0]) == {
        "seed_id": str(A),
        "candidate_id": str(B),
        "grade": 2,
        "graded_at": "2026-10-07T12:00:00+00:00",
    }


def test_judgments_skip_blank_lines_and_reject_bad_grades(tmp_path):
    path = tmp_path / "judgments.jsonl"
    path.write_text("\n" + judgment_line(A, B, 2, AT) + "\n\n")
    assert load_judgments(path) == {(A, B): 2}

    path.write_text(judgment_line(A, B, 3, AT) + "\n")
    with pytest.raises(ValueError, match="line 1"):
        load_judgments(path)


def test_remove_line_removes_only_the_last_exact_copy(tmp_path):
    path = tmp_path / "judgments.jsonl"
    first, other = judgment_line(A, B, 2, AT), judgment_line(A, C, 1, AT)
    for line in (first, other, first):
        append_line(path, line)

    assert remove_line(path, first)
    assert path.read_text().splitlines() == [first, other]
    assert not remove_line(path, judgment_line(B, C, 0, AT))
    assert path.read_text().splitlines() == [first, other]


def test_pool_round_trip(tmp_path):
    path = tmp_path / "eval" / "pool.jsonl"

    save_pool([(A, B), (A, C)], path)

    assert load_pool(path) == [(A, B), (A, C)]
