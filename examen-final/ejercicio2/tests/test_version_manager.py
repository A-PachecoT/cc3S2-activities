import pytest
from datetime import datetime
from src.persistence.version_manager import VersionManager


@pytest.fixture
def version_manager():
    return VersionManager()


def test_version_creation(version_manager):
    # Arrange está en el fixture

    # Act
    version = version_manager.create_version("Andre Testing", {"author": "test"})

    # Assert
    assert version == 0
    assert version_manager.version_exists(version)


def test_version_retrieval(version_manager):
    # Arrange está en el fixture

    # Act
    version = version_manager.create_version("Andre Testing", {"author": "test"})
    metadata = version_manager.get_version_metadata(version)

    # Assert
    assert metadata.description == "Andre Testing"
    assert metadata.metadata["author"] == "test"
    assert isinstance(metadata.timestamp, datetime)


def test_invalid_version(version_manager):
    # Arrange está en el fixture

    # Assert
    assert not version_manager.version_exists(0)
    assert version_manager.get_version_metadata(0) is None


def test_version_metadata(version_manager):
    # Arrange
    metadata = {"author": "test", "type": "update"}

    # Act
    version = version_manager.create_version("Testeando version manager", metadata)

    # Assert
    retrieved = version_manager.get_version_metadata(version)
    assert retrieved.metadata == metadata
    assert retrieved.description == "Testeando version manager"
