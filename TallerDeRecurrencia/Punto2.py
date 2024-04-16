# NO-RECURSIVO---------------------------------------------------
def resolver_recurrencia(coeficientes, condiciones_iniciales, n):
    # Verificar si la recurrencia es lineal homogénea
    grado = len(coeficientes) - 1
    if grado < 0:
        return 0  # Recurrencia trivial f(n) = 0

    # Verificar si hay suficientes condiciones iniciales
    if len(condiciones_iniciales) <= grado:
        raise ValueError("No hay suficientes condiciones iniciales para resolver la recurrencia.")

    # Crear una lista para almacenar los términos de la secuencia
    secuencia = condiciones_iniciales[:]

    # Calcular los términos adicionales de la secuencia hasta alcanzar n
    for i in range(len(secuencia), n + 1):
        nuevo_termino = 0
        for j in range(1, grado + 1):
            nuevo_termino += coeficientes[j] * secuencia[i - j]
        secuencia.append(nuevo_termino)

    # Devolver el término n de la secuencia
    return secuencia[n]

#RECURSIVO-----------------------------------------------
def resolver_recurrencia_recursivo(coeficientes, condiciones_iniciales, n):
    # Comprueba si n está dentro del rango de condiciones iniciales
    if n < len(condiciones_iniciales):
        return condiciones_iniciales[n]

    # Inicializa la lista de la secuencia con las condiciones iniciales
    secuencia = condiciones_iniciales[:]

    # Calcula los términos adicionales de la secuencia hasta alcanzar n
    for i in range(len(condiciones_iniciales), n + 1):
        nuevo_termino = 0
        # Aquí se produce la recursión para calcular el nuevo término
        for j in range(1, len(coeficientes)):
            nuevo_termino += coeficientes[j] * secuencia[i - j]
        secuencia.append(nuevo_termino)

    # Devuelve el término n de la secuencia
    return secuencia[n]



# Coeficientes y condiciones iniciales específicos para el problema dado
coeficientes = [2, -2]  # Coeficientes de la recurrencia: a_n = 2*a_{n-1} - 2*a_{n-2}
condiciones_iniciales = [4, 1]  # Condiciones iniciales: a_0 = 4, a_1 = 1
n =  1879  # Calcular a_1000

resultado = resolver_recurrencia(coeficientes, condiciones_iniciales, n)
print("El valor de la recurrencia en el índice", n, "es:", resultado)

resultado2 = resolver_recurrencia_recursivo(coeficientes, condiciones_iniciales, n)
print("Con recursion el valor de la recurrencia en el índice", n, "es:", resultado2)

