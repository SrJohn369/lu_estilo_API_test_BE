from pydantic import BaseModel, EmailStr


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


class Cliente(ClienteBase):
    id: str
    
    class ConfigDict:
        from_attributes = True