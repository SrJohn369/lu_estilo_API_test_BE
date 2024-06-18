from app.schemas.clienteSchema import Cliente as ClienteSchema
from app.schemas.clienteSchema import ClienteCadastro
from app.models.clienteModel import Cliente as ClienteModel

from sqlalchemy.orm import Session


# GET/ todos os clientes, função com suporte para filtragem
def get_clientes(
        db: Session, 
        limit: int = 10, 
        nome: str = None,
        email: str = None):
    
    # Sem filtro
    query = db.query(ClienteModel)
    # Filtro para nome
    if nome:
        query = query.filter(ClienteModel.nome.ilike(f"%{nome}%"))
    # Filtro para email
    if email:
        query = query.filter(ClienteModel.email.ilike(f"%{email}%"))
    
    return query.limit(limit).all()


# GET/{id} Apenas 1 cliente
def get_cliente_by_id(db: Session, id: str):
    return db.query(ClienteModel).where(ClienteModel.id == id)


# POST/ cria um cliente
def create_cliente(cliente: ClienteCadastro, db: Session):
    # cadastrar cliente
    db_cliente = ClienteModel(email=cliente.email, nome=cliente.nome, cpf=cliente.cpf)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    
    return db_cliente


# PUT/ Atualiza 
def put_cliente():
    pass


# DELETE/ Exclui cliente
def delete_cliente():
    pass