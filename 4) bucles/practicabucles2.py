print("Programa para crear cuenta de gmail:")

contador = 0

miEmail=input("introducie tu email")

for i in miEmail:
    if (i=="@" or i=="."):
        contador = contador + 1

if contador==2:
    print("email introducido")
else:
    print("email incorrecto")



import math

print ("Programa de raiz cuadrada")
numero = int(input("introduci tu numero: "))

intentos=0

while numero<0:
    print("numero incorrecto")
    intentos=intentos+1
    numero = int(input("introduci tu numero de vuelta: "))
    if intentos == 2:
        print("demasiado intentos,chau")
        break;

if intentos<2:
    solucion=math.sqrt(numero)
    print("la raiz cuadrada de", str(numero) + "es" + str(solucion))


numero1 = int(input("introduce tu numero"))
numero2 = int(input("introduce nuevo numero"))

while numero2 > 0:
    numero1 = numero1 + numero2
    numero2 = int(input("introduce nuevo numero"))

print("el total", str(numero1))
numero1 = int(input("introduce tu numero"))
suma = 0

while numero1 > 0:
    suma = numero1 + suma
    numero1 = int(input("introduce nuevo numero"))

print("el total", str(suma))
