import random
import uuid
from datetime import UTC, datetime

import pytest

from crate_backend.evaluation.grade import AlbumCard, first_sentence, load_cards, run_grader
from crate_backend.evaluation.store import Seed, append_line, judgment_line, load_judgments
from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag


def uid(name: str) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_URL, name)


S1, S2, S3, A, B, C = (uid(n) for n in ("s1", "s2", "s3", "a", "b", "c"))
SEEDS = [Seed(S1, "Seed One", "Artist", "top"), Seed(S2, "Seed Two", "Artist", "bottom")]


def card(title: str) -> AlbumCard:
    return AlbumCard(title, "Someone", 1999, ["jazz", "post bop"], f"{title} is an album.")


CARDS = {
    S1: card("Seed One"),
    S2: card("Seed Two"),
    A: card("Alpha"),
    B: card("Beta"),
    C: card("Gamma"),
}


def grade(path, keys, pool, cards=CARDS):
    out: list[str] = []
    remaining = iter(keys)

    def read_key() -> str:
        # Running out of scripted keys behaves like end of input: quit.
        key = next(remaining, "q")
        if isinstance(key, BaseException):
            raise key
        return key

    count = run_grader(
        pool, SEEDS, cards, path, read_key=read_key, write=out.append, rng=random.Random(0)
    )
    return count, "\n".join(out)


def test_shows_the_rubric_and_writes_each_grade_immediately(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, text = grade(path, ["2", "0"], [(S1, A), (S1, B)])

    assert count == 2
    assert "I'd recommend it to someone who loves the seed" in text
    assert set(load_judgments(path)) == {(S1, A), (S1, B)}
    assert sorted(load_judgments(path).values()) == [0, 2]


def test_rerun_resumes_with_only_ungraded_pairs(tmp_path):
    path = tmp_path / "judgments.jsonl"
    grade(path, ["1", "q"], [(S1, A), (S1, B)])
    [first] = load_judgments(path)

    count, _ = grade(path, ["2"], [(S1, A), (S1, B)])

    assert count == 1
    judged = load_judgments(path)
    assert len(judged) == 2 and judged[first] == 1


def test_skip_leaves_the_pair_for_next_time(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, _ = grade(path, ["s", "2"], [(S1, A), (S1, B)])
    assert count == 1
    count, _ = grade(path, ["0"], [(S1, A), (S1, B)])

    assert count == 1
    assert sorted(load_judgments(path).values()) == [0, 2]


def test_undo_removes_the_last_grade_and_asks_again(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, text = grade(path, ["2", "u", "1", "0"], [(S1, A), (S1, B)])

    assert count == 2
    assert len(path.read_text().splitlines()) == 2
    assert sorted(load_judgments(path).values()) == [0, 1]
    assert "Undid" in text


def test_undo_never_touches_grades_from_earlier_sessions(tmp_path):
    path = tmp_path / "judgments.jsonl"
    earlier = judgment_line(S2, C, 2, datetime(2026, 10, 1, tzinfo=UTC))
    append_line(path, earlier)

    count, text = grade(path, ["u", "q"], [(S1, A)])

    assert count == 0
    assert "Nothing to undo" in text
    assert path.read_text().splitlines() == [earlier]


def test_the_last_grade_in_the_pool_can_be_undone(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, text = grade(path, ["1", "2", "u", "0", "q"], [(S1, A), (S1, B)])

    assert count == 2
    assert sorted(load_judgments(path).values()) == [0, 1]
    assert "Undid" in text


def test_quit_reports_progress(tmp_path):
    count, text = grade(tmp_path / "j.jsonl", ["q"], [(S1, A), (S1, B)])

    assert count == 0
    assert "0 graded this session; 2 left" in text


def test_ctrl_c_quits_and_keeps_grades(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, text = grade(path, ["2", KeyboardInterrupt()], [(S1, A), (S1, B)])

    assert count == 1
    assert len(load_judgments(path)) == 1
    assert "1 graded this session; 1 left" in text


def test_unrecognized_key_asks_again(tmp_path):
    count, text = grade(tmp_path / "j.jsonl", ["x", "2"], [(S1, A)])

    assert count == 1
    assert "Unrecognized key" in text


def test_seed_header_once_per_seed_and_variant_never_shown(tmp_path):
    _, text = grade(tmp_path / "j.jsonl", ["0", "0", "0"], [(S1, A), (S2, C), (S1, B)])

    assert text.count("=== Seed") == 2
    assert text.index("Gamma") > max(text.index("Alpha"), text.index("Beta"))
    assert "overlap" not in text and "tfidf" not in text


def test_pairs_for_seeds_no_longer_in_the_seeds_file_are_skipped(tmp_path):
    count, _ = grade(tmp_path / "j.jsonl", [], [(S3, A)])

    assert count == 0


def test_candidates_missing_from_the_catalog_are_skipped_with_a_note(tmp_path):
    cards = {k: v for k, v in CARDS.items() if k != B}

    count, text = grade(tmp_path / "j.jsonl", ["2"], [(S1, B), (S1, A)], cards=cards)

    assert count == 1
    assert "no longer in the catalog" in text


@pytest.mark.parametrize(
    ("article", "sentence"),
    [
        (None, ""),
        ("Kid A is the fourth album. It came out in 2000.\n\n== Background ==\nX.",
         "Kid A is the fourth album."),
        ("A lead that wraps\nonto a second line. More.", "A lead that wraps onto a second line."),
        ("A lead without a full stop", "A lead without a full stop"),
        ("== Background ==\nNo lead at all.", ""),
        ("A" * 400 + ".", "A" * 299 + "…"),
    ],
)  # fmt: skip
def test_first_sentence(article, sentence):
    assert first_sentence(article) == sentence


async def test_load_cards_lists_terms_by_votes_and_reads_the_lead(db_session):
    album = Album(title="Zzfixture Card Album", artist_name="Card Artist", release_year=1965)
    bare = Album(title="Zzfixture Bare Card", artist_name="Card Artist")
    genre = Genre(musicbrainz_id=str(uuid.uuid4()), name="Zzfixture-Card Genre")
    tag = Tag(name="zzfixture card tag")
    db_session.add_all([album, bare, genre, tag])
    await db_session.flush()
    db_session.add_all(
        [
            AlbumGenre(album_id=album.id, genre_id=genre.id, count=1),
            AlbumTag(album_id=album.id, tag_id=tag.id, count=7),
            AlbumText(
                album_id=album.id,
                source=WIKIPEDIA_SOURCE,
                text="Card Album is a record. Second.\n\n== Personnel ==\nX – drums",
                fetched_at=datetime.now(UTC),
            ),
        ]
    )
    await db_session.flush()

    cards = await load_cards(db_session, [album.id, bare.id])

    assert cards[album.id] == AlbumCard(
        "Zzfixture Card Album",
        "Card Artist",
        1965,
        ["zzfixture card tag", "zzfixture card genre"],
        "Card Album is a record.",
    )
    assert cards[bare.id].terms == [] and cards[bare.id].lead == ""
