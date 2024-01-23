# main.py
import sys
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from model import SortingAppModel
from view import SortingAppView

class SortingAppController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sorting Algorithm Visualizer")

        self.model = SortingAppModel()
        self.view = SortingAppView(self.root, self)

    def run(self):
        self.root.mainloop()

    def start_sorting(self, algorithm, data, speed):
        self.model.visualize_sorting(algorithm, data, speed)

if __name__ == "__main__":
    app_controller = SortingAppController()
    app_controller.run()
