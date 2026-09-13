import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.group import AlbumGroup, GroupAlbumMembership
    from crate_backend.models.user import User


class Workspace(UUIDPkMixin, TimestampMixin, Base):
    __tablename__ = "workspaces"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), index=True)
    name: Mapped[str] = mapped_column(String(200), default="Untitled sandbox")

    user: Mapped["User"] = relationship(back_populates="workspaces")
    canvas_instances: Mapped[list["CanvasAlbumInstance"]] = relationship(
        back_populates="workspace", cascade="all, delete-orphan"
    )
    groups: Mapped[list["AlbumGroup"]] = relationship(
        back_populates="workspace", cascade="all, delete-orphan"
    )


class CanvasAlbumInstance(UUIDPkMixin, TimestampMixin, Base):
    """A single album card placed on a workspace's canvas."""

    __tablename__ = "canvas_album_instances"

    workspace_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("workspaces.id"), index=True)
    album_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("albums.id"), index=True)
    position_x: Mapped[float] = mapped_column(default=0)
    position_y: Mapped[float] = mapped_column(default=0)
    size: Mapped[float] = mapped_column(default=176)
    rotation: Mapped[int] = mapped_column(Integer, default=0)

    workspace: Mapped["Workspace"] = relationship(back_populates="canvas_instances")
    memberships: Mapped[list["GroupAlbumMembership"]] = relationship(
        back_populates="canvas_instance", cascade="all, delete-orphan"
    )
