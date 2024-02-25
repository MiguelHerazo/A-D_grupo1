#Permutaciones de una Cadena: Escribe una función recursiva que genere todas las permutaciones posibles de una cadena de caracteres.

#Sln 

from itertools import permutations  # O(n!)

# Definimos los códigos de escape ANSI para cambiar el color del texto (OPCIONAL)
AZUL = '\033[94m'  # Código para azul O(1)
FIN_COLOR = '\033[0m'  # Código para restablecer el color por defecto O(1)

def obtener_permutaciones(cadena): # O(n!)
    try:  # O(1)
        if not isinstance(cadena, str):  # O(1)
            raise TypeError("La entrada debe ser una cadena de caracteres")  # O(1)
        if len(cadena) == 0:  # O(1)
            raise ValueError("La cadena no puede estar vacía")  # O(1)
        if not cadena.isalnum():  # O(n)
            raise ValueError("La cadena solo puede contener caracteres alfanuméricos")  # O(n)

        lista_permutaciones = list(permutations(cadena))  # O(n!)

        for permutacion in lista_permutaciones:  # O(n!)
            print(''.join(permutacion))  # O(n)

        return len(lista_permutaciones)  # O(1)
    except TypeError as te:  # O(1)
        print("Error:", te)  # O(1)
        return 0  # O(1)
    except ValueError as ve:  # O(1)
        print("Error:", ve)  # O(1)
        return 0  # O(1)

def main(): # O(n!)
    try:  #O(1)
        cadena = input("Ingrese una cadena de caracteres: ")  # O(n)
        cantidad_permutaciones = obtener_permutaciones(cadena)  # O(n!)
        if cantidad_permutaciones > 0:  # O(1)
            print(AZUL + "Se generaron {} permutaciones de la cadena '{}'.".format(cantidad_permutaciones, cadena) + FIN_COLOR)  # O(1)
    except KeyboardInterrupt:  # O(1)
        print("\nPrograma interrumpido por el usuario.")  # O(1)

if __name__ == "__main__":  # O(1)
    main()  # O(n!)
