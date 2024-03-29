# main.py
import sys
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from model import SortingAppModel
from view import SortingAppView

class SortingAppController:
    """
    Controller class for the Sorting Algorithm Visualizer application.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sorting Algorithm Visualizer")

        self.model = SortingAppModel()
        self.view = SortingAppView(self.root, self)

    def run(self):
        """
        Runs the Sorting Algorithm Visualizer application.
        """
        self.root.mainloop()

    def start_sorting(self, algorithm, data, speed):
        """
        Starts the sorting process with the specified algorithm, data, and speed.

        Parameters:
        - algorithm (str): The sorting algorithm to use.
        - data (list): The data to be sorted.
        - speed (int): The speed of the sorting animation.
        """
        self.model.visualize_sorting(algorithm, data, speed)

if __name__ == "__main__":
    app_controller = SortingAppController()
    app_controller.run()
