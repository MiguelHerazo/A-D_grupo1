#PERMUTACIONES SOLAMENTE NUMERICAS
import math
def permutacion_con_repeticion(m, n):  # 0(1)
    factorial_suma_repeticiones = math.factorial(m + n - 1)  # 0(1)
    factorial_m = math.factorial(m)  # 0(1)
    resultado = factorial_suma_repeticiones // factorial_m  # 0(1)
    return resultado  # 0(1)


def permutacion_sin_repeticion(m):  # 0(1)
    resultado = math.factorial(m)  # 0(1)
    return resultado  # 0(1)
