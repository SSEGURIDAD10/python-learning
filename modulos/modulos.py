# import modulo_saludar as m_saludar // esto es una manera de cambiar el nombre

from modulo_saludar import saludar #importa la funcion saludar desde el file modulo_saludar.py

# La siguiente bliblioteca hace posible el asignar la direccion exacta de otro archivo
import sys
sys.path.append("C:\\Users\\LUISB\\OneDrive\\Documentos\\SoyDalto\\python\\suma-resta") #De esta manera se apunta, al correr el programa, en terminal se mostrara una ruta parecida (copia y pega)
from args import suma # Selecciono el archivo que necesito y almaceno en "suma" / Marca error pero no es un  error segun fuentes

saludo = saludar("Gerardo")
sumas = suma(1,10)

print(saludo)
print(sumas)