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
  
</details>

<details>
  
  <summary>POST/clientes</summary>
  
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

---  


### database.py
🚧 em construção 🚧
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
### auth.py
🚧 em construção 🚧
### jwt.py
🚧 em construção 🚧
### clienteSchema.py
🚧 em construção 🚧
### configTest.py
🚧 em construção 🚧
### clienteTest.py
🚧 em construção 🚧
