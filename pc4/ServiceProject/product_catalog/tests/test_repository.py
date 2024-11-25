import pytest
from src.repositories.product_repository import ProductRepository
from src.schemas.product import ProductCreate

@pytest.fixture
def repository():
    return ProductRepository()

@pytest.fixture
def sample_product():
    return ProductCreate(name="test", price=100.0)

async def test_create_product(repository, sample_product):
    # Arrange - usando fixture

    # Act
    product = await repository.create(sample_product)

    # Assert
    assert product.id == 1
    assert product.name == "test"
    assert product.price == 100.0

async def test_get_product(repository, sample_product):
    # Arrange
    product = await repository.create(sample_product)

    # Act
    found = await repository.get_by_id(1)

    # Assert
    assert found.id == product.id
    assert found.name == product.name

async def test_get_all_products(repository, sample_product):
    # Arrange
    product1 = await repository.create(sample_product)
    product2 = await repository.create(ProductCreate(name="test2", price=123.0))

    # Act
    products = await repository.get_all()

    # Assert
    assert len(products) == 2
    assert products[0].id == product1.id
    assert products[1].id == product2.id

async def test_update_product(repository, sample_product):
    # Arrange
    product = await repository.create(sample_product)
    update_data = ProductCreate(name="actualizado", price=1234.0)

    # Act
    updated = await repository.update(product.id, update_data)

    # Assert
    assert updated.name == "actualizado"
    assert updated.price == 1234.0

async def test_delete_product(repository, sample_product):
    # Arrange
    product = await repository.create(sample_product)

    # Act
    result = await repository.delete(product.id)
    products = await repository.get_all()

    # Assert
    assert result is True
    assert len(products) == 0 