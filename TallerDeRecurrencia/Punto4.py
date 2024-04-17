########### Encontrar n =151’145.018. y multiplicarlo por el número de letras de su nombre ############

###################################### No recursivo ###########################################

def calcular_termino(n):
    if not isinstance(n, int):
        raise TypeError("El valor de n debe ser un entero.")
    
    if n < 0:
        raise ValueError("El valor de n debe ser no negativo.")

    nombre_multiplicado = len("Dilan")

    # Valores iniciales multiplicados por el nombre
    a_0 = 1 * nombre_multiplicado
    a_1 = 3 * nombre_multiplicado

    if n == 0:
        return a_0
    elif n == 1:
        return a_1

    try:
        # Inicializamos una lista para almacenar los valores calculados
        a = [None] * (n + 1)
        a[0] = a_0
        a[1] = a_1

        # Hacemos un ciclo para calcular los términos sucesivos de la recurrencia iniciando desde 2
        for i in range(2, n + 1):
            a[i] = 5 * a[i - 1] + 6 * a[i - 2]

            # Si se supera el límite permitido, lanzamos una excepción
            if a[i] > 10**99999:
                raise ValueError("Error: El valor del término en la posición {} supera el límite permitido.".format(n))

            # Si el valor resultante es negativo, lanzamos una excepción
            if a[i] < 0:
                raise ValueError("Error: El valor del término en la posición {} es negativo.".format(n))

        # Retornar el término en la posición n
        return a[n]
    except IndexError as error_indice:
        raise IndexError("Error de índice durante el cálculo del término en la posición {}: {}".format(n, error_indice))
    except MemoryError as error_memoria:
        raise MemoryError("Error de memoria durante el cálculo: {}".format(error_memoria))
    except RecursionError as error_recursion:
        raise RecursionError("Error de recursión: {}".format(error_recursion))

# Calculamos el número en la posición n
n = 151145018
try:
    resultado = calcular_termino(n)
    print("El término en la posición n =", n, "es:", resultado)
except ValueError as error_valor:
    print("Error:", error_valor)
except OverflowError as error_desbordamiento:
    print("Error:", error_desbordamiento)
except TypeError as error_tipo:
    print("Error:", error_tipo)
except IndexError as error_indice:
    print("Error:", error_indice)
except MemoryError as error_memoria:
    print("Error en la capacidad de memoria usable:", error_memoria)
except RecursionError as error_recursion:
    print("Error en el calculo:", error_recursion)


#################################### Recursivo #############################################

def calcular_termino_recursivo(n):
    if not isinstance(n, int):
        raise TypeError("El valor de n debe ser un entero.")
    
    if n < 0:
        raise ValueError("El valor de n debe ser no negativo.")

    nombre_multiplicado = len("Dilan")

    if n == 0:
        return 1 * nombre_multiplicado
    elif n == 1:
        return 3 * nombre_multiplicado

    try:
        # Usamos la fórmula para calcular el término en la posición n recursivamente
        return 5 * calcular_termino_recursivo(n - 1) + 6 * calcular_termino_recursivo(n - 2)
    except RecursionError as error_recursion:
        raise RecursionError("Error de recursión: {}".format(error_recursion))
    except MemoryError as error_memoria:
        raise MemoryError("Error de memoria durante el cálculo: {}".format(error_memoria))

# Calculamos el número en la posición n
n = 151145018
try:
    resultado = calcular_termino_recursivo(n)
    print("El término en la posición n =", n, "es:", resultado)
except ValueError as error_valor:
    print("Error:", error_valor)
except RecursionError as error_recursion:
    print("Error en el cálculo:", error_recursion)
except MemoryError as error_memoria:
    print("Error en la capacidad de memoria usable:", error_memoria)
except TypeError as error_tipo:
    print("Error:", error_tipo)
