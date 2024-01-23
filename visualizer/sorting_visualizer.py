# visualizer/sorting_visualizer.py
import time
import matplotlib.pyplot as plt

class SortingVisualizer:
    """
    A class for visualizing sorting algorithms.

    Attributes:
        algorithm (function): The sorting algorithm to visualize.
        data (list): The data to be sorted.
        speed (float): The speed of the visualization.

    Methods:
        visualize: Visualizes the sorting process.
    """

    def __init__(self, algorithm, data, speed):
        self.algorithm = algorithm
        self.data = data
        self.speed = speed

    def visualize(self):
        """
        Visualizes the sorting process using matplotlib.

        This method creates a bar chart to represent the initial list,
        then iterates through each step of the sorting algorithm and
        updates the bar chart accordingly. Finally, it displays the
        sorted list.

        Returns:
            None
        """
        fig, ax = plt.subplots()
        ax.bar(range(len(self.data)), self.data, color='lightblue')
        ax.set_title('Initial List')
        plt.pause(1/self.speed)

        last_sorted_state = self.data.copy()

        num_steps = 0
        for i, step in enumerate(self.algorithm(self.data.copy())):
            ax.clear()
            ax.bar(range(len(step)), step, color='lightgreen')
            ax.set_title(f'Sorting Step {i+1}')
            plt.pause(1/self.speed)
            last_sorted_state = step.copy()
            num_steps += 1

        ax.clear()
        ax.bar(range(len(last_sorted_state)), last_sorted_state, color='lightcoral')
        ax.set_title(f'Sorted List ({num_steps} steps)')
        plt.show()
        plt.close()
