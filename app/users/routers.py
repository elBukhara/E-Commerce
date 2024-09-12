from fastapi import APIRouter

from auth.core.fastapi_users import fastapi_users
from auth.schemas.user import UserRead, UserUpdate
from .schemas import User
from .repository import UserRepository


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/get/{user_id}")
async def get_user(user_id: int) -> User:
    user = await UserRepository.get_user(user_id)
    return user

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate
    ),
)