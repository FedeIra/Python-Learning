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


tupla_indice = (1,2,3,4,5,6,7,8,9,10)

indice = int(input("Introduci tu indice del 0 al 9: "))

if indice == 0 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        print(tupla_indice [indice])
else:
    print("Error. Ingresaste un indice invalido.")



materias = {}

materias["lunes"] = [6150,3356]
materias["martes"] = [6150,3356]
materias["miercoles"] = [6150,3356]
materias["jueves"] = []
materias["viernes"] = [6150,3356]

for i in materias:
    print(i, ":", materias["lunes"])    

materias["lunes"] = [7777, 3356]
print("cambio lunes:", materias["lunes"])

diccionario2 = {0:"cero"}


diccionario = {}

nombre = input("Escribi tu nombre: ")
diccionario["nombre"] = [nombre]

edad = int(input("Escribi edad: "))
diccionario["edad"] = [edad]

direccion = input("Escribi direccion: ")
diccionario["direccion"] = [direccion]

telefono = int(input("Escribi telefono: "))
diccionario["telefono"] = [telefono]

print(diccionario["nombre"], "tiene ", diccionario["edad"], "vive en ",diccionario["direccion"], "y su numero de telefono es: ", diccionario["telefono"])


def sumar (a,b):
    resultado = a + b
    return resultado


numero1 = 50
numero2 = 75

suma = sumar(numero1, numero2)
print("la suma es", suma)

if suma > 100:
    suma = suma + 100
else:
    suma = suma - 100

print("la suma es", suma) 



def numeros(a,b):
    for i in range(a,b,2):
        print(i)

numeros(a = int(input("Ingresa tu primer numero: ")), b = int(input("Ingresa tu segundo numero: ")))



numero1 = int(input("introduce tu numero"))
suma = 0

while numero1 > 0:
    suma = numero1 + suma
    numero1 = int(input("introduce nuevo numero"))

print("el total", str(suma))
