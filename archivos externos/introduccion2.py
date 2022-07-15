    """Al igual que en otros lenguajes de programación
en Python es posible crear, abrir y leer archivos.
La función incorporada open() toma como
argumento la ruta de un archivo y retorna una
instancia del tipo file.
f = open("archivo.txt", modo)
El modo es la forma como se va a trabajar el
archivo.
Para leer modo="r", este es el único modo que
cuando se usa open() y no se pasa de qué
manera interactuar con el archivo se toma
automáticamente “r”. Para escribir y crear se usa
modo="w", además en este modo si el archivo
existe se sobrescribe. Y por último el modo="a"
de append para añadir contenido al final del
archivo si existe el mismo. """

from os import *
from io import open 

f = open("archivo.txt",read)
f = open("archivo.txt") # si no pongo modo es en read

f = open("archivo.txt", write)

"""En cualquiera de los casos anteriores, si no se especifica
una ruta, el fichero se busca en el directorio actual (ruta
relativa). Y si vas a especificar la ruta (ruta absoluta), la
misma se escribe con doble barra para separar los
directorios o barra invertida.
"C:\\Users\\Anonimo\\Desktop\\Python
Programming\\mi_archivo.txt"
"C:/Users/Anonimo/Desktop/Python
Programming/mi_archivo.txt"""

# C:\Users\fedei\Programacion\Python\Chap04\prueba.txt"

"""Cuando abrimos un archivo para leer, el método
.read() retorna el contenido del archivo abierto
en formato string.
f = open("archivo.txt", "r")
print(f.read())
f.close()
Con f.readline() leemos una sola línea del
archivo; el carácter de fin de línea (\n).
Entonces el retorno es una cadena.
Si querés leer todas las líneas de un archivo,
podés usar f.readlines() que crea una lista, y
cada elemento de esta es un renglón del archivo.
Métodos para trabajar con archivos
Por otro lado, cuando abrimos un archivo en
modo escritura, usamos el método .write()
f = open("archivo.txt", "w")
f.write("Hola mundo")
f.close()
La función write() graba una cadena en el
archivo, si trabajamos en modo “w” reemplazará
todo el contenido del archivo, si el archivo existe,
si no existe lo crea. """

f = open("archivo.txt", "r")
print(f.read())
f.close()

"""Recordemos que para añadir datos al final del
archivo sin borrar información previa, el fichero
debe abrirse en la modalidad append ("a") y
también se usa .write() .
f = open("archivo.txt", "a")
f.write("Hola ")
f.write("mundo")
f.close()
También podemos usar el método writelines()
y pasarle una lista como argumento para que
guarde el contenido.
Cuando trabajamos con archivos es importante
cerrarlo cuando acabamos de trabajar con ellos,
vía el método close(). Aunque es verdad que
los ficheros normalmente son cerrados y
guardados automáticamente, es importante
especificarlo para evitar tener comportamientos
inesperados."""

f = open("archivo.txt", "a")
f.write("Hola ")
f.write("mundo")
f.close()

from io import open 
Liquidación = open("Liquidación.txt", "r+") 

"""Es una buena práctica utilizar la sentencia with
cuando se trata de archivos. La ventaja es que el
archivo se cierra correctamente después de que
finaliza su uso, incluso si se genera una excepción en
algún momento.
#Ejemplo with escribiendo archivo
with open("archivo.txt","w") as f:
 f.write("Hola Mundo!")
#Ejemplo with leyendo archivo, el parametro "r" al leer es opcional
with open("archivo.txt","r") as f:
 texto = f.read()"""

with open("archivo.txt","w") as f:
 f.write("Hola Mundo!")

with open("archivo.txt","r") as f:
texto = f.read()

"""Si no utilizas with, debes llamar a f.close(), si o si, para
cerrar el archivo y liberar inmediatamente los recursos del
sistema.
¡Cuidado! Usar f.write() sin usar with o f.close()
puede resultar en que no se escriban completamente los
datos en el archivo"""

f.close()
