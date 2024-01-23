# model.py
from visualizer.sorting_visualizer import SortingVisualizer

class SortingAppModel:
    def visualize_sorting(self, algorithm, data, speed):
        visualizer = SortingVisualizer(algorithm, data, speed)
        visualizer.visualize()
