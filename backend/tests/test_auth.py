import pytest
from httpx import ASGITransport, AsyncClient

from crate_backend.db.session import get_session
from crate_backend.main import app

pytestmark = pytest.mark.asyncio


@pytest.fixture
def client(db_session):
    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session
    transport = ASGITransport(app=app)
    try:
        yield AsyncClient(transport=transport, base_url="http://test")
    finally:
        app.dependency_overrides.pop(get_session, None)


async def test_register_login_and_read_self(client):
    async with client as ac:
        register_response = await ac.post(
            "/auth/register",
            json={"email": "listener@example.com", "password": "correct horse battery staple"},
        )
        assert register_response.status_code == 201

        login_response = await ac.post(
            "/auth/login",
            data={"username": "listener@example.com", "password": "correct horse battery staple"},
        )
        assert login_response.status_code == 204
        assert "crate_auth" in login_response.cookies

        me_response = await ac.get("/users/me")
        assert me_response.status_code == 200
        assert me_response.json()["email"] == "listener@example.com"


async def test_protected_route_requires_auth(client):
    async with client as ac:
        response = await ac.get("/users/me")
        assert response.status_code == 401


async def test_login_rejects_wrong_password(client):
    async with client as ac:
        await ac.post(
            "/auth/register",
            json={"email": "listener2@example.com", "password": "correct horse battery staple"},
        )
        response = await ac.post(
            "/auth/login",
            data={"username": "listener2@example.com", "password": "wrong password"},
        )
        assert response.status_code == 400
