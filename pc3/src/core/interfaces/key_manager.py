from abc import ABC, abstractmethod
from src.models.key_pair import KeyPair

class KeyManager(ABC):
    """
    Interfaz que gestiona un par de claves.
    Esto incluye almacenar, obtener y eliminar un par de claves.
    """
    @abstractmethod
    def store_key_pair(self, key_pair: KeyPair) -> str:
        pass
    
    @abstractmethod
    def get_key_pair(self, id: str) -> KeyPair:
        pass 

    @abstractmethod
    def delete_key_pair(self, id: str) -> bool:
        pass 