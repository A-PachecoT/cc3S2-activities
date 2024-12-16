import pytest
from src.models.graph import Grafo
from src.models.node import Nodo
from src.heuristica_conexion import HeuristicaConexion


@pytest.fixture
def setup_grafo():
    grafo = Grafo()
    nodo_a = Nodo(1, "A")
    nodo_b = Nodo(2, "B")
    grafo.agregar_nodo(nodo_a)
    grafo.agregar_nodo(nodo_b)
    heuristica = HeuristicaConexion(grafo)
    return grafo, nodo_a, nodo_b, heuristica


def test_nodo_sobrecargado(setup_grafo):
    # Arrange
    _, nodo_a, nodo_b, heuristica = setup_grafo
    nodo_a.carga = 0.9  # 90% de carga

    # Act
    resultado = heuristica.es_conexion_valida(nodo_a, nodo_b)

    # Assert
    assert not resultado


def test_conexion_temprana(setup_grafo):
    # Arrange
    _, nodo_a, nodo_b, heuristica = setup_grafo
    nodo_a.iteraciones_conexion = 1  # Pocas iteraciones

    # Act
    heuristica_valor = heuristica.calcular_heuristica(nodo_a, nodo_b)

    # Assert
    assert heuristica_valor >= 10.0  # Debe tener una penalización alta


def test_conexion_valida(setup_grafo):
    # Arrange
    _, nodo_a, nodo_b, heuristica = setup_grafo
    nodo_a.iteraciones_conexion = 5  # Suficientes iteraciones
    nodo_a.carga = 0.3  # Carga moderada

    # Act
    resultado = heuristica.es_conexion_valida(nodo_a, nodo_b)

    # Assert
    assert resultado == True


def test_conexion_no_valida(setup_grafo):
    # Arrange
    _, nodo_a, nodo_b, heuristica = setup_grafo
    nodo_a.iteraciones_conexion = 5  # Suficientes iteraciones
    nodo_a.carga = 0.9  # Carga alta

    # Act
    resultado = heuristica.es_conexion_valida(nodo_a, nodo_b)

    # Assert
    assert resultado == False


def test_actualizacion_iteraciones(setup_grafo):
    # Arrange
    _, nodo_a, _, heuristica = setup_grafo
    iteraciones_iniciales = nodo_a.iteraciones_conexion

    # Act
    heuristica.actualizar_iteraciones()

    # Assert
    assert nodo_a.iteraciones_conexion == iteraciones_iniciales + 1
