"""Utilidades matemáticas para operaciones criptográficas"""

import random
from math import gcd

def is_prime(n: int, k: int = 5) -> bool:
    """Test de primalidad de Miller-Rabin
    Basado en la implementación de GeeksForGeeks:
    https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
    """
    # Casos base
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Encontrar r y d tales que n - 1 = 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2

    # Realizar k rondas de prueba
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # Usando pow() built-in para modular exponentiation
        if x == 1 or x == n - 1:
            continue
            
        # Realizar r-1 cuadrados
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:  # Si no encontramos un testigo válido
            return False
    return True

def generate_prime(bits: int) -> int:
    """Genera un número primo del tamaño especificado"""
    while True:
        n = random.getrandbits(bits) | (1 << bits - 1) | 1
        if is_prime(n):
            return n

def mod_inverse(a: int, m: int) -> int:
    """Calcula el inverso multiplicativo modular de a módulo m."""
    try:
        return pow(a, -1, m)
    except ValueError:
        raise ValueError(f'El inverso modular de {a} mod {m} no existe')

def is_power_of_two(n: int) -> bool:
    """Verifica si un número es potencia de 2"""
    return n > 0 and (n & (n - 1)) == 0