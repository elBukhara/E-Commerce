from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload

from database import async_session
from .models import ItemOrm, CategoryOrm
from .schemas import AddItem, Item

class ItemRepository:
    @classmethod
    async def add_item(cls, item: AddItem) -> int:
        async with async_session() as session:
            # Ensure the category exists before adding the item
            category = await session.get(CategoryOrm, item.category_id)
            if not category:
                raise ValueError("Invalid category ID")

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
            query = select(ItemOrm).join(ItemOrm.category).options(
                selectinload(ItemOrm.category)  # Load category with the item
            )
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
    
    @classmethod
    async def get_item(cls, item_id: int) -> Item:
        async with async_session() as session:            
            query = select(ItemOrm).where(ItemOrm.id == item_id)
            result = await session.execute(query)
            item = result.scalar_one_or_none()

            if item is None:
                raise ValueError(f"Item with ID {item_id} not found")

            return item
