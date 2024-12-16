# Clase Nodo
class Nodo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.carga = 0.0  # Porcentaje de carga (0.0 a 1.0)
        self.conexiones = []
        self.iteraciones_conexion = 0  # Contador para la heurística de conexión tardía

    def agregar_conexion(self, nodo):
        if nodo not in self.conexiones:
            self.conexiones.append(nodo)
            self.iteraciones_conexion = (
                0  # Reiniciamos el contador al establecer una conexión
            )

    def remover_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)

    def incrementar_iteraciones(self):
        self.iteraciones_conexion += 1

    def __str__(self):
        return f"Nodo({self.nombre}, carga={self.carga*100:.1f}%)"

    def __repr__(self):
        return self.__str__()
