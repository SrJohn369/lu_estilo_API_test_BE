import sentry_sdk

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.views import clienteView
from app.db.database import database


sentry_sdk.init(
    dsn="https://ab07dfd9ccdd9be84b1976e4637db6e5@o4507450279723008.ingest.de.sentry.io/4507450283262032",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = FastAPI()

app.include_router(clienteView.router)


# integração com Sentry
@app.get("/error")
def trigger_error():
    raise HTTPException(status_code=500, detail="Erro crítico ocorreu")