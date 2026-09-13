import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.user import User


class Event(UUIDPkMixin, TimestampMixin, Base):
    """An append-only record of a user action. Kept separate per action type
    (group membership changes, recommendation requests, saves, dismissals,
    ratings) rather than inferred from other tables, since group membership
    itself is not a positive training label."""

    __tablename__ = "events"

    user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id"), nullable=True, index=True
    )
    event_type: Mapped[str] = mapped_column(String(50), index=True)
    payload: Mapped[dict] = mapped_column(JSONB, default=dict)

    user: Mapped["User | None"] = relationship()
