from typing import List, Optional

from fastapi import status
from fastapi.param_functions import Depends, Query
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session

from app.controllers import clienteController
from app.schemas.clienteSchema import Cliente, ClienteCadastro
from app.db.database import get_db

router = APIRouter()

# POST/ cria um cliente
@router.post("/clientes/", response_model=Cliente, tags=["clientes"])
def create_user(cliente: ClienteCadastro, db: Session = Depends(get_db)):
    # Verifica se já existe
    db_cliente = db.query(Cliente) \
            .where(Cliente.email == cliente.email or Cliente.cpf == cliente.cpf)
    if db_cliente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado")
    
    return clienteController.create_cliente(db=db, cliente=cliente)


# GET/ todos os clientes, função com suporte para filtragem
@router.get("/clientes/", response_model=List[Cliente], tags=["clientes"])
def read_clientes(
        skip: int = 0, 
        limit: int = 15, 
        name: Optional[str] = Query(None), 
        email: Optional[str] = Query(None), 
        db: Session = Depends(get_db)):
    clientes = clienteController.get_clientes(db=db, skip=skip, limit=limit)
    return clientes

