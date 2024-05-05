def insertion_sort(arr):
    # Iterar a través de la lista, comenzando desde el segundo elemento
    for i in range(1, len(arr)):
        # Guardar el valor actual para comparación
        key = arr[i]
        # Inicializar un índice para comparar con el elemento anterior
        j = i - 1
        # Mover los elementos mayores que el valor actual una posición hacia adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Colocar el valor actual en su posición correcta en la lista ordenada
        arr[j + 1] = key
