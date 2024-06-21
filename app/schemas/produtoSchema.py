from pydantic import BaseModel, PastDate
from typing import Optional


class ProdutoBase(BaseModel):
    nome_produto: str
    descricao: str
    valor_de_venda: float
    data_validade: PastDate
    categoria: str
    disponibilidade: bool
    
    
class ProdutoCadastro(ProdutoBase):
    cod_barra: str
    secao: str
    imagem:str
    estoque_inicial: int


class ClienteUpdate(BaseModel):
    nome_produto: Optional[str] = None
    descricao: Optional[str] = None
    valor_de_venda: Optional[float] = None
    data_validade: Optional[PastDate] = None
    categoria: Optional[str] = None
    disponibilidade: Optional[bool] = None
    cod_barra: Optional[str] = None
    secao: Optional[str] = None
    imagem:Optional[str] = None
    estoque_de_validae: Optional[int] = None


class Produto(ProdutoCadastro):
    produto_id: str
    
    class ConfigDict:
        from_attributes = True