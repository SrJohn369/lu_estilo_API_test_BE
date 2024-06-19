import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from databases import Database

from dotenv import load_dotenv


# carregar variáveis de ambiente
load_dotenv()

# banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")
# --
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()

# cria uma sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# inicia banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# Função para criar tabelas
def init_db():
    Base.metadata.create_all(bind=engine)