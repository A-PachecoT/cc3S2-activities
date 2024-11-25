import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.routes.user_routes import configure_routes
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository
from src.models.user import User

@pytest.fixture
def test_app():
    app = FastAPI()
    repository = UserRepository()
    service = UserService(repository)
    app.include_router(configure_routes(service))
    return app

@pytest.fixture
def client(test_app):
    return TestClient(test_app)

@pytest.fixture
def usuario_datos():
    return {
        "username": "andre",
        "email": "andre.pacheco.t@uni.pe"
    }

def test_create_user_route(client, usuario_datos):
    # Arrange - Cliente ya está configurado por el fixture
    
    # Act
    response = client.post("/users/", json=usuario_datos)
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "andre"
    assert data["email"] == "andre.pacheco.t@uni.pe"
    assert "id" in data

def test_get_user_by_id_route(client):
    # Arrange
    create_response = client.post(
        "/users/",
        json={"username": "usuario_prueba", "email": "usuario_prueba@gmail.com"}
    )
    user_id = create_response.json()["id"]
    
    # Act
    response = client.get(f"/users/{user_id}")
    
    # Assert
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    assert user["username"] == "usuario_prueba"

def test_get_non_existent_user_route(client):
    # Act
    response = client.get("/users/123456")
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontró el usuario"

def test_update_user_route(client, usuario_datos):
    # Arrange
    create_response = client.post("/users/", json=usuario_datos)
    user_id = create_response.json()["id"]
    datos_actualizados = {
        "username": "andre_actualizado",
        "email": "andre.pacheco.t@uni.pe"
    }
    
    # Act
    update_response = client.put(f"/users/{user_id}", json=datos_actualizados)
    
    # Assert
    assert update_response.status_code == 200
    updated_user = update_response.json()
    assert updated_user["username"] == "andre_actualizado"
    assert updated_user["email"] == "andre.pacheco.t@uni.pe"

def test_update_non_existent_user_route(client):
    # Act
    response = client.put(
        "/users/123456",
        json={"username": "usuario_actualizado", "email": "usuario_actualizado@gmail.com"}
    )
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontró el usuario"

def test_delete_user_route(client):
    # Arrange
    create_response = client.post(
        "/users/",
        json={"username": "usuario_prueba", "email": "usuario_prueba@gmail.com"}
    )
    user_id = create_response.json()["id"]
    
    # Act
    delete_response = client.delete(f"/users/{user_id}")
    
    # Assert
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Usuario eliminado exitosamente"
    
    # Assert
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404

def test_delete_non_existent_user_route(client):
    # Act
    response = client.delete("/users/123456")
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontró el usuario" 