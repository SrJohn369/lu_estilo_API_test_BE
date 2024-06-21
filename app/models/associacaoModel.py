from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.database import Base

pedido_produto_associacao = Table(
    'pedido_produto_associacao',
    Base.metadata,
    Column('pedido_id', Integer, ForeignKey('pedidos.id'), primary_key=True),
    Column('produto_id', Integer, ForeignKey('produtos.id'), primary_key=True)
)
