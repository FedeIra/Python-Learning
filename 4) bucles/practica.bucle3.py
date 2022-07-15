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