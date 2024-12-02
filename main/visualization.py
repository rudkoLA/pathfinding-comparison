# visualization.py

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional

def visualize_graph(graph: Dict[str, List[Tuple[str, float]]],\
                    directed: bool = False, path: Optional[List[str]] = None):
    """
    Візуалізує зважений граф та виділяє заданий шлях.

    Args:
        graph (dict): Словник графу з вагами.
        directed (bool): Прапорець, який визначає, чи є граф напрямленим.
        path (list, optional): Список вершин на шляху, який потрібно виділити.

    Приклад:
    >>> graph = {
    ...     'a': [('b', 3.0), ('c', 1.0)],
    ...     'b': [('a', 3.0), ('d', 2.0)],
    ...     'c': [('a', 1.0), ('d', 4.0)],
    ...     'd': [('b', 2.0), ('c', 4.0)]
    ... }
    >>> visualize_graph(graph, path=['a', 'b', 'd'])
    """
    G = nx.DiGraph() if directed else nx.Graph()

    # Додавання ребер з вагами
    for u in graph:
        for v, w in graph[u]:
            G.add_edge(u, v, weight=w)

    # Визначення позицій вершин за допомогою Spring Layout
    pos = nx.spring_layout(G, seed=42)  # seed для відтворюваності

    plt.figure(figsize=(10, 8))

    # Малювання вузлів
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

    # Малювання міток вузлів
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Отримання ваг ребер для налаштування товщини ліній
    edges = G.edges(data=True)
    weights = [data['weight'] for _, _, data in edges]

    if weights:
        max_weight = max(weights)
        normalized_weights = [weight / max_weight * 5 for weight in weights]  # масштабування до 5
    else:
        normalized_weights = [1 for _ in edges]

    # Малювання ребер з урахуванням ваг
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=G.edges(),
        width=normalized_weights,
        edge_color='gray',
        alpha=0.7,
        arrows=True if directed else False
    )

    # Додавання міток ваг на ребрах
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_color='red',
        font_size=10
    )

    # Виділення заданого шляху, якщо він заданий
    if path:
        # Побудова списку ребер на шляху
        path_edges = list(zip(path, path[1:]))
        # Перевірка наявності ребер у графі
        valid_path_edges = [edge for edge in path_edges if G.has_edge(*edge)]

        if valid_path_edges:
            # Малювання ребер шляху червоним кольором і більшою товщиною
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=valid_path_edges,
                width=3,
                edge_color='red',
                arrows=True if directed else False
            )

            # Виділення вузлів на шляху
            nx.draw_networkx_nodes(
                G,
                pos,
                nodelist=path,
                node_size=700,
                node_color='yellow'
            )
            # Повторне малювання міток вузлів, щоб вони були поверх
            nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    plt.title('Візуалізація зваженого графу')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
