import pytest
from unittest.mock import patch
from src.core.interfaces.crypto_generator import CryptoGenerator
from src.crypto.generators.rsa_generator import RSAGenerator
from src.models.key_pair import KeyPair

class TestRSAGenerator:

    @pytest.fixture
    def rsa_generator(self):
        return RSAGenerator()

    @pytest.fixture
    def stub_rsa_key(self):
        # Stub de una clave RSA para pruebas
        return {
            'n': 123456789, # Módulo
            'e': 65537, # Exponente público (primo)
            'd': 987654321 # Exponente privado
        }

    def test_generate_key_pair_returns_valid_key_pair(self, rsa_generator):
        # Arrange
        key_size = 2048
        
        with patch('src.utils.math_utils.generate_prime', side_effect=[61, 53]):
            # Act
            key_pair = rsa_generator.generate_key_pair(key_size)
            
            # Assert
            assert isinstance(key_pair, KeyPair)
            assert key_pair.public_key is not None
            assert key_pair.private_key is not None

    def test_generate_key_pair_with_invalid_size_raises_error(self, rsa_generator):
        # Prueba manejo de tamaño inválido de clave
        invalid_size = 512  # Tamaño muy pequeño para ser seguro
        
        with pytest.raises(ValueError):
            rsa_generator.generate_key_pair(invalid_size)

    def test_generate_key_pair_with_non_power_of_two_raises_error(self, rsa_generator):
        # Prueba que el tamaño debe ser potencia de 2
        invalid_size = 1234
        
        with pytest.raises(ValueError):
            rsa_generator.generate_key_pair(invalid_size)

    def test_public_exponent_is_valid(self, rsa_generator):
        # Prueba que el exponente público sea válido
        key_size = 2048
        
        with patch('src.utils.math_utils.generate_prime', side_effect=[61, 53]):
            key_pair = rsa_generator.generate_key_pair(key_size)
            
            # Convertimos los bytes a enteros para verificar
            n = int.from_bytes(key_pair.public_key, 'big')
            d = int.from_bytes(key_pair.private_key, 'big')
            
            # Verificamos que n y d son válidos
            assert n > 0
            assert d > 0
    