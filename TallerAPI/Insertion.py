def insertion_sort(arr, columna):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][columna] > key[columna]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr