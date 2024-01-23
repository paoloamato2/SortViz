def bubble_sort(arr):
    """
    Sorts the given list using the bubble sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Yields:
        list: The current state of the list after each iteration.

    Returns:
        list: The final sorted list.
    """
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr  # Return the current step

    yield arr  # Return the final result
