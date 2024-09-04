from pydantic import BaseModel
from typing import Optional

class AddItem(BaseModel):
    name: str
    description: Optional[str] = None

class Item(AddItem):
    id: int

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class CartBase(BaseModel):
    user_id: int
    item_id: int
    quantity: int = 1

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int

    class Config:
        orm_mode = True