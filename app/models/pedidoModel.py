import uuid

from sqlalchemy import Column, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


# Cria tabela pedidos
class Pedido(Base):
    __tablename__ = "produtos"

    id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    cliente_id = Column(String, ForeignKey('clientes.id'))
    status_pedido = Column(String, nullable=False)
    data_pedido = Column(DateTime, nullable=False)
    