import pytest
from src.models.graph import Grafo
from src.models.node import Nodo
from src.algoritmo_bfs_invertido import algoritmo_bfs_invertido


@pytest.fixture
def setup_grafo():
    grafo = Grafo()

    # Crear nodos
    nodo_a = Nodo(1, "A")
    nodo_b = Nodo(2, "B")
    nodo_c = Nodo(3, "C")
    nodo_d = Nodo(4, "D")
    nodo_e = Nodo(5, "E")

    # Agregar nodos al grafo
    grafo.nodos.extend([nodo_a, nodo_b, nodo_c, nodo_d, nodo_e])

    # Establecer conexiones
    nodo_a.agregar_conexion(nodo_b)
    nodo_b.agregar_conexion(nodo_c)
    nodo_b.agregar_conexion(nodo_d)
    nodo_c.agregar_conexion(nodo_a)
    nodo_d.agregar_conexion(nodo_e)

    # Simular cargas
    nodo_b.carga = 0.6
    nodo_c.carga = 0.3

    return grafo, nodo_a, nodo_b, nodo_c, nodo_d, nodo_e


def test_camino_simple(setup_grafo):
    # Arrange
    grafo, nodo_a, _, _, _, nodo_e = setup_grafo

    # Act
    camino = algoritmo_bfs_invertido(grafo, nodo_a, nodo_e)

    # Assert
    assert camino is not None
    assert len(camino) == 4
    assert camino[0] == nodo_a
    assert camino[-1] == nodo_e


def test_nodo_no_alcanzable(setup_grafo):
    # Arrange
    grafo, nodo_a, _, _, _, nodo_e = setup_grafo
    nodo_aislado = Nodo(6, "F")  # Nodo aislado
    grafo.nodos.append(nodo_aislado)

    # Act
    camino = algoritmo_bfs_invertido(grafo, nodo_a, nodo_aislado)

    # Assert
    assert camino is None  # No debería encontrar un camino


def test_nodo_sobrecargado(setup_grafo):
    # Arrange
    grafo, nodo_a, nodo_b, _, nodo_d, _ = setup_grafo
    nodo_b.carga = 0.9

    # Act
    camino = algoritmo_bfs_invertido(grafo, nodo_a, nodo_d)

    # Assert
    assert camino is None  # No debería encontrar un camino por la sobrecarga
