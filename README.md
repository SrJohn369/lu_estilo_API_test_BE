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

---

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

Incluímos as rotas definidas em clienteView na nossa aplicação FastAPI.
```python
app.include_router(clienteView.router)
```

---

### clienteModel.py
🚧 em construção 🚧
### clienteView.py
🚧 em construção 🚧
### clienteController.py
🚧 em construção 🚧
### database.py
🚧 em construção 🚧
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
