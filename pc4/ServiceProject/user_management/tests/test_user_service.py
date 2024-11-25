import pytest
from src.models.user import User
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository

@pytest.fixture
def service():
    repository = UserRepository()
    return UserService(repository)

@pytest.fixture
def usuario_prueba():
    return User(username="andre", email="andre.pacheco.t@uni.pe")

def test_create_user(service, usuario_prueba):
    # Arrange - Service ya está configurado por el fixture
    
    # Act - Creamos el usuario
    created_user = service.create_user(usuario_prueba)
    
    # Assert - Verificamos la creación
    assert created_user.id is not None
    assert created_user.username == "andre"
    assert created_user.email == "andre.pacheco.t@uni.pe"

def test_get_all_users(service):
    user1 = User(username="user1", email="user1@example.com")
    user2 = User(username="user2", email="user2@example.com")
    service.create_user(user1)
    service.create_user(user2)
    users = service.get_all_users()
    assert len(users) == 2

def test_get_user_by_id(service):
    user = User(username="test_user", email="test@example.com")
    created_user = service.create_user(user)
    found_user = service.get_user_by_id(created_user.id)
    assert found_user is not None
    assert found_user.id == created_user.id

def test_get_non_existent_user(service):
    found_user = service.get_user_by_id(999)
    assert found_user is None

def test_update_user(service, usuario_prueba):
    # Arrange - Creamos usuario inicial y preparamos datos de actualización
    created_user = service.create_user(usuario_prueba)
    updated_data = User(username="andre_actualizado", 
                       email="andre.pacheco.t@uni.pe")
    
    # Act - Actualizamos el usuario
    updated_user = service.update_user(created_user.id, updated_data)
    
    # Assert - Verificamos la actualización
    assert updated_user is not None
    assert updated_user.username == "andre_actualizado"
    assert updated_user.email == "andre.pacheco.t@uni.pe"

def test_delete_user(service):
    user = User(username="test_user", email="test@example.com")
    created_user = service.create_user(user)
    assert service.delete_user(created_user.id) is True
    assert service.get_user_by_id(created_user.id) is None 