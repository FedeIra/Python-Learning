
#persistencia de datos. Posibilidad de guardar datos en un archivo python para q no se pierdan. Almacena datos q fuimos manejando durante la ejecucion del programa para q no se pierdan.
# guardar esos datos en archivos internos o guardarlo en bases de datos.
#archivos externos de texto plano o sean lo q sean
#primero se crea un archivo externo, luego abrirlo, abierto el archivo hay que manipularlo, y por ultimo luego de trabajado el archivo hay que cerrarlo.

from io import open
#con el metodo open o abre el archivo o lo crea. con el open se abre o crea el archivo, con el write se maninpula, y con el close se cierra
archivo_texto = open("archivo.txt", "w") #la funcion open te pide dos argumentos: nombre del archivo q queremos abrir y el modo en el q lo abrimos (lectura, escritura, append para agregar mas info). La w es para abrirlo en modo escritura

frase = "estupendo dia para estudiar python\n el miercoles"

archivo_texto.write(frase) #la funcion write es para escribir en el doc. Esta es la parte que manipula el archivo

archivo_texto.close() #con el close se cierra el archivo. Cerrar se refiere a cerrar el programa desde python.



from io import open

archivo_texto = open("archivo.txt", "r") # el r es para q lea el archivo

texto = archivo_texto.read() #le decimos q lea el archivo y lo almacene en texto. Tambien esta el metodo real lines. Lee la linea del archivo y la almacena en una lista.

archivo_texto.close() # a pesar de q esta cerrado, podemos imprimr esa info.

print(texto)



from io import open

archivo_texto = open("archivo.txt", "r") 

lineas_texto = archivo_texto.readlines() #el readlines guarda la info dentro de una lista de lineas de texto manipulable

archivo_texto.close()

print(lineas_texto) #ahora te lo imprime como lista. Almancena dentro de esa lista las lineas de texto por lo q te diferencia el \n como si fuera parte del texto.

print(lineas_texto[0]) #aca estoy imprimiendo por numero en la linea. Puedo usar for para recorrer o combinar condicionales para buscar elemento en concreto.

print(lineas_texto[1])
