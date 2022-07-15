print("es el area del triangulo es igual a: {}".format(area)) #el format area es para completar el {} que se agrega al string. Esto, en lugar de sumarle el ",float(area)"




# calcular el maximo comun divisor de dos numeros (el numero mas grande que divide dos numeros)

def mcd (x, y):
    mcd = 1 # se le designa uno porque es generalmente el maximo comun divisor de dos numeros. Divide a cualquiera

    if x % y == 0:
        return y

    for k in range(int(y/2), 0, -1): # el int es para quedarse con la parte entera sin decimales. El 0 es para obtener maximo 0. El -1 es para ir reduciendo
        if x % k == 0 and y % k == 0:
            mcd = k
            break #el break es para terminar el ciclo porque no hay q comprobar nada mas. Es hasta alcanzar el ultimo valor que no puede ser menor a 0. Minimo deberia ser 1

    return mcd #el return lo uso para en lugar de imprimirlo aca, luego al invocar la funcion lo imprima, como se ve abajo

print(mcd(13,7))

print(mcd(2,2))

# se puede recurrir directamente a la funcion de python 
from math import gcd #python cuenta con gcd para calcular el maximo comun divisor de dos numeros




# calcular el minimo comun multiplo
def mcm (x,y):
    z = max(x,y) #el max es una funcion para que te tire el mayor que si puede ser multiple del menor

    while True:
        if (z % x == 0) and (z % y ==0):
            return z
        z +=1 # el += es para sumarle uno. Es mas corto que decir z = z+1. es una abreviacion
print(mcm(2,4))

print(mcm(32,13))




# calcular la suma de tres numeros si todos son diferentes. en caso contraro sera 0

def calculo (a,b,c):
    if a != b and a != c and b != c:
        suma = a + b + c
        print(suma)
    else:
        print("numero ingresado incorrecto")

print(calculo (1,2,2))



#mismo ejercicio que antes, pero te vuelven a preguntar si ingresas numeros incorrectos
def sumar (a,b,c):
    while a == b or a == c or b == c:
        print("numero ingresado incorrecto")
        a = int(input("ingresa primer numero de vuelta"))
        b = int(input("ingresa segundo numero de vuelta"))
        c = int(input("ingresa tercero numero de vuelta"))
       
    else:
        return a + b + c

print(sumar (1,2,3))




def sumar (a,b):
    if 10 < a + b < 30: 
        return 30
    else:
        return a + b

print (sumar(21,10))



# otra forma es:
def sumar (a,b):
    suma = a + b

    if suma in range (10,30 +1): # si la suma da entre 10 y 30 es esto, el + 1 es porque el range llega hasta el numero anterior al indicado, es decir hasta 29 incluido. No se incluye el [ultimo por lo que hay q sumarle 1]
        return 30
    else:
        return suma

print (sumar(5,10))




#validar dos numeros. Si son iguales o la suma o el valor absoluto son 5 retornar verdadero. dE lo contrario retornar false.

def validar_numeros(a,b):
    if a == b or a+b==5 or abs(a - b) == 5: # el abs es para determinar si el valor absoluto de los dos numeros es igual a 5
        return True
    else:
        return False

print(validar_numeros(2,4))
print(validar_numeros(2,3))
print(validar_numeros(16,11))




# crear una funcion unicamente para sumar numeros enteros

def sumar (a,b):
    if isinstance(a, int) and isinstance(b, int): #la funcion isinstance le pones el primer elementos sobre el que queres corroborar algo, y el segundo q es lo debe ser.
        return a + b
    else:
        raise TypeError("Los valores deben ser enteros") #el typeError es para que te tire error y te diga cual en el caso de que no cumpla con el if.
   
print(sumar(3.2,2))




# crear una funcion unicamente para sumar numeros enteros

def sumar (a,b):
    if isinstance(a, int) and isinstance(b, int): #la funcion isinstance le pones el primer elementos sobre el que queres corroborar algo, y el segundo q es lo debe ser.
        return a + b
    else:
        raise TypeError("Los valores deben ser enteros") #el typeError es para que te tire error y te diga cual en el caso de que no cumpla con el if.

try:   # hace el codigo mas robusto
    print(sumar(32,2))
    print(sumar(32.3,2))
except TypeError as e: #para evitar que te tire toda la explicacion previa del error.
    print(e)



    # resolver la expresion algebraica (x + y) * (x + y)

def calculo (a,b): # hay librerias en python q te ayudan a resolver expresiones algebraicas.
    return a**2 + 2*a*b + b**2

a = float(input("escribi tu numero"))
b = float(input("escribi tu segundo numero")) # el float adelante es para convertir un numero entero a uno con comas

print(calculo (a,b))



# calcular el valor futuro para una cantidad, interes y numero de anios especificos

def valor_futuro (vp, i, n):
    return vp* (1 + i)**n

valor_presente = 10000
interes = 3.5
periodos = 7

print(valor_futuro(valor_presente, interes/100, periodos)) # el /100 es porque el interes se tiene que dividir por 100 para que agarre 3.5% en lugar de 350%.
