import pytest
from src.services.product_service import ProductService
from src.schemas.product import ProductCreate
from src.repositories.product_repository import ProductRepository

@pytest.fixture
def service():
    repository = ProductRepository()
    return ProductService(repository)

@pytest.fixture
def valid_product():
    return ProductCreate(name="test", price=100.0)

# Tests de Creación
async def test_create_valid_product(service, valid_product):
    # Arrange - usando fixture

    # Act
    product = await service.create(valid_product)

    # Assert
    assert product.id == 1
    assert product.name == "test"
    assert product.price == 100.0

async def test_create_product_invalid_price(service):
    # Arrange
    invalid_product = ProductCreate(name="test", price=-100.0)

    # Act & Assert
    with pytest.raises(ValueError, match="El precio debe ser mayor a 0"):
        await service.create(invalid_product)

async def test_create_product_empty_name(service):
    # Arrange
    invalid_product = ProductCreate(name="   ", price=100.0) #Espacios en blanco

    # Act & Assert
    with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
        await service.create(invalid_product)

# Tests de Lectura
async def test_get_products_ordered(service, valid_product):
    # Arrange
    await service.create(valid_product)
    await service.create(ProductCreate(name="test2", price=123.0))

    # Act
    products = await service.get_all()

    # Assert
    assert len(products) == 2
    assert products[0].id < products[1].id

async def test_get_product_invalid_id(service):
    # Arrange & Act
    product = await service.get_by_id(-1)

    # Assert
    assert product is None

# Tests de Actualización
async def test_update_product_validation(service, valid_product):
    # Arrange
    product = await service.create(valid_product)
    invalid_update = ProductCreate(name="", price=100.0)

    # Act & Assert
    with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
        await service.update(product.id, invalid_update)

# Tests de Eliminación
async def test_delete_invalid_id(service):
    # Arrange & Act
    result = await service.delete(-1)

    # Assert
    assert result is False 