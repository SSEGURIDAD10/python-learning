# Creacion de una funcion que nos devuelve los numeros primos
# Entre 0 y el argumento proporcionado

def es_primo(num):
    for i in range(2, num-1):
        if num%i==0: return False
    return True
    
def primos_hasta_numero(num):
    primos = []
    for i in range(3, num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta_numero(13)
print(resultado)