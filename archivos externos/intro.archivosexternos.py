#como guardar info de aplicacoines en archivos externos. Primero tenemos q crear el archivo, luego abrirlo, luego guardar la informaci[on ahi y finalmente cerrarlo

from io import open 

#archivo_texto = open("archivo.text", "w") #te pide nombre del archivo y modo q lo vas a abrir: lectura, escritura (w), append para agregar info a algo q existe

#frase = "Estupendo dia para estudiar Python \n el miercoles"

#archivo_texto.write(frase)

#archivo_texto.close() #cerrar el arhcivo desde el programa python

archivo_texto = open("archivo.text", "r") # la r es para leer

#texto = archivo_texto.read()

#archivo_texto.close()

#print(texto)

#Hay otro metodo readlines() La lee y almacena en una lista. Es para manipulacion de la informacion

#lineas_texto = archivo_texto.readlines() #cada linea de texto corresponde a una lista

#archivo_texto.close()

#print(lineas_texto)

#print(lineas_texto[0]) #a partir de cada puedo jugar con listas for, etc.

#Como agregar info a un texto con append (a):

archivo_texto = open("archivo.text", "a")

archivo_texto.write("\n siempre es una buena ocasion para estudiar python")

archivo_texto.close