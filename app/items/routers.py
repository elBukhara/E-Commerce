from fastapi import APIRouter, Depends
from typing import Annotated

from .schemas import AddItem, Item
from .repository import ItemRepository

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post("/add_item")
async def add_item(
    item: Annotated[AddItem, Depends()]
):
    item_id = await ItemRepository.add_item(item)
    return {"message": "Item added" ,"item_id": item_id}  

@router.delete("/delete/{item_id}")
async def delete_item(item_id: int):
    await ItemRepository.delete_item(item_id)
    return {"message": "Item deleted"}

@router.get("/all_items")
async def all_items() -> list[Item]:
    items = await ItemRepository.get_all_items()
    return items

@router.get("/get/{item_id}")
async def get_item(item_id: int) -> Item:
    item = await ItemRepository.get_item(item_id)
    return item