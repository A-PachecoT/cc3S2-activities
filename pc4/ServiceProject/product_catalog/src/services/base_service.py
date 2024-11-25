# Operaciones CRUD para el servicio (clase abstracta)
from abc import ABC, abstractmethod

class BaseService(ABC):
    # -- Leer --
    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def get_by_id(self, id: int):
        pass

    # -- Crear --
    @abstractmethod
    async def create(self, data):
        pass

    # -- Actualizar --
    @abstractmethod
    async def update(self, id: int, data):
        pass

    # -- Eliminar --
    @abstractmethod
    async def delete(self, id: int):
        pass 