from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    username: str
    email: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        orm_mode = True

class CreateUserResponse(BaseModel):
    detail: str
    user_id: int