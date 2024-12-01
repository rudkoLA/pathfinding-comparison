'створюємо алгоритми для пошуку шляхів в графах'

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
        }, 1, 6)[0]
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
                        if result is None or sub_result[1] < result[1]:
                            result = sub_result

        path.pop()
        return result

    return dfs_algorithm(start, [], 0)

def dijkstra(graph, start, goal):
    """
    Виконує алгоритм Дейкстри для знаходження найкоротшого шляху

    Аргументи:
        graph (dict): Граф, представлений у вигляді словника
        start (str): Початкова вершина.
        goal (str): Цільова вершина.

    Повертає:
        tuple: Кортеж, що містить шлях та час виконання.

    Приклад:
    >>> graph = {'A': [('B', 1), ('C', 1)], 'B': [('D', 1)], 'C': [('D', 1)], 'D': []}
    >>> dijkstra(graph, 'A', 'D')
    ['A', 'B', 'D']
    """
    visited = set()
    queue = [(0, start, [start])]

    while queue:
        queue.sort(key=lambda x: x[0])
        cost, vertex, path = queue.pop(0)
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            for neighbor, weight in neighbors:
                if neighbor not in visited:
                    queue.append((cost + weight, neighbor, path + [neighbor]))
    return None

def astar(graph, start, goal):
    """
    Виконує алгоритм A* для знаходження найкоротшого шляху
    
    Аргументи:
        graph (dict): Граф, представлений у вигляді словника
        start (str): Початкова вершина.
        goal (str): Цільова вершина.

    Повертає:
        tuple: Кортеж, що містить шлях та час виконання.

    Приклад:
    >>> graph = {'A': [('B', 1), ('C', 1)], 'B': [('D', 1)], 'C': [('D', 1)], 'D': []}
    >>> astar(graph, 'A', 'D')
    ['A', 'B', 'D']
    """
    visited = set()
    queue = [(0, start, [start])]
    while queue:
        queue.sort(key=lambda x: x[0])
        _, vertex, path = queue.pop(0)
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            for neighbor, weight in neighbors:
                if neighbor not in visited:
                    cost_to_neighbor = len(path) + weight
                    estimated_cost = cost_to_neighbor
                    queue.append((estimated_cost, neighbor, path + [neighbor]))
    return None

def bellman_ford(graph, start, goal):
    """
    Виконує алгоритм Беллмана-Форда для знаходження найкоротшого шляху.

    Аргументи:
        graph (dict): Граф, представлений у вигляді словника
        start (str): Початкова вершина.
        goal (str): Цільова вершина.

    Повертає:
        tuple: Кортеж, що містить шлях та час виконання.

    Приклад:
    >>> graph = {'A': [('B', 1)], 'B': [('C', 1)], 'C': [('A', 1), ('D', 1)], 'D': []}
    >>> bellman_ford(graph, 'A', 'D')
    ['A', 'B', 'C', 'D']
    """
    distance = {vertex: float('inf') for vertex in graph}
    predecessor = {}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight
                    predecessor[neighbor] = vertex

    path = []
    current_vertex = goal
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = predecessor.get(current_vertex)
        if current_vertex is None:
            return None
    path.append(start)
    path.reverse()

    return path

def floyd_warshall(graph, start, end):
    """
    Implements the Floyd-Warshall algorithm for a graph in list format.

    Args:
        graph (dict): Graph as an list where graph[u] is a list of tuples (v, weight).
        start (str): The starting node.
        end (str): The ending node.

    Returns:
        tuple: (distance, path) where:
            - distance (float): Shortest distance from start to end.
            - path (list): List of nodes representing the shortest path, or None if no path exists.

    Example:
        >>> graph = {
        ...     'a': [('b', 3), ('d', 7)],
        ...     'b': [('c', 2)],
        ...     'c': [('d', 1)],
        ...     'd': [('a', 1)]
        ... }
        >>> floyd_warshall(graph, 'a', 'c')
        ['a', 'b', 'c']
        >>> floyd_warshall(graph, 'b', 'd')
        ['b', 'c', 'd']
        >>> floyd_warshall(graph, 'a', 'e') is None 
        True
    """
    if start not in graph or end not in graph:
        return None

    nodes = graph.keys()
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    next_node = {u: {v: None for v in nodes} for u in nodes}

    for u in graph:
        for v, weight in graph[u]:
            dist[u][v] = weight
            next_node[u][v] = v
        dist[u][u] = 0

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    def reconstruct_path(start, end):
        if next_node[start][end] is None:
            return None
        path = [start]
        while start != end:
            start = next_node[start][end]
            path.append(start)
        return path

    shortest_path = reconstruct_path(start, end)
    return shortest_path


def spfa(graph, start, end):
    """
    Виконує алгоритм Shortest Path Faster Algorithm (SPFA) для знаходження найкоротшого шляху.

    Аргументи:
        graph (dict): Граф, представлений у вигляді словника
        start (str): Початкова вершина.
        end (str): Цільова вершина.

    Повертає:
        tuple: Кортеж, що містить шлях та час виконання.

    Приклад:
    >>> graph = {'A': [('B', 1)], 'B': [('C', 1)], 'C': [('A', 1), ('D', 1)], 'D': []}
    >>> spfa(graph, 'A', 'D')
    ['A', 'B', 'C', 'D']
    """

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [start]

    prev_nodes = {node: None for node in graph}

    while queue:
        current_node = queue.pop()

        for neighbor, weight in graph[current_node]:
            new_weight = distances[current_node] + weight
            old_weight = distances[neighbor]

            if new_weight < old_weight:
                distances[neighbor] = new_weight
                prev_nodes[neighbor] = current_node

                if neighbor not in queue:
                    queue.append(neighbor)

    path = []
    current_node = end

    if distances[end] == float('inf'):
        return None

    while current_node is not None:
        path.append(current_node)
        current_node = prev_nodes[current_node]

    path.reverse()

    return path

if __name__ == '__main__':
    import doctest
    doctest.testmod()
