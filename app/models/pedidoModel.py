import uuid

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.associacaoModel import pedido_produto_associacao

# Cria tabela clientes
class Pedido(Base):
    __tablename__ = "produtos"

    pedido_id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    status_pedido = Column(String, nullable=False)
    data_pedido = Column(DateTime, nullable=False)
    
    produtos = relationship('Produto', secondary=pedido_produto_associacao, back_populates='pedidos')