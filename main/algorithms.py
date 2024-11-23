'створюємо алгоритми для пошуку шляхів в графах'

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
    >>> bfs(graph, 'A', 'D')
    ['A', 'B', 'D']
    """
    visited = set()
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            for neighbor in neighbors:
                queue.append((neighbor, path + [neighbor]))
    return None

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
    >>> dfs(graph, 'A', 'D')
    ['A', 'B', 'D']
    """
    visited = set()
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            for neighbor in neighbors:
                stack.append((neighbor, path + [neighbor]))
    return None

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
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((cost + 1, neighbor, path + [neighbor]))
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
    >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
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
            for neighbor in neighbors:
                if neighbor not in visited:
                    cost_to_neighbor = len(path)
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
    >>> graph = {'A': ['B'], 'B': ['C'], 'C': ['A', 'D'], 'D': []}
    >>> bellman_ford(graph, 'A', 'D')
    ['A', 'B', 'C', 'D']
    """
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
            return None
    path.append(start)
    path.reverse()
    return path

if __name__ == '__main__':
    import doctest
    doctest.testmod()
