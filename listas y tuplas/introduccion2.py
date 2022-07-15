# ------------- listas, tuplas y diccionarios --------------

alumno1 = "Matias" # a los efectos de los elementos de la lista cuenta desde el 0
alumno2 = "Sofia"
alumno3 = "Juan"

lista_alumnos = [alumno1 , alumno2 , alumno3]

lista_alumnos += ["Carlos"]

print(lista_alumnos)

x =2
print(lista_alumnos[x])

lista_alumnos[1] = 23 # con esto cambio un elemento de la lista

print(lista_alumnos)

lista_alumnos.append("hola")

print(lista_alumnos)

print(len(lista_alumnos)) #te devuelve la cantidad de elementos

lista_alumnos.insert(3,"chau") #para insertar donde quiera un nuevo elemento a la lista. Primero defino el lugar, luego el elemento

print(lista_alumnos)

print(len(lista_alumnos))

del lista_alumnos[2] #esto es para eliminar un elemento de la lista
print(lista_alumnos)
\
lista_nombres = []

nombre1 = input("Ingresa primer nombre")
lista_nombres.append(nombre1)
nombre2 = input("Ingresa segundo nombre")
lista_nombres.append(nombre2) #el append agrega un nuevo elemento al fnal de la lista
nombre3 = input("Ingresa tercer nombre")
lista_nombres.append(nombre3)
nombre4 = input("Ingresa cuarto nombre")
lista_nombres.append(nombre4)

print(lista_nombres)


lista_nombres = []

lista_nombres.append(input("Ingresa primer nombre"))

lista_nombres.append(input("Ingresa segundo nombre"))

lista_nombres.append(input("Ingresa tercer nombre"))

lista_nombres.append(input("Ingresa cuarto nombre"))

print(lista_nombres)

#la funcion len permite ver la cantidad de elementos.
#lista.sort() para orden ascendente
#lista.sort(reverse=True) si queremos hacer orden descendente

lista_edades = []

lista_edades.append(int(input("Ingresa primer edad: ")))
lista_edades.append(int(input("Ingresa segunda edad: ")))
lista_edades.append(int(input("Ingresa tercera edad: ")))
lista_edades.append(int(input("Ingresa cuarta edad: ")))
lista_edades.append(int(input("Ingresa quinta edad: ")))

lista_edades.sort(reverse=True)

print(lista_edades)

#Matriz: basicamente son listas anidadas donde podemos decir cada lista representa una fila y los elementos dentro una columna

matriz = [[1,2,3],["Hola", "Chau"],[True, False]]

print(type(matriz))

print(matriz [2][0]) #para hacerle print primero eligo numero de lista y despues numero de elemento cada uno entre corchete sin coma

matriz[2].append(5) #para agregar , etc algo a la lista le especifico en el nombre de lista en que numero de lista laburar

print(matriz)

#BUCLES: while y for. El for puede ser para recorrer una lista.

numero = 1
while numero<5:
    print("mal")
    numero = numero + 1

print("Fin del programa")

alumnos = ["Juan", "Sofia", "Leandro","Sol","Ana"]

for alumno in alumnos: #el primer alumno es cualquier palabra que quiera. Puede ser i incluso. Recorre la lista. Cuando no tiene mas elementos para leer se va.
    print(alumno) #es un bucle que va recorriendo la lista. Si le meto un print de termino en el mismo margen, me tira alumno,termino, alumno, termino. En cambio si lo pongo aparte una vez termino el recorrido me imprime el termino

print("Termino")

lista_precios = [50,75,46,22,80,65,8]

menor = lista_precios[0]
mayor = 0

for precio in lista_precios:
    if precio < menor:
        menor = precio
    elif precio > mayor:
        mayor =precio

print("el precio menor es", menor, "y el precio mayor es: ", mayor)


#el range trabajaba integrada al for

i = 1

while i < 10:
    print(i)
    i = i +1


#for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
 #   print(i)

for i in range(0,16,5): #range: hay que especificarle 3 parametros. Un desde, hasta, forma_incremento_iteracion. Tarabaja integrado con el for
    print(i) 

for i in range(20,10,-1): #range: hay que especificarle 3 parametros. Un desde, hasta, forma_incremento_iteracion. Tarabaja integrado con el for
    print(i) 

for i in range(10): #si no lo complete toma valor predeterminado desde 1 hasta el maximo y forma de incremento 1
    print(i)


alumnos = []

numero_alumnos = int(input("Ingresa numero de alumnos: "))

for i in range (numero_alumnos):
    alumnos.append(input("Ingresa nombre alumno: "))

j = 0

while j < numero_alumnos:
    print("Nombre de alumno: ", alumnos[j])
    j = j + 1



contrasenia = "contrasenia"

ingresa_contrasenia = input("Ingresa contrasenia: ")

while ingresa_contrasenia != contrasenia:
    print("Contrasena incorrecta")
    ingresa_contrasenia = input("Ingresala de vuelta: ")

print("contrasenia correcta")

for i in range (11):
    print(i)
    if i ==5:
        break

i = 0

while i <= 10:
    print(i)
    if i ==5:
        continue # el continue es para que se continue la itireacion dentro del while si el codigo sigue
    print("hola", i)

mi_tupla = (1, True, "Hola")

conexion_bd = "127", "Root", "10"

conexion_completa = conexion_bd, "33", "10"

print(conexion_completa)

tupla_indice = (1,2,3,4,5,6,7,8,9,10)

indice = int(input("Introduci tu indice del 0 al 9: "))

if indice == 0 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        print(tupla_indice [indice])
else:
    print("Error. Ingresaste un indice invalido.")


lista = [], []

nombre_alumno1 = input("Ingresa tu nombre: ")
cantidad_cursos_alumno1 = int(input("Ingresa cantidad de cursos del alumno: "))

operacion = input("Que operacion desea ejecutar: 1) Nombre de alumno o 2) Cantidad de cursos: ")

print("Gracias por utilizar el programa!")



variable_nula = None
variable_compleja = 10 + 8j

valor_entero = input("introduci tu valor: ")

print("el valor es: ", int(valor_entero))
print("el valor es: ",float(valor_entero))
print("el valor es: ",bool(valor_entero))
print("el valor es: ",complex(valor_entero))

valor_1 = input("introduci primer valor: ")
valor_2 = input("introduci segundo valor: ")

print(int(valor_1) + int(valor_2))
print(f"Suma {int(valor_1) + int(valor_2)}") # Esto es buena practica
print(f"Resta {int(valor_1) - int(valor_2)}")
print(f"Multiplicar {int(valor_1) * int(valor_2)}")
print(f"Dividir {int(valor_1) / int(valor_2)}")

listas = [1,2,3,4,5,6,7,8, True, "Ezequiel"] #coleccion que almacena tipos de datos. Del estilo q yo quiera
listas[0] =2
listas[1] = "Matias"
listas[2] = False

listas [0: 3: 1]

tuplas = (28, True, "Ezequiel") #el tema de las tuplas es q no se puede modificar a diferencia de las listas. Por lo tanto consume menos recursos.
elemento = tuplas[0] #tambien es mas segura pq no deja q se cambien datos

# diccionario
diccionarios = {
    'valor': 1,
    'valor_2' : 2,

numero1 = int(input("introduce tu numero"))
suma = 0

while numero1 > 0:
    suma = numero1 + suma
    numero1 = int(input("introduce nuevo numero"))

print("el total", str(suma))
