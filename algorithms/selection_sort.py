# selection_sort.py
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Scambia gli elementi se necessario
        arr[i], arr[min_index] = arr[min_index], arr[i]
        yield arr  # Restituisci il passo corrente

    yield arr  # Restituisci il risultato finale
