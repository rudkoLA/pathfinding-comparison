"""
Functions for generating graphs.
"""

import random
import string

def generate_random_graph():
    """
    Generates a random graph.
    """
    num_vertices = random.randint(10, 100)

    def generate_vertex_names(n):
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
