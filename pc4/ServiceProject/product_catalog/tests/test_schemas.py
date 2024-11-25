import pytest
from src.schemas.product import Product, ProductCreate

def test_create_product_schema():
    # Arrange
    product_data = {
        "name": "Papa",
        "description": "Papa de los Andes",
        "price": 2.5
    }

    # Act
    product = ProductCreate(**product_data)

    # Assert
    assert product.name == "Papa"
    assert product.description == "Papa de los Andes"
    assert product.price == 2.5

def test_product_schema():
    # Arrange
    product_data = {
        "id": 1,
        "name": "Papa",
        "description": "Papa de los Andes",
        "price": 2.5
    }

    # Act
    product = Product(**product_data)

    # Assert
    assert product.id == 1
    assert product.name == "Papa"
    assert product.description == "Papa de los Andes"
    assert product.price == 2.5

def test_invalid_price():
    # Arrange
    product_data = {
        "name": "Papa",
        "description": "Papa de los Andes",
        "price": -2.5
    }

    # Act & Assert
    with pytest.raises(ValueError):
        ProductCreate(**product_data)