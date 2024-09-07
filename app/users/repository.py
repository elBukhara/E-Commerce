from fastapi import HTTPException
from sqlalchemy import select
from database import async_session

from .models import UserOrm
from .schemas import UserCreate, User, CreateUserResponse

class UserRepository:
    @classmethod
    async def create_user(cls, user: UserCreate) -> int:
        async with async_session() as session:
            # Check if the username is already taken
            query = select(UserOrm).where(UserOrm.username == user.username)
            result = await session.execute(query)
            existing_user = result.scalar_one_or_none()
            
            if existing_user:
                # If the username exists, raise an exception
                raise HTTPException(status_code=400, detail="Username already taken. Please choose another one.")
            else:            
                user_dict = user.model_dump()
                user = UserOrm(**user_dict)
                session.add(user)                
                await session.flush()
                await session.commit()
                
                return CreateUserResponse(detail="User was successfully created.", user_id=user.id) 
    
    @classmethod
    async def get_user(cls, user_id: int) -> User:
        async with async_session() as session:
            user = await session.get(UserOrm, user_id)
            return user