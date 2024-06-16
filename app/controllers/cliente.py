from app.models.cliente import database, cliente
from sqlalchemy import select


# POST/ cria um cliente
async def create_cliente(nome: str, email: str, cpf: str):
    query = cliente.insert().values(nome=nome, email=email, cpf=cpf)
    ultimo_id_gravado = await database.execute(query)
    
    return {**{"id": ultimo_id_gravado}, "nome": nome, "email": email}


# GET/{id} Apenas 1 cliente
async def get_clientes():
    pass


# GET/ todos os clientes, função com suporte para filtragem
async def get_one_cliene(
        skip: int = 0, limit: int = 15, 
        nome: str = None, email: str = None):
    query = select([cliente]).offset(skip).limit(limit)
    
    if nome:
        query = query.where(cliente.c.nome.ilike(f"%{nome}%"))
        
    elif email:
        query = query.where(cliente.c.email.ilike(f"%{email}%"))
        
    return await database.fetch_all(query)


# PUT/ Atualiza 
async def put_cliente():
    pass


# DELETE/ Exclui cliente
async def delete_cliente():
    pass