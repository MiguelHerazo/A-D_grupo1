import math  # O(1)

def variaciones_con_repeticion(m, n):  # O(1)
    return m ** n  # O(1)

def variaciones_sin_repeticion(m, n):  # O(n)
    return math.factorial(m) // math.factorial(m - n)  # O(m)

