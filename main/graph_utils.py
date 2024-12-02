'''Functions for working with files with graphs'''


def read_graph_from_file(filename):
    """
    read file and return edge_list

    """
    edge_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split()
                if len(parts) == 2:
                    parts.append(1)
                if len(parts) != 3:
                    print(f"Неправильний формат рядка {line_number}: {line}")
                    continue
                a, b, weight_str = parts
                try:
                    weight = float(weight_str)
                except ValueError:
                    print(f"Неправильна вага на рядку {line_number}: {weight_str}")
                    continue
                edge_list.append((a, b, weight))
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    return edge_list

def build_graph(edge_list, directed = False):
    """
    convert edge_list to dict form
    """
    graph = {}
    for a, b, weight in edge_list:
        graph.setdefault(a, []).append((b, weight))
        if not directed:
            graph.setdefault(b, []).append((a, weight))
    return graph



def graph_to_edge_list(graph, directed=False):
    """
    Перетворює граф, заданий у вигляді словника, у список тюплів (edge_list).

    :param graph: Словник, де ключі — вершини, а значення — списки кортежів (сусідня вершина, вага).
    :param directed: Булевий параметр, який вказує, чи граф орієнтований. За замовчуванням False.
    :return: Список кортежів у форматі (a, b, weight).
    """
    edge_list = []
    seen = set()
    for a in graph:
        for (b, weight) in graph[a]:
            if directed:
                edge = (a, b, weight)
                edge_list.append(edge)
            else:
                edge_key = tuple(sorted([a, b]))
                if edge_key not in seen:
                    edge = (a, b, weight)
                    edge_list.append(edge)
                    seen.add(edge_key)

    return edge_list