def imprimir_en_caracol_inverso(matriz):
    if not matriz:
        return

    filas, columnas = len(matriz), len(matriz[0])
    inicio_fila, inicio_columna = 0, 0
    fin_fila, fin_columna = filas - 1, columnas - 1

    while inicio_fila <= fin_fila and inicio_columna <= fin_columna:
        for i in range(inicio_fila, fin_fila + 1):
            print(matriz[i][inicio_columna], end=" ")

        inicio_columna += 1

        for i in range(inicio_columna, fin_columna + 1):
            print(matriz[fin_fila][i], end=" ")

        fin_fila -= 1

        if inicio_columna <= fin_columna:
            for i in range(fin_fila, inicio_fila - 1, -1):
                print(matriz[i][fin_columna], end=" ")

            fin_columna -= 1

        if inicio_fila <= fin_fila:
            for i in range(fin_columna, inicio_columna - 1, -1):
                print(matriz[inicio_fila][i], end=" ")

            inicio_fila += 1

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

imprimir_en_caracol_inverso(matriz)
