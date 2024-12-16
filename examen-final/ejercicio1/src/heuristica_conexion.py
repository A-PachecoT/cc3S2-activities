class HeuristicaConexion:
    def __init__(self, grafo):
        self.grafo = grafo
        self.MIN_ITERACIONES = 3  # Mínimo de iteraciones antes de permitir conexión
        self.THRESHOLD_CARGA = 0.8  # Umbral de carga máxima (80%)
        self.FACTOR_PENALIZACION_CARGA = 2.0
        self.FACTOR_PENALIZACION_CONEXIONES = 0.1

    def calcular_heuristica(self, nodo_actual, nodo_destino):
        """
        Calcula la heurística de conexión tardía entre dos nodos.
        Retorna un valor numérico que representa el costo de la conexión.
        Un valor infinito significa que la conexión no es posible.
        """
        if nodo_actual not in self.grafo.nodos or nodo_destino not in self.grafo.nodos:
            return float("inf")

        # Si el nodo está sobrecargado, no permitimos la conexión
        if nodo_actual.carga >= self.THRESHOLD_CARGA:
            return float("inf")

        # Valor base de la heurística
        heuristica = 1.0

        # Penalización por carga del nodo actual
        heuristica *= 1.0 + nodo_actual.carga * self.FACTOR_PENALIZACION_CARGA

        # Penalización por número de conexiones existentes
        num_conexiones = len(nodo_actual.conexiones)
        heuristica *= 1.0 + num_conexiones * self.FACTOR_PENALIZACION_CONEXIONES

        # Si no ha pasado suficientes iteraciones, aumentamos significativamente la heurística
        if nodo_actual.iteraciones_conexion < self.MIN_ITERACIONES:
            heuristica *= 10.0

        return heuristica

    def es_conexion_valida(self, nodo_actual, nodo_destino):
        heuristica = self.calcular_heuristica(nodo_actual, nodo_destino)
        return heuristica != float("inf")

    def actualizar_iteraciones(self):
        for nodo in self.grafo.nodos:
            nodo.incrementar_iteraciones()
