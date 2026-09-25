import uuid

import pytest
from sqlalchemy import select

from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.recommend.overlap import recommend_by_overlap, seeds_have_terms

pytestmark = pytest.mark.asyncio


def terms(*names: str) -> list[str]:
    """Fixture terms no real catalog album can have."""
    return [f"zzfixture-{name}" for name in names]


async def _genre(db_session, name: str) -> Genre:
    genre = await db_session.scalar(select(Genre).where(Genre.name == name))
    if genre is None:
        genre = Genre(musicbrainz_id=str(uuid.uuid4()), name=name)
        db_session.add(genre)
        await db_session.flush()
    return genre


async def _tag(db_session, name: str) -> Tag:
    tag = await db_session.scalar(select(Tag).where(Tag.name == name))
    if tag is None:
        tag = Tag(name=name)
        db_session.add(tag)
        await db_session.flush()
    return tag


async def _album(db_session, title: str, tags=(), genres=()) -> Album:
    album = Album(title=title, artist_name="Fixture Artist")
    db_session.add(album)
    await db_session.flush()
    for name in genres:
        db_session.add(AlbumGenre(album_id=album.id, genre_id=(await _genre(db_session, name)).id))
    for name in tags:
        db_session.add(AlbumTag(album_id=album.id, tag_id=(await _tag(db_session, name)).id))
    await db_session.flush()
    return album


async def _recommend(db_session, *seeds: Album, limit: int = 20):
    return await recommend_by_overlap(db_session, [s.id for s in seeds], limit)


async def test_small_overlap_outranks_heavily_tagged_album(db_session):
    seed = await _album(db_session, "Seed", tags=terms("a", "b", "c", "d", "e"))
    focused = await _album(db_session, "Focused", tags=terms("a", "b", "c", "d"))
    heavy = await _album(
        db_session, "Heavy", tags=terms("a", "b", "c", "d", *[f"x{i}" for i in range(36)])
    )

    results = await _recommend(db_session, seed)

    assert [r.album_id for r in results] == [focused.id, heavy.id]
    assert results[0].score == pytest.approx(4 / 5)
    assert results[1].score == pytest.approx(4 / 41)


async def test_seeds_are_never_recommended(db_session):
    first = await _album(db_session, "First Seed", tags=terms("a", "b"))
    second = await _album(db_session, "Second Seed", tags=terms("a", "b"))
    other = await _album(db_session, "Other", tags=terms("a"))

    results = await _recommend(db_session, first, second)

    assert [r.album_id for r in results] == [other.id]


async def test_group_score_sums_each_seeds_similarity(db_session):
    first = await _album(db_session, "First Seed", tags=terms("a", "b"))
    second = await _album(db_session, "Second Seed", tags=terms("c", "d"))
    matches_one_fully = await _album(db_session, "One", tags=terms("a", "b"))
    bridges_both = await _album(db_session, "Both", tags=terms("a", "c"))

    results = await _recommend(db_session, first, second)

    assert [r.album_id for r in results] == [matches_one_fully.id, bridges_both.id]
    assert results[0].score == pytest.approx(1.0)
    assert results[1].score == pytest.approx(1 / 3 + 1 / 3)


async def test_untagged_seed_does_not_block_tagged_seed(db_session):
    tagged = await _album(db_session, "Tagged Seed", tags=terms("a", "b"))
    untagged = await _album(db_session, "Untagged Seed")
    match = await _album(db_session, "Match", tags=terms("a", "b"))

    results = await _recommend(db_session, tagged, untagged)

    assert [r.album_id for r in results] == [match.id]
    assert results[0].score == pytest.approx(1.0)


async def test_genre_and_tag_with_the_same_name_count_once(db_session):
    seed = await _album(
        db_session, "Seed", genres=terms("rock"), tags=["ZZFIXTURE-ROCK", *terms("x")]
    )
    candidate = await _album(db_session, "Candidate", tags=terms("rock"))

    [result] = await _recommend(db_session, seed)

    assert result.album_id == candidate.id
    assert result.score == pytest.approx(1 / 2)
    assert result.shared_terms == terms("rock")


async def test_ties_prefer_more_shared_terms_then_title(db_session):
    seed = await _album(db_session, "Seed", tags=terms("a", "b", "c", "d"))
    beta = await _album(db_session, "Beta", tags=terms("a", "b"))
    alpha = await _album(db_session, "Alpha", tags=terms("c", "d"))
    many = await _album(db_session, "Many", tags=terms("a", "b", "c", "d", "e", "f", "g", "h"))

    results = await _recommend(db_session, seed)

    assert [r.score for r in results] == [0.5, 0.5, 0.5]
    assert [r.album_id for r in results] == [many.id, alpha.id, beta.id]


async def test_shared_terms_ordered_by_seed_count_then_name(db_session):
    first = await _album(db_session, "First Seed", tags=terms("a", "b"))
    second = await _album(db_session, "Second Seed", tags=terms("b", "c"))
    await _album(db_session, "Candidate", tags=terms("a", "b", "c", "z"))

    [result] = await _recommend(db_session, first, second)

    assert result.shared_terms == terms("b", "a", "c")


async def test_limit_caps_results(db_session):
    seed = await _album(db_session, "Seed", tags=terms("a"))
    for i in range(5):
        await _album(db_session, f"Candidate {i}", tags=terms("a"))

    assert len(await _recommend(db_session, seed, limit=3)) == 3


async def test_no_shared_terms_means_no_results(db_session):
    seed = await _album(db_session, "Seed", tags=terms("lonely"))

    assert await _recommend(db_session, seed) == []


async def test_seeds_have_terms(db_session):
    untagged = await _album(db_session, "Untagged")
    genre_only = await _album(db_session, "Genre Only", genres=terms("g"))
    tag_only = await _album(db_session, "Tag Only", tags=terms("t"))

    assert await seeds_have_terms(db_session, [untagged.id]) is False
    assert await seeds_have_terms(db_session, [untagged.id, genre_only.id]) is True
    assert await seeds_have_terms(db_session, [tag_only.id]) is True
