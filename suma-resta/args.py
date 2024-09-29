# Suma de numeros en tupla +

def suma(*numeros):
    return sum(numeros)

if __name__ == "__main__":
    resultado = suma(1,2,3,4,5)
    print(f'Suma de numeros en : {resultado}')

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    # Suma de numeros en lista

    def suma_lista(numeros):
        return sum([*numeros])

    resultado2 = suma_lista([1,2,3,4,5])
    print(f'Suma de numeros en una lista: {resultado2}')

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    # Resta de numeros en una lista

    def resta(numeros):
        resultado = numeros[0]
        for i in numeros[1:]:
            resultado -= i
        return resultado

    resultado3 = resta([10,3,3])
    print(f"La resta en lista es: {resultado3}")

    """^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
    # Resta de numeros en tupla

    def resta(*numeros):
        resultado = numeros[0]
        for i in numeros[1:]:
            resultado -= i
        return resultado

    resultado4 = resta(10,3,3)
    print(f"La resta en tupla es: {resultado4}")