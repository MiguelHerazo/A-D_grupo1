# 1. Encontrar la posición n=100

# Encuentre una relación de recurrencia, con una condición inicial, que determine de manera única cada una de las siguientes progresiones geométricas

# B) 6, -18, 54, -162,...

#----------------NO RECURSIVO-------------------

def termino_n_geometrica(a1, r, n):
    if not all(isinstance(arg, (int, float)) for arg in (a1, r, n)) or n <= 0:
        raise ValueError("Los argumentos deben ser: a1 (número), r (número), y n (entero positivo).")
    if r == 0 and n > 1:
        raise ValueError("r no puede ser cero si n es mayor que 1.")
    return a1 * (r ** (n - 1))

try:
    a1 = 6
    r = -3
    n = 100

    termino_100 = termino_n_geometrica(a1, r, n)
    print("El término en la posición n=100 es:", termino_100)
except ValueError as e:
    print("Error:", e)


#-----------------RECURSIVO---------------------

def term_n(a1, r, n):
    if not isinstance(a1, (int, float)) or not isinstance(r, (int, float)) or n <= 0:
        raise ValueError("Los parámetros a1 y r deben ser números enteros o flotantes, y n debe ser un entero positivo.")
        
    if n == 1:
        return a1
    else:
        return r * term_n(a1, r, n-1)

try:
    a1 = 6
    r = -3
    n = 100
    a_100 = term_n(a1, r, n)
    print("El término en la posición n=100 es:", a_100)
except ValueError as e:
    print("Error:", e)

