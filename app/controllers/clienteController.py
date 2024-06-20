from app.schemas.clienteSchema import Cliente as ClienteSchema
from app.schemas.clienteSchema import ClienteCadastro
from app.schemas.clienteSchema import ClienteUpdate
from app.models.clienteModel import Cliente as ClienteModel

from sqlalchemy.orm import Session


# GET/ todos os clientes, função com suporte para filtragem
def get_clientes(
        db: Session, 
        offset: int = 0,
        limit: int = 15, 
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
    
    return query.offset(offset).limit(limit).all()


# GET/{id} Apenas 1 cliente
def get_cliente_by_id(db: Session, id: str):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == id).first()
    return cliente


# POST/ cria um cliente
def create_cliente(cliente: ClienteCadastro, db: Session):
    # cadastrar cliente
    db_cliente = ClienteModel(email=cliente.email, nome=cliente.nome, cpf=cliente.cpf)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    
    return db_cliente


# PUT/ Atualiza todos dados cliente
def put_cliente(db: Session, id: str, cliente_data: ClienteCadastro):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == id).first()
    if cliente:
        cliente.email = cliente_data.email
        cliente.nome = cliente_data.nome
        cliente.cpf = cliente_data.cpf
        db.commit()
        db.refresh(cliente)
        return cliente
    return None


# DELETE/ Exclui cliente
def delete_cliente(db: Session, id: str):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == id).first()
    if cliente:
        db.delete(cliente)
        db.commit()
        return cliente
    return None


# PATCH/ Atualiza parcialmente cliente
def patch_cliente(db: Session, id: str, cliente_data: ClienteUpdate):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == id).first()
    if not cliente:
        return None
    if cliente_data.email is not None:
        cliente.email = cliente_data.email
    if cliente_data.nome is not None:
        cliente.nome = cliente_data.nome
    if cliente_data.cpf is not None:
        cliente.cpf = cliente_data.cpf
    db.commit()
    db.refresh(cliente)
    return cliente
