def suma(*numeros):
    return sum(numeros)

resultado = suma(1,2,3,4,5)
print(resultado)


def suma_lista(numeros):
    return sum([*numeros])

resultado2 = suma_lista([1,2,3,4,5])
print(resultado2)