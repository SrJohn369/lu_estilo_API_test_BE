import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.database import engine, get_db
from app.db.database import Base, SessionLocal
from app.models.clienteModel import Cliente


# -------------- TEST DATABASE ------------------- #
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# -------------- ============= ------------------- #


@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as client:
        yield client
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    session = SessionLocal()
    yield session
    session.close()


# Sobrescrevendo a dependência get_db para usar SQLite para testes
app.dependency_overrides[get_db] = db_session


def test_post_clientes(client):
    response = client.post(
        "/clientes/", 
        json={
                "email": "test@example.com", 
                "name": "Test User", 
                "cpf": "12345678901", 
                "password": "password"
            }
    )
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"



def test_get_clientes(client, db_session):
    db_session.add(
        Cliente(
            email="alice@example.com", 
            name="Alice", 
            cpf="12345678902", 
            hashed_password="password"
        )
    )
    db_session.add(
        Cliente(
            email="bob@example.com", 
            name="Bob", 
            cpf="12345678903", 
            hashed_password="password"
        )
    )
    db_session.commit()

    response = client.get("/clientes/")
    assert response.status_code == 200
    users = response.json()
    assert len(users) >= 2

    response = client.get("/users/?nome=Alice")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 1
    assert users[0]["nome"] == "Alice"

    response = client.get("/clientes/?email=bob@example.com")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 1
    assert users[0]["email"] == "bob@example.com"
