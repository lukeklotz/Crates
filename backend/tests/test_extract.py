from crate_backend.musicbrainz.extract import (
    artist_ids_in_credits,
    filter_and_rank_release_groups,
    resolve_artists,
)


def _release_group(
    *,
    rg_id="test-rg-1",
    primary_type="Album",
    secondary_types=None,
    genres=None,
    tags=None,
    artist_credit=None,
    first_release_date="2020-01-01",
):
    return {
        "id": rg_id,
        "title": "Test Album",
        "primary-type": primary_type,
        "secondary-types": secondary_types or [],
        "genres": [{"id": "test-genre-1", "name": "test-jazz", "count": 2}]
        if genres is None
        else genres,
        "tags": [{"name": "test-smooth", "count": 1}] if tags is None else tags,
        "artist-credit": [
            {"name": "Test Artist", "artist": {"id": "test-artist-1", "name": "Test Artist"}}
        ]
        if artist_credit is None
        else artist_credit,
        "first-release-date": first_release_date,
    }


def test_filter_excludes_non_album_primary_type():
    assert filter_and_rank_release_groups([_release_group(primary_type="Single")], 10) == []


def test_filter_excludes_null_primary_type():
    assert filter_and_rank_release_groups([_release_group(primary_type=None)], 10) == []


def test_filter_excludes_disallowed_secondary_type():
    records = [_release_group(secondary_types=["Compilation"])]
    assert filter_and_rank_release_groups(records, 10) == []


def test_filter_excludes_live_combined_with_disallowed_type():
    records = [_release_group(secondary_types=["Live", "Compilation"])]
    assert filter_and_rank_release_groups(records, 10) == []


def test_filter_allows_live_secondary_type():
    records = [_release_group(secondary_types=["Live"])]
    assert len(filter_and_rank_release_groups(records, 10)) == 1


def test_filter_excludes_records_with_no_genre_or_tag():
    assert filter_and_rank_release_groups([_release_group(genres=[], tags=[])], 10) == []


def test_filter_keeps_records_with_genre_but_no_tag():
    assert len(filter_and_rank_release_groups([_release_group(tags=[])], 10)) == 1


def test_filter_ranks_by_tag_vote_total_and_caps_at_target():
    records = [
        _release_group(rg_id="test-low", tags=[{"name": "x", "count": 1}]),
        _release_group(rg_id="test-high", tags=[{"name": "x", "count": 100}]),
        _release_group(rg_id="test-mid", tags=[{"name": "x", "count": 10}]),
    ]
    result = filter_and_rank_release_groups(iter(records), target_size=2)
    assert [c.musicbrainz_id for c in result] == ["test-high", "test-mid"]


def test_filter_normalizes_empty_release_date_to_none():
    result = filter_and_rank_release_groups([_release_group(first_release_date="")], 10)
    assert result[0].first_release_date is None


def test_artist_ids_in_credits_collects_unique_ids():
    credit = [{"name": "A", "artist": {"id": "test-artist-1", "name": "A"}}]
    candidates = filter_and_rank_release_groups(
        [
            _release_group(rg_id="test-rg-1", artist_credit=credit),
            _release_group(rg_id="test-rg-2", artist_credit=credit),
        ],
        10,
    )
    assert artist_ids_in_credits(candidates) == {"test-artist-1"}


def test_resolve_artists_filters_to_allowlisted_relationship_types():
    records = [
        {
            "id": "test-artist-1",
            "name": "Test Artist",
            "relations": [
                {
                    "type": "member of band",
                    "direction": "forward",
                    "target-type": "artist",
                    "artist": {"id": "test-artist-2", "name": "Test Band"},
                },
                {
                    "type": "performer",
                    "direction": "forward",
                    "target-type": "recording",
                    "recording": {"id": "test-recording-1", "title": "Dropped"},
                },
                {
                    "type": "wikidata",
                    "direction": "forward",
                    "target-type": "url",
                    "url": {"resource": "https://www.wikidata.org/wiki/Q1"},
                },
            ],
        }
    ]
    resolved = resolve_artists(records, wanted_ids={"test-artist-1"})
    relationships = resolved["test-artist-1"].relationships
    assert [(r.related_artist_id, r.relationship_type, r.direction) for r in relationships] == [
        ("test-artist-2", "member of band", "forward")
    ]


def test_resolve_artists_ignores_records_not_in_wanted_ids():
    records = [
        {"id": "test-artist-1", "name": "Wanted", "relations": []},
        {"id": "test-artist-2", "name": "Not Wanted", "relations": []},
    ]
    assert set(resolve_artists(records, {"test-artist-1"})) == {"test-artist-1"}


def test_resolve_artists_omits_ids_missing_from_the_dump():
    records = [{"id": "test-artist-1", "name": "Present", "relations": []}]
    resolved = resolve_artists(records, {"test-artist-1", "test-artist-orphan"})
    assert set(resolved) == {"test-artist-1"}
