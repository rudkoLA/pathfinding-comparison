'функції для візуалізації графу'
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(edge_list, directed=False, path=None):
    """
    Візуалізує граф та виділяє заданий шлях.

    Args:
        edge_list (list): Список ребер графу.
        directed (bool): Прапорець, який визначає, чи є граф напрямленим.
        path (list): Список вершин на шляху, який потрібно виділити.

    Приклад:
    >>> edge_list = [('A', 'B'), ('B', 'C')]
    >>> visualize_graph(edge_list, path=['A', 'B', 'C'])
    """
    G = nx.DiGraph() if directed else nx.Graph()
    G.add_edges_from(edge_list)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.5)

    if path:
        # Побудова списку ребер на шляху
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.title('Візуалізація графу')
    plt.axis('off')
    plt.show()
