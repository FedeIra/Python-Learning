import sqlite3 
import pymysql

#conexion a la BD (base de datos)
db_path = r"C:\Users\fedei\OneDrive\Escritorio\Programacion\Python\generadores.py"
db = sqlite3.connect(db_path)

#creacion de un cursor
cursor = db.cursor()

#ejecturar una consulta
cursor.execute("CREATE TABLE personas (nombre TEXT, apellido TEXT, edad NUMERIC)")

#POST CRUD (CREATE, INSERT, UPDATE, DELETE, etc)
# Para guardar los cambios se debe hacer un commit()
db.commit() # es como un save para guardar las modificaciones

#cerramos la conexion
db.close()


##################################################

"""

Parte 1

Desarrollar un programa de Python que cree una base de datos de SQLite llamada productos.db y una tabla de nombre productos con las siguientes columnas.

Luego, el programa debe insertar las siguientes filas.

"""

 

"""

TEXT - NUMERIC

id - texto

nombre - texto

precio - numerico

 

id         nombre                                         precio

1                          Teclado                                         -

2                          Mouse                                           -

3                          Monitor                          -

4                          Parlantes                        -

5                          Auriculares                    -

"""

 

"""

# Conexión a la BD

db_path = r"C:/Users/EducaciónIT/Desktop/EducaciónIT/Cursos/Python Programming/Módulo 4/Ejercicios/Bases de datos/sqlite/ejemplo.sqlite"

db = sqlite3.connect(db_path)

 

# Creación de un cursor

cursor = db.cursor()

 

# Ejecutar una consulta.

cursor.execute("CREATE TABLE personas (nombre TEXT, apellido TEXT, edad NUMERIC)")

 

# POST CRUD (CREATE, INSERT, UPDATE, DELETE, etc)

# Para guardar los cambios se debe hacer un commit()

db.commit()

 

# Cerramos la conexión

db.close()

 

# Insertar un elemento

cursor.execute("INSERT INTO personas VALUES (?)", (variable))

"""

 

 

"""

Parte 2

 

Se deberá solicitar para cada producto un id (numérico entero), un nombre (texto) y un precio (numérico entero). En el caso de los datos numéricos, volver a preguntar si el valor ingresado por el usuario es incorrecto.

Para acompañar al programa, hacer un menú como el siguiente:

Menú

1 – Agregar Productos

2 – Ver productos

3 – Salir

La opción de agregar productos será la que despliegue la entrada de datos.  La opción ver productos mostrara todos los productos cargados en la tabla.  La opción de salir nos permite salir del programa.

"""

 

"""

try:

    cursor.execute("SELECT * FROM personas")

except sqlite3.OperationalError:

    print("La consulta no se ejecutó correctamente.")

 

# Obtengo el primer elemento del cursor

personas = cursor.fetchone()

print(personas)

 

# Obtengo todos los elementos del cursor

personas = cursor.fetchall()

print(personas)

"""

 

# Pablo - Parte 1

 

import sqlite3

 

path = r"C:\Users\loro_\Desktop\curso_data_science\python_programming\productos.db"

 

listado = [["1","teclado",0],["2","mouse",0],["3","monitor",0],["4","parlantes",0],["5","auriculares",0]]

 

db = sqlite3.connect(path)

 

cursor = db.cursor()

 

cursor.execute("CREATE TABLE producto (id TEXT, nombre TEXT, precio NUMERIC)")

db.commit()

 

for id,producto,precio in listado:

    cursor.execute("INSERT INTO producto VALUES (?,?,?)",(id,producto,precio))

 

db.commit()

 

db.close()



# Guido

import sqlite3

 

db_path=r"C:\Python\Curso intermedio de Python\tabla.sqlite"

db=sqlite3.connect(db_path)

 

cursor=db.cursor()

 

#cursor.execute("CREATE TABLE tabla (id TEXT,nombre TEXT,precio NUMERIC)")

 

tupla = (("1","Teclado","1000"),("2","Mouse","500"))

 

for id,nombre,precio in tupla:

    cursor.execute("INSERT INTO tabla VALUES (?,?,?)", (id,nombre,precio))

    db.commit()

 

db.close()

 

# Claudio

 

import sqlite3

 

db_path = r"C:/Users/EducaciónIT/Desktop/EducaciónIT/Cursos/Python Programming/Módulo 4/Ejercicios/Bases de datos/sqlite/ejemplo.sqlite"

db = sqlite3.connect(db_path)

cursor = db.cursor()

 

productos = ("id" , "nombre" , "precio")

 

id=input("ingrese id")

nombre=input("nombre")

precio=input("ingrese precio")

 

for _ in productos:

    productos.append(id)

 

for nombre in productos:

    productos.append(nombre)

 

for precio in productos:

    productos.append(precio)

 

 

cursor.execute("INSERT INTO personas VALUES (?)", (id),(nombre),(precio))

 

#Guido. Parte 2.

 

import sqlite3

conn = sqlite3.connect("tabla2.sqlite")

cursor = conn.cursor()

try:

    cursor.execute("CREATE TABLE tabla2 (id TEXT, nombre TEXT, precio NUMERIC)")

except sqlite3.OperationalError:

    pass

 

 

def verificador(dato, tipo_de_dato):

              pass

 

 

def insertador(cursor):

              id = int(input("ID: "))

              nombre = input("Nombre: ")

              precio = int(input("Precio: "))

              cursor.execute(f"INSERT INTO tabla2 VALUES (?,?,?)",(id,nombre,precio))

              return

 

while True:

  print("""

                Menú

                            1 – Agregar Productos

                            2 – Ver productos

                            3 – Salir

                """)

  opcion = verificador(input("Opcion: "), int())

 

  if opcion == "1":

              sumador()

    insertador()

    db.commit()

 

  elif opcion == "2"

              try:

              cursor.execute("SELECT * FROM personas")

              except sqlite3.OperationalError:

              print("La consulta no se ejecutó correctamente.")

       

    personas = cursor.fetchall()

    print(personas)

 

    elif opcion == '3':

      break

 

 

conn.close()

 

 

#######################################

import sqlite3

from tkinter import *

 

db_path = r"C:/Users/EducaciónIT/Desktop/EducaciónIT/Cursos/Python Programming/Módulo 4/Ejercicios/Bases de datos/sqlite/ejemplo.sqlite"

db = sqlite3.connect(db_path)

cursor = db.cursor()

 

productos = ("id" , "nombre" , "precio")

 

id=input("ingrese id")

nombre=input("nombre")

precio=input("ingrese precio")

 

def quit(event):                          

    print("Double click  to stop")

    import sys; sys.exit()

 

def task(event):

  while True:

    pyautogui.click(button='left')   

 

ws=Tk()

ws.title("Python guides")

ws.geometry("200x200")

 

button = Button(ws, text='cargar')

button2 = Button(ws, text='salir')

button.pack(pady=10)

button.bind('<Button-1>', task)

button2.bind('<Double-1>', quit)

button.mainloop()

 

 

cursor.execute("INSERT INTO personas VALUES (?)", (id),(nombre),(precio))

 

 

#####################################

 

### LEANDRO

 

import sqlite3

 

while True:

    print(" Menu ")

    print(" 1 - Agregar Productos")

    print(" 2 - Ver Productos")

    print(" 3 - Salir")

 

    opcion = int(input("Elija una opcion: "))

    data= []

 

    if opcion >= 4:

        print("El Valor es invalido")

 

    elif opcion == 1:

        id = input("Ingrese el ID: ")

        name = input("Ingrese el nombre del producto: ")

        precio = input("Ingrese el valor del producto: ")

 

        data = data.append(id,name,precio)

 

        conn = sqlite3.connect("productos.db")

        cursor = conn.cursor()

 

        for id, name, precio in data:

            cursor.execute("INSERT INTO personas VALUES (?, ?, ?)", (id, name, precio))

            conn.commit()

        conn.close()

 

    elif opcion == 2:

        conn = sqlite3.connect("productos.db")

        cursor = conn.cursor()

 

        cursor.execute("SELECT * FROM personas")

        personas = cursor.fetchall()

        print(personas)

        conn.commit()

        conn.close()

 

    elif opcion == 3:

        break

       

        

#########claudio

        

        import sqlite3

from tkinter import *

 

db_path = r"C:/Users/EducaciónIT/Desktop/EducaciónIT/Cursos/Python Programming/Módulo 4/Ejercicios/Bases de datos/sqlite/ejemplo.sqlite"

db = sqlite3.connect(db_path)

cursor = db.cursor()

 

productos = ("id" , "nombre" , "precio")

 

id=input("ingrese id")

nombre=input("nombre")

precio=input("ingrese precio")

 

def quit(event):                          

    print("Double click  to stop")

    import sys; sys.exit()

    conn.close()

 

def task(event):

  while True:

   cursor.execute("INSERT INTO personas VALUES (?)",(id),(nombre),(precio))

    

 

ws=Tk()

ws.title("cargar datos")

ws.geometry("200x200")

 

button = Button(ws, text='cargar')

button2 = Button(ws, text='salir')

button.pack(pady=10)

button.bind('<Button-1>', task)

button2.bind('<Double-1>', quit)

button.mainloop()

 

 

# Natalia

 

file_path = "C:\\Users\\natal\\Desktop\\productos.sqlite"

 

try:

  productos = sqlite3.connect(file_path)

except:

  print("Database not found")

 

cursor = productos.cursor()

 

while True:

    print("""

    Menú

    1 – Agregar Productos

    2 – Ver productos

    3 – Salir""")

 

    ingreso = input("\nIngrese una opción: ")

 

    if ingreso == "1":

        nombre = input ("Ingrese el nombre: ")

        precio = int(input("Ingrese el precio: "))

        try:

            listado = cursor.execute("SELECT * FROM productos")

 

            cursor.execute("INSERT INTO productos VALUES (?,?,?)", (str((len(list(listado))+1)), nombre, precio))

        except OperationalError:

            print("Ha habido un error en la consulta")

 

    if ingreso == "2":

        try:

            print()

            listado = cursor.execute("SELECT * FROM productos").fetchall()

#            personas = cursor.fetchall()

            for item in listado:

                print(item)

        except OperationalError:

            print("Ha habido un error en la consulta")

   

    if ingreso == "3":

        break

 

productos.commit()

productos.close()


