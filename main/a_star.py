def a_star(graph, start, goal):
    """
    A* algorithm for finding the shortest path.
    Args:
        graph (dict): A dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
        start: The starting node.
        goal: The goal node.
    Returns:
        list: The shortest path as a list of nodes, or an empty list if no path exists.
    """
    open_set = [(0, start)]
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    came_from = {}
    while open_set:
        open_set.sort(key=lambda x: x[0])
        current_f_score, current = open_set.pop(0)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for neighbor, weight in graph.get(current, []):
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                open_set.append((f_score[neighbor], neighbor))
    
    return []

def heuristic(a, b):
    """
    Heuristic function for A*.
    In this example, we assume nodes are represented as coordinates (x, y).
    If nodes are not coordinates, use a different heuristic.
    """
    if isinstance(a, tuple) and isinstance(b, tuple):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    return 0
