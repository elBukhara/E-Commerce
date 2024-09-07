from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from .schemas import UserCreate, User, CreateUserResponse
from .repository import UserRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/create_user")
async def create_user(
    user: Annotated[UserCreate, Depends()]
) -> CreateUserResponse:
    
    response = await UserRepository.create_user(user)
    return response    

@router.get("/get/{user_id}")
async def get_user(user_id: int) -> User:
    user = await UserRepository.get_user(user_id)
    return user