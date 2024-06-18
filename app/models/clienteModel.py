import uuid

from sqlalchemy import Column, String, PrimaryKeyConstraint
from app.db.database import Base


# Cria tabela clientes
class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cpf = Column(String(length=14), nullable=False)

    primary_key_constraint = PrimaryKeyConstraint("email", "cpf", name="pk_cliente")
