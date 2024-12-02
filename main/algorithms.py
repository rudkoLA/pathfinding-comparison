'''algorithms for finding shortest path in graph'''

from collections import deque
import heapq

def bfs(graph, start, end):
    """
    """
    queue = deque()
    queue.append((start, [start], 0.0))
    visited = set()

    while queue:
        current, path, total_weight = queue.popleft()
        if current == end:
            return (path, total_weight)
        visited.add(current)
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], total_weight + weight))
    return None

def dfs(graph, start, end):
    """
    """
    def dfs_recursive(current, end, path, total_weight, visited):
        if current == end:
            return (path.copy(), total_weight)
        visited.add(current)
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                path.append(neighbor)
                result = dfs_recursive(neighbor, end, path, total_weight + weight, visited)
                if result:
                    return result
                path.pop()
        visited.remove(current)
        return None

    return dfs_recursive(start, end, [start], 0.0, set())

def dijkstra(graph, start, goal):
    """
    """
    priority_queue = []
    heapq.heappush(priority_queue, (0.0, start, [start]))
    visited = {}

    while priority_queue:
        current_distance, current_vertex, path = heapq.heappop(priority_queue)

        if current_vertex == goal:
            return (path, current_distance)

        if current_vertex in visited:
            continue

        visited[current_vertex] = current_distance

        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight
            if neighbor not in visited or distance < visited.get(neighbor, float('inf')):
                heapq.heappush(priority_queue, (distance, neighbor, path + [neighbor]))

    return None
def astar(graph, start, goal, heuristic):
    """
    """
    if heuristic is None:
        heuristic = {vertex: 0.0 for vertex in graph}

    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], 0.0, start, [start]))
    visited = {}

    while priority_queue:
        _, current_distance, current_vertex, path = heapq.heappop(priority_queue)

        if current_vertex == goal:
            return (path, current_distance)

        if current_vertex in visited and visited[current_vertex] <= current_distance:
            continue

        visited[current_vertex] = current_distance

        for neighbor, weight in graph.get(current_vertex, []):
            distance = current_distance + weight
            estimated = distance + heuristic.get(neighbor, 0.0)
            if neighbor not in visited or distance < visited.get(neighbor, float('inf')):
                heapq.heappush(priority_queue, (estimated, distance, neighbor, path + [neighbor]))

    return None

def bellman_ford(graph, start, goal):
    """
    """
    distance = {vertex: float('inf') for vertex in graph}
    predecessor = {vertex: None for vertex in graph}
    distance[start] = 0.0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u

    for u in graph:
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                print("Граф містить негативний цикл.")
                return None

    path = []
    current = goal
    if distance[goal] == float('inf'):
        return None
    while current is not None:
        path.insert(0, current)
        current = predecessor[current]
    total_weight = distance[goal]
    return (path, total_weight)

def floyd_warshall(graph, start, end):
    """
    """
    nodes = list(graph.keys())
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    next_node = {u: {v: None for v in nodes} for u in nodes}

    for u in graph:
        for v, weight in graph[u]:
            dist[u][v] = weight
            next_node[u][v] = v
        dist[u][u] = 0.0
        next_node[u][u] = u

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    def reconstruct_path(start, end):
        if next_node[start][end] is None:
            return None
        path = [start]
        while start != end:
            start = next_node[start][end]
            if start is None:
                return None
            path.append(start)
        return path

    path = reconstruct_path(start, end)
    if path is None:
        return None
    total_weight = dist[start][end]
    return (path, total_weight)

def spfa(graph, start, goal):
    """
    """
    distance = {node: float('inf') for node in graph}
    predecessor = {node: None for node in graph}
    distance[start] = 0.0

    in_queue = {node: False for node in graph}
    queue = deque([start])
    in_queue[start] = True
    count = {node: 0 for node in graph}

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        for v, weight in graph.get(u, []):
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    count[v] += 1
                    if count[v] > len(graph):
                        print("Граф містить негативний цикл.")
                        return None

    if distance[goal] == float('inf'):
        return None

    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = predecessor[current]
    total_weight = distance[goal]
    return (path, total_weight)
