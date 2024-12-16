import pytest
from src.segment_tree.persistent_tree import PersistentSegmentTree


def test_create_tree():
    # Arrange
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    # Act
    tree = PersistentSegmentTree(arr)

    # Assert
    assert tree.query_range(0, 0, 7) == sum(arr)


def test_range_query():
    # Arrange
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    # Act
    tree = PersistentSegmentTree(arr)

    # Assert
    assert tree.query_range(0, 2, 5) == sum(arr[2:6])
    assert tree.query_range(0, 2, 5) == sum(arr[2:6])


def test_update_creates_version():
    # Arrange
    arr = [1, 2, 3, 4]
    tree = PersistentSegmentTree(arr)

    # Act
    version = tree.update(2, 10)

    # Assert
    assert version == 1

    # Assert
    assert tree.query_range(0, 0, 3) == sum(arr)

    # Assert
    expected_sum = sum(arr[:2]) + 10 + arr[3]
    assert tree.query_range(1, 0, 3) == expected_sum


def test_version_isolation():
    # Arrange
    arr = [1, 2, 3, 4]
    tree = PersistentSegmentTree(arr)

    # Act
    v1 = tree.update(0, 10)  # [10,2,3,4]
    v2 = tree.update(1, 20)  # [10,20,3,4]

    # Assert
    assert tree.query_range(0, 0, 3) == sum(arr)  # Original
    assert tree.query_range(v1, 0, 3) == 19  # Version 1
    assert tree.query_range(v2, 0, 3) == 37  # Version 2
