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

