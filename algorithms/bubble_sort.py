# bubble_sort.py
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Scambia gli elementi se sono fuori ordine
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr  # Restituisci il passo corrente

    yield arr  # Restituisci il risultato finale
