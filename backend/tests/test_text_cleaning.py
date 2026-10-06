from crate_backend.recommend.text_cleaning import clean_article, merge_term_votes, normalize_term


def test_normalize_term_merges_spelling_variants():
    assert normalize_term("Post-Bop") == "post bop"
    assert normalize_term("post bop") == "post bop"
    assert normalize_term("  Drum_and_Bass ") == "drum and bass"
    assert normalize_term("R&B") == "r and b"
    # NFKC folds full-width letters into plain ones.
    assert normalize_term("ｊａｚｚ") == "jazz"


def test_merge_term_votes_keeps_largest_count_per_normalized_term():
    merged = merge_term_votes([("Post-Bop", 3), ("post bop", 5), ("jazz", 0), ("Jazz", 2)])

    assert merged == {"post bop": 5, "jazz": 2}


def test_merge_term_votes_skips_names_that_normalize_to_nothing():
    assert merge_term_votes([("-", 4), ("jazz", 1)]) == {"jazz": 1}


ARTICLE = """Kid A is the fourth studio album by Radiohead.
It features electronic textures.

== Background ==
Burned out after OK Computer, Yorke wrote on piano.

=== Recording ===
Sessions began in Paris.

== Track listing ==
Everything in Its Right Place – 4:11

=== Side two ===
Idioteque – 5:09

== Critical reception ==
Critics praised its glitch influences.

== Personnel ==
Credits adapted from liner notes.

=== Radiohead ===
Thom Yorke – vocals, piano
Nigel Godrich – production, mixing

=== Technical ===
Bob Ludwig – mastering
Stanley Donwood – artwork, cover design

== Charts & certifications ==
Number one in the UK.

== References =="""


def test_clean_article_drops_listed_sections_with_their_subsections():
    cleaned = clean_article(ARTICLE)

    assert "fourth studio album" in cleaned  # lead
    assert "Burned out" in cleaned and "Paris" in cleaned  # kept section and its subsection
    assert "glitch influences" in cleaned  # Reception is kept by default
    assert "4:11" not in cleaned and "Idioteque" not in cleaned  # dropped, with subsection
    assert "Number one" not in cleaned  # "&" heading normalizes to a dropped one
    assert "==" not in cleaned  # heading lines themselves are removed


def test_clean_article_keeps_only_musical_credits():
    cleaned = clean_article(ARTICLE)

    assert "Thom Yorke – vocals, piano" in cleaned
    assert "Nigel Godrich – production, mixing" in cleaned
    assert "Bob Ludwig" not in cleaned  # mastering only
    assert "Stanley Donwood" not in cleaned  # artwork and design only
    assert "adapted from liner notes" not in cleaned  # not a credit line


def test_credit_with_any_musical_role_is_kept():
    article = (
        "== Credits and personnel ==\n"
        "Bob Thiele – production and cover photo\n"
        "Rudy Van Gelder – engineering and mastering\n"
        "George Gray / Viceroy – cover design"
    )

    assert clean_article(article) == "Bob Thiele – production and cover photo"


def test_clean_article_can_drop_reception_sections():
    cleaned = clean_article(ARTICLE, drop_reception=True)

    assert "glitch influences" not in cleaned
    assert "Burned out" in cleaned


def test_clean_article_can_drop_personnel_sections():
    cleaned = clean_article(ARTICLE, drop_personnel=True)

    assert "Thom Yorke" not in cleaned and "Nigel Godrich" not in cleaned
    assert "Burned out" in cleaned and "glitch influences" in cleaned


def test_clean_article_of_only_dropped_sections_is_empty():
    article = "== Track listing ==\nSong – 3:00\n\n== Personnel ==\nSomeone – mastering"

    assert clean_article(article) == ""
