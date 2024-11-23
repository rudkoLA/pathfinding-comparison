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
    >>> graph = {'A': ['B'], 'B': ['C'], 'C': ['A', 'D'], 'D': []}
    >>> spfa(graph, 'A', 'D')
    ['A', 'B', 'C', 'D']
    """

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [start]

    prev_nodes = {node: None for node in graph}

    while queue:
        current_node = queue.pop()

        for neighbor in graph[current_node]:
            new_weight = distances[current_node] + 1
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
