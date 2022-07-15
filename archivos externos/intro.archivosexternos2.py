from io import open 

archivo_texto = open("archivo.text", "r")

print(archivo_texto.read()) #el puntero (donde esta titilando para empezar a escribir) esta al comienzo del archivo y pasa al final despues de leerlo

archivo_texto.seek(0) #le pongo la posicion 0 entonces se puede leer completo  en el siguiente read pq el puntero se coloca al principio

print(archivo_texto.read()) 
#para cambiar de lugar el puntero o hago con seek() le pones el numero.

print(archivo_texto.read()) #con este no te lee nada pq el puntero no esta al principio.

print(archivo_texto.read(11)) # le puedo decir hasta donde leerle completando numero en el parentesis
