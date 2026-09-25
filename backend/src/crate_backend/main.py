from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from crate_backend.api.routes.albums import router as albums_router
from crate_backend.api.routes.health import router as health_router
from crate_backend.api.routes.recommendations import router as recommendations_router
from crate_backend.auth.backend import auth_backend, fastapi_users
from crate_backend.auth.schemas import UserCreate, UserRead, UserUpdate
from crate_backend.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_router)
    app.include_router(albums_router)
    app.include_router(recommendations_router)
    app.include_router(
        fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"]
    )
    return app


app = create_app()
