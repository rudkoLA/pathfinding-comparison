'''main'''

import tkinter as tk
from tkinter import ttk
import app


def main():
    """
    Main function for this project.
    """
    root = tk.Tk()
    title_label = ttk.Label(root, text="Пошук найкоротшого шляху в Графах", \
                            font=("Arial", 18), background="#F0F8FF")
    title_label.pack(pady=20)

    root.configure(bg="#F0F8FF")

    icon_photo = tk.PhotoImage(file='logo.png')
    root.iconphoto(True, icon_photo)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    widgets = app.create_widgets(root)

    state = {}

    widgets['load_button'].config(command=lambda: app.load_graph(state, widgets))
    widgets['run_button'].config(command=lambda: app.run_algorithms(state, widgets))
    widgets['generate_graph'].config(command=lambda:app.random_graph(state, widgets))
    widgets['visualize_button'].config(command=lambda: app.visualize(state))
    root.mainloop()

if __name__ == '__main__':
    main()
