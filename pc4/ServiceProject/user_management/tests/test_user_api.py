import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.fixture
def usuario_datos():
    return {
        "username": "andre",
        "email": "andre.pacheco.t@uni.pe"
    }

def test_create_user(usuario_datos):
    # Arrange
    # No se requiere configuración adicional
    
    # Act
    response = client.post("/users/", json=usuario_datos)
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "andre"
    assert data["email"] == "andre.pacheco.t@uni.pe"
    assert "id" in data

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user(usuario_datos):
    # Arrange - Primero creamos un usuario de prueba
    create_response = client.post("/users/", json=usuario_datos)
    user_id = create_response.json()["id"]
    
    # Act - Obtenemos el usuario creado
    response = client.get(f"/users/{user_id}")
    
    # Assert - Verificamos los datos
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["username"] == "andre"

def test_get_non_existent_user():
    response = client.get("/users/123456")
    assert response.status_code == 404

def test_update_user():
    # First create a user
    create_response = client.post(
        "/users/",
        json={"username": "usuario_prueba", "email": "usuario_prueba@gmail.com"}
    )
    user_id = create_response.json()["id"]
    
    # Then update the user
    response = client.put(
        f"/users/{user_id}",
        json={"username": "usuario_actualizado", "email": "usuario_actualizado@gmail.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "usuario_actualizado"
    assert data["email"] == "usuario_actualizado@gmail.com"

def test_delete_user():
    # First create a user
    create_response = client.post(
        "/users/",
        json={"username": "usuario_prueba", "email": "usuario_prueba@gmail.com"}
    )
    user_id = create_response.json()["id"]
    
    # Then delete the user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    
    # Verify user is deleted
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404 