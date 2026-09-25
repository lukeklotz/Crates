from crate_backend.lastfm.match import normalize, verify_match


def test_normalize_lowercases():
    assert normalize("Kid A") == "kid a"


def test_normalize_strips_diacritics():
    assert normalize("Beyoncé") == "beyonce"


def test_normalize_strips_punctuation_and_collapses_whitespace():
    assert normalize("Rock & Roll!!  Part  One") == "rock roll part one"


def test_verify_match_true_for_exact_match():
    assert verify_match("Radiohead", "Kid A", "Radiohead", "Kid A") is True


def test_verify_match_true_ignoring_case_and_diacritics():
    assert verify_match("Beyonce", "Lemonade", "Beyoncé", "Lemonade") is True


def test_verify_match_false_for_artist_mismatch():
    assert verify_match("Radiohead", "Kid A", "Thom Yorke", "Kid A") is False


def test_verify_match_false_for_title_mismatch():
    assert verify_match("Radiohead", "Kid A", "Radiohead", "OK Computer") is False
