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
### Clientes
🚧 em construção 🚧
### Produtos 
🚧 em construção 🚧
### Pedidos
🚧 em construção 🚧

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


### main.py
🚧 em construção 🚧
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
