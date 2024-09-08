from fastapi import APIRouter

from .manager import fastapi_users
from .auth import auth_backend
from .schemas import UserRead, UserCreate, UserUpdate

router = APIRouter()

# Registration route
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

# TODO: Fix login authentication
# Login route
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

# # Current user route
# router.include_router(
#     fastapi_users.get_users_router(UserRead, user_update_schema=UserUpdate),
#     prefix="/users",
#     tags=["Users"],
# )
