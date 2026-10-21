import math

import pytest

from crate_backend.scenes.matching import classify, descriptive_terms, scene_evidence
from tests.scene_fixtures import MINIMAL, minimal_config

config = minimal_config()


def test_descriptive_terms_drops_non_positive_nondescriptive_and_years():
    terms = descriptive_terms(
        [{"name": "Shoegaze", "count": 2}],
        [
            {"name": "shoegaze", "count": 3},
            {"name": "seen live", "count": 9},
            {"name": "90s", "count": 4},
            {"name": "1991", "count": 4},
            {"name": "1990s", "count": 4},
            {"name": "noise", "count": 0},
            {"name": "loud", "count": -1},
        ],
        config,
    )
    assert terms == {"shoegaze": 3}


def test_descriptive_terms_tolerates_missing_counts():
    assert descriptive_terms([], [{"name": "shoegaze"}], config) == {}


def test_scene_evidence_weights_broad_terms():
    assert scene_evidence({"shoegaze": 3, "rock": 5}, config.scene("d"), 0.3) == pytest.approx(
        2 + 0.3 * math.log2(6)
    )


def test_classify_without_year_is_none():
    assert classify({"shoegaze": 3}, None, config) is None


def test_classify_outside_every_window_is_none():
    assert classify({"shoegaze": 3}, 1970, config) is None


def test_classify_without_scene_terms_is_none():
    assert classify({"polka": 3}, 1991, config) is None


def test_exclude_term_as_main_tag_removes_scene():
    assert classify({"shoegaze": 3, "post punk revival": 3}, 1991, config) is None


def test_exclude_term_below_main_tag_is_ignored():
    assert classify({"shoegaze": 5, "post punk revival": 1}, 1991, config).home == "d"


def test_broad_terms_alone_place_no_album():
    assert classify({"rock": 4}, 1991, config) is None


def test_broad_terms_add_evidence_to_a_specific_match():
    match = classify({"shoegaze": 2, "rock": 4}, 1991, config)
    assert match.matched_terms == ("rock", "shoegaze")
    assert match.evidence == pytest.approx(math.log2(3) + 0.3 * math.log2(5))


def test_cut_term_as_main_tag_removes_album_from_every_scene():
    assert classify({"shoegaze": 2, "black metal": 5}, 1991, config) is None


def test_cut_term_tied_for_main_tag_removes_album():
    assert classify({"shoegaze": 3, "black metal": 3}, 1991, config) is None


def test_cut_term_below_main_tag_is_ignored():
    assert classify({"shoegaze": 19, "black metal": 3}, 1991, config).home == "d"


def test_company_term_alone_places_no_album():
    assert classify({"ambient": 3}, 1995, config) is None
    assert classify({"ambient": 3, "electronic": 2}, 1995, config) is None


def test_company_term_with_another_scenes_term_places_album():
    assert classify({"ambient": 3, "shoegaze": 1}, 1995, config).home == "e"


def test_company_term_with_an_own_other_term_places_album():
    assert classify({"ambient": 3, "idm": 1}, 1995, config).home == "e"


def test_home_is_highest_evidence_and_ties_go_to_earlier_scene():
    assert classify({"shibuya kei": 1, "shoegaze": 7}, 1996, config).home == "d"
    assert classify({"shibuya kei": 3, "shoegaze": 3}, 1996, config).home == "a"


def test_open_ended_years_match_recent_albums():
    assert classify({"hauntology": 2}, 2024, config).home == "b"


def test_connector_ignores_neighbor_year_window():
    match = classify({"hauntology": 2, "krautrock": 1}, 2010, config)
    assert match.home == "b"
    assert match.connects_to == ("c",)


def test_matching_a_non_neighbor_is_not_a_connector():
    match = classify({"shoegaze": 2, "hauntology": 1}, 2008, config)
    assert match.home == "d"
    assert match.connects_to == ()


def test_min_matched_terms():
    strict = minimal_config(
        MINIMAL.replace("years = [2005]", "years = [2005]\nmin_matched_terms = 2")
    )
    assert classify({"hauntology": 2}, 2010, strict) is None


def test_requires_any():
    gated = minimal_config(
        MINIMAL.replace(
            'terms = ["Shibuya-kei"]', 'terms = ["Shibuya-kei"]\nrequires_any = ["japanese"]'
        )
    )
    assert classify({"shibuya kei": 2}, 1996, gated) is None
    assert classify({"shibuya kei": 2, "japanese": 1}, 1996, gated).home == "a"


def test_broad_term_alone_does_not_make_a_connector():
    # d's only neighbor is a; give a a broad term the album also carries.
    widened = minimal_config(
        MINIMAL.replace('terms = ["Shibuya-kei"]', 'terms = ["Shibuya-kei"]\nbroad_terms = ["pop"]')
    )
    assert classify({"shoegaze": 3, "pop": 2}, 1996, widened).connects_to == ()
    assert classify({"shoegaze": 3, "shibuya kei": 1}, 1996, widened).connects_to == ("a",)
