#Tienes dos arreglos A  y B  de igual longitud N .
# Su tarea es emparejar cada elemento de la matriz A
# con un elemento de la matriz B , de modo que la suma de las
# diferencias absolutas de todos los pares sea mínima.

def min_absolute_difference(A, B, index=0, current_pairs=None, min_diff=float('inf')):
    if current_pairs is None:
        current_pairs = []

    if index == len(A):
        diff = sum(abs(a - b) for a, b in current_pairs)
        return min(diff, min_diff)

    for b in B:
        diff = abs(A[index] - b)
        min_diff = min_absolute_difference(A, B, index + 1, current_pairs + [(A[index], b)], min_diff)
    
    return min_diff


A = [4, 1, 2]
B = [2,4,1]
min_diff = min_absolute_difference(A, B)
print("Mínima diferencia absoluta:", min_diff)

