#Daniel Alzate Arias

# EXAMEN DE ANALISIS Y DISEÑO DE ALGORITMOS

# PUNTO 1

#Punto 1 (1.5): Resolver la siguiente relación de recurrencia entregando la recurrencia sin recursividad y su ecuación particular según las condiciones de frontera:n>=4 donde, 𝑎0 = # 𝑑𝑒 𝑙𝑒𝑡𝑟𝑎𝑠 𝑑𝑒 𝑠𝑢 𝑝𝑟𝑖𝑚𝑒𝑟 𝑛𝑜𝑚𝑏𝑟𝑒 y 𝑎1 = # 𝑑𝑒 𝑙𝑒𝑡𝑟𝑎𝑠 𝑑𝑒 𝑠𝑢 𝑝𝑟𝑖𝑚𝑒𝑟 𝑎𝑝𝑒𝑙𝑙𝑖𝑑𝑜 hallar el termino 1500 de la sucesión.


 #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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



 #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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
