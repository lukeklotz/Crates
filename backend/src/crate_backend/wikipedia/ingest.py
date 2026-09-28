"""Idempotent sync of one album's Wikipedia AlbumText row, keyed by
(album_id, source) so re-runs update in place."""

import re
import uuid
from datetime import UTC, datetime

import httpx
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album
from crate_backend.wikipedia.client import ArticleResult, FetchOutcome, fetch_article

# AlbumText.article_title's column length.
_MAX_TITLE_LENGTH = 500
_DISAMBIGUATOR = re.compile(r"\s*\([^)]*\)\s*$")


async def get_or_create_text(session: AsyncSession, album_id: uuid.UUID) -> AlbumText:
    row = await session.scalar(
        select(AlbumText).where(
            AlbumText.album_id == album_id, AlbumText.source == WIKIPEDIA_SOURCE
        )
    )
    if row is None:
        row = AlbumText(album_id=album_id, source=WIKIPEDIA_SOURCE)
        session.add(row)
        await session.flush()
    return row


def _bare(name: str) -> str:
    return _DISAMBIGUATOR.sub("", name).strip().casefold()


def _redirected_to_artist(album: Album, result: ArticleResult) -> bool:
    """Minor albums' Wikipedia links often redirect to the band's article or
    discography, which would give the album its artist's biography."""
    if not result.redirected or not album.artist_name or not result.title:
        return False
    artist = _bare(album.artist_name)
    return _bare(result.title) in {artist, f"{artist} discography"}


async def sync_album_text(
    session: AsyncSession,
    client: httpx.AsyncClient,
    album: Album,
    enwiki_titles: dict[str, str | None],
) -> AlbumText:
    """Fetch `album`'s English Wikipedia article and record it.

    `enwiki_titles` holds resolve_enwiki_titles answers. Wikidata's English
    sitelink is preferred over MusicBrainz's direct Wikipedia link. An
    album whose Wikidata id is absent from `enwiki_titles` (unresolved) is
    not fetched and keeps fetched_at null, as does a failed fetch.
    """
    row = await get_or_create_text(session, album.id)
    if album.wikidata_id and album.wikidata_id not in enwiki_titles:
        return row

    title = enwiki_titles.get(album.wikidata_id) if album.wikidata_id else None
    title = title or album.wikipedia_title
    result = await fetch_article(client, title) if title else ArticleResult(FetchOutcome.MISSING)
    if result.outcome is FetchOutcome.FAILED:
        return row

    row.article_title = result.title[:_MAX_TITLE_LENGTH] if result.title else None
    if result.outcome is FetchOutcome.FOUND and not _redirected_to_artist(album, result):
        row.revision_id = result.revision_id
        row.text = result.text
    else:
        row.revision_id = None
        row.text = None
    row.fetched_at = datetime.now(UTC)
    await session.flush()
    return row
