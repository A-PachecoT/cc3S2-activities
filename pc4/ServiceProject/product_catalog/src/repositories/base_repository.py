# Clase abstracta base para los repositorios
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def get_by_id(self, id: int):
        pass

    @abstractmethod
    async def create(self, data):
        pass

    @abstractmethod
    async def update(self, id: int, data):
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass 