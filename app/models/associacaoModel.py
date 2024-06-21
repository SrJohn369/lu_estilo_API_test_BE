from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

class PedidoProduto(Base):
    __tablename__ = 'pedido_produto'

    pedido_id = Column(Integer, ForeignKey('pedidos.id'), primary_key=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'), primary_key=True)
    quantidade = Column(Integer)

    pedido = relationship("Pedido", back_populates="produtos")
    produto = relationship("Produto", back_populates="pedidos")

