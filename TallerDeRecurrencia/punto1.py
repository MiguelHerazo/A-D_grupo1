# 1. Encontrar la posición n=100

# Encuentre una relación de recurrencia, con una condición inicial, que determine de manera única cada una de las siguientes progresiones geométricas

# B) 6, -18, 54, -162,...

#----------------NO RECURSIVO-------------------

def termino_n_geometrica(a1, r, n):
    return a1 * (r ** (n - 1))

a1 = 6
r = -3
n = 100

termino_100 = termino_n_geometrica(a1, r, n)
print("El término en la posición n=100 es:", termino_100)

#-----------------RECURSIVO---------------------

def term_n(a1, r, n):
    if n == 1:
        return a1
    else:
        return r * term_n(a1, r, n-1)

a1 = 6  
r = -3  

n = 100
a_100 = term_n(a1, r, n)
print("El término en la posición n=100 es:", a_100)
