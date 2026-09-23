import pytest
from sqlalchemy import or_, select

from crate_backend.models.artist_relationship import ArtistRelationship
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Artist
from crate_backend.musicbrainz.extract import (
    CandidateAlbum,
    ResolvedArtist,
    ResolvedArtistRelationship,
)
from crate_backend.musicbrainz.ingest import upsert_album, upsert_artist_relationships

pytestmark = pytest.mark.asyncio


def _candidate(**overrides) -> CandidateAlbum:
    fields = dict(
        musicbrainz_id="test-rg-1",
        title="Test Album",
        first_release_date="1959-08-17",
        artist_credit=[
            {"name": "Test Artist", "artist": {"id": "test-artist-1", "name": "Test Artist"}}
        ],
        genres=[{"id": "test-genre-1", "name": "test-jazz", "count": 5}],
        tags=[{"name": "test-modal", "count": 2}],
    )
    fields.update(overrides)
    return CandidateAlbum(**fields)


async def _album(session, mbid: str) -> Album:
    return await session.scalar(select(Album).where(Album.musicbrainz_release_group_id == mbid))


async def _artist(session, mbid: str) -> Artist:
    return await session.scalar(select(Artist).where(Artist.musicbrainz_id == mbid))


async def _edges_touching(session, artist: Artist) -> list[ArtistRelationship]:
    rows = await session.scalars(
        select(ArtistRelationship).where(
            or_(
                ArtistRelationship.artist_id == artist.id,
                ArtistRelationship.related_artist_id == artist.id,
            )
        )
    )
    return list(rows)


async def test_upsert_album_creates_album_artist_genre_and_tag(db_session):
    await upsert_album(db_session, _candidate())
    await db_session.commit()

    album = await _album(db_session, "test-rg-1")
    artist = await _artist(db_session, "test-artist-1")
    assert album.title == "Test Album"
    assert album.release_year == 1959
    assert album.artist_name == "Test Artist"
    assert album.primary_artist_id == artist.id

    genre_links = (await db_session.scalars(
        select(AlbumGenre).where(AlbumGenre.album_id == album.id)
    )).all()
    tag_links = (await db_session.scalars(
        select(AlbumTag).where(AlbumTag.album_id == album.id)
    )).all()
    assert [g.count for g in genre_links] == [5]
    assert [t.count for t in tag_links] == [2]


async def test_upsert_album_links_artist_missing_from_artist_dump(db_session):
    """The artist pass never resolves this MBID; the album still links to an
    Artist row built from the credit's embedded name."""
    candidate = _candidate(
        artist_credit=[
            {"name": "Orphan Credit", "artist": {"id": "test-artist-orphan", "name": "Orphan"}}
        ]
    )
    await upsert_album(db_session, candidate)
    await db_session.commit()

    album = await _album(db_session, "test-rg-1")
    artist = await _artist(db_session, "test-artist-orphan")
    assert album.artist_name == "Orphan Credit"
    assert album.primary_artist_id == artist.id
    assert await _edges_touching(db_session, artist) == []


async def test_upsert_album_with_empty_artist_credit(db_session):
    await upsert_album(db_session, _candidate(artist_credit=[]))
    await db_session.commit()

    album = await _album(db_session, "test-rg-1")
    assert album.artist_name is None
    assert album.primary_artist_id is None


@pytest.mark.parametrize(
    ("raw_date", "expected_year"),
    [("1994", 1994), ("1994-05", 1994), (None, None), ("not-a-date", None), ("19", None)],
)
async def test_upsert_album_release_year(db_session, raw_date, expected_year):
    await upsert_album(db_session, _candidate(first_release_date=raw_date))
    await db_session.commit()

    album = await _album(db_session, "test-rg-1")
    assert album.release_year == expected_year


async def test_upsert_album_clips_overlong_values(db_session):
    long_name = "n" * 400
    candidate = _candidate(
        title="t" * 600,
        artist_credit=[{"name": long_name, "artist": {"id": "test-artist-long", "name": long_name}}],
        tags=[{"name": "g" * 300, "count": 1}],
    )
    await upsert_album(db_session, candidate)
    await db_session.commit()

    album = await _album(db_session, "test-rg-1")
    assert len(album.title) == 500
    assert len(album.artist_name) == 255
    assert len((await _artist(db_session, "test-artist-long")).name) == 255


async def test_upsert_album_is_idempotent(db_session):
    await upsert_album(db_session, _candidate())
    await db_session.commit()
    await upsert_album(db_session, _candidate(title="Renamed"))
    await db_session.commit()

    albums = (await db_session.scalars(
        select(Album).where(Album.musicbrainz_release_group_id == "test-rg-1")
    )).all()
    assert [a.title for a in albums] == ["Renamed"]
    genre_links = (await db_session.scalars(
        select(AlbumGenre).where(AlbumGenre.album_id == albums[0].id)
    )).all()
    assert len(genre_links) == 1


def _band_seen_by(mbid: str, direction: str, related_mbid: str) -> ResolvedArtist:
    return ResolvedArtist(
        musicbrainz_id=mbid,
        name=mbid,
        relationships=[
            ResolvedArtistRelationship(
                related_artist_id=related_mbid,
                related_artist_name=related_mbid,
                relationship_type="member of band",
                direction=direction,
            )
        ],
    )


async def test_upsert_artist_relationships_stores_forward_orientation(db_session):
    # The band's own record lists its member with direction "backward".
    await upsert_artist_relationships(
        db_session, _band_seen_by("test-band", "backward", "test-member")
    )
    await db_session.commit()

    member = await _artist(db_session, "test-member")
    band = await _artist(db_session, "test-band")
    edges = await _edges_touching(db_session, band)
    assert [(e.artist_id, e.related_artist_id) for e in edges] == [(member.id, band.id)]


async def test_same_edge_from_both_artists_is_stored_once(db_session):
    await upsert_artist_relationships(
        db_session, _band_seen_by("test-band", "backward", "test-member")
    )
    await upsert_artist_relationships(
        db_session, _band_seen_by("test-member", "forward", "test-band")
    )
    await db_session.commit()

    band = await _artist(db_session, "test-band")
    assert len(await _edges_touching(db_session, band)) == 1


async def test_upsert_artist_relationships_is_idempotent(db_session):
    artist = _band_seen_by("test-band", "backward", "test-member")
    await upsert_artist_relationships(db_session, artist)
    await db_session.commit()
    await upsert_artist_relationships(db_session, artist)
    await db_session.commit()

    band = await _artist(db_session, "test-band")
    assert len(await _edges_touching(db_session, band)) == 1
