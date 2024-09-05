from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables

from items.routers import router as items_router
from cart.routers import router as cart_router
from users.routers import router as users_router
from category.routers import router as category_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    # print("Shutting down the database...")
    await create_tables()
    print("The database is successfully created!")
    yield
    print("Exit!")

app = FastAPI(lifespan=lifespan)

app.include_router(category_router)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(cart_router)