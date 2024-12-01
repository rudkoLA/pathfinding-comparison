"Time"

import time
from typing import Callable, Dict, List, Tuple, Optional

def time_algorithm(algorithm: Callable, graph: Dict[str, List[Tuple[str, float]]], start: str, goal: str, **kwargs) -> Optional[Tuple[List[str], float, float]]:
    """
    Вимірює час виконання алгоритму пошуку шляху.

    Args:
        algorithm (Callable): Алгоритм пошуку шляху.
        graph (dict): Граф у форматі словника з вагами.
        start (str): Початкова вершина.
        goal (str): Цільова вершина.
        **kwargs: Додаткові аргументи для алгоритму (наприклад, heuristic для A*).

    Returns:
        tuple[list[str], float, float]: Шлях, сумарна вага та час виконання.
                                       Повертає None, якщо шляху немає.
    """
    start_time = time.perf_counter()
    result = algorithm(graph, start, goal, **kwargs)
    end_time = time.perf_counter()
    exec_time = end_time - start_time

    if result:
        path, total_weight = result
        return (path, total_weight, exec_time)
    else:
        return None
