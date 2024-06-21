from pydantic import BaseModel, EmailStr
from typing import Optional


class ClienteBase(BaseModel):
    email: EmailStr
    nome: str
    cpf: str
    
    
class ClienteCadastro(ClienteBase):
    '''
    O campo cpf tem limite de tamanho em 14 caracteres sendo a formatação 
    123.456.789-10. O campos email e cpf devem ser obrigatoriamente
    preenchidos pois são primary key
    '''
    pass


class ClienteUpdate(BaseModel):
    email: Optional[EmailStr] = None
    nome: Optional[str] = None
    cpf: Optional[str] = None


class Cliente(ClienteBase):
    cliente_id: str
    
    class ConfigDict:
        from_attributes = True