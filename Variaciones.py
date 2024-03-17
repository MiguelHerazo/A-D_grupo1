import math

def variaciones_con_repeticion(m, n):
    return m ** n #O(1)

def variaciones_sin_repeticion(m, n):
    return math.factorial(m) // math.factorial(m - n)  #O(1)

def main():
    m = int(input("Ingrese el valor de 'm': ")) #O(1)
    n = int(input("Ingrese el valor de 'n': ")) #O(1)

    if m <= 0 or n <= 0: #O(1)
        print("Los valores de 'm' y 'n' deben ser mayores que cero.") #O(1)
        return

    print("\nSeleccione el tipo de variación:") #O(1)
    print("1. Con repeticiones") #O(1)
    print("2. Sin repeticiones") #O(1)
    opcion = int(input("Ingrese su elección (1 o 2): ")) #O(1)

    if opcion == 1: #O(1)
        resultado = variaciones_con_repeticion(m, n) #O(1)
        print(f"El número de variaciones con repeticiones es: {resultado}") #O(1)
    elif opcion == 2:#O(1)
        if m < n:#O(1)
            print("No se pueden seleccionar más elementos de los que hay disponibles.")#O(1)
            return#O(1)
        resultado = variaciones_sin_repeticion(m, n)#O(1)
        print(f"El número de variaciones sin repeticiones es: {resultado}")#O(1)
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")#O(1)

if __name__ == "__main__":
    main()#O(1)
