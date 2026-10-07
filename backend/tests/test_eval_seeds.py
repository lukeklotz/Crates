import uuid
from collections import Counter
from dataclasses import replace

import pytest

from crate_backend.evaluation.seeds import (
    GENRE_BUCKETS,
    SeedCandidate,
    broad_genre,
    load_seed_candidates,
    propose_seeds,
    write_proposal,
)
from crate_backend.evaluation.store import Seed
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag

POPULARITY = {"top": 0.9, "upper-mid": 0.6, "lower-mid": 0.3, "bottom": 0.1}
# One real-looking top genre per broad genre.
GENRE_NAMES = {
    "jazz": "Post-Bop",
    "rock": "Rock",
    "electronic": "Ambient",
    "hip hop": "Hip-Hop",
    "metal": "Black Metal",
    "folk": "Folk",
    "pop": "Pop",
    "classical": "Classical",
    "soul/r&b": "Soul",
    "world": "Reggae",
}


def cand(i: int, popularity: float | None, genre: str, *, n_terms=8, artist=None):
    key = f"{genre}-{popularity}-{i}"
    return SeedCandidate(
        album_id=uuid.uuid5(uuid.NAMESPACE_URL, key),
        title=f"Album {key}",
        artist_name=artist or f"Artist {key}",
        release_year=2000,
        popularity=popularity,
        top_genre=genre,
        n_terms=n_terms,
    )


def full_catalog() -> list[SeedCandidate]:
    return [
        cand(i, popularity, name)
        for popularity in POPULARITY.values()
        for name in GENRE_NAMES.values()
        for i in range(3)
    ]


@pytest.mark.parametrize(
    ("name", "bucket"),
    [
        ("Post-Bop", "jazz"),
        ("Avant-Garde Jazz", "jazz"),
        ("Heavy Metal", "metal"),
        ("Metalcore", "metal"),
        ("Trip Hop", "electronic"),
        ("Hip-Hop", "hip hop"),
        ("Gangsta Rap", "hip hop"),
        ("Dark Ambient", "electronic"),
        ("Dubstep", "electronic"),
        ("Contemporary R&B", "soul/r&b"),
        ("Blues", "soul/r&b"),
        ("Blues Rock", "rock"),
        ("Folk Rock", "rock"),
        ("Country", "folk"),
        ("Synth-Pop", "pop"),
        ("Dance-Pop", "pop"),
        ("K-Pop", "world"),
        ("Reggae", "world"),
        ("Modern Classical", "classical"),
        ("Post-Punk", "rock"),
        ("Experimental", None),
        ("Christmas Music", None),
    ],
)
def test_broad_genre(name, bucket):
    assert broad_genre(name) == bucket


def test_proposes_25_seeds_split_7_6_6_6_by_quartile():
    seeds = propose_seeds(full_catalog())

    assert len(seeds) == 25
    assert Counter(s.popularity_quartile for s in seeds) == {
        "top": 7,
        "upper-mid": 6,
        "lower-mid": 6,
        "bottom": 6,
    }


def test_spreads_seeds_across_all_ten_genres():
    by_id = {c.album_id: c for c in full_catalog()}

    counts = Counter(
        broad_genre(by_id[s.album_id].top_genre) for s in propose_seeds(full_catalog())
    )

    assert set(counts) == set(GENRE_BUCKETS)
    assert set(counts.values()) == {2, 3}


def test_proposal_is_deterministic_whatever_the_input_order():
    catalog = full_catalog()

    assert propose_seeds(catalog) == propose_seeds(list(reversed(catalog)))


def test_skips_few_terms_unknown_popularity_and_unmapped_genres():
    good = cand(0, 0.9, "Jazz")

    seeds = propose_seeds(
        [
            good,
            cand(1, 0.9, "Jazz", n_terms=4),
            replace(cand(2, 0.9, "Jazz"), popularity=None),
            cand(3, 0.9, "Experimental"),
            replace(cand(4, 0.9, "Jazz"), top_genre=None),
        ]
    )

    assert seeds == [Seed(good.album_id, good.title, good.artist_name, "top")]


def test_fills_a_quartile_from_other_genres_when_one_runs_out():
    catalog = [cand(i, 0.9, "Jazz") for i in range(10)] + [cand(0, 0.9, "Rock")]

    seeds = propose_seeds(catalog)

    assert len(seeds) == 7
    assert sum("Rock" in s.title for s in seeds) == 1


def test_never_picks_two_albums_by_the_same_artist():
    catalog = [cand(i, 0.9, "Jazz", artist="Same Artist") for i in range(5)]
    catalog += [cand(i, 0.9, "Rock", artist="same artist") for i in range(5)]
    catalog += [cand(i, 0.9, "Pop") for i in range(5)]

    seeds = propose_seeds(catalog)

    assert sum(s.artist_name.casefold() == "same artist" for s in seeds) == 1


def test_write_proposal_refuses_to_overwrite_without_force(tmp_path):
    path = tmp_path / "seeds.json"
    path.write_text("[]\n")
    seeds = propose_seeds(full_catalog())

    with pytest.raises(FileExistsError):
        write_proposal(seeds, path, force=False)
    assert path.read_text() == "[]\n"

    write_proposal(seeds, path, force=True)
    assert path.read_text() != "[]\n"


async def test_load_seed_candidates_merges_terms_and_picks_top_genre(db_session):
    album = Album(
        title="Zzfixture Seed Album",
        artist_name="Fixture Artist",
        popularity=0.8,
        release_year=1999,
    )
    low = Genre(musicbrainz_id=str(uuid.uuid4()), name="Zzfixture-Seed Low Genre")
    high = Genre(musicbrainz_id=str(uuid.uuid4()), name="Zzfixture-Seed High Genre")
    same_as_high = Tag(name="zzfixture seed high genre")
    other = Tag(name="zzfixture seed other tag")
    db_session.add_all([album, low, high, same_as_high, other])
    await db_session.flush()
    db_session.add_all(
        [
            AlbumGenre(album_id=album.id, genre_id=low.id, count=1),
            AlbumGenre(album_id=album.id, genre_id=high.id, count=4),
            AlbumTag(album_id=album.id, tag_id=same_as_high.id, count=9),
            AlbumTag(album_id=album.id, tag_id=other.id, count=2),
        ]
    )
    await db_session.flush()

    [candidate] = await load_seed_candidates(db_session, only=[album.id])

    assert candidate == SeedCandidate(
        album_id=album.id,
        title="Zzfixture Seed Album",
        artist_name="Fixture Artist",
        release_year=1999,
        popularity=0.8,
        top_genre="Zzfixture-Seed High Genre",
        n_terms=3,
    )
