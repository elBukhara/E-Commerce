from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated

from .schemas import CartCreate, Cart
from .repository import CartRepository

router = APIRouter(
    prefix="/carts",
    tags=["Carts"]
)

@router.post("/add_to_cart")
async def add_to_cart(
    cart: Annotated[CartCreate, Depends()]
):
    cart_id = await CartRepository.add_to_cart(cart)
    return {"message": "Item added to cart", "cart_id": cart_id}

@router.delete("/delete_cart/{cart_id}")
async def delete_cart(cart_id: int):
    result = await CartRepository.delete_cart(cart_id)
    return {"message": "Cart was deleted", "cart_id": cart_id}

@router.get("/user_cart/{user_id}")
async def get_user_cart(user_id: int) -> list[Cart]:
    cart_items = await CartRepository.get_user_cart(user_id)
    return cart_items