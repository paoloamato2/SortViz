def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the elements if necessary
        arr[i], arr[min_index] = arr[min_index], arr[i]
        yield arr  # Return the current step

    yield arr  # Return the final result
