import uuid

from sqlalchemy import Column, String, Float, Text, Integer, Date, Boolean
from sqlalchemy.orm import relationship

from app.db.database import Base


# Cria tabela produtos
class Produto(Base):
    __tablename__ = "produtos"

    produto_id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome_produto = Column(String, nullable=False)
    descricao = Column(Text, nullable=False)
    valor_de_venda = Column(Float, nullable=False)
    cod_barra = Column(String(length=13), nullable=False)
    secao = Column(String, nullable=False)
    imagem = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    disponibilidade = Column(Boolean, nullable=False)
    data_validade = Column(Date, nullable=True)
    estoque_inicial = Column(Integer, nullable=True)
    
    pedidos = relationship('Pedido', back_populates='produtos')

