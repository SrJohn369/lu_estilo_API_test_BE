import os
import uuid

from sqlalchemy import Column, String, Table, MetaData, PrimaryKeyConstraint
from databases import Database
from dotenv import load_dotenv


# carrrega variaveis de ambiente
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
metadata = MetaData()

# Criar tabela clientes
cliente = Table(
    "clientes", metadata,
    Column("id", String, default=lambda: str(uuid.uuid4()), unique=True),
    Column("email", String),
    Column("cpf", String),
    Column("senha", String),
    PrimaryKeyConstraint("email", "cpf", name="pk_cliente")
)