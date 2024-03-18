import math

# Función para calcular combinaciones con repetición
def combinaciones_con_repeticion(m, n):
    return math.comb(m + n - 1, n)

# Función para calcular combinaciones sin repetición
def combinaciones_sin_repeticion(m, n):
    return math.comb(m, n)

# Función principal
def main():
    # Lectura de entrada para 'm' y 'n'
    m = int(input("Ingrese el valor de 'm': "))  # O(1)
    n = int(input("Ingrese el valor de 'n': "))  # O(1)

    # Validación de entrada
    if m <= 0 or n <= 0:  # O(1)
        print("Los valores de 'm' y 'n' deben ser mayores que cero.")
        return

    # Elección del tipo de combinación
    print("\nSeleccione el tipo de combinación:")
    print("1. Con repeticiones")
    print("2. Sin repeticiones")
    opcion = int(input("Ingrese su elección (1 o 2): "))  # O(1)

    # Determinación de la operación a realizar
    if opcion == 1:
        resultado = combinaciones_con_repeticion(m, n)  # O(1) (dentro de la función)
        print(f"El número de combinaciones con repeticiones es: {resultado}")
    elif opcion == 2:
        # Validación adicional para combinaciones sin repetición
        if m < n:
            print("No se pueden seleccionar más elementos de los que hay disponibles.")
            return
        resultado = combinaciones_sin_repeticion(m, n)  # O(1) (dentro de la función)
        print(f"El número de combinaciones sin repeticiones es: {resultado}")
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
