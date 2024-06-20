<h1 align="center">
  Lu Estilo API <img width="48" height="48" src="https://img.icons8.com/color/48/gear.png" alt="gear" />
</h1>  

<h4 align="center">  
  
  ![Static Badge](https://img.shields.io/badge/status-em_desenvolvimento-blue?style=for-the-badge&labelColor=grey)
  ![GitHub Tag](https://img.shields.io/github/v/tag/SrJohn369/lu_estilo_API_test_BE?style=for-the-badge&label=version)
</h4>

## Índice  

- [Descrição](#Descrição)
- [Estrutura](#Estrutura)
- [Endpoints](#Endpoints)
   - [Autenticação](#Autenticação)
   - [Clientes](#Clientes)
   - [Produtos](#Produtos)
   - [Pedidos](#Pedidos)
- [Documentação](#Documentação)
  - app/[main.py](#mainpy)
  - app/models/[clienteModel.py](#clienteModelpy)
  - app/views/[clienteView.py](#clienteViewpy)
  - app/controllers/[clienteController.py](#clienteControllerpy)
  - app/db/[database.py](#databasepy)
  - app/auth/[auth.py](#authpy)
  - app/auth/[jwt.py](#jwtpy)
  - app/schemas/[clienteSchema.py](#clienteSchemapy)
  - tests/[configTest.py](#configTestpy)
  - tests/[clienteTest.py](#clienteTestpy)

## Descrição

A Lu Estilo é uma empresa de confecção que está buscando novas oportunidades de negócio. 
Esta API é desenvolvida com FastAPI e será usada para fornecer dados e funcionalidades para 
facilitar a comunicação entre o time comercial, os clientes e a empresa.  
  
Tudo que está documentado de models, controllers, views, schemas e tests são base para os outros arquivos como produtos, usuários e pedidos.  
  
## Estrutura  
A API tem uma estrutura montada no padrão MVC:
```
lu_estilo_API_test_Be/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── clienteModel.py
│   ├── views/
│   │   ├── __init__.py
│   │   └── clienteView.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── clienteController.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── jwt.py
│   └── schemas/
│       ├── __init__.py
│       └── clienteSchema.py
├── tests/
│   ├── __init__.py
│   ├── configTest.py
│   └── clienteTest.py
├── requirements.txt
├── alembic.ini
└── alembic/
    ├── env.py
    ├── README
    ├── script.py.mako
    └── versions/
```


## Endpoints
A documentação dos endpoints tambem podem ser vzualizada de forma dinamica no Swaager [aqui]().
### Autenticação
🚧 em construção 🚧


<details>
  
  <summary>POST/auth/login</summary>
  
</details>  

<details>
  
  <summary>POST/auth/register</summary>
  
</details>  

<details>
  
  <summary>POST/refresh-token</summary>
  
</details>  


### Clientes
🚧 em construção 🚧


<details>
  
<summary>GET/clientes</summary>

#### Descrição
Este endpoint retornará todos os clientes com limite de 15 registros por padrão no parâmentro limit  

---  
#### URL
`/clientes`

---  
#### Método HTTP
GET  

---  
#### Parâmetros
##### Path Parameters
- Sem parâmetros obrigatórios
##### Query Parameters
- `nome` (Opcional):
   - irá filtrar clientes trazendo apenas o dados no cliente com *nome* fornecido.
      - Exemplo: `/clientes/?nome=joao`
- `email` (Opcional):
   - irá filtrar clientes trazendo apenas o dados no cliente com *email* fornecido.
      - Exemplo: `/clientes/?email=claudia.fernanda@email.com`
- `limit` (Valor Padrão):
    - Parâmetro padrão das requests GET para clientes que trará apenas 15 resgistros , ou seja, 15 clientes.
        - Exemplo: `/clientes/?limit=15`
          
---  
#### Respostas
Curl
```Curl
curl -X 'GET' \
  'http://localhost:8000/clientes/?limit=15' \
  -H 'accept: application/json'
```
Request URL
```url
http://localhost:8000/clientes/?limit=15&nome=joao&email=claudia.fernanda@email.com
```
Status code: 200 OK  
Response Body:  
```JSON
[
  {
    "email": "claudia.fernanda@email.com",
    "nome": "joao",
    "cpf": "345.567.999-00",
    "id": "206457ab-4c04-4c26-82c7-49d032158e72"
  }
]
```
</details>  

<details>
  
  <summary>GET/clientes/{id}</summary>
  #### Descrição
Este endpoint retornará todos os clientes com limite de 15 registros por padrão no parâmentro limit  

---  
#### URL
`/clientes`

---  
#### Método HTTP
GET  

---  
#### Parâmetros
##### Path Parameters
- `id`: Parâmetro obrigatório para buscar usuário
##### Query Parameters
- Sem parâmetros
          
---  
#### Respostas
Curl
```Curl
curl -X 'GET' \
  'http://localhost:8000/clientes/f4805512-9c23-4e03-9eaf-f756eb3334f8' \
  -H 'accept: application/json'
```
Request URL
```url
http://localhost:8000/clientes/f4805512-9c23-4e03-9eaf-f756eb3334f8
```
Status code: 200 OK  
Response Body:  
```JSON
{
  "email": "carlos.jose@emal.com",
  "nome": "Carl",
  "cpf": "987.654.987-00",
  "id": "f4805512-9c23-4e03-9eaf-f756eb3334f8"
}
```
</details>

<details>
  
  <summary>POST/clientes</summary>

#### Descrição
Este endpoint criará um registro de cliente 

---  
#### URL
`/clientes`

---  
#### Método HTTP
POST  

---  
#### Parâmetros
##### Path Parameters
- Sem parâmetros obrigatórios
##### Query Parameters
- Sem parâmetros
          
##### Request body
```JSON
{
  "email": "user@example.com",
  "nome": "string",
  "cpf": "string"
}
```
---  
#### Respostas
Curl
```curl
curl -X 'POST' \
  'http://localhost:8000/clientes/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "carlos.jose@emal.com",
  "nome": "Carl",
  "cpf": "987.654.987-00"
}'
```
Request URL
```url
http://localhost:8000/clientes/
```
Status code: 200 OK  
Response Body:  
```JSON
{
  "email": "carlos.jose@emal.com",
  "nome": "Carl",
  "cpf": "987.654.987-00",
  "id": "f4805512-9c23-4e03-9eaf-f756eb3334f8"
}
```
  
</details>  

<details>
  
  <summary>PUT/clientes/{id}</summary>
  
</details>

<details>
  
  <summary>DELETE/clientes/{id}</summary>
  
</details>

### Produtos 
🚧 em construção 🚧

<details>
  
  <summary>GET/produtos</summary>
  
</details>  

<details>
  
  <summary>GET/produtos/{id}</summary>
  
</details>  

<details>
  
  <summary>POST/produtos</summary>
  
</details>  

<details>
  
  <summary>PUT/produtos/{id}</summary>
  
</details>  


<details>
  
  <summary>DELETE/produtos/{id}</summary>
  
</details>  


### Pedidos
🚧 em construção 🚧


<details>
  
  <summary>GET/ordens</summary>
  
</details>  

<details>
  
  <summary>GET/ordens/{id}</summary>
  
</details>  

<details>
  
  <summary>POST/ordens</summary>
  
</details>  

<details>
  
  <summary>PUT/ordens</summary>
  
</details>  


<details>
  
  <summary>DELETE/ordens</summary>
  
</details>  


## Documentação

Esta API depende das libs:  
- `fastapi`
- `psycopg2` & `psycopg2-binary`
- `SQLAlchemy`
- `databases`
- `python-dotenv`
- `alembic`
- `pytest`
- `jose`
- `passlib`
- `uvicorn`

Dentre outras que estão listados e devem ser instaladas usando o comando:
```bash
pip install -r requirements.txt
```

---

### main.py
##### DESCRIÇÃO 
  
Este código cria uma aplicação web usando o framework FastAPI. Ele gerencia o ciclo de vida da aplicação, conectando-se ao banco de dados ao iniciar e desconectando-se ao finalizar. As rotas da aplicação são definidas em app.include_router() e são incluídas na instância principal da aplicação.    
Ao usar o comando:
```bash
fastapi dev main.py
```
O framework irá identificar a instância do FastAPI() e iniciará todo trabalho.  

---

##### CÓDIGO 
```python
import sentry_sdk

from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.views import clienteView
from app.db.database import database, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    init_db()
    yield 
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(clienteView.router)
```
As views são importadas de app/views
  
`sentry_sdk`: Esta biblioteca é usada para monitoramento de erros e desempenho.  
`FastAPI`: Importamos a classe FastAPI do framework FastAPI, que é usada para criar nossa aplicação web.  
`asynccontextmanager`: Importamos asynccontextmanager do módulo contextlib para criar um gerenciador de contexto assíncrono.  
`database` e `init_db`: Importamos database, que é nosso objeto de conexão com o banco de dados, e init_db, que é uma função para inicializar o banco de dados.  

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    init_db()
    yield 
    await database.disconnect()
```
Neste trecho do código definimos uma função para gerenciar a conexão com o banco de dados durante o ciclo de vida da aplicação.  

`@asynccontextmanager`: Este decorador transforma a função lifespan em um gerenciador de contexto assíncrono.  
`async def lifespan(app: FastAPI)`: Definimos uma função assíncrona chamada lifespan que aceita nossa aplicação FastAPI como argumento.  
`await database.connect()`: Estabelecemos a conexão com o banco de dados quando a aplicação inicia.  
`init_db()`: Inicializamos o banco de dados (por exemplo, criando tabelas ou inserindo dados iniciais).  
`yield`: Pausamos a função até que a aplicação esteja pronta para ser encerrada. Após o yield, qualquer código é executado quando a aplicação está sendo finalizada.  
`await database.disconnect()`: Desconectamos do banco de dados quando a aplicação está sendo encerrada.  

Criamos uma instância da nossa aplicação FastAPI e passamos o gerenciador de contexto lifespan para gerenciar o ciclo de vida da aplicação.
```python
app = FastAPI(lifespan=lifespan)
```
`app = FastAPI(lifespan=lifespan)`: Criamos uma instância da aplicação FastAPI e especificamos que queremos usar o gerenciador de contexto `lifespan` para gerenciar o ciclo de vida da aplicação.  

Incluímos as rotas definidas como [clienteView](#clienteViewpy), na nossa aplicação FastAPI.
```python
app.include_router(clienteView.router)
```
  
[Voltar ao índice](#Índice)

---

### clienteModel.py
##### DESCRIÇÃO

Este código define um modelo de dados para a tabela clientes usando SQLAlchemy. A tabela armazena informações sobre clientes, incluindo id, nome, email e cpf. A coluna id é um UUID gerado automaticamente, e há uma restrição de chave primária composta nas colunas email e cpf.  
  
---

##### CÓDIGO
```python
import uuid

from sqlalchemy import Column, String, PrimaryKeyConstraint
from app.db.database import Base


# Cria tabela clientes
class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cpf = Column(String(length=14), nullable=False)

    primary_key_constraint = PrimaryKeyConstraint("email", "cpf", name="pk_cliente")
```
  
---
  
##### Detalhamento do Código
```python
import uuid
from sqlalchemy import Column, String, PrimaryKeyConstraint
from app.db.database import Base
```

`uuid`: Biblioteca para gerar identificadores únicos universais (UUID).  
`Column`, `String`, `PrimaryKeyConstraint`: Componentes do SQLAlchemy para definir colunas e restrições de tabelas.  
`Base`: Classe base de onde todos os modelos de tabela herdam, fornecida pelo módulo [app.db.database](#databasepy).  


Definição da Classe
```python
class Cliente(Base):
    __tablename__ = "clientes"
```
  
`Cliente`: Define um modelo de dados que mapeia para a tabela clientes no banco de dados.  
`__tablename__`: Nome da tabela no banco de dados.  

  
Definição das Colunas
```python
id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
nome = Column(String, nullable=False)
email = Column(String, nullable=False)
cpf = Column(String(length=14), nullable=False)
```
  
`id`: Coluna do tipo String com comprimento de 36 caracteres. É a chave primária e usa um UUID gerado automaticamente como valor padrão.  
`nome`: Coluna do tipo String que não pode ser nula.  
`email`: Coluna do tipo String que não pode ser nula.
`cpf`: Coluna do tipo String com comprimento de 14 caracteres que não pode ser nula. Foi posta com 14 caracteres para suportar esta formatação 123.456.789-00
  
Restrição de Chave Primária Composta:
```python
primary_key_constraint = PrimaryKeyConstraint("email", "cpf", name="pk_cliente")
```  
Define uma chave primária composta pelas colunas email e cpf.
`name="pk_cliente"`: Nomeia a restrição como pk_cliente.

  
[Voltar ao índice](#Índice)
  
---
  
### clienteView.py

##### DESCRIÇÃO

Este código define endpoints para uma API de gerenciamento de clientes usando FastAPI. Ele permite a criação e leitura de registros de clientes no banco de dados, com suporte para filtragem.

---

##### CÓDIGO
```python
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
    clientes = clienteController.get_clientes(db=db, limit=limit, nome=nome, email=email)
    return clientes
```
  
Detalhamento do Código
```python
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
```

Importações  
`typing`: Importa tipos para anotação, como List e Optional.  
`fastapi`: Importa componentes do FastAPI para definição de status HTTP, dependências e parâmetros de consulta.  
`sqlalchemy.orm`: Importa Session para interagir com o banco de dados.
`[app.controllers](#clienteControllerpy), [app.schemas](#clienteSchemapy), [app.models](#clienteModelpy), [app.db](#databasepy)`: Importa controladores, esquemas, modelos e a função de obtenção da sessão do banco de dados de módulos internos.  
`APIRouter`: Cria um roteador para definir rotas.  
`HTTPException`: Define exceções HTTP para erros.  


Criação de Cliente (POST)
```python
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
```
  
`@router.post("/clientes/", response_model=Cliente, tags=["clientes"])`: Define um endpoint POST para [/clientes/](#Clientes) que retorna um objeto Cliente e é categorizado sob a tag clientes.  
`create_cliente(cliente: ClienteCadastro, db: Session = Depends(get_db))`: Função que aceita um objeto [ClienteCadastro](#clienteSchemapy) e uma sessão de banco de dados.  

O que a Função faz:
- Verifica se já existe um cliente com o mesmo email.
- Se existir, lança uma exceção HTTP 400 com a mensagem "Email já cadastrado".
- Se não existir, chama a função [create_cliente](#clienteControllerpy) do controlador para criar um novo cliente.  


Leitura de Clientes (GET):
```python
# GET/ todos os clientes, função com suporte para filtragem
@router.get("/clientes/", response_model=List[Cliente], tags=["clientes"])
def read_clientes(
        offset: int = 0,
        limit: int = 15, 
        nome: Optional[str] = Query(None), 
        email: Optional[str] = Query(None), 
        db: Session = Depends(get_db)):
    clientes = clienteController.get_clientes(db=db, limit=limit, nome=nome, email=email)
    return clientes
```

`@router.get("/clientes/", response_model=List[Cliente], tags=["clientes"])`: Define um endpoint GET para [/clientes/](#Clientes) que retorna uma lista de objetos Cliente e é categorizado sob a tag clientes.  
`read_clientes(offset: int = 0, limit: int = 15, nome: Optional[str] = Query(None), email: Optional[str] = Query(None), db: Session = Depends(get_db))`: Função que aceita parâmetros de consulta opcionais (nome, email) e um limite de registros a serem retornados, além de uma sessão de banco de dados e um offset para que em conjunto com limit fornecer suporte para paginação.  

O que a Função faz:
- Usa os parâmetros de consulta para filtrar os clientes por nome e email, se fornecidos.
- Limita o número de registros retornados.
- Chama a função [get_clientes](#clienteControllerpy) do controlador para obter os clientes do banco de dados.
  

  [Voltar ao índice](#Índice)

---

### clienteController.py
🚧 em construção 🚧
##### DESCRIÇÃO

Este código define funções de controlador para gerenciar clientes em um banco de dados usando SQLAlchemy. As funções permitem buscar clientes com filtros opcionais, buscar um cliente por ID e criar um novo cliente.

---

##### CÓDIGO
```python
from app.schemas.clienteSchema import Cliente as ClienteSchema
from app.schemas.clienteSchema import ClienteCadastro
from app.models.clienteModel import Cliente as ClienteModel

from sqlalchemy.orm import Session


# GET/ todos os clientes, função com suporte para filtragem
def get_clientes(
        db: Session, 
        limit: int = 10, 
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
    
    return query.limit(limit).all()


# GET/{id} Apenas 1 cliente
def get_cliente_by_id(db: Session, id: str):
    return db.query(ClienteModel).where(ClienteModel.id == id)


# POST/ cria um cliente
def create_cliente(cliente: ClienteCadastro, db: Session):
    # cadastrar cliente
    db_cliente = ClienteModel(email=cliente.email, nome=cliente.nome, cpf=cliente.cpf)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    
    return db_cliente
```
  
Detalhamento do Código
```python
from app.schemas.clienteSchema import Cliente as ClienteSchema
from app.schemas.clienteSchema import ClienteCadastro
from app.models.clienteModel import Cliente as ClienteModel

from sqlalchemy.orm import Session
```
  
Importações:
- Importa os [esquemas](#clienteSchemapy) Cliente e ClienteCadastro de clienteSchema.  
- Importa o [modelo](#databasepy) Cliente de clienteModel.  
- Importa Session do SQLAlchemy para interagir com o banco de dados.
  
Função get_clientes:  
Busca clientes no banco de dados com suporte a filtros opcionais por nome e email.
```python
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
```
  
`db: Session`: A sessão de banco de dados.  
`limit: int = 15`: Limite de registros a serem retornados, padrão é 15.  
`offset: int = 0`: Define apartir de que registro devem ser retornados, padrão é 0.  
`nome: str = None`: Filtro opcional por nome.  
`email: str = None`: Filtro opcional por email.  
  
O que a Função faz:  
- Inicia uma consulta ao banco de dados.  
- Aplica filtros de nome e email, se fornecidos.
- Limita o número de resultados e retorna a lista de clientes.
  
Função get_cliente_by_id  
Busca um cliente no banco de dados pelo ID.
```python
# GET/{id} Apenas 1 cliente
def get_cliente_by_id(db: Session, id: str):
    return db.query(ClienteModel).where(ClienteModel.id == id)
```
  
`db: Session`: A sessão de banco de dados.  
`id: str`: O ID do cliente a ser buscado.  
  
O que a Função faz:  
- Inicia uma consulta ao banco de dados filtrando pelo ID do cliente.  
- Retorna o cliente encontrado.
  
Função create_cliente  
Cria um novo cliente no banco de dados.  
```python
# POST/ cria um cliente
def create_cliente(cliente: ClienteCadastro, db: Session):
    # cadastrar cliente
    db_cliente = ClienteModel(email=cliente.email, nome=cliente.nome, cpf=cliente.cpf)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    
    return db_cliente
```

`cliente: [ClienteCadastro](#clienteSchemapy)`: Os dados do cliente a ser criado.  
`db: Session`: A sessão de banco de dados.  
  
O que a Função faz:  
- Cria uma instância de ClienteModel com os dados fornecidos.
- Adiciona a instância à sessão de banco de dados e realiza o commit.
- Atualiza a instância do cliente com os dados do banco de dados (incluindo o ID gerado).
- Retorna a instância do cliente criada.
  
  
[Voltar ao índice](#Índice)

---  


### database.py

##### DESCRIÇÃO
  
Este código configura a conexão com o banco de dados usando SQLAlchemy e databases. Ele carrega variáveis de ambiente, cria a engine e a sessão do banco de dados, e define funções para gerenciar a sessão e inicializar o banco de dados.  
  
---
  
##### CÓDIGO
```python
import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from databases import Database

from dotenv import load_dotenv


# carregar variáveis de ambiente
load_dotenv()

# banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")
# --
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()

# cria uma sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# inicia banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# Função para criar tabelas
def init_db():
    Base.metadata.create_all(bind=engine)
```
  
Detalhamento do Código  
Importações
```python
import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from databases import Database

from dotenv import load_dotenv


# carregar variáveis de ambiente
load_dotenv()
```
  
`os`: Utilizado para acessar variáveis de ambiente.  
`sqlalchemy`: Importa componentes para criar a engine do banco de dados, metadados e a base declarativa.  
`databases`: Biblioteca para manipulação de bancos de dados de forma assíncrona.  
`dotenv`: Biblioteca para carregar variáveis de ambiente a partir de um arquivo .env.
`load_dotenv()`: Carrega variáveis de ambiente do arquivo .env.  
  
Configuração do Banco de Dados
```python
# banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")
# --
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()

# cria uma sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```
  
`DATABASE_URL = os.getenv("DATABASE_URL")`: Obtém a URL do banco de dados a partir das variáveis de ambiente.  
`database = Database(DATABASE_URL)`: Cria uma instância de Database para operações assíncronas.  
`engine = create_engine(DATABASE_URL)`: Cria a engine do banco de dados usando SQLAlchemy.  
`metadata = MetaData()`: Cria um objeto MetaData para manter informações sobre as tabelas.  
`Base = declarative_base()`: Cria uma base declarativa para definir os modelos ORM.  
`SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)`: Cria uma fábrica de sessões para interagir com o banco de dados, sem commits ou flushes automáticos.  
  
Função get_db  
Gerencia a sessão do banco de dados.  
```python
# inicia banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
  
db = SessionLocal(): Cria uma nova sessão.
try: Inicia um bloco try para utilizar a sessão.
yield db: Fornece a sessão para uso.
finally: Assegura que a sessão será fechada após o uso.
  
  
O que a Função faz:  
- A sessão é criada e fornecida para o contexto de uso.
- A sessão é fechada ao sair do contexto, garantindo a liberação dos recursos.
  
  
Função init_db  
Inicializa o banco de dados, criando todas as tabelas definidas na base declarativa.  
```python
# Função para criar tabelas
def init_db():
    Base.metadata.create_all(bind=engine)
```
  
`ase.metadata.create_all(bind=engine)`: Cria todas as tabelas no banco de dados vinculadas à engine.
  
O que a Função faz:  
- Usa a metadata da base declarativa para criar as tabelas no banco de dados.
  
  
[Voltar ao índice](#Índice)
   
---
  
### auth.py

##### DESCRIÇÃO
Este código define funções para hash e verificação de senhas utilizando a biblioteca passlib com o esquema bcrypt.
  
---
  
##### CÓDIGO
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)
```
  
---
  
Detalhamento do Código:  
Importação:  
`CryptContext`: Importa a classe CryptContext da biblioteca passlib, que é usada para gerenciar esquemas de hashing de senha.  
  
Configuração do Contexto de Senhas:  
`pwd_context`: Cria um contexto de senhas com bcrypt como o esquema de hashing.  
`schemes=["bcrypt"]`: Define bcrypt como o esquema de hashing a ser usado.  
`deprecated="auto"`: Define o gerenciamento automático de esquemas obsoletos.  
  
  
Função verify_password:  
Verifica se uma senha em texto plano corresponde a uma senha hash.  
```python
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
```
  
`plain_password`: A senha em texto plano que precisa ser verificada.  
`hashed_password`: A senha hash contra a qual a senha em texto plano será verificada.  
 
Utiliza o método verify do pwd_context para comparar a senha em texto plano com a senha hash.  
Retorna True se as senhas coincidirem, caso contrário, retorna False.  
  
Função get_password_hash:  
Gera um hash para uma senha em texto plano.  
```python
def get_password_hash(password):
    return pwd_context.hash(password)
```

`password`: A senha em texto plano que precisa ser hash. 
  
pwd_context.hash(password): Utiliza o método hash do pwd_context para gerar um hash da senha em texto plano. Retorna o hash da senha.  
  
  
[Voltar ao índice](#Índice)
  
---
  
### jwt.py

##### DESCRIÇÃO
Este código implementa a geração e verificação de tokens JWT para autenticação em uma aplicação FastAPI. Ele define funções para criar tokens de acesso e obter o usuário atual a partir do token.
  
---
  
##### CÓDIGO
```python
import os

from datetime import datetime, timedelta

from typing import Optional

from jose import JWTError, jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.controllers import clienteController
from app.schemas.clienteSchema import Cliente
from app.db.database import get_db


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = clienteController.get_cliente_by_id(db, user_id=user_id)
    if user is None:
        raise credentials_exception
    return user
```
  
Detalhamento do Código:  
```python
import os

from datetime import datetime, timedelta

from typing import Optional

from jose import JWTError, jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.controllers import clienteController
from app.schemas.clienteSchema import Cliente
from app.db.database import get_db
```
  
Importações:
`os`: Utilizado para acessar variáveis de ambiente.  
`datetime e timedelta`: Utilizados para manipular datas e tempos.  
`Optional`: Utilizado para anotações de tipos opcionais.  
`jose`: Biblioteca para manipulação de tokens JWT.  
`fastapi`: Importa componentes do FastAPI para tratamento de dependências, exceções HTTP e status.   
`fastapi.security`: Importa OAuth2PasswordBearer para implementar OAuth2.  
`sqlalchemy.orm`: Importa Session para interagir com o banco de dados.  
Importa controladores, esquemas, e função de banco de dados de módulos internos.
  
  
Configurações e Inicializações:  
```python
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```
  
`SECRET_KEY`: Obtém a chave secreta para assinatura dos tokens JWT a partir das variáveis de ambiente.  
`ALGORITHM`: Define o algoritmo de criptografia a ser usado (HS256).  
`ACCESS_TOKEN_EXPIRE_MINUTES`: Define o tempo de expiração dos tokens de acesso (30 minutos).  
`oauth2_scheme`: Configura OAuth2 com o fluxo de senha, especificando o endpoint token para obtenção dos tokens.  
  
  
Função create_access_token:  
Cria um token de acesso JWT com dados fornecidos e um tempo de expiração opcional.  
```python
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```
  
`data`: dict: Dados a serem incluídos no token.  
`expires_delta: Optional[timedelta]`: Tempo opcional de expiração do token.  
  
O que a Função faz:  
Copia os dados fornecidos para to_encode.  
Calcula a data de expiração com base em expires_delta ou um valor padrão de 15 minutos.  
Adiciona a expiração aos dados e codifica o token com a chave secreta e o algoritmo especificado.  
Retorna o token JWT codificado.  
  
  
Função get_current_user:  
Obtém o usuário atual a partir do token JWT fornecido.  
```python
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = clienteController.get_cliente_by_id(db, user_id=user_id)
    if user is None:
        raise credentials_exception
    return user
```
  
`db: Session = Depends(get_db)`: A sessão do banco de dados.  
`token: str = Depends(oauth2_scheme)`: O token JWT obtido através do esquema OAuth2.  
  
  
O que a Função faz:  
- Define uma exceção para credenciais inválidas.
- Tenta decodificar o token JWT usando a chave secreta e o algoritmo especificado.
- Obtém o user_id do payload do token.
- Se o user_id não estiver presente ou ocorrer um erro ao decodificar o token, lança uma exceção.
- Busca o usuário no banco de dados usando o user_id.
- Se o usuário não for encontrado, lança uma exceção.
- Retorna o usuário obtido do banco de dados.
  
  
  [Voltar ao índice](#Índice)
  
---
  

### clienteSchema.py

##### DESCRIÇÃO
Este código define modelos de dados para clientes usando Pydantic, especificando as validações e esquemas necessários para cadastro e representação de clientes na aplicação.  
  
---
  
##### CÓDIGO
```python
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
```
  
Detalhamento do Código:  
Importações:  
`BaseModel` e `EmailStr` do Pydantic: Usados para definir e validar os modelos de dados. BaseModel é a classe base para criar modelos de dados, e EmailStr é um tipo de dado específico para emails que realiza validação automática.
  
Classe ClienteBase:  
Define os campos básicos comuns a todos os modelos de cliente.  
```python
class ClienteBase(BaseModel):
    email: EmailStr
    nome: str
    cpf: str
```
  
`email: EmailStr`: Campo obrigatório para o email, que é validado como um endereço de email.  
`nome: str`: Campo obrigatório para o nome.  
`cpf: str`: Campo obrigatório para o CPF.  
  
Implementação:  
Esta classe serve como base para outros modelos, garantindo que os campos email, nome e cpf estejam presentes e sejam validados.  

  
Classe ClienteCadastro:  
Extende ClienteBase para uso específico no cadastro de clientes. É usada uma docstring para especificar algumas restrições no swagger do fastAPI.  
```python
class ClienteCadastro(ClienteBase):
    '''
    O campo cpf tem limite de tamanho em 14 caracteres sendo a formatação 
    123.456.789-10. O campos email e cpf devem ser obrigatoriamente
    preenchidos pois são primary key
    '''
    pass

```

Doc String:  
- Explica a formatação do campo cpf (14 caracteres no formato 123.456.789-10).  
- Ressalta que os campos email e cpf são obrigatórios e usados como chaves primárias.  

Implementação:  
- Utiliza todos os campos e validações de ClienteBase sem adicionar novos campos ou validações.


  [Voltar ao índice](#Índice)
  
---
  
### configTest.py
🚧 em construção 🚧
##### DESCRIÇÃO
  
---
  
##### CÓDIGO
```python
import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.db.database import engine
from app.db.database import Base, SessionLocal


# Configuração do banco de dados para os testes
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Fixture para gerenciar a sessão do banco de dados
@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Fixture para o cliente de teste
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
```
  
Detalhamento do código  
  
Importações:  
`pytest`: Biblioteca de testes para Python.  
`TestClient do FastAPI`: Cliente de teste para simular requisições HTTP à aplicação FastAPI.  
Importa a aplicação FastAPI (app) e componentes de banco de dados (engine, Base, SessionLocal) da aplicação.  
  
  
Fixture setup_database:  
Configura o banco de dados para os testes.  
```python
# Configuração do banco de dados para os testes
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
```
  
  
`@pytest.fixture(scope="session", autouse=True)`: Define a fixture com escopo de sessão, executada automaticamente uma vez por sessão de testes.  
  
Implementação:  
`Base.metadata.create_all(bind=engine)`: Cria todas as tabelas definidas no modelo Base antes de iniciar os testes.  
`yield`: Pausa a execução da fixture, permitindo a execução dos testes.  
`Base.metadata.drop_all(bind=engine)`: Remove todas as tabelas do banco de dados após a execução dos testes.  
  
  
Fixture db_session:  
Gerencia uma sessão do banco de dados para uso em testes.  
```python
# Fixture para gerenciar a sessão do banco de dados
@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
  
  

`@pytest.fixture`: Define a fixture para ser utilizada em testes individuais.  
  
Implementação:  
`db = SessionLocal()`: Cria uma nova sessão do banco de dados.  
`try`: Inicia um bloco try para utilizar a sessão.  
`yield db`: Fornece a sessão para uso nos testes.  
`finally`: Assegura que a sessão será fechada após o uso, liberando recursos.  
  
  
Fixture client:  
]Cria um cliente de teste para simular requisições HTTP à aplicação FastAPI.  
```python
# Fixture para o cliente de teste
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
```
`@pytest.fixture`: Define a fixture para ser utilizada em testes individuais.  
  
Implementação:  
`with TestClient(app) as c`: Cria uma instância de TestClient com a aplicação FastAPI (app).  
`yield c`: Fornece o cliente de teste para uso nos testes.  


  [Voltar ao índice](#Índice)
  
  ---
  
### clienteTest.py

##### DESCRIÇÃO
Este código implementa testes automatizados para uma aplicação FastAPI que gerencia clientes, utilizando pytest. Ele verifica a funcionalidade de criar clientes, lidar com duplicatas, e buscar clientes por nome e email. Como o código é extenso será falado apenas dos trechos do código.
  
O codigo pode ser testado com o comando:  
certifique se de estar no diretório de tests
```bash
pytest --tb=short --no-header -v arquivo-para-ser-testado
```
  
`--tb=short`: Formato menor do traceback  
`--no-header`: Remove o cabeçalho inicial  
`-v`: por padão o pytest retorna '.' para PASSED e 'F' para FAILED com -v é possível ver qual teste está sendo testado como no exemplo:  
![image](https://github.com/SrJohn369/lu_estilo_API_test_BE/assets/106630200/0efc1ad2-42f9-444f-be5d-10bd0b60141e)  
  


##### Detalhamento do Código
```python
from tests.configTest import *
from app.models.clienteModel import Cliente
```
  
Importações:  
Importa configurações e fixtures necessárias para os testes a partir de tests.configTest.  
Importa o modelo Cliente para uso nos testes.  
  
  
Teste test_post_cliente:  
Testa o endpoint de cadastro de cliente (POST [/clientes/](#Clientes)).  
```python
# TESTE POST/ cadastro usuario
def test_post_cliente(client):
    response = client.post(
        "/clientes/", 
        json={
            "email": "test4@example.com", 
            "nome": "Test User", 
            "cpf": "123402678901", 
        }
    )
    assert response.status_code == 200, f"Returned: {response.status_code}"
    assert response.json()["email"] == "test4@example.com", \
        f"Returned: {response.json()['email']}"
```
  
Implementação:  
Envia uma requisição POST para [/clientes/](#Clientes) com dados de um novo cliente.  
Verifica se o status da resposta é 200 (OK).  
Verifica se o email do cliente retornado na resposta é o esperado (test4@example.com).  
  
  
Teste test_post_cliente_Error_400:  
Testa o endpoint de cadastro de cliente para lidar com duplicatas (POST [/clientes/](#Clientes)).  
```python
# TESTE POST/ cadastro do mesmo usuario para gerar um 400
def test_post_cliente_Error_400(client):
    response = client.post(
        "/clientes/",
        json={
            "email": "test4@example.com",
            "nome": "Test User",
            "cpf": "123402678901",
        }
    )
    assert response.status_code == 400, f"Returned: {response.status_code}"
```
  
Implementação:  
Envia uma requisição POST para [/clientes/](#Clientes) com os mesmos dados de um cliente já existente.  
Verifica se o status da resposta é 400 (Bad Request), indicando que o cliente já existe.  
  
  
Teste test_get_clientes:  
Testa o endpoint de listagem de clientes (GET [/clientes/](#Clientes)).  
```python
# TESTE GET/ todos clientes
def test_get_clientes(client, db_session):
    db_session.add(
        Cliente(
            email="alice@example.com",
            nome="Alice",
            cpf="12345678902"
        )
    )
    db_session.add(
        Cliente(
            email="bob@example.com",
            nome="Bob",
            cpf="12345678903"
        )
    )
    db_session.commit()

    response = client.get("/clientes/")
    assert response.status_code == 200, f"Returned: {response.status_code}"
    users = response.json()
    assert len(users) >= 2, f"Retorno dado: {users}"
```
  
Implementação:  
Adiciona dois clientes (Alice e Bob) diretamente no banco de dados.  
Envia uma requisição GET para [/clientes/](#Clientes).  
Verifica se o status da resposta é 200 (OK).  
Verifica se a lista de clientes retornada contém pelo menos 2 clientes.  
  
  
Teste test_get_cliente_by_nome:  
Testa o endpoint de listagem de clientes com filtro por nome (GET [/clientes/?nome=Alice](#Clientes)).  
```python
# TESTE GET/ filtro por nome
def test_get_cliente_by_nome(client):
    response = client.get("/clientes/?nome=Alice")
    assert response.status_code == 200, f"Returned: {response.status_code}"
    users = response.json()
    assert len(users) == 1, f"Returned: {users}"
    assert users[0]["nome"] == "Alice", f"Returned: {users}"
```
  
Implementação:  
Envia uma requisição GET para [/clientes/](#Clientes) com o parâmetro de consulta nome=Alice.  
Verifica se o status da resposta é 200 (OK).  
Verifica se a lista de clientes retornada contém exatamente um cliente e se o nome do cliente é Alice.  
  
  
Teste test_get_cliente_by_email:  
Testa o endpoint de listagem de clientes com filtro por email (GET [/clientes/?email=bob@example.com](#Clientes)).  
```python
# TESTE GET/ filtro por email
def test_get_cliente_by_email(client):
    response = client.get("/clientes/?email=bob@example.com")
    assert response.status_code == 200, f"Returned: {response.status_code}"
    users = response.json()
    assert len(users) == 1, f"Returned: {users}"
    assert users[0]["email"] == "bob@example.com", f"Returned: {users}"
```
  
Implementação:  
Envia uma requisição GET para [/clientes/](#Clientes) com o parâmetro de consulta email=bob@example.com.  
Verifica se o status da resposta é 200 (OK).  
Verifica se a lista de clientes retornada contém exatamente um cliente e se o email do cliente é bob@example.com  


[Voltar ao índice](#Índice)
