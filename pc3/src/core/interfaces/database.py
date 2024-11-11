from abc import ABC, abstractmethod
from typing import Optional
from src.models.encrypted_data import EncryptedData

class Database(ABC):
    """
    Interfaz que define las operaciones de base de datos.
    Esto incluye guardar, obtener y eliminar datos cifrados.
    """
    @abstractmethod
    def save(self, data: EncryptedData) -> str:
        pass
    
    @abstractmethod
    def get(self, id: str) -> Optional[EncryptedData]:
        pass
    
    @abstractmethod
    def delete(self, id: str) -> bool:
        pass 