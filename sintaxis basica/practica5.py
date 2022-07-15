print("Programa becas")

distancia_escuela = int(input("a que distancia estas?"))
print(distancia_escuela)

numeros_hermanos = int(input("cuantos hermanos tenes?"))
print(numeros_hermanos)

salario_familiar = int(input("que salario tiene?"))
print(salario_familiar)

if (distancia_escuela>40 or numeros_hermanos>2 or salario_familiar<=20000):
        print("sale beca")
else:
    print("no sale nada")



import random

valor_aleatorio = random.randint(0, len(lista) - 1)

curso = lista[valor_aleatorio]

print(f"El curso que deberias hacer ahora es: {curso[valor_aleatorio]}.")

import random

print("Bienvenido a Guess it")

valor_aleatorio = random.randint(0,4)

print(valor_aleatorio)

intentos = 0

while intentos < 3:
    intento_numero = int(input("Ingresa primer numero: "))
    intentos += 1
    
    if intento_numero == valor_aleatorio:
        print("correcto")
        break
    else:
        print("Equivocado")

lista = [1,2,3,4,5]

1 in lista # es para preguntar si el valor q se denuncia incicialmente esta en la lista. Funciona en tuplas y listas.

"hola" in lista

cadena = "Hola"

print(variable:=123)
