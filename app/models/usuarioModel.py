import uuid

from sqlalchemy import Column, String


from app.db.database import Base


# Cria tabela usuarios
class Usuario(Base):
    __tablename__ = "usuarios"

    usuario_id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)