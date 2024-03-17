from itertools import permutations

def obtener_permutaciones(cadena):
    if not isinstance(cadena, str):
        print("La entrada debe ser una cadena de caracteres")
        return []

    if len(cadena) == 0:
        print("La cadena no puede estar vacía")
        return []

    if not cadena.isalnum():
        print("La cadena solo puede contener caracteres alfanuméricos")
        return []

    lista_permutaciones = list(permutations(cadena))

    for permutacion in lista_permutaciones:
        print(''.join(permutacion))

    return lista_permutaciones

def main():
    try:
        cadena = input("Ingrese una cadena de caracteres: ")
        permutaciones = obtener_permutaciones(cadena)
        if permutaciones:
            print("Se generaron {} permutaciones de la cadena '{}'.".format(len(permutaciones), cadena))
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")


if __name__ == "__main__":
    main()
