from src.core.interfaces.crypto_strategy import CryptoStrategy
from typing import Tuple
import math

class RSAStrategy(CryptoStrategy):
    """Implementación de la estrategia de cifrado RSA"""
    
    def __init__(self, block_size: int = 4):
        self._block_size = block_size

    def encrypt(self, data: str, key: bytes) -> bytes:
        """Cifra datos usando RSA"""
        try:
            # Obtener componentes de la clave (n, e)
            n, e = self._bytes_to_key_components(key)
            
            # Convertir mensaje a bytes y bloques
            message_bytes = data.encode('utf-8')
            blocks = self._bytes_to_blocks(message_bytes)
            
            # Cifrar cada bloque: c = m^e mod n
            encrypted_blocks = []
            for block in blocks:
                if block >= n:
                    raise ValueError("Mensaje demasiado grande para la clave")
                encrypted_block = pow(block, e, n)
                encrypted_blocks.append(encrypted_block)
            
            return self._blocks_to_bytes(encrypted_blocks)
            
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise RuntimeError(f"Error en el cifrado RSA: {str(e)}")

    def decrypt(self, encrypted_data: bytes, key: bytes) -> str:
        """Descifra datos usando RSA"""
        try:
            # Obtener componentes de la clave (n, d)
            n, d = self._bytes_to_key_components(key)
            
            # Convertir datos cifrados a bloques
            encrypted_blocks = self._bytes_to_blocks(encrypted_data)
            
            # Descifrar cada bloque: m = c^d mod n
            decrypted_blocks = []
            for block in encrypted_blocks:
                if block >= n:
                    raise ValueError("Bloque cifrado inválido")
                decrypted_block = pow(block, d, n)
                decrypted_blocks.append(decrypted_block)
            
            # Convertir bloques a bytes y luego a string
            decrypted_bytes = self._blocks_to_bytes(decrypted_blocks)
            return decrypted_bytes.decode('utf-8')
            
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise RuntimeError(f"Error en el descifrado RSA: {str(e)}")

    def _bytes_to_key_components(self, key: bytes) -> Tuple[int, int]:
        """Convierte bytes de la clave a componentes RSA (n, e/d)"""
        if len(key) < 8:
            raise ValueError("Formato de clave inválido")
        n = int.from_bytes(key[:4], 'big')
        exp = int.from_bytes(key[4:8], 'big')
        return n, exp

    def _bytes_to_blocks(self, data: bytes) -> list:
        """Convierte bytes a bloques de números"""
        blocks = []
        for i in range(0, len(data), self._block_size):
            block = int.from_bytes(data[i:i+self._block_size], 'big')
            blocks.append(block)
        return blocks

    def _blocks_to_bytes(self, blocks: list) -> bytes:
        """Convierte bloques de números a bytes"""
        result = b''
        for block in blocks:
            size = max(1, math.ceil(block.bit_length() / 8))
            result += block.to_bytes(size, 'big')
        return result