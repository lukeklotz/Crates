from collections.abc import AsyncIterator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.db.session import get_session
from crate_backend.models.user import User


async def get_user_db(
    session: AsyncSession = Depends(get_session),
) -> AsyncIterator[SQLAlchemyUserDatabase]:
    yield SQLAlchemyUserDatabase(session, User)
