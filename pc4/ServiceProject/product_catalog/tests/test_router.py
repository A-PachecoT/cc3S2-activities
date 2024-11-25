import pytest
from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_product_data():
    return {
        "name": "test",
        "description": "un testeo de software",
        "price": 100.0
    }

def test_get_products_empty(client):
    # Arrange & Act
    response = client.get("/products/")
    
    # Assert
    assert response.status_code == 200
    assert response.json() == []

def test_create_and_get_product(client, valid_product_data):
    # Arrange
    client.post("/products/", json=valid_product_data)
    
    # Act
    response = client.get("/products/")
    
    # Assert
    assert response.status_code == 200
    products = response.json()
    assert len(products) == 1
    assert products[0]["name"] == valid_product_data["name"]

def test_create_product(client, valid_product_data):
    # Arrange & Act
    response = client.post("/products/", json=valid_product_data)
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == valid_product_data["name"]
    assert "id" in data

def test_create_invalid_product(client):
    # Arrange
    invalid_data = {
        "name": "test",
        "price": -123.0
    }
    
    # Act
    response = client.post("/products/", json=invalid_data)
    
    # Assert
    assert response.status_code == 422 # error de validación

def test_update_product(client, valid_product_data):
    # Arrange
    create_response = client.post("/products/", json=valid_product_data)
    product_id = create_response.json()["id"]
    update_data = {
        "name": "actualizado",
        "description": "una actualización del SaaS",
        "price": 1234.0
    }
    
    # Act
    response = client.put(f"/products/{product_id}", json=update_data)
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "actualizado"
    assert data["price"] == 1234.0

def test_update_nonexistent_product(client, valid_product_data):
    # Arrange & Act
    response = client.put("/products/123123", json=valid_product_data)
    
    # Assert
    assert response.status_code == 404 # no encontrado

def test_delete_product(client, valid_product_data):
    # Arrange
    create_response = client.post("/products/", json=valid_product_data)
    product_id = create_response.json()["id"]
    
    # Act
    response = client.delete(f"/products/{product_id}")
    
    # Assert
    assert response.status_code == 200
    
    # Verificar eliminación
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404 