import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import NullPool

from crate_backend.core.config import get_settings


@pytest_asyncio.fixture
async def db_session():
    """A session bound to a connection whose outer transaction is always
    rolled back, so integration tests never leave data behind in the local
    Postgres database.

    Uses a fresh, unpooled engine per test: pytest-asyncio gives each test
    function its own event loop, and pooled asyncpg connections can't be
    reused across loops.
    """
    engine = create_async_engine(get_settings().database_url, poolclass=NullPool)
    try:
        async with engine.connect() as connection:
            transaction = await connection.begin()
            session = AsyncSession(
                bind=connection, expire_on_commit=False, join_transaction_mode="create_savepoint"
            )
            try:
                yield session
            finally:
                await session.close()
                await transaction.rollback()
    finally:
        await engine.dispose()
