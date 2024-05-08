#Tienes dos arreglos A  y B  de igual longitud N .
# Su tarea es emparejar cada elemento de la matriz A
# con un elemento de la matriz B , de modo que la suma de las
# diferencias absolutas de todos los pares sea mínima.

def min_absolute_difference(A, B, index=0, current_pairs=None, min_diff=float('inf'), min_pairs=None):
    if current_pairs is None:
        current_pairs = []

    if index == len(A):
        diff = sum(abs(a - b) for a, b in current_pairs)
        if diff < min_diff:
            min_diff = diff
            min_pairs = current_pairs
        return min_diff, min_pairs

    for b in B:
        new_pairs = current_pairs + [(A[index], b)]
        diff, pairs = min_absolute_difference(A, B, index + 1, new_pairs, min_diff, min_pairs)
        if diff < min_diff:
            min_diff = diff
            min_pairs = pairs

    return min_diff, min_pairs

A = [1, 3, 5]
B = [2, 4, 6]
min_diff, pairs = min_absolute_difference(A, B)
print("Mínima diferencia absoluta:", min_diff)
print("Pares de emparejamiento que la logran:", pairs)
