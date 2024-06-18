from fastapi import FastAPI

from app.views import clienteView
from app.db.database import database


app = FastAPI()

app.include_router(clienteView.router)

