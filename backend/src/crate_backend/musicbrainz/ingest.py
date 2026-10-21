"""Idempotent upserts of parsed MusicBrainz data into Crate's catalog
tables. Rows are matched by MusicBrainz ID, so re-runs update in place."""

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.models.artist_relationship import ArtistRelationship
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Artist, Genre, Tag
from crate_backend.musicbrainz.extract import CandidateAlbum, ResolvedArtist, release_year

_TITLE_MAX = 500
_NAME_MAX = 255


# MusicBrainz caps no name lengths; one overlong value would otherwise abort
# the whole single-transaction ingest.
def _clip(value: str, max_length: int) -> str:
    return value[:max_length]


async def _get_or_create_artist(session: AsyncSession, musicbrainz_id: str, name: str) -> Artist:
    artist = await session.scalar(select(Artist).where(Artist.musicbrainz_id == musicbrainz_id))
    if artist is None:
        artist = Artist(musicbrainz_id=musicbrainz_id, name=_clip(name, _NAME_MAX))
        session.add(artist)
        await session.flush()
    elif name:
        artist.name = _clip(name, _NAME_MAX)
    return artist


async def _get_or_create_genre(session: AsyncSession, musicbrainz_id: str, name: str) -> Genre:
    genre = await session.scalar(select(Genre).where(Genre.musicbrainz_id == musicbrainz_id))
    if genre is None:
        genre = Genre(musicbrainz_id=musicbrainz_id, name=_clip(name, _NAME_MAX))
        session.add(genre)
        await session.flush()
    else:
        genre.name = _clip(name, _NAME_MAX)
    return genre


async def _get_or_create_tag(session: AsyncSession, name: str) -> Tag:
    name = _clip(name, _NAME_MAX)
    tag = await session.scalar(select(Tag).where(Tag.name == name))
    if tag is None:
        tag = Tag(name=name)
        session.add(tag)
        await session.flush()
    return tag


async def upsert_album(session: AsyncSession, candidate: CandidateAlbum) -> Album:
    primary_credit = candidate.artist_credit[0] if candidate.artist_credit else {}
    credit_name = "".join(
        (credit.get("name") or "") + (credit.get("joinphrase") or "")
        for credit in candidate.artist_credit
    )
    credited = primary_credit.get("artist") or {}
    primary_artist = None
    if credited.get("id"):
        primary_artist = await _get_or_create_artist(
            session, credited["id"], credited.get("name") or primary_credit.get("name") or ""
        )

    album = await session.scalar(
        select(Album).where(Album.musicbrainz_release_group_id == candidate.musicbrainz_id)
    )
    if album is None:
        album = Album(musicbrainz_release_group_id=candidate.musicbrainz_id)
        session.add(album)
    album.title = _clip(candidate.title, _TITLE_MAX)
    album.artist_name = _clip(credit_name, _NAME_MAX) if credit_name else None
    album.primary_artist = primary_artist
    album.release_year = release_year(candidate.first_release_date)
    await session.flush()

    kept_genre_ids = []
    for genre in candidate.genres:
        genre_row = await _get_or_create_genre(session, genre["id"], genre["name"])
        kept_genre_ids.append(genre_row.id)
        link = await session.scalar(
            select(AlbumGenre).where(
                AlbumGenre.album_id == album.id, AlbumGenre.genre_id == genre_row.id
            )
        )
        if link is None:
            link = AlbumGenre(album_id=album.id, genre_id=genre_row.id)
            session.add(link)
        link.count = genre.get("count", 0)

    kept_tag_ids = []
    for tag in candidate.tags:
        tag_row = await _get_or_create_tag(session, tag["name"])
        kept_tag_ids.append(tag_row.id)
        link = await session.scalar(
            select(AlbumTag).where(AlbumTag.album_id == album.id, AlbumTag.tag_id == tag_row.id)
        )
        if link is None:
            link = AlbumTag(album_id=album.id, tag_id=tag_row.id)
            session.add(link)
        link.count = tag.get("count", 0)

    # Drop links MusicBrainz no longer lists, so re-runs don't keep ghosts.
    await session.execute(
        delete(AlbumGenre).where(
            AlbumGenre.album_id == album.id, AlbumGenre.genre_id.not_in(kept_genre_ids)
        )
    )
    await session.execute(
        delete(AlbumTag).where(AlbumTag.album_id == album.id, AlbumTag.tag_id.not_in(kept_tag_ids))
    )
    await session.flush()
    return album


async def upsert_artist_relationships(session: AsyncSession, artist: ResolvedArtist) -> None:
    artist_row = await _get_or_create_artist(session, artist.musicbrainz_id, artist.name)
    for rel in artist.relationships:
        related_row = await _get_or_create_artist(
            session, rel.related_artist_id, rel.related_artist_name
        )
        # Normalize to MusicBrainz's forward orientation so the edge is one
        # row whether it was read from the band's record or the member's.
        subject, obj = (
            (related_row, artist_row) if rel.direction == "backward" else (artist_row, related_row)
        )
        existing = await session.scalar(
            select(ArtistRelationship).where(
                ArtistRelationship.artist_id == subject.id,
                ArtistRelationship.related_artist_id == obj.id,
                ArtistRelationship.relationship_type == rel.relationship_type,
            )
        )
        if existing is None:
            session.add(
                ArtistRelationship(
                    artist_id=subject.id,
                    related_artist_id=obj.id,
                    relationship_type=rel.relationship_type,
                )
            )
            await session.flush()
