from pydantic import BaseModel

class CartBase(BaseModel):
    user_id: int
    item_id: int
    quantity: int = 1

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int
    # item: Item # Include the item information

    class Config:
        orm_mode = True