from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from routers import items, users, carts

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    # print("Shutting down the database...")
    await create_tables()
    print("The database is successfully created!")
    yield
    print("Exit!")

app = FastAPI(lifespan=lifespan)


app.include_router(items.router)
app.include_router(users.router)
app.include_router(carts.router)