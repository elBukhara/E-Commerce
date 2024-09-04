from sqlalchemy import select, delete
from database import ItemOrm, UserOrm, CartOrm, async_session
from schemas import AddItem, Item, UserCreate, User, CartCreate, Cart

class ItemRepository:
    @classmethod
    async def add_item(cls, item: AddItem) -> int:
        async with async_session() as session:
            item_dict = item.model_dump()
            
            item = ItemOrm(**item_dict)
            session.add(item)
            
            await session.flush()
            await session.commit()
            return item.id
    
    @classmethod
    async def delete_item(cls, item_id: int):
        async with async_session() as session:
            result = await session.execute(
                delete(ItemOrm)
                .where(ItemOrm.id == item_id)
                )
            
            await session.flush()
            await session.commit()
            
            return result
    
    @classmethod
    async def get_all_items(cls) -> list[Item]:
        async with async_session() as session:
            
            query = select(ItemOrm)
            
            result = await session.execute(query)
            task_models = result.scalars().all()
            # TODO fix the sample output
            # task_schemas = [Item.model_validate(task_model) for task_model in task_models]
            
            return task_models
    
    @classmethod
    async def get_item(cls, item_id: int) -> Item:
        async with async_session() as session:
            item = await session.get(ItemOrm, item_id)
            
            return item

class UserRepository:
    @classmethod
    async def create_user(cls, user: UserCreate) -> int:
        async with async_session() as session:
            user_dict = user.model_dump()
            # TODO fix unique constraint on username
            
            user = UserOrm(**user_dict)
            session.add(user)
            
            await session.flush()
            await session.commit()
            return user.id
    
    @classmethod
    async def get_user(cls, user_id: int) -> User:
        async with async_session() as session:
            user = await session.get(UserOrm, user_id)
            return user

class CartRepository:
    @classmethod
    async def add_to_cart(cls, cart: CartCreate) -> int:
        async with async_session() as session:
            cart_dict = cart.model_dump()
            
            cart = CartOrm(**cart_dict)
            session.add(cart)
            
            await session.flush()
            await session.commit()
            return cart.id
    
    @classmethod
    async def get_user_cart(cls, user_id: int) -> list[Cart]:
        async with async_session() as session:
            query = select(CartOrm).where(CartOrm.user_id == user_id)
            
            result = await session.execute(query)
            cart_items = result.scalars().all()
            return cart_items
