#Dado la dimensión de una matriz cuadrada muestre los
#valores en forma de caracol o vórtice.
def caracol(matriz):
    if not matriz or not matriz[0]: # O(1)
        return

    n = len(matriz) # O(1)
    inicio_fila, inicio_columna = 0, 0 # O(1)
    fin_fila, fin_columna = n - 1, n - 1 # O(1)

    while inicio_fila <= fin_fila and inicio_columna <= fin_columna: # O(n)

        for i in range(inicio_fila, fin_fila + 1):  # O(n)
            print(matriz[i][inicio_columna], end=" ")  # O(n)

        inicio_columna += 1  # O(1)

        for i in range(inicio_columna, fin_columna + 1):  # O(n)
            print(matriz[fin_fila][i], end=" ")  # O(n)

        fin_fila -= 1  # O(1)

        for i in range(fin_fila, inicio_fila - 1, -1):  # O(n)
            print(matriz[i][fin_columna], end=" ")  # O(n)

        fin_columna -= 1  # O(1)

        for i in range(fin_columna, inicio_columna - 1, -1):  # O(n)
            print(matriz[inicio_fila][i], end=" ")  # O(n)

        inicio_fila += 1  # O(1)

# Ejemplo de uso con la matriz dada
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

caracol(matriz)

#BigO =  # O(n^2)
#Complejidad espacial: O(n^2) 
