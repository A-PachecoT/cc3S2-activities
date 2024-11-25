import pytest
from src.models.user import User
from src.repositories.user_repository import UserRepository

@pytest.fixture
def repository():
    return UserRepository()

@pytest.fixture
def usuario_prueba():
    return User(username="andre", email="andre.pacheco.t@uni.pe")

def test_create_user(repository, usuario_prueba):
    # Arrange - Repository ya está configurado por el fixture
    
    # Act - Creamos el usuario
    created_user = repository.create(usuario_prueba)
    
    # Assert - Verificamos la creación correcta
    assert created_user.id == 1
    assert created_user.username == "andre"
    assert created_user.email == "andre.pacheco.t@uni.pe"

def test_get_all_users(repository, usuario_prueba):
    user1 = User(username="usuario1", email="usuario1@gmail.com")
    user2 = User(username="usuario2", email="usuario2@gmail.com")
    repository.create(usuario_prueba)
    repository.create(user1)
    repository.create(user2)
    users = repository.get_all()
    assert len(users) == 3

def test_get_user_by_id(repository, usuario_prueba):
    created_user = repository.create(usuario_prueba)
    found_user = repository.get_by_id(created_user.id)
    assert found_user is not None
    assert found_user.id == created_user.id

def test_get_non_existent_user(repository):
    found_user = repository.get_by_id(999)
    assert found_user is None

def test_update_user(repository, usuario_prueba):
    # Arrange - Creamos un usuario inicial
    created_user = repository.create(usuario_prueba)
    updated_data = User(username="andre_actualizado", 
                       email="andre.pacheco.t@uni.pe")
    
    # Act - Actualizamos el usuario
    updated_user = repository.update(created_user.id, updated_data)
    
    # Assert - Verificamos la actualización
    assert updated_user is not None
    assert updated_user.username == "andre_actualizado"
    assert updated_user.email == "andre.pacheco.t@uni.pe"

def test_delete_user(repository):
    created_user = repository.create(usuario_prueba)
    assert repository.delete(created_user.id) is True
    assert repository.get_by_id(created_user.id) is None 