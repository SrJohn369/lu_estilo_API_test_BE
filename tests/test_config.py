import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.db.database import engine
from app.db.database import Base, SessionLocal


# Configuração do banco de dados para os testes
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Fixture para gerenciar a sessão do banco de dados
@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Fixture para o cliente de teste
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c