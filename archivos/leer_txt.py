archivo = open("archivos\\texto_gerardo.txt", encoding="UTF-8")

# texto_archivo = archivo.read()

# lineas = archivo.readlines()

linea_1 = archivo.readline()
linea_2 = archivo.readline()

archivo.close()

print(linea_2)
