"""Import every model module so Base.metadata is fully populated for
Alembic autogeneration and for creating tables in tests."""

from crate_backend.models.catalog import Album, Artist
from crate_backend.models.event import Event
from crate_backend.models.group import AlbumGroup, GroupAlbumMembership, GroupSettings
from crate_backend.models.rating import Descriptor, Rating
from crate_backend.models.recommendation import ModelVersion, Recommendation, RecommendationRun
from crate_backend.models.user import User
from crate_backend.models.workspace import CanvasAlbumInstance, Workspace

__all__ = [
    "Album",
    "AlbumGroup",
    "Artist",
    "CanvasAlbumInstance",
    "Descriptor",
    "Event",
    "GroupAlbumMembership",
    "GroupSettings",
    "ModelVersion",
    "Rating",
    "Recommendation",
    "RecommendationRun",
    "User",
    "Workspace",
]
