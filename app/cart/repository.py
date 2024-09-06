from sqlalchemy import select, delete, update
from database import async_session
from sqlalchemy.orm import selectinload

from items.models import ItemOrm
from .models import CartOrm
from .schemas import CartCreate, Cart

class CartRepository:
    @classmethod
    async def add_to_cart(cls, cart: CartCreate) -> int:
        # TODO: add/remove items in a single dictionary
        async with async_session() as session:

            existing_cart_query = select(CartOrm).where(
                CartOrm.user_id == cart.user_id,
                CartOrm.item_id == cart.item_id
                )
            result = await session.execute(existing_cart_query)
            existing_cart = result.scalar_one_or_none()
            
            if existing_cart:
                print(existing_cart.id)
                await cls.increment_quantity_of_item_in_cart(cart_quantity=cart.quantity, cart_id=existing_cart.id)
            else:            
                cart_dict = cart.model_dump()
                
                cart = CartOrm(**cart_dict)
                session.add(cart)
                
                await session.flush()
                await session.commit()
                return cart.id
            
            # Return the cart ID (either updated or newly created)
            return existing_cart.id if existing_cart else cart.id
    
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
            # Load the cart items along with the item and its category
            query = select(CartOrm).where(CartOrm.user_id == user_id)
                        
            result = await session.execute(query)
            cart_items = result.scalars().all()
            return cart_items
    
    @classmethod
    async def increment_quantity_of_item_in_cart(cls, cart_quantity: int, cart_id: int):
        async with async_session() as session:
            result = await session.execute(
                update(CartOrm)
                .where(CartOrm.id == cart_id)
                .values(quantity = CartOrm.quantity + cart_quantity)
                )
            
            await session.flush()
            await session.commit()
            
            return cart_id
