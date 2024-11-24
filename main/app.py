'графічний інтерфейс'

import tkinter as tk
from tkinter import filedialog, messagebox
from algorithms import bfs, dfs, dijkstra, astar, bellman_ford, spfa
from graph_utils import read_graph_from_file, build_graph
from timing import time_algorithm
from visualization import visualize_graph
import matplotlib.pyplot as plt

def create_widgets(root):
    """
    Створює елементи інтерфейсу та повертає їх у вигляді словника.
    """
    widgets = {}

    frame = tk.Frame(root)
    frame.pack(pady=10)

    widgets['load_button'] = tk.Button(frame, text="Завантажити граф")
    widgets['load_button'].grid(row=0, column=0, padx=5)

    tk.Label(frame, text="Стартова вершина:").grid(row=1, column=0, sticky='e')
    widgets['start_entry'] = tk.Entry(frame)
    widgets['start_entry'].grid(row=1, column=1)

    tk.Label(frame, text="Цільова вершина:").grid(row=2, column=0, sticky='e')
    widgets['goal_entry'] = tk.Entry(frame)
    widgets['goal_entry'].grid(row=2, column=1)

    widgets['directed_var'] = tk.BooleanVar()
    widgets['directed_check'] = tk.Checkbutton(frame, text="Напрямлений граф", variable=widgets['directed_var'])
    widgets['directed_check'].grid(row=3, column=0, columnspan=2)

    widgets['run_button'] = tk.Button(frame, text="Запустити алгоритми")
    widgets['run_button'].grid(row=4, column=0, columnspan=2, pady=5)

    widgets['visualize_button'] = tk.Button(frame, text="Візуалізувати граф")
    widgets['visualize_button'].grid(row=5, column=0, columnspan=2, pady=5)

    widgets['output_text'] = tk.Text(root, width=80, height=20)
    widgets['output_text'].pack(pady=10)

    return widgets

def load_graph(state):
    """
    Завантажує граф з файлу та оновлює стан.
    """

    filename = filedialog.askopenfilename(title="Виберіть файл з графом")
    if filename:
        state['edge_list'] = read_graph_from_file(filename)
        if not state['edge_list']:
            messagebox.showerror("Помилка", "Не вдалося завантажити граф. Перевірте файл.")
        else:
            messagebox.showinfo("Успіх", "Граф успішно завантажено.")

def run_algorithms(state, widgets):
    """
    Виконує алгоритми пошуку шляху та виводить результати.
    """
    if not state.get('edge_list'):
        messagebox.showwarning("Попередження", "Спочатку завантажте граф.")
        return

    state['directed'] = widgets['directed_var'].get()
    state['graph'] = build_graph(state['edge_list'], state['directed'])

    start = widgets['start_entry'].get()
    goal = widgets['goal_entry'].get()

    if start not in state['graph'] or goal not in state['graph']:
        messagebox.showerror("Помилка", "Стартова або цільова вершина відсутня у графі.")
        return

    algorithms = [
        ('BFS', bfs),
        ('DFS', dfs),
        ('Алгоритм Дейкстри', dijkstra),
        ('Алгоритм A*', astar),
        ('Алгоритм Беллмана-Форда', bellman_ford),
        ('SPFA', spfa)
    ]

    widgets['output_text'].delete(1.0, tk.END)
    state['times'] = {}
    state['paths'] = {}

    for name, algorithm in algorithms:
        path, exec_time = time_algorithm(algorithm, state['graph'], start, goal)
        state['times'][name] = exec_time
        if path:
            state['paths'][name] = path
            widgets['output_text'].insert(tk.END, f"Знайдений шлях ({name}): {path}\n")
        else:
            widgets['output_text'].insert(tk.END, f"Шлях не знайдено ({name}).\n")
        widgets['output_text'].insert(tk.END, f"Час виконання: {exec_time:.6f} секунд\n\n")

    plot_times(state['times'])

def visualize(state):
    """
    Візуалізує граф та (якщо можливо) виділяє знайдені шляхи.
    """
    if not state.get('edge_list'):
        messagebox.showwarning("Попередження", "Спочатку завантажте граф.")
        return

    if not state.get('paths'):
        messagebox.showwarning("Попередження", "Спочатку запустіть алгоритми для знаходження шляхів.")
        return

    algorithm_window = tk.Toplevel()
    algorithm_window.title("Виберіть алгоритм для візуалізації шляху")

    tk.Label(algorithm_window, text="Виберіть алгоритм:").pack(pady=5)

    algorithms_with_paths = list(state['paths'].keys())

    selected_algorithm = tk.StringVar()
    selected_algorithm.set(algorithms_with_paths[0])

    for algo in algorithms_with_paths:
        tk.Radiobutton(algorithm_window, text=algo, variable=selected_algorithm, value=algo).pack(anchor='w')

    def on_confirm():
        algorithm = selected_algorithm.get()
        path = state['paths'].get(algorithm)
        algorithm_window.destroy()
        visualize_graph(state['edge_list'], directed=state['directed'], path=path)

    tk.Button(algorithm_window, text="Візуалізувати", command=on_confirm).pack(pady=10)

def plot_times(times):
    """
    Побудовує графік часу виконання алгоритмів.
    """
    algorithm_names = list(times.keys())
    execution_times = [times[name] for name in algorithm_names]

    plt.figure(figsize=(8, 6))
    plt.bar(algorithm_names, execution_times, color='skyblue')
    plt.xlabel('Алгоритми')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння часу виконання алгоритмів')
    plt.show()
