from pydantic import BaseModel
from items.schemas import Item

# TODO: Improve the structure of the cart

class CartBase(BaseModel):
    item_id: int
    quantity: int = 1

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int
    item: Item  # Include the item details in the response

    class Config:
        orm_mode = True

class CartCreateResponse(BaseModel):
    message: str
    cart_id: int

class CartDeleteResponse(BaseModel):
    message: str
    cart_id: int
