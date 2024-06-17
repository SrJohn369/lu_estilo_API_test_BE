from pydantic import BaseModel, EmailStr


class ClienteBase(BaseModel):
    email: EmailStr
    nome: str
    cpf: str
    
    
class ClienteCadastro(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: str
    
    class Config:
        orm_mode = True