from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from routers.items import router as items_router 

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Shutting down the database...")
    await create_tables()
    print("The database is successfully created!")
    yield
    print("Exit!")

app = FastAPI(lifespan=lifespan)

app.include_router(items_router)