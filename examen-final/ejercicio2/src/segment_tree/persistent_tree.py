from typing import List, Optional
from .node import Node


class PersistentSegmentTree:
    def __init__(self, arr: List[int]):
        """Inicializa el árbol de segmentos persistente con un array"""
        self.versions = []
        self.root = self._build_tree(arr, 0, len(arr) - 1)
        self.versions.append(self.root)

    def _build_tree(self, arr: List[int], start: int, end: int) -> Node:
        """Construye el árbol de segmentos inicial"""
        node = Node(start, end)

        if start == end:
            node.value = arr[start]
            return node

        mid = node.get_mid()
        node.left = self._build_tree(arr, start, mid)
        node.right = self._build_tree(arr, mid + 1, end)
        node.value = node.left.value + node.right.value

        return node

    def update(self, index: int, value: int) -> int:
        """Actualiza un valor y crea una nueva versión"""
        if not self.versions:
            raise ValueError("No versiones disponibles")

        new_root = self._update(self.versions[-1], index, value)
        self.versions.append(new_root)
        return len(self.versions) - 1

    def _update(self, node: Node, index: int, value: int) -> Node:
        """Método interno que mantiene la persistencia"""
        if node.start == node.end:
            new_node = node.clone()
            new_node.value = value
            return new_node

        new_node = node.clone()
        mid = node.get_mid()

        if index <= mid:
            new_node.left = self._update(node.left, index, value)
            new_node.right = node.right
        else:
            new_node.left = node.left
            new_node.right = self._update(node.right, index, value)

        new_node.value = new_node.left.value + new_node.right.value
        return new_node

    def query_range(self, version: int, start: int, end: int) -> int:
        """Consulta la suma de un rango en una versión específica"""
        if version >= len(self.versions):
            raise ValueError(f"Versión {version} no existe")

        return self._query_range(self.versions[version], start, end)

    def _query_range(self, node: Node, start: int, end: int) -> int:
        """Método interno que consulta la suma de un rango"""
        if start > end or start > node.end or end < node.start:
            return 0

        if start <= node.start and end >= node.end:
            return node.value

        mid = node.get_mid()
        left_sum = self._query_range(node.left, start, min(mid, end))
        right_sum = self._query_range(node.right, max(start, mid + 1), end)

        return left_sum + right_sum
