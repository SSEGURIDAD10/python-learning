def obtener_personas(cantidad_de_personas):
    personas = []
    for i in range(cantidad_de_personas):
        nombre = input('Ingrese el nombre del la persona: ') 
        edad = int(input('Ingrese la edad de esa persona'))
        persona = (nombre, edad)
        personas.append(persona)
    personas.sort(key=lambda x:x[1]) #Ordena de menor a mayor apuntando a la key edad = [1]
    asistente = personas[0][0]
    profesor = personas[-1][0] #De esta manera apuntas al ultimo elemento de la lista (-1) y al nombre (0)
    return asistente, profesor

asistente, profesor = obtener_personas(5)

print(f'El profesor es {profesor} y su asistente {asistente}')