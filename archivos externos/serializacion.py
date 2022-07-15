"""
SERIALIZACION: consiste en guardar en un fichero externo una coleccion diccionario o incluso en objeto. En codigo binario.

La distribucion de archivos en codigo binario se hace mas facil

Biblioteca pickle. Tiene biblioteca de coleccion de metodos. Especialmente dum y load

dump(): volcado de datos al fichero binario externo
load(): carga de los datos del fichero binario externo

"""

import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario = open("lista_nombres", "wb") #w por write y b por binaria

pickle.dump(lista_nombres, fichero_binario) #primero te pide q escribir y segundo donde

fichero_binario.close()

del(fichero_binario) #se crea una nota con la lista en codigo binario. 