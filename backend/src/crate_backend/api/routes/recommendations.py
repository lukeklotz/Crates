import uuid

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.db.session import get_session
from crate_backend.models.catalog import Album
from crate_backend.recommend.overlap import recommend_by_overlap, seeds_have_terms

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


class RecommendationRequest(BaseModel):
    album_ids: list[uuid.UUID] = Field(min_length=1, max_length=50)
    limit: int = Field(default=20, ge=1, le=50)


class RecommendedAlbum(BaseModel):
    id: str
    title: str
    artist_name: str | None
    release_year: int | None
    cover_art_url: str | None
    score: float
    shared_terms: list[str]


class RecommendationResponse(BaseModel):
    results: list[RecommendedAlbum]
    reason: str | None


@router.post("", response_model=RecommendationResponse)
async def recommend(
    request: RecommendationRequest, session: AsyncSession = Depends(get_session)
) -> RecommendationResponse:
    """Albums related to a group's seed albums by shared genres and tags."""
    seed_ids = list(dict.fromkeys(request.album_ids))
    found = set(await session.scalars(select(Album.id).where(Album.id.in_(seed_ids))))
    missing = [str(album_id) for album_id in seed_ids if album_id not in found]
    if missing:
        raise HTTPException(
            status_code=404, detail={"message": "Unknown album ids", "missing": missing}
        )

    if not await seeds_have_terms(session, seed_ids):
        return RecommendationResponse(results=[], reason="seeds_have_no_terms")

    ranked = await recommend_by_overlap(session, seed_ids, request.limit)
    albums = {
        album.id: album
        for album in await session.scalars(
            select(Album).where(Album.id.in_([r.album_id for r in ranked]))
        )
    }
    return RecommendationResponse(
        results=[
            RecommendedAlbum(
                id=str(r.album_id),
                title=albums[r.album_id].title,
                artist_name=albums[r.album_id].artist_name,
                release_year=albums[r.album_id].release_year,
                cover_art_url=albums[r.album_id].cover_art_url,
                score=r.score,
                shared_terms=r.shared_terms,
            )
            for r in ranked
        ],
        reason=None,
    )
