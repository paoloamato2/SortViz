# visualizer/sorting_visualizer.py
import time
import matplotlib.pyplot as plt

class SortingVisualizer:
    def __init__(self, algorithm, data, speed):
        self.algorithm = algorithm
        self.data = data
        self.speed = speed

    def visualize(self):
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
