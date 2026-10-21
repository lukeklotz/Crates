from crate_backend.scenes.pool import to_pool_album
from crate_backend.scenes.profile import ProfileCounts, render_profile
from tests.scene_fixtures import minimal_config
from tests.test_scene_pool import release_group

config = minimal_config()


def _profile(records_in_catalog):
    counts = ProfileCounts(config.settings)
    for record, in_catalog in records_in_catalog:
        counts.add_release_group(record, to_pool_album(record, config), in_catalog)
    return counts


def _six_records():
    return [
        (release_group(rg_id="single", primary_type="Single"), False),
        (release_group(rg_id="comp", secondary_types=["Compilation"]), False),
        (release_group(rg_id="untagged", tags=[]), False),
        (release_group(rg_id="seen-live", tags=[{"name": "seen live", "count": 3}]), True),
        (release_group(rg_id="no-year", first_release_date=None), False),
        (release_group(rg_id="in-scene"), True),
    ]


def test_profile_funnel_counts():
    counts = _profile(_six_records())
    assert counts.release_groups == 6
    assert counts.album_primary == 5
    assert counts.allowed_types == 4
    assert counts.with_any_term == 3
    assert counts.with_descriptive_term == 2
    assert counts.no_year == 1
    assert counts.in_scene == 1
    assert counts.in_scene_in_catalog == 1
    assert counts.catalog_in_pool == 1


def test_profile_counts_live_and_artists_per_scene():
    counts = _profile(
        [
            (release_group(rg_id="studio"), False),
            (release_group(rg_id="live", secondary_types=["Live"]), False),
        ]
    )
    assert counts.scene_studio["d"] == 1
    assert counts.scene_live["d"] == 1
    assert counts.scene_artists["d"]["Test Artist"] == 2


def test_render_profile_marks_unassigned_terms():
    record = release_group(tags=[{"name": "shoegaze", "count": 3}, {"name": "polka", "count": 2}])
    report = render_profile(
        _profile([(record, False)]), config, snapshot="2026-10-18", catalog_size=25000
    )
    assert "| polka | 1 | unassigned |" in report
    assert "| shoegaze | 1 | d |" in report
    for heading in (
        "## Funnel",
        "## Scenes",
        "## Years",
        "## Terms",
        "## Artists",
        "## Existing catalog",
    ):
        assert heading in report
    for scene in config.scenes:
        assert scene.id in report


def test_render_profile_marks_deprioritized_terms():
    record = release_group(
        tags=[{"name": "shoegaze", "count": 3}, {"name": "indie rock", "count": 2}]
    )
    report = render_profile(_profile([(record, False)]), config, snapshot="x", catalog_size=0)
    assert "| indie rock | 1 | unassigned, deprioritized |" in report
