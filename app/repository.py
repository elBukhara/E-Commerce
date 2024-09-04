from sqlalchemy import select, delete
from database import ItemOrm, async_session
from schemas import AddItem, Item

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
            # task_schemas = [Item.model_validate(task_model) for task_model in task_models]
            
            return task_models
    
    @classmethod
    async def get_item(cls, item_id: int) -> Item:
        async with async_session() as session:
            item = await session.get(ItemOrm, item_id)
            
            return item