#NORECURSIVO
def geometric_progression_term(a, r, n):
    if n <= 0:
        raise ValueError("La posición n debe ser un entero positivo.")
    # Calcular el término en la posición n
    term_n = a * (r ** (n - 1))
    return term_n
#RECURSIVO
def geometric_progression_term_r(a, r, n):
    if n <= 0:
        raise ValueError("La posición n debe ser un entero positivo.")
    # Calcular el término en la posición n
    term_n = a * (r ** (n - 1))
    return term_n
    
def find_ratio():
    # Resolver la ecuación 4r - 5 = 0 para encontrar r
    r = 5 / 4
    return r

def interpolated_term(a, r, n):
    if n <= 0:
        raise ValueError("La posición n debe ser un entero positivo.")
    
    # Calcular la parte entera de n
    integer_part = int(n)
    # Calcular la parte decimal de n
    decimal_part = n - integer_part
    
    # Calcular el término en la posición n sin la parte decimal
    term_n = geometric_progression_term(a, r, integer_part)
    
    # Calcular el siguiente término
    next_term = geometric_progression_term(a, r, integer_part + 1)
    
    # Calcular el término interpolado
    interpolated_term = term_n + decimal_part * (next_term - term_n)
    
    return interpolated_term

try:
    # Definir el primer término y la posición n
    a = 1  # Primer término
    n = 1245.123  # Posición

    # Encontrar la razón r
    r = find_ratio()

    # Calcular el término en la posición n
    term_n = interpolated_term(a, r, n)
    print("El término en la posición", n, "es:", term_n)

except ValueError as ve:
    print("Error:", ve)
