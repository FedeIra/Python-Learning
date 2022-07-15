print("~~~ The Shimmy ~~~")

def shimmy ():
    print("Take one step to the right and stomp.")
    print("Take one step to the left and stomp.")
    print("Shake those hips!") 

shimmy ()
shimmy ()
shimmy ()



def iguales (texto1, texto2):
    return texto1 == texto2
    
t1 = input("Ingrese palabra uno: ")
t2 = input("Ingrese palabra dos: ")

comparar = iguales(t1, t2)

if comparar:
    print ("Los valores son iguales")
else:
    print ("Los valores son distintos")


def numeros(a,b):
    for i in range(a,b,2):
        print(i)

numeros(a = int(input("Ingresa tu primer numero: ")), b = int(input("Ingresa tu segundo numero: ")))

import time #El sleep hace que duerma el tiempo que le indiques.

i = 0

while i < 10:
    print(i)
    time.sleep(2)
    i = i+1

import tkinter as tk

def saludar():
    nombre= caja1.get()  # el metodo get es leer el contenido del control
    print("Hola mundo para", nombre)
    
def imprimir_numero():
    for i in range(1,11):
        print(i)
