def sumar(op1, op2):
    print("El resultado es ", op1 + op2)

def restar(op1, op2):
    print("El resultado  es ", op1 - op2)

def multiplicar(op1, op2):
    print("El resultado es ", op1 * op2)

def dividir(dividendo, divisor):
    print("El resultado  es ", dividendo / divisor)

def potencia(base, exponente):
    print("El resultado es ", base ** exponente)

def redondear(numero):
    print("El resultado es ", round(numero))

redondear(3.3)



def conversion(segundos):
    minutos = int(segundos / 60)
    horas = int(minutos / 60)
    minutos_resto = minutos - (horas*60) 
    segundos_resto = segundos - (horas*60*60) - (minutos_resto *60)
    if horas<10:
        horast = "0" + str(horas)
    else:
        horast = str(horas)
    if minutos_resto < 10:
        minutost = "0" + str(minutos_resto)
    else:
        minutost = str(minutos_resto)
    if segundos_resto < 10:
        segundost = "0" + str(segundos_resto)
    else:
        segundost = str(segundos_resto)

    return(horast + ":" + minutost + ":" + segundost)

#####################################################

print(conversion(1000))

""""
Hacer una función que calcule el promedio, si es
posible, de todos los números primos que encuentre
en una lista que se le pasa por argumento
"""

def primedio(numeros):
    esprimo = []
    for numero in numeros:
        contador = 0
        for n in range(1,numero+1,1):
            if numero % n == 0:
                contador += 1
            if contador > 2:
                break
        if contador <= 2:
            esprimo.append(numero)
    p = sum(esprimo) / len(esprimo)
    return p

####################################

print(primedio([23,10,17,2,15,1]))

"""
Construir una función que debe tomar un número
arbitrario de argumentos posicionales (*args) y
deben ser nombres de personas, además la
función debe tener un keyword argument
(argumento por defecto) llamado grupo, por
defecto grupo = 2.
Nuestra función debe devolver una lista, con
listas en su interior con 2 nombres por cada una,
si grupo queda por defecto.
Si el argumento “grupo” recibe un valor, debemos
asegurarnos de que sea mayor que 2, si no lo es,
forzar para que el valor quede en 2.
Ejercicio 5: Hay Equipo
Crearemos los grupos según el número pasado
por argumento a “grupo”.
Por ejemplo:
equipo("Juan","Tamara","Lautaro","Gabriel"
"Agustin","Susana",grupo=3)
>>> [['Juan', 'Tamara', 'Lautaro'],
['Gabriel', 'Agustín', 'Susana']]

Si no se pasa el valor de grupo o se pasa un valor menor a 2:
[['Juan', 'Tamara'], ['Lautaro', 'Gabriel'],
['Agustín', 'Susana']]
Y si se pasa un número no múltiplo, los participantes que
sobran formarán el último grupo. Como a continuación
grupo = 4 :
[['Juan', 'Tamara', 'Lautaro', 'Gabriel'],
['Agustín', 'Susana']]
"""

def funcion (*args):
    lista = []

    return lista

print(funcion(["Maria", "Marta", "Fede", "Juan"]))


def equipo(*participantes,grupo=2):
    equipos = []
    if grupo < 2:
        grupo = 2
    for n in range(grupo,len(participantes)+1,grupo):
        equipos.append(list(participantes[n-grupo:n]))
    if n < len(participantes):
        equipos.append(list(participantes[n:]))
    print(equipos)
        
equipo("Juan","Tamara","Lautaro","Gabriel","Agustin","Susana",grupo=4)

def promedio_variable(*numeros):
    suma=0
    for n in numeros:
        suma+=n
    return suma/len(numeros)

promedio=promedio_variable(3,7,22,9,0,123)
print(promedio)

def promedio_variable(*args):
    total = 0
    for n in args:
        total = n + total
        valor_final = total / len(args)
    return valor_final

print(promedio_variable(1,2,3))

# Funciones - ORDEN SUPERIOR: recibe una funcion o devuelve una funcion

def sumar(x):
    return x+100

def cuadrado(x):
    return x**2

def superior(funcion,lista): #funcion que recibe de otro parametro una funcion
    resultado = []
 
    for n in lista:
        resultado.append(funcion(n))
    return resultado

numeros = [2,5,10]
print(superior(sumar,numeros))
print(superior(cuadrado,numeros))

#Funciones lambda> son funciones implicitas.

sumar = lambda x, y: x+y

# Hay dos funciones en python q sirven mucho:

map() #recorre elementos para hacer una funcion. En realidad es una clase. ES PARECIDA AL FOR
filter() # es para filtrar valores

enteros = [1,2,4,7]
cuadrados = list(map(lambda x: x**2,enteros)) # el map recorre los elementos, el lista es para q se guarde los datos como lista y no como map
print(cuadrados)

#Pandas> manejar volumenes grande de datos

# Clousures / Decorators

filter() # es para filtrar valores

valores = [1,2,3,4,5,6,7,8]
pares = []
for valor in valores:
    if valor %2 ==0:
        pares.append(valor)
print(pares)

lista = []
valores = [1,2,3,4,5,6,7,8]
pares = list(filter(lambda x: x % 2 == 0))

# EXCEPCIONES. Preves un error, lo agregas como except y hace q el programa noo se corte. 
# si pones except sin aclarar el tipo toma como predeterminado el exception q te agarra todos
# se puede acumular tipos de error en una tupla

"""
Podemos crear funciones que pueden tomar
funciones como parámetros y también retornar
(devolver) funciones como resultado. Una función
que hace ambas cosas, o alguna de ellas, se la
llama función de orden superior.
En el ejemplo genérico a continuación se pasa
una función y una lista para que la función
superior() trabaje:
"""

def antiguedad(meses, anios):
    if meses >= 3:
        anios_antiguedad = anios + 1
    return anios_antiguedad
    
def indemnizacion_antiguedad(funcion, salario):
    indemnizacion = antiguedad(3,1) * sueldo
    return indemnizacion

sueldo = 30000
print(indemnizacion_antiguedad(antiguedad, sueldo))

"""
Las funciones lambda son un tipo de funciones
que típicamente se pueden escribir en una línea y
cuyo código a ejecutar suele ser pequeño.
Resulta complicado explicar las diferencias
porque, básicamente, la diferencia es cómo se
escribe, la sintaxis. Para que tengas una idea son
funciones que queremos usar y descartar.
Idealmente se usan como argumento en
funciones de orden superior.
La función cuadrado(x) que usamos en el
ejemplo anterior la podríamos escribir como:
"""
lambda x : x**2 
"""def sumar(x):
    return x+100"""

lambda x : x+100
"""def cuadrado(x):
    return x**2"""

def superior(funcion,lista): 
    resultado = []
 
    for n in lista:
        resultado.append(funcion(n))
    return resultado

numeros = [2,5,10]

print(superior(lambda x : x**2 , numeros))
"""print(superior(sumar,numeros))"""
print(superior(lambda x : x+100 , numeros))
"""print(superior(cuadrado,numeros))"""

"""A las funciones anónimas también se les puede asignar
un nombre como si fuera una variable (en realidad, como si
fuera un objeto). Esto último no es muy aconsejable y no
fueron pensadas para esto.
Pero si estamos en la consola interactiva haciendo pruebas
puede ser de gran utilidad para definir pequeñas subrutinas.
"""

cuadrado = lambda x : x**2
print(cuadrado(10))
