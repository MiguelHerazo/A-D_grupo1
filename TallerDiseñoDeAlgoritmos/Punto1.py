#Dada una matriz n*n mostrar el camino más óptimo desde la posición (0,0) a (n,n).

def greedy_path(matrix, x, y):
    if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
        return [(x, y)]
    
    if x == len(matrix) - 1:
        return [(x, y)] + greedy_path(matrix, x, y + 1)
    
    if y == len(matrix[0]) - 1:
        return [(x, y)] + greedy_path(matrix, x + 1, y)
    
    if matrix[x+1][y] < matrix[x][y+1]:
        return [(x, y)] + greedy_path(matrix, x + 1, y)
    else:
        return [(x, y)] + greedy_path(matrix, x, y + 1)

matrix = [
    [1, 3, -1],
    [1, -9, 1],
    [-4, 2, 1]
]

path = greedy_path(matrix, 0, 0)
print("Camino_Optimo:",path)
