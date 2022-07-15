#######################################################

"""
SCRIPTING: argumentos de un programa

Le queremos dar info. a un programa, como argumentos, antes de ejecutarlo

Se le puede pasar info separada por un espacio

lo hacemos con la libreria sys
"""

import sys
argumentos = sys.argv #significa q le estas pasando informacion previa. almacena en una lista los argumentos q le vamos pasando

for argumento in argumentos: #levantamos lista q pasamos por consola
    print(argumento)

try: # los pasamos por try except por si alguien mete argumentos invalidos
    argumento = argumentos [1]
except:
    print("No hay tantos argumentos ingresados!")




import sys
argumentos = sys.argv #significa q le estas pasando informacion previa. almacena en una lista los argumentos q le vamos pasando

for argumento in argumentos: #levantamos lista q pasamos por consola
    print(argumento)

try: # los pasamos por try except por si alguien mete argumentos invalidos
    argumento = argumentos [1]
except:
    print("No hay tantos argumentos ingresados!")

# SLICING: para recortar una lista o quedarnos con un solo elemento

lista = [1,2,3,4,5,6]

lista[1,6,1] #la primera posicion corresponde al inicio, el segundo hasta cual elemento te queres mover, y el ultimo cada cuanto queres q salte

import os
directorio_actual = os.getcwd() # para saber en que directorio estas actualmente

resultado = os.path.exists("ejemplo.json") #para saber si existe la ruta para este archivo. te devuelve un booleano
print(resultado)

os.rename("ejemplo.json", "ejercicio.json") #para renombrar archivos

os.remove("ejercicio.json")

sistema = os.name #te dice el nombre de tu sistema operativo


import shutil #es parecido al os pero mejor

shutil.rmtree("Carpeta_a_borrar") #para borrar una carpeta

# import keyboard

# import pyautogui #para interacciones con el usuario


import sys
import os
import sys

try:
    #Acceder a los argumentos pasados al programa por el usuario
    ruta = sys.argv[1]
    ext = sys.argv[2]

except IndexError:
    print("Argumentos insuficientes. Indique la ruta en donde buscar "
    "y la extension.")
    sys.exit()

# OS - Obtener la lista de archivos en la ruta especificada
try:
    archivos = os.listdir(ruta)
except FileNotFoundError:
    print("LA ruta no existe.")
    sys.exit()

#metodos de string
# si la extension no empieza con un punto, agregarselo.
if not ext.startswith("."):
    ext = "." + ext

print(f"Archivos con extension {ext}:")
#Recorrer la lista de archivos
for archivo in archivos:
    # imprimir unicamente los que terminan con la extension ingresada
    if not ext.startswith("."):
        print("   ->", archivo)

import subprocess #libreria

#Ejemplo 1
subprocess.run(["mkdir", "Nueva carpeta"], shell = True) #shell de linux. el argumento shell lo definimos en true
print("La carpeta ha sido creada")

# BASE DE DATOS

# hay dos corrientes> modelo relacional (es mas antiguo. nocion de tablas como excel) y no relacional (es mas desestructurado. libertad a la hora de modelar la info).

#el modelo relacional sirve para info q no va a ir cambiando con el tiempo. La estructura va a mutar poco.

# SQLite. HAY QUE HACER EL CURSO SQL

import sqlite3 

db_path = r""
db = sqlite3.connect(db_path)

cursor = db.cursor()
