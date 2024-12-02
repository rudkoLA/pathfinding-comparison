"Time"

import time

def time_algorithm(algorithm, graph, start, goal, **kwargs):
    """
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
