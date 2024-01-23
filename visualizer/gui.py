# gui.py
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from algorithms import bubble_sort
from visualizer import visualization
import algorithms

def start_sorting(algorithm_var, list_entry, speed_var):
    selected_algorithm = algorithm_var.get()
    data = list(map(int, list_entry.get().split(',')))
    size = int(len(data))
    speed = int(speed_var.get())

    # Get the sublist to be sorted
    sublist_to_sort = data[:size]

    # Import the algorithm based on the selected name
    algorithm_module = getattr(algorithms, selected_algorithm, None)
    
    # Get the function associated with the selected algorithm
    algorithm_function = getattr(algorithm_module, selected_algorithm, None)

    # Execute the sorting algorithm
    if algorithm_function:
        visualization.visualize_sorting(algorithm_function, sublist_to_sort, speed)

def run_gui():
    root = tk.Tk()
    root.title("Sorting Algorithm Visualizer")

    # Apply a custom theme to the main window
    style = ThemedStyle(root)
    style.set_theme("arc")

    # Tkinter variables for dropdown menu and text box
    algorithm_var = tk.StringVar(root)
    list_var = tk.StringVar(root)
    speed_var = tk.StringVar(root)

    # Labels for the dropdown menu and text box
    algorithm_label = tk.Label(root, text="Algorithm:")
    algorithm_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    list_label = tk.Label(root, text="List:")
    list_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    speed_label = tk.Label(root, text="Speed:")
    speed_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

    # Options for the algorithm dropdown menu
    algorithms = ['bubble_sort', 'insertion_sort', 'selection_sort']
    algorithm_var.set(algorithms[0])

    # Create the dropdown menu for algorithms
    algorithm_menu = ttk.Combobox(root, textvariable=algorithm_var, values=algorithms)
    algorithm_menu.grid(row=0, column=1, padx=10, pady=10)

    # Create the text box for the list
    list_entry = tk.Entry(root, textvariable=list_var, width=50)
    list_entry.grid(row=1, column=1, padx=10, pady=10)
    list_var.set("10, 20, 30, 40, 50, 60, 70, 80, 90, 100")

    # Create the text box for the visualization speed
    speed_entry = tk.Entry(root, textvariable=speed_var)
    speed_entry.grid(row=2, column=1, padx=10, pady=10)
    speed_var.set(1)

    # Button to start the sorting
    start_button = tk.Button(root, text="Start Sorting", command=lambda: start_sorting(algorithm_var, list_entry, speed_var))
    start_button.grid(row=3, column=1, padx=10, pady=10)

    # Configure columns and rows to expand with window resizing
    for i in range(7):
        root.grid_columnconfigure(i, weight=1)
    for i in range(7):
        root.grid_rowconfigure(i, weight=1)

    # Start the main window
    root.mainloop()

