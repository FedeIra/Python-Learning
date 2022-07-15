"""
Archivos externos: el objetivo es la persistencia de datos. Posibilidad de guardar los datos de la aplicacion para q no se pierdan.

Para eso se puede guardar en archivos externos o base de datos.

En archivos externos tenes binarios y archivos de texto plano. Dentro de ellos tenes muchos.

Vamos a ver archivos de texto plano.

Son 4 fases> crear archivo, abrirlo, manipular su informacion y por ultimo cerrarlo.

"""

#importamos el modulo

from io import open # el open es para poder abrir un archivo externo

archivo_texto = open("ejemplo_archivo_externo", "w") #nos pide dos argumentos, nombre del archivo y modo en q lo vamos a abrir (modo lectura, escritura, append)
#Con esto ya cree el archivo

frase = "Estupendo dia para estudiar Python \n el miercoles"

archivo_texto.write(frase) #el write te pide q queres escribir. Aca estoy manipulando el archivo

archivo_texto.close() #por ultimo cierro el archivo. No es cerrar el archivo desde windows, sino desde el programa python