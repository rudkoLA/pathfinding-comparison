"""Функції для аналізування часу виконання функцій"""

from time import time

def time_algorithm(func, *args) -> float:
    """
    Функція для рахування часу виконання функції func для параметрів заданих у *args.
    :param func: Callable, функція яку будеми тестити.
    :param *args: Callable, аргументи якими будем тестити данну функцію.
    :return: float, час який треба було функції щоб виконатись.
    """
    start_time = time()

    func(*args)

    return time() - start_time

def time_algorithm_with_functions(func, graph_func, node_func) -> list[float]:
    """
    Функція для рахування часу виконання функції func з аргументами функцій graph_func та node_func.
    :param func: Callable, функція яку будеми тестити.
    :param graph_func: Callable, функція яка мала би генерувати граф для тестування.
    :param node_func: Callable, функція яка мала би повертати одну точку з графа з graph_func.
    :return: float, час який треба було функції щоб виконатись.
    """

    graph = graph_func()

    return time_algorithm(func, graph_func(), node_func(graph), node_func(graph))


def time_algorithm_repeat(func, num: int, *args) -> list[float]:
    """
    Функція для повторного тестування данної функції func num разів з аргументами *args.
    :param func: Callable, функція яку будеми тестити.
    :param num: int, кількість виконання данної функції.
    :param *args: Callable, аргументи якими будем тестити данну функцію.
    :return: list[float], список часів виконання функції.
    """
    times = []

    for _ in range(num):
        times.append(time_algorithm(func, *args))

    return times


def time_algorithm_with_functions_repeat(func, num: int, graph_func, node_func) -> list[float]:
    """
    Функція для рахування часу виконання функції func з аргументами функцій graph_func та node_func.
    :param func: Callable, функція яку будеми тестити.
    :param num: int, кількість виконання данної функції.
    :param graph_func: Callable, функція яка мала би генерувати граф для тестування.
    :param node_func: Callable, функція яка мала би повертати одну точку з графа з graph_func.
    :return: list[float], список часів виконання функції.
    """
    times = []

    for _ in range(num):
        times.append(time_algorithm_with_functions(func, graph_func, node_func))

    return times



if __name__ == '__main__':
    from algorithms import astar

    print(time_algorithm(astar, {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}, "A", "D"))
    print(list(map(lambda x: round(x, 5), time_algorithm_repeat(astar, 10, \
    {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}, "A", "D"))))
