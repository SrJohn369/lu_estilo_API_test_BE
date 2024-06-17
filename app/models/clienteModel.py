import uuid

from sqlalchemy import Column, String, PrimaryKeyConstraint
from app.db.database import Base

# Criar tabela clientes
class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(String, default=lambda: str(uuid.uuid4()), unique=True),
    nome = Column(String, nullable=False),
    email = Column(String,  nullable=False),
    cpf = Column(String, nullable=False),
    PrimaryKeyConstraint("email", "cpf", name="pk_cliente")