from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Integer

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

class UserOrm(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))  # Store hashed password
    
    carts = relationship("CartOrm", back_populates="user")

class CartOrm(Base):
    __tablename__ = "carts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    
    user = relationship("UserOrm", back_populates="carts")
    item = relationship("ItemOrm")

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)