with open('archivos\\texto_gerardo.txt','w', encoding="UTF-8") as archivo:
    
# Sobre escribe en el archivo
    # archivo.write('Escribiendo en el archivo de texto')
    
    archivo.writelines(['Hola en una linea\n','Segunda linea'])