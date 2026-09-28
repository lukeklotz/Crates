"""Import every model module so Base.metadata is fully populated for
Alembic autogeneration and for creating tables in tests."""

from crate_backend.models.album_text import AlbumText
from crate_backend.models.artist_relationship import ArtistRelationship
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Artist, Genre, Tag
from crate_backend.models.event import Event
from crate_backend.models.group import AlbumGroup, GroupAlbumMembership, GroupSettings
from crate_backend.models.popularity import PopularitySignal
from crate_backend.models.rating import Descriptor, Rating
from crate_backend.models.recommendation import ModelVersion, Recommendation, RecommendationRun
from crate_backend.models.user import User
from crate_backend.models.workspace import CanvasAlbumInstance, Workspace

__all__ = [
    "Album",
    "AlbumGenre",
    "AlbumGroup",
    "AlbumTag",
    "AlbumText",
    "Artist",
    "ArtistRelationship",
    "CanvasAlbumInstance",
    "Descriptor",
    "Event",
    "Genre",
    "GroupAlbumMembership",
    "GroupSettings",
    "ModelVersion",
    "PopularitySignal",
    "Rating",
    "Recommendation",
    "RecommendationRun",
    "Tag",
    "User",
    "Workspace",
]
