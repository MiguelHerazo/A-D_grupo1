########### Encontrar n =151’145.018. y multiplicarlo por el número de letras de su nombre ############

###################################### No recursivo ###########################################

def calcular_termino(n):
    nombre_multiplicado = len("Dilan")

    # Valoresiniciales multiplicados por el nombre
    a_0 = 1 * nombre_multiplicado
    a_1 = 3 * nombre_multiplicado

    if n == 0:
        return a_0
    elif n == 1:
        return a_1

    # inicializamos una lista para almacenar los valores calculados
    a = [None] * (n + 1)
    a[0] = a_0
    a[1] = a_1

    # hacemos un ciclo para calcular los términos sucesivos de la recurrencia iniando desde 2
    for i in range(2, n + 1):
        a[i] = 5 * a[i - 1] + 6 * a[i - 2] + 2 * nombre_multiplicado

        # nos retornara un mensaje de error si se supera el limite establecido
        if a[i] > 10**99999:
            return "Error: El valor del término en la posición {} supera el límite permitido.".format(n)


    # Retornar el termino en la posición n
    return a[n]

# calculamos el numero en la pocicion n
n = 151145018
resultado = calcular_termino(n)
print("El término en la posición n =", n, "es:", resultado)


#################################### Recursivo #############################################

def calcular_termino_recursivo(n):
    
    nombre_multiplicado = len("Dilan")

    if n == 0:
        return 1 * nombre_multiplicado
    elif n == 1:
        return 3 * nombre_multiplicado

    # usamos la formula para calcular el término en la posición n
    return 5 * calcular_termino_recursivo(n - 1) + 6 * calcular_termino_recursivo(n - 2) + 2 * nombre_multiplicado

# calculamos el numero en la pocicion n
n = 151145018
resultado = calcular_termino_recursivo(n)
print("El término en la posición n =", n, "es:", resultado)
