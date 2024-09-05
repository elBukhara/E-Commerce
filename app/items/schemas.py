from pydantic import BaseModel
from typing import Optional

class AddCategory(BaseModel):
    name: str

class Category(AddCategory):
    id: int

    class Config:
        orm_mode = True

class AddItem(BaseModel):
    name: str
    description: Optional[str] = None
    category_id: int  # Include category_id to associate with a category

class Item(AddItem):
    id: int
    category: Optional[Category]  # Include the category information

    class Config:
        orm_mode = True
