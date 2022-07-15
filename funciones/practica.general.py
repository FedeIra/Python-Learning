def generapares(limite):
    num = 1
    
    while num<limite:
        yield num*2
        num=num+1

devuelvepares = generapares(10)
    
print(next(devuelvepares))

print("aqui podr[ia ir mas codigo")

print(next(devuelvepares))

print("aqui podr[ia ir mas codigo")

print(next(devuelvepares))

# funcion operacion con return 

def calculo(n):

    if n>10:
        return n + 10
    else:
      return n - 2

print(calculo(10))

print(calculo(2))




def cercano (n):
    """
    Bienvenido al juego.
    Cuando se hace verdader.
    Se hace un laberinto eterno
    """

    return (abs(1000 - n) < 100) or (abs(2000 - n) < 100)

print(cercano(1000))




def validar_nombre_archivo (nombre_archivo):
    """
    valida si el nombre de archivo tiene la extension .py.
    si no lo tiene, la agrega
    """
    if len(nombre_archivo) >= 4 and nombre_archivo[-3:] == ".py":
        return nombre_archivo
    else:
        return nombre_archivo+ ".py"

print(validar_nombre_archivo(".py"))



def generar_numeros_pares(n = 100):

    """
    Esto general los primeros numeros positivos
    """
    pares = []

    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)    
            contador += 1

        numero += 1
    
    return pares

n = int(input("escribi la cantidad de numeros pares positivos a generar"))

if n > 0:
    pares = generar_numeros_pares(n)
    print(pares)
    print("cantidad de pares: ", len(pares))
else:
    print("el numero debe ser positivo")



def replicar():
    a = str(input("introduce la palabra"))
    b = int(input("introduci el numero"))
    print((a)[:1])*b

replicar()



#crear una subcadena de n caraceres resplicada n cantidad de veces
# "Python" , n = 2 => "Py", "PyPy"

def replicar_subcadena(cadena, n):
    n_caracteres = n

    if n_caracteres > len(cadena):
        n_caracteres = len(cadena)
    
    subcadena = cadena[:n_caracteres]

    resultado = " "

    for i in range(n):
        resultado += subcadena
    
    return resultado

print(replicar_subcadena("Python", 2))

print(replicar_subcadena("Python", 10))



# comprobar si un caracter dado es una vocal

def detector_vocales (c):
    vocales = "aeiou"

    c = c.lower() # para convertir a minuscula la c

    return c in vocales

print(detector_vocales ("c"))

print(detector_vocales ("a"))

print(detector_vocales ("A"))



# comprobar si un caracter dado es una vocal

def detector_vocales (c):
    
    if len(c) == 1:  # esta parte es para q tire false si se pone mas de una letra
        vocales = "aeiou"
        c = c.lower() # para convertir a minuscula la c
        return c in vocales
    else:
        return False

print(detector_vocales ("c"))

print(detector_vocales ("a"))

print(detector_vocales ("ae"))



# simlar el funcionamiento del operador in

milista = (1, 2, 3, 4, 5)

print("a" in milista)


print(5 in [2, 3, 5, 7, 11]) # esto te dice true/false de si el 5 se encuentra dentro de la tupla o lista q creaste
print("k" in "Fork")




# simlar el funcionamiento del operador in

def pertenece_a(lista, elemento): #comprueba si un elemento esta disponible en la lista
    for i in lista:
        if elemento == i:
            return True
    
    return False

print(pertenece_a("aeiou", "j"))

print(pertenece_a([1,3,4,6], 5))

print(pertenece_a("hola", "a"))

print(pertenece_a(["h","o","l", "a"], "a"))




# crear un histograma a partir de una lista de enteros

def crear_histograma(lista, caracter="*"): #predefinimos el caracter al ponerle "*"
    for i in lista:
        print(caracter * i)

print(crear_histograma([1,2,3,4,5])) #aca cuando defino lista, al poner [...] le puse una lista adentro. Ni me gasto en definir caracter pq ya esta definido al principio

print(crear_histograma([4,10,3,4,21]))



# emular el funcionamiento de join para concatenar una lista

def concatenar_lista(lista):
    resultado = " "

    for i in lista:
        resultado += str(i)
    
    return resultado

numeros = [2,3,5,7,11]

print(concatenar_lista(numeros))



# generar un conjunto de numeros aleatorios y determinar si son impares

from random import randint

def generador (n=randint(1,100)):
    print(n)
    if n % 2 == 0:
        return False
    else:
        print("es numero impar")

print(generador())
