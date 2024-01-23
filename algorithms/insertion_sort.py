# insertion_sort.py
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr  # Restituisci il passo corrente
        arr[j + 1] = key
        yield arr  # Restituisci il passo corrente

    yield arr  # Restituisci il risultato finale
