'створюємо алгоритми для пошуку шляхів в графах'
import time

def bfs(graph, start, goal):
    """
    Виконує пошук у ширину для знаходження найкоротшого шляху

    Аргументи:
        graph (dict): Граф, представленний у вигляді словника
        start (str): Початкова вершина.
        goal (str): Цільова вершина.

    Повертає:
        tuple: Кортеж, що містить шлях та час виконання.

    Приклад:
    >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
    >>> bfs(graph, 'A', 'D')[0]
    ['A', 'B', 'D']
    """
    start_time = time.time()
    visited = set()
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex == goal:
            end_time = time.time()
            return path, end_time - start_time
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            for neighbor in neighbors:
                queue.append((neighbor, path + [neighbor]))
    end_time = time.time()
    return None, end_time - start_time

def dfs(graph, start, goal):
    """
    Виконує пошук у глибину для знаходження шляху

    Аргументи:
        graph (dict): Граф, представлений у вигляді словника
        start (str): Початкова вершина.
        goal (str): Цільова вершина.

    Повертає:
        tuple: Кортеж, що містить шлях та час виконання.

    Приклад:
    >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
    >>> dfs(graph, 'A', 'D')[0]
    ['A', 'B', 'D']
    """
    start_time = time.time()
    visited = set()
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        if vertex == goal:
            end_time = time.time()
            return path, end_time - start_time
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            for neighbor in neighbors:
                stack.append((neighbor, path + [neighbor]))
    end_time = time.time()
    return None, end_time - start_time

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
    >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
    >>> dijkstra(graph, 'A', 'D')[0]
    ['A', 'B', 'D']
    """
    start_time = time.time()
    visited = set()
    queue = [(0, start, [start])]

    while queue:
        queue.sort(key=lambda x: x[0])
        cost, vertex, path = queue.pop(0)
        if vertex == goal:
            end_time = time.time()
            return path, end_time - start_time
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((cost + 1, neighbor, path + [neighbor]))
    end_time = time.time()
    return None, end_time - start_time

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
    >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
    >>> astar(graph, 'A', 'D')[0]
    ['A', 'B', 'D']
    """
    start_time = time.time()
    visited = set()
    queue = [(0, start, [start])]
    while queue:
        queue.sort(key=lambda x: x[0])
        _, vertex, path = queue.pop(0)
        if vertex == goal:
            end_time = time.time()
            return path, end_time - start_time
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    cost_to_neighbor = len(path)
                    estimated_cost = cost_to_neighbor
                    queue.append((estimated_cost, neighbor, path + [neighbor]))
    end_time = time.time()
    return None, end_time - start_time

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
    >>> graph = {'A': ['B'], 'B': ['C'], 'C': ['A', 'D'], 'D': []}
    >>> bellman_ford(graph, 'A', 'D')[0]
    ['A', 'B', 'C', 'D']
    """
    start_time = time.time()
    distance = {vertex: float('inf') for vertex in graph}
    predecessor = {}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor in graph[vertex]:
                if distance[vertex] + 1 < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + 1
                    predecessor[neighbor] = vertex

    path = []
    current_vertex = goal
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = predecessor.get(current_vertex)
        if current_vertex is None:
            end_time = time.time()
            return None, end_time - start_time
    path.append(start)
    path.reverse()
    end_time = time.time()
    return path, end_time - start_time


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
        (5, ['a', 'b', 'c'])
        >>> floyd_warshall(graph, 'b', 'd')
        (3, ['b', 'c', 'd'])
        >>> floyd_warshall(graph, 'a', 'e')
        (inf, None)
    """
    if start not in graph or end not in graph:
        return float('inf'), None

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
    return dist[start][end], shortest_path