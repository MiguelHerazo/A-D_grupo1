import itertools


def generar_combinaciones(elementos, con_repeticion=False):
    todas_combinaciones = []  # Lista para almacenar todas las combinaciones

    # Verificar si se permiten repeticiones
    if con_repeticion:
        # Generar combinaciones con repetición utilizando itertools.product
        for r in range(1, len(elementos) + 1):
            combinaciones = itertools.product(elementos, repeat=r)
            todas_combinaciones.extend(combinaciones)
    else:
        # Generar combinaciones ordinarias utilizando itertools.combinations
        for r in range(1, len(elementos) + 1):
            combinaciones = itertools.combinations(elementos, r)
            todas_combinaciones.extend(combinaciones)

    return todas_combinaciones


def main():
    try:
        # Solicitar al usuario los elementos y si se permiten repeticiones
        elementos = input("Ingrese los elementos separados por espacios: ").split()
        permitir_repeticion = input("¿Permitir repeticiones? (s/n): ").lower() == 's'

        # Generar las combinaciones con los elementos proporcionados
        resultado = generar_combinaciones(elementos, permitir_repeticion)

        # Imprimir las combinaciones generadas
        print("Combinaciones generadas:")
        for combinacion in resultado:
            print(combinacion)

        # Imprimir el número total de combinaciones generadas
        print("\nSe generaron {} combinaciones.".format(len(resultado)))

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")


if __name__ == "__main__":
    main()
