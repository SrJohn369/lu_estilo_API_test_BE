import sentry_sdk
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_trigger_error():
    with sentry_sdk.Hub(sentry_sdk.Client()) as hub:
        response = client.get("/error")
        assert response.status_code == 500
        
