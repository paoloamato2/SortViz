# view.py
import tkinter as tk
from tkinter import ttk
from model import SortingAppModel
from algorithms import bubble_sort, insertion_sort, selection_sort

class SortingAppView:
    """
    The view class for the sorting visualizer application.
    """

    def __init__(self, root, controller):
        """
        Initializes the SortingAppView.

        Parameters:
        - root: The root Tkinter window.
        - controller: The controller object for the application.
        """

        self.controller = controller

        # Tkinter variables for dropdown menu and text box
        self.algorithm_var = tk.StringVar(root)
        self.list_var = tk.StringVar(root)
        self.speed_var = tk.StringVar(root)

        # Labels for the dropdown menu and text box
        algorithm_label = tk.Label(root, text="Algorithm:")
        algorithm_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        list_label = tk.Label(root, text="List:")
        list_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        speed_label = tk.Label(root, text="Speed:")
        speed_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        # Options for the algorithm dropdown menu
        algorithms = ['bubble_sort', 'insertion_sort', 'selection_sort']
        self.algorithm_var.set(algorithms[0])

        # Create the dropdown menu for algorithms
        algorithm_menu = ttk.Combobox(root, textvariable=self.algorithm_var, values=algorithms)
        algorithm_menu.grid(row=0, column=1, padx=10, pady=10)

        # Create the text box for the list
        self.list_entry = tk.Entry(root, textvariable=self.list_var, width=50)
        self.list_entry.grid(row=1, column=1, padx=10, pady=10)
        self.list_var.set("10, 20, 30, 40, 50, 60, 70, 80, 90, 100")

        # Create the text box for the visualization speed
        speed_entry = tk.Entry(root, textvariable=self.speed_var)
        speed_entry.grid(row=2, column=1, padx=10, pady=10)
        self.speed_var.set(1)

        # Button to start the sorting
        start_button = tk.Button(root, text="Start Sorting", command=self.start_sorting)
        start_button.grid(row=3, column=1, padx=10, pady=10)

        # Configure columns and rows to expand with window resizing
        for i in range(7):
            root.grid_columnconfigure(i, weight=1)
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)

    def start_sorting(self):
        """
        Starts the sorting process based on the selected algorithm, list, and speed.
        """

        algorithm_name = self.algorithm_var.get()
        data = list(map(int, self.list_entry.get().split(',')))
        speed = int(self.speed_var.get())

        # Map algorithm name to the corresponding function
        algorithm_functions = {
            'bubble_sort': bubble_sort.bubble_sort,
            'insertion_sort': insertion_sort.insertion_sort,
            'selection_sort': selection_sort.selection_sort
        }

        # Use the selected algorithm function
        algorithm_function = algorithm_functions.get(algorithm_name)

        if algorithm_function:
            self.controller.start_sorting(algorithm_function, data, speed)
