import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.database import engine, get_db
from app.db.database import Base, SessionLocal
from app.models.clienteModel import Cliente


# -------------- TEST DATABASE ------------------- #
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# -------------- ============= ------------------- #

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


def test_post_clientes(client):
    response = client.post(
        "/clientes/", 
        json={
                "email": "test4@example.com", 
                "nome": "Test User", 
                "cpf": "123402678901", 
            }
    )
    print(response.text)
    assert response.status_code == 200
    assert response.json()["email"] == "test4@example.com"



def test_get_clientes(client, db_session):
    db_session.add(
        Cliente(
            email="alice@example.com", 
            nome="Alice", 
            cpf="12345678902"
        )
    )
    db_session.add(
        Cliente(
            email="bob@example.com", 
            nome="Bob", 
            cpf="12345678903"
        )
    )
    db_session.commit()

    response = client.get("/clientes/")
    assert response.status_code == 200
    users = response.json()
    assert len(users) >= 2

    response = client.get("/clientes/?nome=Alice")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 1
    assert users[0]["nome"] == "Alice"

    response = client.get("/clientes/?email=bob@example.com")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 1
    assert users[0]["email"] == "bob@example.com"
