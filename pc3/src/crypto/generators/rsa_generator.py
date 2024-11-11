from src.core.interfaces.crypto_generator import CryptoGenerator
from src.models.key_pair import KeyPair
from src.utils.math_utils import (
    generate_prime, 
    mod_inverse, 
    is_power_of_two
)
from math import gcd

class RSAGenerator(CryptoGenerator):
    """Implementación del generador de claves RSA
    
    Basado en https://www.askpython.com/python/examples/rsa-algorithm-in-python
    De acuerdo al artículo, el algoritmo para RSA es el siguiente:
    1. Select 2 prime numbers, preferably large, p and q.
    2. Calculate n = p*q.
    3. Calculate phi(n) = (p-1)*(q-1)
    4. Choose a value of e such that 1<e<phi(n) and gcd(phi(n), e) = 1.
    5. Calculate d such that d = (e^-1) mod phi(n).
    """
    
    def __init__(self, valid_exponents=None, min_key_size=2048):
        # Exponentes públicos comunes y seguros por defecto
        self._valid_exponents = valid_exponents or {3, 5, 17, 257, 65537}
        self._min_key_size = min_key_size

    def generate_key_pair(self, key_size: int) -> KeyPair:
        """Genera un par de claves RSA"""
        if key_size < self._min_key_size:
            raise ValueError("Key size must be at least 2048 bits")
        
        if not is_power_of_two(key_size):
            raise ValueError("Key size must be a power of 2")

        try:
            # Paso 1: Seleccionar dos números primos grandes p y q
            # Si key_size = 2048, entonces key_size // 2 = 1024
            p = generate_prime(key_size // 2)  # genera primo de 1024 bits
            q = generate_prime(key_size // 2)  # genera otro primo de 1024 bits


            # Paso 2: Calcular n = p * q
            # n = p * q será de aproximadamente 2048 bits
            n = p * q

            # Paso 3: Calcular phi(n) = (p-1) * (q-1)
            phi = (p - 1) * (q - 1)

            # Paso 4: Elegir e tal que 1 < e < phi(n) y gcd(phi(n), e) = 1
            e = self._select_public_exponent(phi)

            # Paso 5: Calcular d tal que d = (e^-1) mod phi(n)
            d = mod_inverse(e, phi)

            # Conversión de las claves a bytes
            public_key = n.to_bytes(key_size // 8, 'big')
            private_key = d.to_bytes(key_size // 8, 'big')

            return KeyPair(
                public_key=public_key,
                private_key=private_key,
                algorithm="RSA",
                key_size=key_size
            )
        except Exception as e:
            raise RuntimeError(f"Error al generar par de claves RSA: {str(e)}")

    def _select_public_exponent(self, phi: int) -> int:
        """Selecciona un exponente público válido"""
        for e in sorted(self._valid_exponents):
            if gcd(e, phi) == 1:
                return e
        raise ValueError("No se encontró un exponente público válido")