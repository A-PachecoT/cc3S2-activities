import pytest
from unittest.mock import patch
from src.crypto.strategies.rsa_strategy import RSAStrategy

class TestRSAStrategy:
    @pytest.fixture
    def rsa_strategy(self):
        return RSAStrategy(block_size=1) # Como los mensajes son cortos, usamos un bloque de 1 byte

    # Test para verificar que el cifrado devuelve un texto cifrado válido
    def test_encrypt_returns_valid_ciphertext(self, rsa_strategy):
        # Arrange
        data = "Hola mundo"
        # Clave pública (n=33, e=7)
        key = (33).to_bytes(4, 'big') + (7).to_bytes(4, 'big')
        
        # Act
        encrypted = rsa_strategy.encrypt(data, key)
        
        # Assert
        assert encrypted is not None
        assert isinstance(encrypted, bytes)
        assert len(encrypted) > 0

    # Test para verificar que el descifrado devuelve el mensaje original
    def test_decrypt_returns_original_message(self, rsa_strategy):
        # Arrange
        original = "Hola mundo"
        # Clave pública (n=33, e=7) y privada (d=3)
        pub_key = (33).to_bytes(4, 'big') + (7).to_bytes(4, 'big')
        priv_key = (33).to_bytes(4, 'big') + (3).to_bytes(4, 'big')
        
        # Act
        encrypted = rsa_strategy.encrypt(original, pub_key)
        decrypted = rsa_strategy.decrypt(encrypted, priv_key)
        
        # Assert
        assert decrypted == original

    # Test para verificar que el cifrado con un mensaje largo usa bloques
    def test_encrypt_with_large_message_uses_blocks(self, rsa_strategy):
        # Arrange
        data = "x" * 1000  # Mensaje largo
        n = 65535
        key = (n).to_bytes(4, 'big') + (65537).to_bytes(4, 'big')
        
        # Act
        encrypted = rsa_strategy.encrypt(data, key)
        
        # Assert
        assert len(encrypted) > len(data)

    # Test para verificar que un formato de clave inválido lanza un error
    def test_invalid_key_format_raises_error(self, rsa_strategy):
        # Arrange
        data = "test"
        invalid_key = b'invalid'
        
        # Act & Assert
        with pytest.raises(ValueError):
            rsa_strategy.encrypt(data, invalid_key) 
    
    # Test para verificar que un formato de clave inválido lanza un error en el descifrado
    def test_invalid_key_format_raises_error_decrypt(self, rsa_strategy):
        # Arrange
        data = b'test'
        invalid_key = b'invalido'
        
        # Act & Assert
        with pytest.raises(ValueError):
            rsa_strategy.decrypt(data, invalid_key)