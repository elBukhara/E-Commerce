from fastapi import APIRouter, Depends
from typing import Annotated

from items.schemas import Category, AddCategory
from .repository import CategoryRepository

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/add_category")
async def add_category(
    category: Annotated[AddCategory, Depends()]
):
    category_id = await CategoryRepository.add_category(category)
    return {"message": "Category added", "category_id": category_id}

@router.get("/all_categories")
async def all_categories() -> list[Category]:
    categories = await CategoryRepository.get_all_categories()
    return categories
