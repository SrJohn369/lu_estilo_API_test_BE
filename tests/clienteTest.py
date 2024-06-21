from tests.configTest import *
from app.models.clienteModel import Cliente
        

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
        f"Returned: {response.json()["email"]}"
    

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
    assert response.status_code == 400, f"Retorno dado: {response.status_code}"


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
    assert response.status_code == 200, f"Retorno dado: {response.status_code}"
    users = response.json()
    assert len(users) >= 2, f"Retorno dado: {len(users)}"


# TESTE GET/ filtro por nome
def test_get_cliente_by_nome(client):
    response = client.get("/clientes/?nome=Alice")
    assert response.status_code == 200, f"Retorno dado: {response.status_code}"
    users = response.json()
    assert len(users) == 1, f"Returned: {len(users)}"
    assert users[0]["nome"] == "Alice", f"Retorno dado: {users[0]["nome"]}"
    

# TESTE GET/ filtro por nome ERROR 404    
def test_get_cliente_by_nome_Error_404(client):
    response = client.get("/clientes/?nome=Cleusa")
    assert response.status_code == 404, f"Retorno dado: {response.status_code}"


# TESTE GET/ filtro por email
def test_get_cliente_by_email(client):
    response = client.get("/clientes/?email=bob@example.com")
    assert response.status_code == 200, f"Retorno dado: {response.status_code}"
    users = response.json()
    assert len(users) == 1, f"Returned: {len(users)}"
    assert users[0]["email"] == "bob@example.com", f"Returned: {users[0]["email"]}"


# TESTE GET/ filtro por email ERROR 404    
def test_get_cliente_by_email_Error_404(client):
    response = client.get("/clientes/?nome=Cleusa.fatima@email.com")
    assert response.status_code == 404, f"Retorno dado: {response.status_code}"


# TESTE GET/ clientes por ID
def test_get_clientes_by_id(client, db_session):
    db_session.add(
        Cliente(
            email="alice@example.com",
            nome="Alice",
            cpf="12345678902",
            id="348e-56f6"
        )
    )
    db_session.commit()

    response = client.get("/clientes/348e-56f6")
    assert response.status_code == 200, f"Retorno dado: {response.status_code}"
    users = response.json()
    assert users["id"] == "348e-56f6", f"Retorno dado: {users["id"]}"
    
    
# TESTE GET/ filtro por id ERROR 404    
def test_get_cliente_by_id_Error_404(client):
    response = client.get("/clientes/123456ewert")
    assert response.status_code == 404, f"Retorno dado: {response.status_code}"
    

# TESTE PUT/ Atualiza dados    
def test_put_cliete(client):
    response = client.put(
        '/clientes/348e-56f6',
        json={
            'email': 'cleusa.email@email.com',
            'nome': 'Cleusa',
            'cpf': '123.456.789-02'
        }
    )
    
    assert response.status_code == 200, f"Retorno dado: {response.status_code}"
    assert response.json() == {'email': 'cleusa.email@email.com',
                               'nome': 'Cleusa',
                               'cpf': '123.456.789-02',
                               'id': '348e-56f6'}, f"Retorno dado: {response.status_code}"
    

# TESTE PUT/ Atualiza dados Error 422
def test_put_cliete_Error_422(client):
    response = client.put(
        '/clientes/348e-56f6',
        json={
            'nome': 'Cláudia',
        }
    )
    assert response.status_code == 422, f"Retorno dado: {response.status_code}"
    

# TESTE PUT/ Atualiza dados Error 404
def test_put_cliete_Error_404(client):
    response = client.put(
        '/clientes/348e-56f6-556e',
        json={
            'email': 'cleusa.email@email.com',
            'nome': 'Cláudia',
            'cpf': '123.456.789-02'
        }
    )
    assert response.status_code == 404, f"Retorno dado: {response.status_code}"
    
    
# TESTE PATCH/ Atualiza parcialmente
def test_patch_cliente(client):
    response = client.patch(
        '/clientes/348e-56f6',
        json={
            'nome': 'Júlia',
        }
    )
    user = response.json()
    assert response.status_code == 200, f"Retorno dado: {response.status_code}"
    assert user["nome"] == "Júlia", f"Retorno dado: {user["nome"]}"
    
 
 # TESTE PATCH/ Atualiza parcialmente Error 422
def test_patch_cliente_Error_422(client):
    response = client.patch('/clientes/348e-56ere6')
    assert response.status_code == 422, f"Retorno dado: {response.status_code}"
    

# TESTE PATCH/ Atualiza parcialmente Error 404
def test_patch_cliente_Error_404(client):
    response = client.patch(
        '/clientes/348e-56ere6',
        json={
            'nome': 'José',
        }
    )
    assert response.status_code == 404, f"Retorno dado: {response.status_code}"
    
    
# TEST DELETE/ Deleta um cliete
def test_delete_cliete(client):
    response = client.delete('/clientes/348e-56f6')
    assert response.status_code == 200, f"Retorno dado: {response.status_code}"
    
    
# TEST DELETE/ Error 404
def test_delete_cliete_Error_404(client):
    response = client.delete('/clientes/348e-5-556e')
    assert response.status_code == 404, f"Retorno dado: {response.status_code}"