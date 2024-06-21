import uuid

from sqlalchemy import Column, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


# Cria tabela clientes
class Pedido(Base):
    __tablename__ = "produtos"

    pedido_id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    cliente_id = Column(String, ForeignKey('clientes.id'))
    status_pedido = Column(String, nullable=False)
    data_pedido = Column(DateTime, nullable=False)
    
    produtos = relationship('Produto', back_populates='pedidos')
    cliente = relationship('Cliente', back_populates='pedidos')