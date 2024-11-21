"""
Module provides function that implements dfs algorithm.
"""

def dfs(graph: dict, start: int, end: int) -> tuple[list[int], int]:
    """
    :param graph: dict, A dictionary where keys are nodes and values are 
    lists of tuples (neighbor, weight).
    :param start: int, The starting node.
    :param end: int, The goal node.

    :return: tuple[list[int], int], shortest path, which is presented in a 
    tuple (path: list of nodes, weight).
    >>> dfs({\
        1: [(2, 3), (3, 1)], \
        2: [(1, 3), (5, 4)], \
        3: [(4, 1), (6, 3)], \
        4: [(3, 1), (6, 3)], \
        5: [(2, 4)], \
        6: [(4, 3), (3, 3)]\
        }, 1, 6)
    ([1, 3, 6], 4)
    """
    def dfs_algorithm(node: int, path: list[int], weight: int) -> tuple[list[int], int] | None:
        path.append(node)

        if node == end:
            result = (list(path), weight)
        else:
            result = None
            for neighbor, edge_weight in graph[node]:
                if neighbor not in path:
                    sub_result = dfs_algorithm(neighbor, path, weight + edge_weight)
                    if sub_result:
                        if not result or sub_result[1] < result[1]:
                            result = sub_result

        path.pop()
        return result

    return dfs_algorithm(start, [], 0)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
