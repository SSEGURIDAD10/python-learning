# import modulo_saludar as m_saludar // esto es una manera de cambiar el nombre

from modulo_saludar import saludar

import sys
sys.path.append("C:\\Users\\LUISB\\OneDrive\\Documentos\\SoyDalto\\python\\suma-resta")
from args import suma

saludo = saludar("Gerardo")
sumas = suma(1,10)

print(saludo)
print(sumas)