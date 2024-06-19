import sentry_sdk

from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.views import clienteView
from app.db.database import database, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    init_db()
    yield 
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(clienteView.router)