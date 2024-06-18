from fastapi import FastAPI

from app.views import clienteView
from app.db.database import database, init_db


app = FastAPI()

app.include_router(clienteView.router)


@app.on_event("startup")
async def startup():
    await database.connect()
    init_db()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()