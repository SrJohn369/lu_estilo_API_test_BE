from app.schemas.clienteSchema import Cliente
from app.schemas.clienteSchema import ClienteCadastro

from sqlalchemy.orm import Session


# GET/ todos os clientes, função com suporte para filtragem
async def get_clientes(
        db: Session, 
        skip: int = 0, 
        limit: int = 10, 
        name: str = None,
        email: str = None):
    
    # Sem filtro
    query = db.query(Cliente)
    # Filtro para nome
    if name:
        query = query.filter(Cliente.name.ilike(f"%{name}%"))
    # Filtro para email
    if email:
        query = query.filter(Cliente.email.ilike(f"%{email}%"))
    
    return await query.offset(skip).limit(limit).all()


# GET/{id} Apenas 1 cliente
async def get_cliente_by_id(db: Session, id: str):
    return await db.query(Cliente).where(Cliente.id == id)


# POST/ cria um cliente
async def create_cliente(cliente: ClienteCadastro, db: Session):
    # cadastrar cliente
    db_cliente = Cliente(email=cliente.email, nome=cliente.nome, cpf=cliente.cpf)
    db.add(db_cliente)
    await db.commit()
    await db.refresh(db_cliente)
    
    return db_cliente


# PUT/ Atualiza 
async def put_cliente():
    pass


# DELETE/ Exclui cliente
async def delete_cliente():
    pass