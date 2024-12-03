"""
Functions for generating graphs.
"""

import random
import string

def generate_random_graph() -> dict[str, list[tuple[str, int]]]:
    """
    Generates a random graph.

    Returns:
        dict: A dictionary representation of the graph where keys are vertex names (str),
              and values are lists of tuples. Each tuple represents an edge and consists
              of a connected vertex name (str) and the edge weight (int).

    Example output:
        {
            'a': [('b', 3), ('c', 5)],
            'b': [('a', 3)],
            'c': [('a', 5)]
        }

    The graph is randomly generated with the following properties:
    - The number of vertices is chosen randomly between 10 and 100.
    - Vertices are labeled with unique alphabetic names ('a', 'b', ..., 'z', 'aa', 'ab', ..., etc.).
    - The number of edges is chosen randomly, between 50 and a reasonable maximum based on the
      total number of possible edges.
    - Each edge has a randomly assigned weight between 1 and 10.
    - The graph is undirected, meaning that for every edge (u, v), both u -> v and v -> u are stored.
    """
    num_vertices = random.randint(10, 100)

    def generate_vertex_names(n):
        """
        Generates unique names for vertices using alphabetic labels.

        Args:
            n (int): Number of vertices.
        Returns:
            List[str]: A list of unique vertex names.
        """
        names = []
        letters = string.ascii_lowercase
        for i in range(n):
            name = ''
            num = i
            while True:
                name = letters[num % 26] + name
                num = num // 26 - 1
                if num < 0:
                    break
            names.append(name)
        return names

    vertices = generate_vertex_names(num_vertices)

    max_edges = num_vertices * (num_vertices - 1) // 2
    num_edges = random.randint(50, min(150, max_edges))

    possible_edges = [(u, v) for idx, u in enumerate(vertices) for v in vertices[idx+1:]]

    selected_edges = random.sample(possible_edges, num_edges)

    graph = {vertex: [] for vertex in vertices}
    for u, v in selected_edges:
        weight = random.randint(1, 10)
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    return graph
