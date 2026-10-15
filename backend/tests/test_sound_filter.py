from crate_backend.recommend.sound_filter import (
    OTHER_EXAMPLES,
    SOUND_EXAMPLES,
    filter_sound,
    split_sentences,
)
from tests.fakes import FakeEncoder

# Every example sentence of a kind maps to that kind's axis, so a test
# sentence's side is set by the vector it is given.
SOUND = [1.0, 0.0]
OTHER = [0.0, 1.0]


def encoder(sentences: dict[str, list[float]]) -> FakeEncoder:
    table = {text: SOUND for text in SOUND_EXAMPLES}
    table.update({text: OTHER for text in OTHER_EXAMPLES})
    table.update(sentences)
    return FakeEncoder(table)


def test_sentences_split_on_end_punctuation_and_newlines():
    text = 'It was loud. Was it fast? Yes! "Quoted" works.\nA – bass guitar\n\n'

    assert split_sentences(text) == [
        "It was loud.",
        "Was it fast?",
        "Yes!",
        '"Quoted" works.',
        "A – bass guitar",
    ]


def test_a_period_not_followed_by_a_capital_does_not_split():
    assert split_sentences("Released on 1.5 rpm vinyl. It sold.") == [
        "Released on 1.5 rpm vinyl.",
        "It sold.",
    ]


def test_keeps_sentences_closer_to_the_sound_examples():
    enc = encoder({"Jangly guitars.": [0.9, 0.1], "It charted.": [0.1, 0.9]})

    result = filter_sound(["Jangly guitars. It charted."], enc)

    assert result.texts == ["Jangly guitars."]
    assert (result.n_sentences, result.n_kept, result.n_emptied) == (2, 1, 0)


def test_the_margin_raises_the_bar():
    enc = encoder({"Somewhat musical.": [0.6, 0.4]})

    assert filter_sound(["Somewhat musical."], enc, margin=0.0).texts == ["Somewhat musical."]
    assert filter_sound(["Somewhat musical."], enc, margin=0.5).texts == [""]


def test_an_album_left_with_nothing_is_counted_and_empty_text_is_skipped():
    enc = encoder({"It charted.": [0.1, 0.9]})

    result = filter_sound(["It charted.", ""], enc)

    assert result.texts == ["", ""]
    assert (result.n_sentences, result.n_kept, result.n_emptied) == (1, 0, 1)


def test_all_sentences_are_encoded_in_one_call():
    enc = encoder({"A.": SOUND, "B.": SOUND, "C.": OTHER})

    filter_sound(["A. B.", "C."], enc)

    assert len(enc.calls) == 2  # the examples, then every sentence
    assert enc.calls[1] == ["A.", "B.", "C."]


def test_credit_lines_are_dropped_without_scoring():
    enc = encoder({"Thundercat – bass (tracks 2, 10)": SOUND, "Jangly guitars.": SOUND})

    result = filter_sound(["Thundercat – bass (tracks 2, 10)\nJangly guitars."], enc)

    assert result.texts == ["Jangly guitars."]
    assert (result.n_sentences, result.n_kept) == (2, 1)
    assert enc.calls[1] == ["Jangly guitars."]


def test_a_sentence_is_scored_by_its_three_closest_examples_of_each_kind():
    # Near one sound example but far from the rest: the top-3 average is
    # what decides, not the single best match.
    table = {text: [0.0, 1.0, 0.0] for text in OTHER_EXAMPLES}
    table.update({text: [0.0, 0.0, 1.0] for text in SOUND_EXAMPLES})
    table[SOUND_EXAMPLES[0]] = [1.0, 0.0, 0.0]
    table["Lucky match."] = [1.0, 0.4, 0.0]

    assert filter_sound(["Lucky match."], FakeEncoder(table)).texts == [""]
