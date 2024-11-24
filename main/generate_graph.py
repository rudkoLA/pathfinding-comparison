"""Generate random directed graph"""
import random

def generate_graph(num_nodes, num_edges):
    """
    Генерує орієнтований граф з num_nodes вузлами та num_edges ребрами.
    """
    graph = {i: [] for i in range(num_nodes)}

    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        
        if u != v:
            edges.add((u, v))

    for u, v in edges:
        weight = random.randint(1, 10)
        graph[u].append((v, weight))

    return graph

print(generate_graph(4, 3))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
