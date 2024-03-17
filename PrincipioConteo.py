def principio_conteo_aditivo(m, n):
    return m + n

def principio_conteo_multiplicativo(m, n):
    return m * n

def main():
    print("Principio de conteo aditivo:")
    m_aditivo = int(input("Ingrese el número de formas para el primer evento (m): "))
    n_aditivo = int(input("Ingrese el número de formas para el segundo evento (n): "))
    resultado_aditivo = principio_conteo_aditivo(m_aditivo, n_aditivo)
    print(f"El número total de formas en que ambos eventos pueden ocurrir es: {resultado_aditivo}")

    print("\nPrincipio de conteo multiplicativo:")
    m_multiplicativo = int(input("Ingrese el número de formas para el primer evento (m): "))
    n_multiplicativo = int(input("Ingrese el número de formas para el segundo evento (n): "))
    resultado_multiplicativo = principio_conteo_multiplicativo(m_multiplicativo, n_multiplicativo)
    print(f"El número total de formas en que ambos eventos pueden ocurrir es: {resultado_multiplicativo}")

if __name__ == "__main__":
    main()
