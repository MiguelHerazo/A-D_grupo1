def geometric_progression_term(a, r, n):
    term_n = a * (r ** (n - 1))
    return term_n


def interpolated_term(a, r, n):
    integer_part = int(n)
    decimal_part = n - integer_part


    term_n = geometric_progression_term(a, r, integer_part)
    next_term = geometric_progression_term(a, r, integer_part + 1)
    interpolated_term = term_n + decimal_part * (next_term - term_n)

    return interpolated_term


a = 1  # Primer término
r = 1.1  # Razón
n = 1245.123  # Posición

# Calcular el término en la posición n
term_n = interpolated_term(a, r, n)
print("El término en la posición", n, "es:", term_n)
