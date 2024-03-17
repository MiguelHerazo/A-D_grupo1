import math

def variaciones_con_repeticion(m, n):
    return m ** n

def variaciones_sin_repeticion(m, n):
    return math.factorial(m) // math.factorial(m - n)

def main():
    m = int(input("Ingrese el valor de 'm': "))
    n = int(input("Ingrese el valor de 'n': "))

    if m <= 0 or n <= 0:
        print("Los valores de 'm' y 'n' deben ser mayores que cero.")
        return

    print("\nSeleccione el tipo de variación:")
    print("1. Con repeticiones")
    print("2. Sin repeticiones")
    opcion = int(input("Ingrese su elección (1 o 2): "))

    if opcion == 1:
        resultado = variaciones_con_repeticion(m, n)
        print(f"El número de variaciones con repeticiones es: {resultado}")
    elif opcion == 2:
        if m < n:
            print("No se pueden seleccionar más elementos de los que hay disponibles.")
            return
        resultado = variaciones_sin_repeticion(m, n)
        print(f"El número de variaciones sin repeticiones es: {resultado}")
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
