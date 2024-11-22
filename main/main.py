'головний модуль'
import tkinter as tk
import app

def main():
    root = tk.Tk()
    root.title("Алгоритми пошуку шляху")

    state = {
        'edge_list': [],
        'graph': {},
        'directed': False,
        'times': {},
        'paths': {}
    }

    widgets = app.create_widgets(root)

    widgets['load_button'].config(command=lambda: app.load_graph(state))
    widgets['run_button'].config(command=lambda: app.run_algorithms(state, widgets))
    widgets['visualize_button'].config(command=lambda: app.visualize(state))

    root.mainloop()

if __name__ == "__main__":
    main()
