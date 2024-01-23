# model.py
from visualizer.sorting_visualizer import SortingVisualizer

class SortingAppModel:
    """
    Represents the model of the sorting application.

    This class provides methods to visualize sorting algorithms on given data.

    Attributes:
        None

    Methods:
        visualize_sorting: Visualizes the sorting algorithm on the given data with the specified speed.

    """

    def visualize_sorting(self, algorithm, data, speed):
        visualizer = SortingVisualizer(algorithm, data, speed)
        visualizer.visualize()
