from io import open 

archivo_texto = open("archivo.text", "r")

#archivo_texto.seek(len(archivo_texto.read())/2) #len te da la longitud del archivo. Nos queda la mitad en el seek, es decir en la mitad del texto.

archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.read())