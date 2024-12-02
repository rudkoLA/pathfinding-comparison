import random
import string

def generate_random_graph():
    # Визначаємо кількість вершин від 10 до 100
    num_vertices = random.randint(10, 100)
    
    # Функція для генерації унікальних ідентифікаторів вершин (a, b, ..., z, aa, ab, ...)
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
    
    # Визначаємо кількість ребер від 50 до 150, не більше можливих без повторів і без циклів
    max_edges = num_vertices * (num_vertices - 1) // 2
    num_edges = random.randint(50, min(150, max_edges))
    
    # Генеруємо всі можливі ребра без повторів і без циклів
    possible_edges = [(u, v) for idx, u in enumerate(vertices) for v in vertices[idx+1:]]
    
    # Випадково вибираємо необхідну кількість ребер
    selected_edges = random.sample(possible_edges, num_edges)
    
    graph = {vertex: [] for vertex in vertices}
    for u, v in selected_edges:
        weight = random.randint(1, 10)
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    
    return graph
print(generate_random_graph())