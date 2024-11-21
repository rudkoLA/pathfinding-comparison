"""
Module provides bfs algorithm of finding the shortest path in graph.
"""

def bfs(graph: dict, start: int, end: int) -> tuple[list[int], int]:
    """
    :param graph: dict, A dictionary where keys are nodes and values are 
    lists of tuples (neighbor, weight).
    :param start: int, The starting node.
    :param end: int, The goal node.

    :return: tuple[list[int], int], shortest path, which is presented in a 
    tuple (path: list of nodes, weight).
    >>> bfs({\
        1: [(2, 3), (3, 1)], \
        2: [(1, 3), (5, 4)], \
        3: [(4, 1), (6, 3)], \
        4: [(3, 1), (6, 3)], \
        5: [(2, 4)], \
        6: [(4, 3), (3, 3)]\
        }, 1, 6)
    ([1, 3, 6], 4)
    """
    queue = [([start], 0)]
    paths = []

    while queue:
        path, current_weight = queue.pop(0)
        node = path[-1]

        if node == end:
            paths.append((path, current_weight))
            continue

        for neighbor, weight in graph.get(node, []):
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((new_path, current_weight + weight))

    return paths

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
