#funcion No recursiva que cuente el numero de digitos en un numero entero

def ContarCantidadNumerosDeEntero(numero):  # O(log n)
    if numero == 0:  # O(0)
        return 1  # O(0) 
    
    count = 0  # O(0) 
    numero = abs(numero)  # O(0) 
    while numero > 0:  # O(log n) 
        count += 1  # O(0)
        numero //= 10  # O(0)

    return count  # O(0) 


numero_ejemplo = 934783.36 # O(0)
resultado = ContarCantidadNumerosDeEntero(numero_ejemplo)  # O(log n)
print(f"El numero de digitos en {numero_ejemplo} es: {resultado}") # O(0)

# complejidad algorimica big O = 9 O(0)+ 2 O(log n)  
# peor caso O(log n)
# complejidad espacial = O(0) o O(1)
# Nota: O(0) == O(1) 
