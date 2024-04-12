#Daniel Alzate Arias

# EXAMEN DE ANALISIS Y DISEÑO DE ALGORITMOS

# PUNTO 1




# PUNTO 2

# Punto 2 (2.0): Escribir un algoritmo que indique los múltiplos de un número de forma recursiva.

def encontrar_multiplos(numero, limite, multiplo_actual=0):
    if multiplo_actual > limite:
        return []
    
    if multiplo_actual != 0:
        multiplos = [multiplo_actual]
    else:
        multiplos = []
    
    return multiplos + encontrar_multiplos(numero, limite, multiplo_actual + numero)

numero = 3
limite = 20
multiplos = encontrar_multiplos(numero, limite)

print(f"Los múltiplos de {numero} hasta {limite} son: {multiplos}")


#PUNTO 3

#Punto 3 (1.5): ¿Cuántos números de cinco cifras distintas se pueden formar con las cifras impares? ¿Cuántos de ellos son mayores de 70.000?

import itertools

cifras_impares = [1, 3, 5, 7, 9]
combinaciones_total = list(itertools.permutations(cifras_impares, 5))
cantidad_total = len(combinaciones_total)

combinaciones_mayores_70000 = [comb for comb in combinaciones_total if comb[0] in [7, 9]]
cantidad_mayores_70000 = len(combinaciones_mayores_70000)

print("Cantidad total de números de cinco cifras distintas con cifras impares:", cantidad_total)
print("Cantidad de números de cinco cifras distintas con cifras impares y mayores de 70,000:", cantidad_mayores_70000)
