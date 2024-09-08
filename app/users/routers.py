from fastapi import APIRouter

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