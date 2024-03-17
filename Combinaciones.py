import math

def combinaciones_con_repeticion(m, n):
    return math.comb(m + n - 1, n)

def combinaciones_sin_repeticion(m, n):
    return math.comb(m, n)

def main():
    m = int(input("Ingrese el valor de 'm': "))
    n = int(input("Ingrese el valor de 'n': "))

    if m <= 0 or n <= 0:
        print("Los valores de 'm' y 'n' deben ser mayores que cero.")
        return

    print("\nSeleccione el tipo de combinación:")
    print("1. Con repeticiones")
    print("2. Sin repeticiones")
    opcion = int(input("Ingrese su elección (1 o 2): "))

    if opcion == 1:
        resultado = combinaciones_con_repeticion(m, n)
        print(f"El número de combinaciones con repeticiones es: {resultado}")
    elif opcion == 2:
        if m < n:
            print("No se pueden seleccionar más elementos de los que hay disponibles.")
            return
        resultado = combinaciones_sin_repeticion(m, n)
        print(f"El número de combinaciones sin repeticiones es: {resultado}")
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
