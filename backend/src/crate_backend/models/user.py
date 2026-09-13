from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from crate_backend.models.rating import Descriptor, Rating
    from crate_backend.models.workspace import Workspace


class User(SQLAlchemyBaseUserTableUUID, TimestampMixin, Base):
    """id, email, hashed_password, is_active, is_superuser, is_verified come
    from fastapi-users' base table mixin."""

    __tablename__ = "users"

    workspaces: Mapped[list["Workspace"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    ratings: Mapped[list["Rating"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    descriptors: Mapped[list["Descriptor"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
