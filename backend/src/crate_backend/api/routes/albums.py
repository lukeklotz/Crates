from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.db.session import get_session
from crate_backend.models.catalog import Album

router = APIRouter(prefix="/albums", tags=["albums"])

MAX_RESULTS = 24


class AlbumSearchResult(BaseModel):
    id: str
    title: str
    artist_name: str | None
    release_year: int | None
    cover_art_url: str | None


@router.get("/search", response_model=list[AlbumSearchResult])
async def search_albums(
    q: str = Query(..., max_length=200),
    session: AsyncSession = Depends(get_session),
) -> list[AlbumSearchResult]:
    term = q.strip()
    if not term:
        return []

    pattern = f"%{term}%"
    stmt = (
        select(Album)
        .where(Album.title.ilike(pattern) | Album.artist_name.ilike(pattern))
        .order_by(Album.title)
        .limit(MAX_RESULTS)
    )
    albums = (await session.scalars(stmt)).all()
    return [
        AlbumSearchResult(
            id=str(album.id),
            title=album.title,
            artist_name=album.artist_name,
            release_year=album.release_year,
            cover_art_url=album.cover_art_url,
        )
        for album in albums
    ]
