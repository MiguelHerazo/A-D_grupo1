from itertools import permutations # IMPORTACIÓN DE MODULOS: Complejidad algorítmica: O(1), # Complejidad espacial: O(1)
from math import factorial

def validar_cadena(cadena): # Complejidad algorítmica: O(n), Complejidad espacial: O(1)
    if not isinstance(cadena, str):  # O(1)
        raise TypeError("La entrada debe ser una cadena de caracteres")  # O(1)
    if len(cadena) == 0:  # O(1)
        raise ValueError("La cadena no puede estar vacía")  # O(1)
    if not all(caracter.isalnum() for caracter in cadena):  # O(n)
        raise ValueError("La cadena solo puede contener caracteres alfanuméricos")  # O(1)

def obtener_permutaciones(cadena, con_repeticion=False): # Complejidad algorítmica: O(n!), Complejidad espacial: O(n!)
    validar_cadena(cadena)  # O(n)

    if con_repeticion:  # O(1)
        lista_permutaciones = list(permutations(cadena))  # O(n!)
        for permutacion in lista_permutaciones:  # O(n!)
            print(''.join(permutacion))  # O(n!)
        print("Se generaron {} permutaciones de la cadena '{}'.".format(len(lista_permutaciones), cadena))  # O(1)
        return lista_permutaciones  # O(n!)
    else:
        elementos_unicos = len(set(cadena))  # O(n)
        resultado = factorial(elementos_unicos)  # O(n!)
        print("El resultado de las permutaciones sin repetición es:", resultado)  # O(1)
        return resultado  # O(1)



#PERMUTACIONES SOLAMENTE NUMERICAS 
import math
def permutacion_con_repeticion(self, m, n):  # 0(1)
    factorial_suma_repeticiones = math.factorial(m + n - 1)  # 0(1)
    factorial_m = math.factorial(m)  # 0(1)
    resultado = factorial_suma_repeticiones // factorial_m  # 0(1)
    return resultado  # 0(1)


def permutacion_sin_repeticion(self, m):  # 0(1)
    resultado = math.factorial(m)  # 0(1)
    return resultado  # 0(1)
