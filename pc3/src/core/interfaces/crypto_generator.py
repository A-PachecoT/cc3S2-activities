from abc import ABC, abstractmethod
from src.models.key_pair import KeyPair

class CryptoGenerator(ABC):
    """
    Interfaz que genera un par de claves.
    """
    @abstractmethod
    def generate_key_pair(self, key_size: int) -> KeyPair:
        pass 