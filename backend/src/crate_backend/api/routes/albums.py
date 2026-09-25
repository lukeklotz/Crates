import uuid

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.auth.backend import current_active_user
from crate_backend.db.session import get_session
from crate_backend.models.catalog import Album
from crate_backend.models.event import Event
from crate_backend.models.popularity import PopularitySignal
from crate_backend.models.user import User

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


@router.post("/{album_id}/add-to-sandbox", status_code=status.HTTP_204_NO_CONTENT)
async def add_to_sandbox(
    album_id: uuid.UUID,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_session),
) -> None:
    """Count an add-to-sandbox for the album and log it as an Event. The
    count is tracked separately and does not affect Album.popularity."""
    if await session.get(Album, album_id) is None:
        raise HTTPException(status_code=404, detail="Album not found")

    # One atomic upsert, so concurrent adds neither lose counts nor collide
    # on the unique album_id when creating the row.
    await session.execute(
        insert(PopularitySignal)
        .values(id=uuid.uuid4(), album_id=album_id, sandbox_add_count=1)
        .on_conflict_do_update(
            index_elements=[PopularitySignal.album_id],
            set_={"sandbox_add_count": PopularitySignal.sandbox_add_count + 1},
        )
    )
    session.add(
        Event(
            user_id=user.id,
            event_type="album_added_to_sandbox",
            payload={"album_id": str(album_id)},
        )
    )
    await session.commit()
