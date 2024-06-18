from pydantic import BaseModel, EmailStr


class ClienteBase(BaseModel):
    email: EmailStr
    nome: str
    cpf: str
    
    
class ClienteCadastro(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: str
    
    class ConfigDict:
        from_attributes = True