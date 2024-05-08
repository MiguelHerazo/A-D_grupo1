#Dado un número N. Encuentra el número mínimo de operaciones
#necesarias para llegar a N  a partir de 0 . Tienes 2 operaciones disponibles:
#Duplicar el numero
#Añadir uno al número

def min_operaciones(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return min(min_operaciones(n // 2) + 1, min_operaciones(n - 1) + 1)
    else:
        return min_operaciones(n - 1) + 1

min_operaciones(7)

