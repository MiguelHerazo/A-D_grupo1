def principio_conteo_aditivo(m, n):  # O(1)
    return m + n  # O(1)

def principio_conteo_multiplicativo(m, n):  # O(1)
    return m * n  # O(1)

def main():  # O(1)
    print("Principio de conteo aditivo:")  # O(1)
    m_aditivo = int(input("Ingrese el número de formas para el primer evento (m): "))  # O(1)
    n_aditivo = int(input("Ingrese el número de formas para el segundo evento (n): "))  # O(1)
    resultado_aditivo = principio_conteo_aditivo(m_aditivo, n_aditivo)  # O(1)
    print(f"El número total de formas en que ambos eventos pueden ocurrir es: {resultado_aditivo}")  # O(1)

    print("\nPrincipio de conteo multiplicativo:")  # O(1)
    m_multiplicativo = int(input("Ingrese el número de formas para el primer evento (m): "))  # O(1)
    n_multiplicativo = int(input("Ingrese el número de formas para el segundo evento (n): "))  # O(1)
    resultado_multiplicativo = principio_conteo_multiplicativo(m_multiplicativo, n_multiplicativo)  # O(1)
    print(f"El número total de formas en que ambos eventos pueden ocurrir es: {resultado_multiplicativo}")  # O(1)

if __name__ == "__main__":  # O(1)
    main()  # O(1)

