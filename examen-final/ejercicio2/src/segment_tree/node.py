class Node:
    def __init__(self, start: int, end: int, value: int = 0):
        self.start = start
        self.end = end
        self.value = value
        self.left = None
        self.right = None
        self.version = 0

    def clone(self) -> "Node":
        """Crea una copia del nodo para persistencia"""
        node = Node(self.start, self.end, self.value)
        node.left = self.left
        node.right = self.right
        return node

    def get_mid(self) -> int:
        """Devuelve el punto medio del rango del nodo"""
        return self.start + (self.end - self.start) // 2

    def __str__(self) -> str:
        return f"Node([{self.start}, {self.end}], value={self.value})"
