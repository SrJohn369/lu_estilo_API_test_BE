import uuid

from sqlalchemy import Column, String, Float, Text, Integer, Date
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.associacaoModel import pedido_produto_associacao


# Cria tabela clientes
class Produto(Base):
    __tablename__ = "produtos"

    produto_id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    descricao = Column(Text, nullable=False)
    valor_de_venda = Column(Float, nullable=False)
    cod_barra = Column(String(length=13), nullable=False)
    secao = Column(String, nullable=False)
    imagem = Column(String, nullable=False)
    data_validade = Column(Date, nullable=True)
    estoque_de_validae = Column(Integer, nullable=True)
    
    pedidos = relationship('Pedido', back_populates='produtos')

