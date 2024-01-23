# visualization.py
import time
import matplotlib.pyplot as plt
import numpy as np

def visualize_sorting(algorithm, data, speed):
    """
    Visualizes the sorting process using a bar chart.

    Parameters:
    algorithm (function): The sorting algorithm to be visualized.
    data (list): The list of data to be sorted.
    speed (float): The speed of the visualization.

    Returns:
    None
    """

    # Create a figure for the chart
    fig, ax = plt.subplots()

    # Display the initial list
    ax.bar(range(len(data)), data, color='lightblue')
    ax.set_title('Initial List')
    plt.pause(1/speed)

    last_sorted_state = data.copy()

    # Execute the sorting algorithm
    num_steps = 0  # Add a variable to count the number of steps
    for i, step in enumerate(algorithm(data.copy())):
        ax.clear()
        ax.bar(range(len(step)), step, color='lightgreen')
        ax.set_title(f'Sorting Step {i+1}')
        plt.pause(1/speed)  # You can adjust the pause as desired
        last_sorted_state = step.copy()
        num_steps += 1  # Increment the number of steps at each iteration

    # Display the final sorted list with the number of steps
    ax.clear()
    ax.bar(range(len(last_sorted_state)), last_sorted_state, color='lightcoral')
    ax.set_title(f'Sorted List ({num_steps} steps)')  # Add the number of steps to the title
    plt.show()

    # Close the chart window
    plt.close()
