# Clase Grafo
class Grafo:
    def __init__(self):
        self.nodos = []
        self.aristas = []

    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos.append(nodo)

    def agregar_arista(self, nodo_origen, nodo_destino):
        if nodo_origen in self.nodos and nodo_destino in self.nodos:
            arista = (nodo_origen, nodo_destino)
            if arista not in self.aristas:
                self.aristas.append(arista)
                nodo_origen.agregar_conexion(nodo_destino)

    def obtener_vecinos(self, nodo):
        return [n for n in nodo.conexiones if n in self.nodos]
