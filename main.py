from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from router import router as file_router
from models import create_tables, delete_tables
from schemas import SchemaFile, SchemaFileAdd

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова')
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(file_router)

# messages = []


