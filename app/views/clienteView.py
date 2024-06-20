from typing import List, Optional

from fastapi import status
from fastapi.param_functions import Depends, Query
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session

from app.controllers import clienteController
from app.schemas.clienteSchema import Cliente, ClienteCadastro
from app.models.clienteModel import Cliente as ClienteModel
from app.db.database import get_db

router = APIRouter()

# POST/ cria um cliente
@router.post("/clientes/", response_model=Cliente, tags=["clientes"])
def create_cliente(cliente: ClienteCadastro, db: Session = Depends(get_db)):
    # Verifica se já existe
    db_cliente = db.query(ClienteModel) \
            .where((ClienteModel.email == cliente.email)).first()
    if db_cliente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"Email já cadastrado")
    
    return clienteController.create_cliente(db=db, cliente=cliente)


# GET/ todos os clientes, função com suporte para filtragem
@router.get("/clientes/", response_model=List[Cliente], tags=["clientes"])
def read_clientes(
        offset: int = 0,
        limit: int = 15, 
        nome: Optional[str] = Query(None), 
        email: Optional[str] = Query(None), 
        db: Session = Depends(get_db)):
    clientes = clienteController.get_clientes(db=db, offset=offset, limit=limit, nome=nome, email=email)
    if clientes == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                             detail="não há clientes com esse esses parâmentros")
    return clientes


# GET/ Um cliente por id
@router.get("/clientes/{id}", response_model=Cliente, tags=["clientes"])
def read_clientes_by_id( id: str, db: Session = Depends(get_db)):
    cliente = clienteController.get_cliente_by_id(db=db, id=id)
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                             detail="Cliente não encontrado!")
    return cliente