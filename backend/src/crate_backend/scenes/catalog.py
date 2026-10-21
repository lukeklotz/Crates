"""Catalog albums with their scene matches, for the batch selector and the
coverage and path-reach reports.

Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
"""

import uuid
from collections import defaultdict
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Artist, Genre, Tag
from crate_backend.scenes.config import SceneConfig
from crate_backend.scenes.matching import SceneMatch, classify, descriptive_terms


@dataclass(frozen=True)
class CatalogAlbum:
    album_id: uuid.UUID
    musicbrainz_id: str | None
    title: str
    artist_name: str | None
    # The primary artist's MusicBrainz ID, comparable with PoolAlbum's.
    primary_artist_id: str | None
    year: int | None
    terms: dict[str, int]
    match: SceneMatch | None
    has_text: bool
    popularity: float | None


async def load_catalog_albums(session: AsyncSession, config: SceneConfig) -> list[CatalogAlbum]:
    """Every catalog album, in four bulk queries rather than one per album."""
    albums = (
        await session.execute(
            select(
                Album.id,
                Album.musicbrainz_release_group_id,
                Album.title,
                Album.artist_name,
                Artist.musicbrainz_id,
                Album.release_year,
                Album.popularity,
            ).outerjoin(Artist, Album.primary_artist_id == Artist.id)
        )
    ).all()

    genres: dict[uuid.UUID, list[dict]] = defaultdict(list)
    for album_id, name, count in await session.execute(
        select(AlbumGenre.album_id, Genre.name, AlbumGenre.count).join(
            Genre, AlbumGenre.genre_id == Genre.id
        )
    ):
        genres[album_id].append({"name": name, "count": count})
    tags: dict[uuid.UUID, list[dict]] = defaultdict(list)
    for album_id, name, count in await session.execute(
        select(AlbumTag.album_id, Tag.name, AlbumTag.count).join(Tag, AlbumTag.tag_id == Tag.id)
    ):
        tags[album_id].append({"name": name, "count": count})
    with_text = set(
        (
            await session.scalars(
                select(AlbumText.album_id).where(
                    AlbumText.source == WIKIPEDIA_SOURCE, AlbumText.text.is_not(None)
                )
            )
        ).all()
    )

    result = []
    for album_id, mbid, title, artist_name, artist_mbid, year, popularity in albums:
        terms = descriptive_terms(genres.get(album_id, []), tags.get(album_id, []), config)
        result.append(
            CatalogAlbum(
                album_id=album_id,
                musicbrainz_id=mbid,
                title=title,
                artist_name=artist_name,
                primary_artist_id=artist_mbid,
                year=year,
                terms=terms,
                match=classify(terms, year, config),
                has_text=album_id in with_text,
                popularity=popularity,
            )
        )
    return result
