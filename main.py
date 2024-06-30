from typing import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import STaskAdd

from router import router as stasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Data is cleaned")
    await create_tables()
    print("Data is ready")
    yield
    print("Switching off")

app = FastAPI(lifespan=lifespan)

app.include_router(stasks_router)
