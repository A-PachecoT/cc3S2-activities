from abc import ABC, abstractmethod

class CryptoStrategy(ABC):
    """
    Interfaz que define las operaciones de cifrado y descifrado.
    """
    @abstractmethod
    def encrypt(self, data: str, key: bytes) -> bytes:
        pass
    
    @abstractmethod
    def decrypt(self, encrypted_data: bytes, key: bytes) -> str:
        pass 