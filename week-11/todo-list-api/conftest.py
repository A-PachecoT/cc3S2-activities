# tests/conftest.py
import pytest
from api_client import APIClient
from todo_service import TodoService

@pytest.fixture
def api_client():
    base_url = "https://example.com"
    return APIClient(base_url)

@pytest.fixture
def todo_service(api_client):
    return TodoService(api_client)