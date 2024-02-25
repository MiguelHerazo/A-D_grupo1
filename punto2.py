def sum_digits(number):
    sum = 0                  # Complejidad Espacial: O(1)
    while number != 0:       # Complejidad Espacial: O(1)
        digit = number % 10  # Complejidad Espacial: O(1)
        sum += digit         # Complejidad Espacial: O(1)
        number //= 10        # Complejidad Espacial: O(1)
    return sum

                            # Complejidad Temporal: O(n), donde n es la cantidad de dígitos en el número de entrada.
# Ejemplo
number = 12345
result = sum_digits(number)
print(f"la suma de los digitos es {result}")
