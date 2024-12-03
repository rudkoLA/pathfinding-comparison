'''Algoritms for finding shortest path'''

def bfs(graph, start, end):
    """
    param graph: dict, A dictionary where keys are tuple of nodes and values 
    
    param start: The starting node
    
    param end: The goal node

    returns shortest path, which is presented in a 
    tuple (path: list of nodes, weight)
    
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

    priority_queue = [(0, [start])]
    visited = {}

    while priority_queue:
        min_index = 0
        for i in range(1, len(priority_queue)):
            if priority_queue[i][0] < priority_queue[min_index][0]:
                min_index = i

        current_weight, path = priority_queue.pop(min_index)
        node = path[-1]

        if node == end:
            return path, current_weight

        if node in visited and visited[node] <= current_weight:
            continue
        visited[node] = current_weight

        for neighbor, weight in graph.get(node, []):
            if neighbor not in path:
                new_path = path + [neighbor]
                priority_queue.append((current_weight + weight, new_path))
    return [], float('inf')

def dfs(graph, start, end):
    """
    param graph: dict, A dictionary where keys are tuple of nodes and values 
    
    param start: The starting node
    
    param end: The goal node

    returns shortest path, which is presented in a 
    tuple (path: list of nodes, weight)
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
    visited = {}

    def dfs_algorithm(node: int, path: list[int], weight: int) -> tuple[list[int], int] | None:
        result = []
        if node in visited and visited[node] <= weight:
            return None

        visited[node] = weight
        path.append(node)

        if node == end:
            result = (list(path), weight)
        else:
            result = None
            for neighbor, edge_weight in graph.get(node, []):
                if neighbor not in path:
                    sub_result = dfs_algorithm(neighbor, path, weight + edge_weight)
                    if sub_result:
                        if result is None or sub_result[1] < result[1]:
                            result = sub_result

        path.pop()
        return result if result is not None else ([], float('inf'))

    return dfs_algorithm(start, [], 0)

def dijkstra(graph, start, goal):
    """
    param graph: dict, A dictionary where keys are tuple of nodes and values 
    
    param start: The starting node
    
    param end: The goal node

    returns shortest path, which is presented in a 
    tuple (path: list of nodes, weight)

    >>> graph = {'A': [('B', 1), ('C', 1)], 'B': [('D', 1)], 'C': [('D', 1)], 'D': []}
    >>> dijkstra(graph, 'A', 'D')
    (['A', 'B', 'D'], 2)
    """
    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    previous_vertices = {vertex: None for vertex in graph}

    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = None
        current_distance = float('infinity')
        for vertex in unvisited:
            if distances[vertex] < current_distance:
                current_distance = distances[vertex]
                current_vertex = vertex

        if current_vertex is None:
            break

        if current_vertex == goal:
            break

        for neighbor, weight in graph[current_vertex]:
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex

        unvisited.remove(current_vertex)

    path = []
    current = goal
    while previous_vertices[current] is not None:
        path.insert(0, current)
        current = previous_vertices[current]
    if distances[goal] != float('infinity'):
        path.insert(0, current)

    return path, distances[goal]

def astar(graph, start, goal):
    """
    param graph: dict, A dictionary where keys are tuple of nodes and values 
    
    param start: The starting node
    
    param end: The goal node

    returns shortest path, which is presented in a 
    tuple (path: list of nodes, weight)

    >>> graph = {'A': [('B', 1), ('C', 1)], 'B': [('D', 1)], 'C': [('D', 1)], 'D': []}
    >>> astar(graph, 'A', 'D')
    (['A', 'B', 'D'], 2)
    """
    
    def find_min_edge_weight(graph):
        min_weight = float('infinity')
        for neighbors in graph.values():
            for neighbor, weight in neighbors:
                if weight < min_weight:
                    min_weight = weight
        return min_weight if min_weight != float('infinity') else 0

    min_edge_weight = find_min_edge_weight(graph)

    def compute_min_steps(graph, goal):
        reverse_graph = {vertex: [] for vertex in graph}
        for vertex, neighbors in graph.items():
            for neighbor, _ in neighbors:
                reverse_graph[neighbor].append(vertex)
        
        min_steps = {vertex: float('infinity') for vertex in graph}
        min_steps[goal] = 0
        
        queue = [goal]

        while queue:
            current = queue.pop(0)
            for neighbor in reverse_graph[current]:
                if min_steps[neighbor] > min_steps[current] + 1:
                    min_steps[neighbor] = min_steps[current] + 1
                    queue.append(neighbor)
        
        return min_steps

    min_steps = compute_min_steps(graph, goal)

    heuristic = {}
    for vertex in graph:
        if min_steps[vertex] != float('infinity'):
            heuristic[vertex] = min_edge_weight * min_steps[vertex]
        else:
            heuristic[vertex] = float('infinity')

    def a_star_with_heuristic(graph, start, goal, heuristic):
        open_set = set([start])
        closed_set = set()
        g_scores = {vertex: float('infinity') for vertex in graph}
        g_scores[start] = 0

        f_scores = {vertex: float('infinity') for vertex in graph}
        f_scores[start] = heuristic[start]

        came_from = {vertex: None for vertex in graph}

        while open_set:
            current = min(open_set, key=lambda vertex: f_scores[vertex])

            if current == goal:
                path = []
                while current:
                    path.insert(0, current)
                    current = came_from[current]
                return path, g_scores[goal]

            open_set.remove(current)
            closed_set.add(current)

            for neighbor, cost in graph[current]:
                if neighbor in closed_set:
                    continue

                tentative_g = g_scores[current] + cost

                if neighbor not in open_set:
                    open_set.add(neighbor)
                elif tentative_g >= g_scores[neighbor]:
                    continue

                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g
                f_scores[neighbor] = g_scores[neighbor] + heuristic.get(neighbor, float('infinity'))

        return None, float('infinity')

    path, distance = a_star_with_heuristic(graph, start, goal, heuristic)

    return path, distance


def bellman_ford(graph, start, goal):
    """
    param graph: dict, A dictionary where keys are tuple of nodes and values 
    
    param start: The starting node
    
    param end: The goal node

    returns shortest path, which is presented in a 
    tuple (path: list of nodes, weight)

    >>> graph = {'A': [('B', 1)], 'B': [('C', 1)], 'C': [('A', 1), ('D', 1)], 'D': []}
    >>> bellman_ford(graph, 'A', 'D')
    (['A', 'B', 'C', 'D'], 3)
    """
    distance = {vertex: float('inf') for vertex in graph}
    predecessor = {}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph.get(vertex, []):
                if neighbor in distance and distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight
                    predecessor[neighbor] = vertex

    path = []
    current_vertex = goal
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = predecessor.get(current_vertex)
        if current_vertex is None:
            return [], float('inf')
    path.append(start)
    path.reverse()

    return path, distance[goal]


def floyd_warshall(graph, start, end):
    """
    Implements the Floyd-Warshall algorithm

    param graph: dict, A dictionary where keys are tuple of nodes and values 
    
    param start: The starting node
    
    param end: The goal node

    returns shortest path, which is presented in a uple (path: list of nodes, weight)
    """
    if start not in graph or end not in graph:
        return [], float('inf')

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
            return []
        path = [start]
        while start != end:
            start = next_node[start][end]
            path.append(start)
        return path

    shortest_path = reconstruct_path(start, end)
    return shortest_path, dist[start][end] if shortest_path else float('inf')



def spfa(graph, start, end):
    """
    Implements the  Shortest Path Faster Algorithm (SPFA)

    param graph: dict, A dictionary where keys are tuple of nodes and values 
    
    param start: The starting node
    
    param end: The goal node

    returns shortest path, which is presented in a uple (path: list of nodes, weight)

    >>> graph = {'A': [('B', 1)], 'B': [('C', 1)], 'C': [('A', 1), ('D', 1)], 'D': []}
    >>> spfa(graph, 'A', 'D')
    (['A', 'B', 'C', 'D'], 3)
    """

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [start]

    prev_nodes = {node: None for node in graph}

    while queue:
        current_node = queue.pop()

        for neighbor, weight in graph.get(current_node, []):
            if neighbor in distances:
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
        return [], float('inf')

    while current_node is not None:
        path.append(current_node)
        current_node = prev_nodes[current_node]

    path.reverse()

    return path, distances[end]
