# main.py
import sys
import os

from algorithms import bubble_sort, selection_sort, insertion_sort
from visualizer import gui
import sys

def main():
    """
    Entry point of the program.
    Runs the GUI and exits the program afterwards.
    """
    gui.run_gui()

    sys.exit()

if __name__ == "__main__":
    main()