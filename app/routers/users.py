from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from schemas import UserCreate, User
from repository import UserRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/create_user")
async def create_user(
    user: Annotated[UserCreate, Depends()]
):
    try:
        user_id = await UserRepository.create_user(user)
        return {"status": "200", "detail": "User created", "user_id": user_id}
    except HTTPException as e:
        raise e
    

@router.get("/get/{user_id}")
async def get_user(user_id: int) -> User:
    user = await UserRepository.get_user(user_id)
    return user