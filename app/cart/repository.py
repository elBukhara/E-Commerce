from sqlalchemy import select, delete
from database import async_session
from sqlalchemy.orm import selectinload

from .models import CartOrm
from .schemas import CartCreate, Cart

class CartRepository:
    @classmethod
    async def add_to_cart(cls, cart: CartCreate) -> int:
        # TODO: add/remove items in a single dictionary
        async with async_session() as session:
            cart_dict = cart.model_dump()
            
            cart = CartOrm(**cart_dict)
            session.add(cart)
            
            await session.flush()
            await session.commit()
            return cart.id
    
    @classmethod
    async def delete_cart(cls, cart_id: int):
        async with async_session() as session:
            result = await session.execute(
                delete(CartOrm)
                .where(CartOrm.id == cart_id)
                )
            
            await session.flush()
            await session.commit()
            
            return result
    
    @classmethod
    async def get_user_cart(cls, user_id: int) -> list[Cart]:
        async with async_session() as session:
            query = select(CartOrm).where(CartOrm.user_id == user_id)
            # TODO: the query should also show the information of the item
            # query = select(CartOrm).join(CartOrm.item).where(CartOrm.user_id == user_id).options(
            #     selectinload(CartOrm.item)  # Load the cart with the item
            # )            
            
            result = await session.execute(query)
            cart_items = result.scalars().all()
            return cart_items
