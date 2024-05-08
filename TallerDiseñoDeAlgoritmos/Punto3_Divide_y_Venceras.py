#Encontrar el mínimo de una lista (divide y vencerás).
def find_minimum(arr):
    if len(arr) == 0:
        return "Lista Vacia"
    
    if len(arr) == 1:
        return arr[0]
    
    if arr[0] <= arr[-1]:
        return arr[0]
    
    mid = len(arr) // 2
    mita_izqui = arr[:mid]
    mita_dere = arr[mid:]
    
    return min(find_minimum(mita_izqui), find_minimum(mita_dere))

lista = [7, 8, 10, 2, 3, 5]
print("El minimo de la lista es ", find_minimum(lista))
