name = input("Hi, what's your name? ")
age = int(input("How old are you? "))

if (age < 13):
    print("You're too young to register", name)
else:
    print("Feel free to join", name)   



# generar un conjunto de numeros aleatorios y determinar cuales son impares (de otro modo)

from random import randint

numeros_aleatorios = [randint(1,100) for i in range(50)] # crea un siclo q se repite 50 veces, es decir, 50 numeros impares

print(numeros_aleatorios)
