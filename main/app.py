'''графічний інтерфейс'''

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from algorithms import bfs, dfs, dijkstra, astar, bellman_ford, floyd_warshall, spfa
from graph_utils import read_graph_from_file, build_graph, graph_to_edge_list
from timing import time_algorithm
from visualization import visualize_graph
import generate_graph
import matplotlib.pyplot as plt

def create_widgets(root):
    """
    Create elements for interface
    """
    widgets = {}

    style = ttk.Style()
    style.configure("Custom.TButton", foreground="#000000", font=("Arial", 12))


    frame = tk.Frame(root, bg="#d5f0f9", padx=65, pady=35, highlightthickness=2)
    frame.pack(pady=20)

    widgets['load_button'] = ttk.Button(frame, text="Вибрати файл", style="Custom.TButton")
    widgets['load_button'].grid(row=0, column=0, padx=5, pady=15)

    widgets['generate_graph'] = ttk.Button(frame, text="Згенерувати граф", style="Custom.TButton")
    widgets['generate_graph'].grid(row=0, column=1, padx=5, pady=15)

    ttk.Label(frame, text="Стартова вершина:", font=("Arial", 12), background="#d5f0f9")\
                                                .grid(row=1, column=0, sticky="w", pady=5)
    widgets['start_entry'] = ttk.Entry(frame, width=20)
    widgets['start_entry'].grid(row=1, column=1, pady=5)

    ttk.Label(frame, text="Цільова вершина:", font=("Arial", 12), background="#d5f0f9")\
                                                .grid(row=2, column=0, sticky="w", pady=5)
    widgets['goal_entry'] = ttk.Entry(frame, width=20)
    widgets['goal_entry'].grid(row=2, column=1, pady=10)

    widgets['directed_var'] = tk.BooleanVar()
    widgets['directed_check'] = tk.Checkbutton(frame, text="Направлений граф",\
        variable=widgets['directed_var'], background='White', font=("Arial", 12))
    widgets['directed_check'].grid(row=3, column=0, columnspan=2, pady=10)


    widgets['run_button'] = ttk.Button(frame, text="Запустити алгоритми", style="Custom.TButton")
    widgets['run_button'].grid(row=4, column=0, columnspan=2, pady=5)

    widgets['visualize_button'] = ttk.Button(frame, text="Візуалізувати граф",\
                                                    style="Custom.TButton")
    widgets['visualize_button'].grid(row=5, column=0, columnspan=2, pady=5)

    widgets['output_text'] = tk.Text(root, width=90, height=30)
    widgets['output_text'].pack(pady=15)

    return widgets

def load_graph(state, widgets):
    """
    Gets graph from file.
    """
    filename = filedialog.askopenfilename(title="Виберіть файл з графом")
    if filename:
        edge_list = read_graph_from_file(filename)
        if not edge_list:
            messagebox.showerror("Помилка", "Не вдалося завантажити граф. Перевірте файл")
        else:
            state['edge_list'] = edge_list
            state['graph'] = build_graph(edge_list, state.get('directed', False))
            messagebox.showinfo("Успіх!", "Граф успішно завантажено")

def random_graph(state, widgets):
    """
    Random graph widget generator.
    """
    graph = generate_graph.generate_random_graph()
    state['graph'] = graph
    state['edge_list'] = graph_to_edge_list(graph, state.get('directed', False))
    messagebox.showinfo("Успіх!", "Граф успішно згенеровано")
    widgets['output_text'].delete(1.0, tk.END)
    widgets['output_text'].insert(tk.END,\
        f"Граф містить вершини: {graph_to_edge_list(graph, state.get('directed', False))}\n\n")

def run_algorithms(state, widgets):
    """
    Виконує алгоритми пошуку шляху та виводить результати.
    """
    if not state.get('graph'):
        messagebox.showwarning("Попередження", "Спочатку завантажте граф.")
        return None

    state['directed'] = widgets['directed_var'].get()
    state['graph'] = build_graph(state['edge_list'], state['directed'])

    start = widgets['start_entry'].get()
    goal = widgets['goal_entry'].get()

    if not start or not goal:
        messagebox.showerror("Помилка", "Введіть стартову та цільову вершину.")
        return None

    if start not in state['graph'] or goal not in state['graph']:
        messagebox.showerror("Помилка", "Стартова або цільова вершина відсутня у графі.")
        return None

    algorithms = [
        ('BFS', bfs),
        ('DFS', dfs),
        ('Dijkstra', dijkstra),
        ('A*', astar),
        ('Bellman-Ford', bellman_ford),
        ('Floyd-Warshall', floyd_warshall),
        ('SPFA', spfa)
    ]

    widgets['output_text'].delete(1.0, tk.END)
    state['times'] = {}
    state['paths'] = {}


    for name, algorithm in algorithms:
        result = time_algorithm(algorithm, state['graph'], start, goal)

        if result:
            path, total_weight, exec_time = result
            state['times'][name] = exec_time
            state['paths'][name] = path
            widgets['output_text'].insert(tk.END,\
                    f"Знайдений шлях ({name}): {path} з сумарною вагою {total_weight}\n")
            widgets['output_text'].insert(tk.END, f"Час виконання: {exec_time:.7f} секунд\n\n")
        else:
            widgets['output_text'].insert(tk.END, f"Шлях не знайдено ({name}).\n\n")
            state['times'][name] = None
            state['paths'][name] = None

    plot_times(state['times'])

def visualize(state):
    """
    Візуалізує граф та (якщо можливо) виділяє знайдені шляхи.
    """
    if not state.get('graph'):
        messagebox.showwarning("Попередження", "Спочатку завантажте граф.")
        return None

    if not any(state.get('paths').values()):
        messagebox.showwarning("Попередження",\
                               "Спочатку запустіть алгоритми для знаходження шляхів.")
        return None

    algorithm_window = tk.Toplevel()
    algorithm_window.title("Виберіть алгоритм для візуалізації шляху")

    tk.Label(algorithm_window, text="Виберіть алгоритм:").pack(pady=5)

    algorithms_with_paths = [name for name, path in state['paths'].items() if path]

    if not algorithms_with_paths:
        messagebox.showwarning("Попередження",\
                               "Немає алгоритмів з знайденими шляхами для візуалізації.")
        algorithm_window.destroy()
        return None

    selected_algorithm = tk.StringVar()
    selected_algorithm.set(algorithms_with_paths[0])

    for algo in algorithms_with_paths:
        tk.Radiobutton(algorithm_window, text=algo, variable=selected_algorithm, value=algo)\
            .pack(anchor='w')

    def on_confirm():
        algorithm = selected_algorithm.get()
        path = state['paths'].get(algorithm)
        algorithm_window.destroy()
        if path:
            visualize_graph(state['graph'], directed=state['directed'], path=path)
        else:
            messagebox.showinfo("Інформація", f"Алгоритм {algorithm} не має знайденого шляху.")

    tk.Button(algorithm_window, text="Візуалізувати", command=on_confirm).pack(pady=10)

def plot_times(times):
    """
    Побудовує графік часу виконання алгоритмів.
    """
    algorithm_names = [name for name, t in times.items() if t is not None]
    execution_times = [t for t in times.values() if t is not None]

    if not execution_times:
        return None

    plt.figure(figsize=(10, 6))
    plt.bar(algorithm_names, execution_times, color='skyblue')
    plt.xlabel('Алгоритми')
    plt.ylabel('Час виконання')
    plt.title('Порівняння часу виконання алгоритмів')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
