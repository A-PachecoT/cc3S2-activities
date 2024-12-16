# Lógica principal del algoritmo BFS invertido

from collections import deque


def algoritmo_bfs_invertido(grafo, nodo_inicial, nodo_final):
    # Si alguno de los nodos no existe en el grafo, retornamos None
    if nodo_inicial not in grafo.nodos or nodo_final not in grafo.nodos:
        return None

    # Cola para BFS y conjunto de visitados
    cola = deque([(nodo_final, [nodo_final])])
    visitados = {nodo_final}

    THRESHOLD_CARGA = 0.8  # Umbral de carga máxima permitida

    while cola:
        nodo_actual, camino = cola.popleft()

        # Si llegamos al nodo inicial, hemos encontrado un camino
        if nodo_actual == nodo_inicial:
            return list(reversed(camino))

        # Exploramos los vecinos (conexiones inversas)
        for nodo in grafo.nodos:
            if nodo_actual in nodo.conexiones and nodo not in visitados:
                # Verificamos la carga del nodo
                if nodo.carga >= THRESHOLD_CARGA:
                    continue

                visitados.add(nodo)
                nuevo_camino = camino + [nodo]
                cola.append((nodo, nuevo_camino))

    # Si no encontramos un camino, retornamos None
    return None
