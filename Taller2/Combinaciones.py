import math

# Función para calcular combinaciones con repetición
def combinaciones_con_repeticion(m, n):
    return math.comb(m + n - 1, n)#O(n)

# Función para calcular combinaciones sin repetición
def combinaciones_sin_repeticion(m, n):
    return math.comb(m, n)#O(n)
