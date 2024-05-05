def bubble_sort(arr, columna):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][columna] > arr[j+1][columna]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr