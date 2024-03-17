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

def main(): # Complejidad algorítmica: O(n!), Complejidad espacial: O(n!)
    try:
        opcion = input("¿Desea calcular permutaciones con repetición (c) o sin repetición (s)? ")  # O(1)
        if opcion == 'c' or opcion == 's':  # O(1)
            cadena = input("Ingrese una cadena de caracteres: ")  # O(n)
            try:
                if opcion == 'c':  # O(1)
                    obtener_permutaciones(cadena, True)  # O(n!)
                else:
                    obtener_permutaciones(cadena)  # O(n!)
            except (TypeError, ValueError) as error:  # O(1)
                print(error)  # O(1)
        else:
            print("Debes seleccionar una opción valida.")  # O(1)
    except KeyboardInterrupt:  # O(1)
        print("\nPrograma interrumpido por el usuario.")  # O(1)

if __name__ == "__main__":  # O(1)
    main()  # O(n!)


#PERMUTACIONES SOLAMENTE NUMERICAS 
import math

def permutaciones_con_repeticion(m, n):
    return m ** n

def permutaciones_sin_repeticion(m):
    return math.factorial(m)

def main():
    m = int(input("Ingrese el valor de 'm': "))
    n = int(input("Ingrese el valor de 'n': "))

    if m <= 0 or n <= 0:
        print("Los valores de 'm' y 'n' deben ser mayores que cero.")
        return

    print("\nSeleccione el tipo de permutación:")
    print("1. Con repeticiones")
    print("2. Sin repeticiones")
    opcion = int(input("Ingrese su elección (1 o 2): "))

    if opcion == 1:
        resultado = permutaciones_con_repeticion(m, n)
        print(f"El número de permutaciones con repeticiones es: {resultado}")
    elif opcion == 2:
        if m < n:
            print("No se pueden seleccionar más elementos de los que hay disponibles.")
            return
        resultado = permutaciones_sin_repeticion(m, n)
        print(f"El número de permutaciones sin repeticiones es: {resultado}")
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
