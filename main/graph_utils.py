'функції для роботи з файлом в якому містится граф та переведення графу зі списку ребер до словника'
def build_graph(edge_list, directed=False):
    """
    Побудова графу на основі списку ребер

    Args:
        edge_list (list): Список ребер графу у вигляді кортежів (a, b)
        directed (bool): Прапорець, який визначає, чи є граф напрямленим

    Returns:
        dict: Граф, представлений у вигляді словника

    Приклад:
    >>> edge_list = [('A', 'B'), ('B', 'C')]
    >>> build_graph(edge_list)
    {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}
    """
    graph = {}
    for a, b in edge_list:
        graph.setdefault(a, []).append(b)
        if not directed:
            graph.setdefault(b, []).append(a)
    return graph

def read_graph_from_file(filename):
    """
    Читає граф з файлу та повертає список ребер

    Args:
        filename (str): Шлях до файлу з описом графу.

    Returns:
        list: Список ребер графу.
    """
    edge_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split()
                if len(parts) != 2:
                    print(f"Неправильний формат рядка: {line}")
                    continue
                a, b = parts
                edge_list.append((a, b))
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    return edge_list
