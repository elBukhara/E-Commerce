from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String 

from typing import Optional

engine = create_async_engine(
    url='sqlite+aiosqlite:///db.sqlite3'
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class ItemOrm(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]]

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)