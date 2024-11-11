from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated

from auth.core.fastapi_users import current_user
from users.models import UserOrm
from .schemas import CartCreate, Cart
from .repository import CartRepository

router = APIRouter(
    prefix="/carts",
    tags=["Carts"]
)

# TODO: check 'is_authorized' in functions => which will remove the unused user_id 

@router.get("/user_cart")
async def get_user_cart(
    user: Annotated[UserOrm, Depends(current_user)]
) -> list[Cart]:
    
    cart_items = await CartRepository.get_user_cart(user_id=user.id)
    return cart_items


@router.post("/add_to_cart")
async def add_to_cart(
    cart: Annotated[CartCreate, Depends()],
    user: Annotated[UserOrm, Depends(current_user)]
):
    response = await CartRepository.add_to_cart(user_id=user.id, cart=cart)
    return response


@router.delete("/delete_cart/{cart_id}")
async def delete_cart(
    cart_id: int,
    user: Annotated[UserOrm, Depends(current_user)]
):
    response = await CartRepository.delete_cart(user_id=user.id, cart_id=cart_id)
    return response


@router.put("/decrement_quantity/{cart_id}")
async def decrement_quantity_of_item_in_cart(
    cart_id: int,
    user: Annotated[UserOrm, Depends(current_user)]
):
    response = await CartRepository.decrement_quantity_of_item_in_cart(user_id=user.id, cart_id=cart_id)
    return response