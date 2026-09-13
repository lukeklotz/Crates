import enum
import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.recommendation import RecommendationRun
    from crate_backend.models.workspace import CanvasAlbumInstance, Workspace


class PopularityPreference(str, enum.Enum):
    NO_PREFERENCE = "no_preference"
    LESSER_KNOWN = "lesser_known"
    MODERATE = "moderate"
    WIDELY_POPULAR = "widely_popular"


class AlbumGroup(UUIDPkMixin, TimestampMixin, Base):
    """A user-created collection of albums; the primary recommendation context."""

    __tablename__ = "album_groups"

    workspace_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("workspaces.id"), index=True)
    name: Mapped[str] = mapped_column(String(200))
    # Bumped on membership or settings change; snapshotted onto each
    # RecommendationRun so results stay reproducible.
    revision: Mapped[int] = mapped_column(Integer, default=1)

    workspace: Mapped["Workspace"] = relationship(back_populates="groups")
    memberships: Mapped[list["GroupAlbumMembership"]] = relationship(
        back_populates="group", cascade="all, delete-orphan"
    )
    settings: Mapped["GroupSettings"] = relationship(
        back_populates="group", cascade="all, delete-orphan", uselist=False
    )
    recommendation_runs: Mapped[list["RecommendationRun"]] = relationship(
        back_populates="group", cascade="all, delete-orphan"
    )


class GroupAlbumMembership(UUIDPkMixin, TimestampMixin, Base):
    """Links a canvas album card to a group. Membership is search context,
    not an implicit positive rating."""

    __tablename__ = "group_album_memberships"

    group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("album_groups.id"), index=True)
    canvas_instance_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("canvas_album_instances.id"), index=True
    )
    # Denormalized from the owning workspace for direct ownership queries.
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), index=True)

    group: Mapped["AlbumGroup"] = relationship(back_populates="memberships")
    canvas_instance: Mapped["CanvasAlbumInstance"] = relationship(back_populates="memberships")

    __table_args__ = (UniqueConstraint("group_id", "canvas_instance_id"),)


class GroupSettings(UUIDPkMixin, TimestampMixin, Base):
    __tablename__ = "group_settings"

    group_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("album_groups.id"), unique=True, index=True
    )
    popularity_preference: Mapped[PopularityPreference] = mapped_column(
        Enum(PopularityPreference, native_enum=False, length=20),
        default=PopularityPreference.NO_PREFERENCE,
    )

    group: Mapped["AlbumGroup"] = relationship(back_populates="settings")
