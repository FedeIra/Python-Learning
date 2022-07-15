from io import open 

archivo_texto = open("archivo.text", "r+") #le puede agregar el mas para usar mas funciones aparte del read. lectura y escritura


archivo_texto.write("Comienzo del texto") #aca lo va a escribir en la primera linea del doc reemplazando lo q ya esta

#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()