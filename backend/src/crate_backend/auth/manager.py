import uuid
from collections.abc import AsyncIterator

from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from crate_backend.auth.db import get_user_db
from crate_backend.core.config import get_settings
from crate_backend.models.user import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    @property
    def reset_password_token_secret(self) -> str:
        return get_settings().auth_secret

    @property
    def verification_token_secret(self) -> str:
        return get_settings().auth_secret


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
) -> AsyncIterator[UserManager]:
    yield UserManager(user_db)
