'''visualization'''

from typing import Optional
import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph: dict[str, list[tuple[str, float]]],\
                    directed: bool = False, path: Optional[list[str]] = None):
    """

    >>> graph = {
    ...     'a': [('b', 3.0), ('c', 1.0)],
    ...     'b': [('a', 3.0), ('d', 2.0)],
    ...     'c': [('a', 1.0), ('d', 4.0)],
    ...     'd': [('b', 2.0), ('c', 4.0)]
    ... }
    >>> visualize_graph(graph, path=['a', 'b', 'd'])
    """
    G = nx.DiGraph() if directed else nx.Graph()

    for u in graph:
        for v, w in graph[u]:
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 8))

    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    edges = G.edges(data=True)
    weights = [data['weight'] for _, _, data in edges]

    if weights:
        max_weight = max(weights)
        normalized_weights = [weight / max_weight * 5 for weight in weights]
    else:
        normalized_weights = [1 for _ in edges]

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=G.edges(),
        width=normalized_weights,
        edge_color='gray',
        alpha=0.7,
        arrows=True if directed else False
    )

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_color='red',
        font_size=12
    )

    if path:
        path_edges = list(zip(path, path[1:]))
        valid_path_edges = [edge for edge in path_edges if G.has_edge(*edge)]

        if valid_path_edges:
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=valid_path_edges,
                width=3,
                edge_color='red',
                arrows=True if directed else False
            )

            nx.draw_networkx_nodes(
                G,
                pos,
                nodelist=path,
                node_size=700,
                node_color='yellow'
            )
            nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    plt.title('Візуалізація графу')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
