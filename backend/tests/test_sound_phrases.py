import pytest
import spacy

from crate_backend.recommend.sound_phrases import (
    SPACY_MODEL,
    extract,
    extract_all,
    prose_only,
)

# Expected outputs were checked against spacy 3.8.7 + en_core_web_sm 3.8.0.
# A parser upgrade that changes them should fail here, not drift silently.
KNOWN = frozenset({"acid jazz", "hip hop", "heavy metal", "new wave"})


@pytest.fixture(scope="module")
def nlp():
    return spacy.load(SPACY_MODEL)


@pytest.fixture
def phrases(nlp):
    return lambda text, known=KNOWN: extract(nlp(text), known)


def test_modifiers_of_music_nouns_and_their_conjuncts(phrases):
    assert phrases("The album pairs jangly guitars and breathy vocals.") == [
        "jangly guitars",
        "breathy vocals",
    ]


def test_a_generic_noun_keeps_only_its_descriptor(phrases):
    assert phrases("They are an industrial band from Vancouver.") == ["industrial"]


def test_adjectives_after_a_linking_verb(phrases):
    assert phrases("The sound is warm and spacious.") == ["warm sound", "spacious sound"]


def test_labels_after_a_describing_verb(phrases):
    assert phrases("Critics called the album ferocious.") == ["ferocious"]
    assert phrases("Reviewers described it as brash and raw.") == ["brash", "raw"]


def test_hyphenated_words_are_rebuilt_and_normalized_like_tags(phrases):
    assert phrases("It has a lo-fi production.") == ["lo fi production"]


def test_adjacent_descriptors_join_only_into_known_terms(phrases):
    assert phrases("It is an acid jazz record.") == ["acid jazz"]
    assert phrases("It is a hip hop album.") == ["hip hop"]
    assert phrases("A hip hop group from Atlanta.") == ["hip hop"]
    assert phrases("A loud punk band.") == ["loud", "punk"]


def test_a_known_join_may_use_an_ignored_word(phrases):
    assert phrases("A new wave band.") == ["new wave"]
    assert phrases("A new band.") == []


def test_without_known_terms_nothing_is_joined(phrases):
    assert phrases("It is an acid jazz record.", frozenset()) == ["acid", "jazz"]


def test_negated_nouns_give_nothing(phrases):
    assert phrases("There is no ska on the record.") == []
    assert phrases("The album lacks melodic guitars.") == []
    assert phrases("It was recorded without distorted guitars.") == []


def test_names_places_ordinals_and_ignored_words_give_nothing(phrases):
    assert phrases("It was the second album by the Canadian band.") == []
    assert phrases("It opens with the best-selling opening track.") == []
    assert phrases("His solo album.") == []


def test_only_an_adverb_right_before_the_noun_is_a_descriptor(phrases):
    assert phrases("It features jangly guitars.") == ["jangly guitars"]
    assert phrases("Crunchy guitars. Crunchy guitars again.") == ["crunchy guitars"]


def test_guitar_solo_is_a_specific_phrase(phrases):
    assert phrases("The guitar solo is long.") == ["guitar solo"]


def test_prose_only_removes_credit_lines():
    text = "Thundercat – bass (tracks 2, 10)\nThe album has a chunky groove."

    assert prose_only(text) == "The album has a chunky groove."


def test_a_long_line_with_a_dash_is_prose_not_a_credit():
    line = "The band – " + "very " * 40 + "loud"

    assert prose_only(line) == line


def test_extract_all_keeps_one_list_per_text_including_empty_ones(nlp):
    texts = ["The record has a funk groove.", "", "Elvin Jones – drums"]

    assert extract_all([prose_only(t) for t in texts], nlp, KNOWN) == [["funk groove"], [], []]
