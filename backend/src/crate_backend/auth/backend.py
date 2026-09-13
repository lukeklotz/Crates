import uuid

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy

from crate_backend.auth.manager import get_user_manager
from crate_backend.core.config import get_settings
from crate_backend.models.user import User

settings = get_settings()

cookie_transport = CookieTransport(
    cookie_name="crate_auth",
    cookie_max_age=settings.access_token_lifetime_seconds,
    cookie_secure=settings.cookie_secure,
    cookie_samesite="lax",
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.auth_secret, lifetime_seconds=settings.access_token_lifetime_seconds)


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
