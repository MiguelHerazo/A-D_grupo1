def termino_n_geometrica(a1, r, n):
    return a1 * (r ** (n - 1))

a1 = 6
r = -3
n = 100

termino_100 = termino_n_geometrica(a1, r, n)
print("El término en la posición n=100 es:", termino_100)
