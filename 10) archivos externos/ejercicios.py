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




# generar un conjunto de numeros aleatorios y determinar cuales son impares (de otro modo)

from random import randint

numeros_aleatorios = [randint(1,100) for i in range(50)] # crea un siclo q se repite 50 veces, es decir, 50 numeros impares

print(numeros_aleatorios)

#crear funcion de filtro, o la q esta incorporada en python de filter

numeros_impares = filter(lambda n: n % 2 == 1, numeros_aleatorios) #las expresiones lamda son una forma corta de declarar funciones pequenias y anonimas (no es necesario proporcionar un nombre para las fnciones lambda). Las funciones lamba se comportan como funciones normales declaradas con la palabra clave def

print(list(numeros_impares))

#a continuacion, forma de crear filtro sin la funcion automatica de python. dan los mismos numeros impares

def encontrar_impares(lista):
    impares = []

    for i in lista:
        if i%2==1:
            impares.append(i)
    return impares

print(encontrar_impares(numeros_aleatorios))




# calcular la diferencia de conjuntos con colores

colores_lista_1 = ["Negro", "Rojo", "Verde", "Blanco"]
colores_lista_2 = ["Blanco", "Azul","Gris","Amarillo","Verde"]

colores_conjunto_1 = set(colores_lista_1) # aca se usa la funcio set para hacer con conjunto de las listas creadas anteriormente
colores_conjunto_2 = set(colores_lista_2)

diferencia = colores_conjunto_1.difference(colores_conjunto_2) # aca se usa la funcion difference para que te informe la diferencia del conjunto 1 con el conjunto 2

print(diferencia) # la anotiacion para conjunto es el de llaves. En este caso son objetos de tipo string.




# calcular el area de un triangulo (base por altura)/2

def calculo ():
    base = float(input("introduzca la base"))
    altura = float(input("introduzca la altura"))
    if base>0 and altura>0:
        print(float((base*altura)/2), "es el area del triangulo")
    else:
        print("introdujiste un numero incorrecto")

calculo ()


# calcular el area de un triangulo (base por altura)/2. En esta la hago sin interactuar con terminal
def calculo (base, altura):
    
    if base>0 and altura>0:
        print(float((base*altura)/2), "es el area del triangulo")
    else:
        print("introdujiste un numero incorrecto")

calculo (2,2)




# calcular el area de un triangulo (base por altura)/2. interactuando y previendo error al escribir palabra en lugar de numero

base = None # se usa None con asignacion de variable cuando aun no le queremos dar un valor
altura = None

while True: # el while es para que si escribis mal, vuelva a preguntarte
    try:
        base = float(input("escriba la base del traingulo: "))
        break #se rompe el while al escribir un numero
    except: # si escribis una palabra no se rompe
        print("debe escribir un numero.")

while True:
    try:
        altura = float(input("escriba la altura del traingulo: "))
        break
    except:
        print("debe escribir un numero.")

area = base*altura/2

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



#CLASES

class Coche():  #debe ser con mayuscula el nombre de la clase
    largoChasis = 250 #estoy estableciendo propiedades
    anchoChasis = 120
    ruedas = 4
    enmarcha = False 
    color = "rojo"

# para establecer un comportamiento para metodo usas def. Un metodo  es una funcion especial q pertenece a la clase q estas creando mientras que una funcion no pertenece a ninguna clase
    def arrancar(self): #este comportamiento cambia la propiedad enmarcha
        self.enmarcha = True 

    def estado(self): #el self te lo obliga a poner python. Agrego otra funcion para que me confirme el estado del auto. Si esta en marcha o no
        if (self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"
#con lo anterior creamos una clase. A continuacion, creamos un objeto

miCoche = Coche() #le tenes que asignar la clase con Coche(). Es INSTANCIAR (o ejemplejarizar) una clase

print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene:", miCoche.ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes

miCoche.arrancar() #con esto llamo la funcion de arrancar, y el coche para de estar a enmarcha a arrancar

print(miCoche.estado())





class Coche():  #debe ser con mayuscula el nombre de la clase

    def __init__(self): #con esto define que es un contructor. es decir, que las propiedades de abajo van a ser el estado inicial de los objetos que pertenezcan a la clase coche. El constructor tiene siempre el nombre init, que significa estado inicial
        self.largoChasis = 250 #estoy estableciendo propiedades. Estas caracteristicas comunes son el estado inicial de los objetos pertenecientes a esta clase. el self. al principio es para decir que queremos que sean propiedades del estado inicial de los objetos
        self.anchoChasis = 120
        self.__ruedas = 4 #con el doble guion bajo encapsulo esta propiedad para q no pueda accederse y modificarse desde fuera, pero si es posible desde dentro de la propia clase. cada vez q utilices la variable ruedas hay que agregarle el doble guion bajo. solo se puede modificar desde una funcion dentro de la clase como las funciones de estado, cambio de color y arrancar.
        self.enmarcha = False # es decir, en principio, los objetos que pertenecen a esta clase no tienen la propiedad de estar en marcha
        self.color = "rojo"

# para establecer un comportamiento para metodo usas def. Un metodo es una funcion especial q pertenece a la clase q estas creando mientras que una funcion no pertenece a ninguna clase
    def arrancar(self, arrancamos): #Cuando haces una funcion para una clase, le tenes que agregar un parametro self que es el parametro por defecto. este comportamiento cambia la propiedad enmarcha. le agrgamos un parametro "arrancamos"
        self.enmarcha = arrancamos #el self.en marcha le agregamos el self para llamar a la propiedad de la case antes definida

        if(self.enmarcha):
             return "el coche esta en marcha"
        else:
            return "el coche esta parado"
    
    def cambio_de_color(self): #le tengo que agregar un parametro. Aparte recibe el parametro por defecto que es self
        self.color = "azul"
        print("pediste cambio de color a azul")
       
    def estado(self): #el self te lo obliga a poner python. Agrego otra funcion para que me confirme el estado del auto. Si esta en marcha o no
        print("el coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis, "y es de color", self.color)

#con lo anterior creamos una clase. A continuacion, creamos un objeto

miCoche = Coche() #para incorporar el objeto a la clase le tenes que asignar antes la clase con Coche(). Es INSTANCIAR (o ejemplejarizar) una clase

print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene:", miCoche.__ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes
print("el color del coche es:", miCoche.color)

print(miCoche.arrancar(True)) #con esto llamo la funcion de arrancar, y el coche para de estar a enmarcha a arrancar al ponerle True. Ademas al agarrar la funcion me dice si esta en marcha o parado

miCoche.cambio_de_color() # aca no le tengo q poner imprimir porque en la funcion en lugar de return tiene print

miCoche.estado() #aca llamo la segunda funcion de def estado(self) y por lo tanto me imprime las propiedad del coche

print("----- a continuacion creamos el segundo objeto ----------")

miCoche2 = Coche() #aca creo un segundo objeto q lo asigno a la clase coche. El objeto es una instancia de la clase (objeto = instancia)
print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene:", miCoche.__ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes
print(miCoche.arrancar(False)) # aca llamo la funcion de arrancar, pero al ponerle False no arranca y me retorna que esta parado

miCoche2.estado() #aca llamo a la funcion estado y me dice las propiedades del objeto. Como tiene print la funcion no necesita que le ponga print al invocar la funcion

print("----- a continuacion creamos el tercer objeto ----------")

cocheFede = Coche() #creo una nuevo objeto para la clase de coche
cocheFede.cambio_de_color()
cocheFede.arrancar(True)
cocheFede.estado()


print("----- a continuacion creamos el cuarto objeto ----------")

cochedelpueblo = Coche()
cochedelpueblo.__ruedas = 2 #esto es para cambiar propiedades mas facilmente. 
print(cochedelpueblo.estado(), "aguante el auto del pueblo!")

#ahora bien, esta mal que tenga 2 ruedas. Para evitar que se modifieque una propiedad desde fuera como este caso puedo encapsular esta propiedad. 




class Coche():  #debe ser con mayuscula el nombre de la clase

    def __init__(self): #con esto define que es un contructor. es decir, que las propiedades de abajo van a ser el estado inicial de los objetos que pertenezcan a la clase coche. El constructor tiene siempre el nombre init, que significa estado inicial
        self.largoChasis = 250 #estoy estableciendo propiedades. Estas caracteristicas comunes son el estado inicial de los objetos pertenecientes a esta clase. el self. al principio es para decir que queremos que sean propiedades del estado inicial de los objetos
        self.anchoChasis = 120
        self.__ruedas = 4 #con el doble guion bajo encapsulo esta propiedad para q no pueda accederse y modificarse desde fuera, pero si es posible desde dentro de la propia clase. cada vez q utilices la variable ruedas hay que agregarle el doble guion bajo. solo se puede modificar desde una funcion dentro de la clase como las funciones de estado, cambio de color y arrancar.
        self.enmarcha = False # es decir, en principio, los objetos que pertenecen a esta clase no tienen la propiedad de estar en marcha
        self.color = "rojo"

# para establecer un comportamiento para metodo usas def. Un metodo es una funcion especial q pertenece a la clase q estas creando mientras que una funcion no pertenece a ninguna clase
    def arrancar(self, arrancamos): #Cuando haces una funcion para una clase, le tenes que agregar un parametro self que es el parametro por defecto. este comportamiento cambia la propiedad enmarcha. le agrgamos un parametro "arrancamos"
        self.enmarcha = arrancamos #el self.en marcha le agregamos el self para llamar a la propiedad de la case antes definida

        if(self.enmarcha):
             return "el coche esta en marcha"
        else:
            return "el coche esta parado"
    
    def cambio_de_color(self): #le tengo que agregar un parametro. Aparte recibe el parametro por defecto que es self
        self.color = "azul"
        print("pediste cambio de color a azul")
       
    def estado(self): #el self te lo obliga a poner python. Agrego otra funcion para que me confirme el estado del auto. Si esta en marcha o no
        print("el coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis, "y es de color", self.color)

#con lo anterior creamos una clase. A continuacion, creamos un objeto

miCoche = Coche() #para incorporar el objeto a la clase le tenes que asignar antes la clase con Coche(). Es INSTANCIAR (o ejemplejarizar) una clase

print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene:", miCoche.__ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes
print("el color del coche es:", miCoche.color)

print(miCoche.arrancar(True)) #con esto llamo la funcion de arrancar, y el coche para de estar a enmarcha a arrancar al ponerle True. Ademas al agarrar la funcion me dice si esta en marcha o parado

miCoche.cambio_de_color() # aca no le tengo q poner imprimir porque en la funcion en lugar de return tiene print

miCoche.estado() #aca llamo la segunda funcion de def estado(self) y por lo tanto me imprime las propiedad del coche

print("----- a continuacion creamos el segundo objeto ----------")

miCoche2 = Coche() #aca creo un segundo objeto q lo asigno a la clase coche. El objeto es una instancia de la clase (objeto = instancia)
print("el largo del coche es: ", miCoche2.largoChasis)
print("el coche tiene:", miCoche2.__ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes
print(miCoche.arrancar(False)) # aca llamo la funcion de arrancar, pero al ponerle False no arranca y me retorna que esta parado

miCoche2.estado() #aca llamo a la funcion estado y me dice las propiedades del objeto. Como tiene print la funcion no necesita que le ponga print al invocar la funcion

print("----- a continuacion creamos el tercer objeto ----------")

cocheFede = Coche() #creo una nuevo objeto para la clase de coche
cocheFede.cambio_de_color()
cocheFede.arrancar(True)
cocheFede.estado()


print("----- a continuacion creamos el cuarto objeto ----------")

cochedelpueblo = Coche()
cochedelpueblo.__ruedas = 2 #esto es para cambiar propiedades mas facilmente. 
print(cochedelpueblo.estado(), "aguante el auto del pueblo!")

#ahora bien, esta mal que tenga 2 ruedas. Para evitar que se modifieque una propiedad desde fuera como este caso puedo encapsular esta propiedad. 


class Coche():  

    def __init__(self): 
        self.largoChasis = 250 
        self.anchoChasis = 120
        self.ruedas = 4 
        self.__enmarcha = False
      
    def arrancar(self, arrancamos): 
        self.__enmarcha = arrancamos 

        if(self.__enmarcha): 
            chequeo = self.__chequeo_interno() # Aca le pongo chequeo es igual chequeo interno para el proximo if

        if(self.__enmarcha and chequeo): # aca la agregams el and chequeo para que arranque solo si la funcion de chequeo interno es True.
             return "el coche esta en marcha"
        
        elif(self.__enmarcha and chequeo == False):
            return "algo ha ido mal en el chequeo. no podemos arrancar"

        else:
            return "el coche esta parado"
       
    def estado(self):
        print("el coche tiene ", self.ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

    def __chequeo_interno(self): # le agrego otro comportamiento que es un cheque general. Pero lo quiero q se haga antes de arrancar. Al ponerle el __ encapsulamos el metodo. Esto para que no lo puedas llamar desde afuero sino desde una funcion de la clase. La llamamos desde afuera cuando decimos: print(miCoche.__chequeo_interno())
        print("realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False 

miCoche = Coche() 

print(miCoche.arrancar(True)) 

miCoche.estado() 

print("----- a continuacion creamos el segundo objeto ----------")

miCoche2 = Coche()

print(miCoche.arrancar(False)) 

miCoche2.estado() 




# HERENCIA 
# #las clases se pueden representar por jerarquias. La primera es clase padre o super clase.
# la clase s2 seria subclase o padre de las siguiente clases
#la utilidad es re utilizar un codigo. A la hora de elaborar un programa llegasa  crear programas similares. Por ejemplo, con el programa de los coches, crear objetos de tipo camion, lanchas, motos, etc.
#para crear herencia tenes q pensar q caracteristcas en comun van a tener los objetos dentro de la clase, tambien los comportamientos

class Vehiculos():
    def __init__(self, marca, modelo):
    
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frene = False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frene = True

    def estado(self):
        marca = "a determinar"
        modelo = "a determinar"
        print("Marca:", self.marca, "\nModelo", self.modelo, "\nEn Marcha", self.enmarcha, "\nAcelerando", self.acelera, "\nFrenando", self.frene) #la /n hace un salto de linea en pantalla

class Moto(Vehiculos): #aca es cuando creamos una nueva clase "moto", que hereda de (Vehiculos)
    pass #es palabra reservada para no construir nada sobre esta clase

miMoto = Moto("Honda" , "CBR")

miMoto.estado()




class Vehiculos():
    def __init__(self, marca, modelo):
    
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frene = False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frene = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo", self.modelo, "\nEn Marcha", self.enmarcha, "\nAcelerando", self.acelera, "\nFrenando", self.frene) 

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"

class Moto(Vehiculos): 
    hcaballito = ""

    def caballito(self): # agrego un nuevo metodo o comportamiento a los otros 5 de la clase padre
        self.hcaballito = "voy haciendo el caballito"

    def estado(self): #aunq estoy usando el mismo comportamiento de la clase padre, el nuevo metodo de la clase hija la reemplaza para esta subclase
        print("Marca:", self.marca, "\nModelo", self.modelo, "\nEn Marcha", self.enmarcha, "\nAcelerando", self.acelera, "\nFrenando", self.frene, "\n", self.hcaballito) 

class VElectricos(): #esto seria una clase independiente
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


miMoto = Moto("Honda" , "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.estado()

class Quad(Moto):
    pass

micuatri = Quad("cuatri", "super")

micuatri.estado()

print(miFurgoneta.carga(True))


class BicicletaElectrica(Vehiculos, VElectricos): #Herencia multiple: hereda de dos clases o mas, separando las clases con una coma. Hereda todos los metodos y propiedades. Utiliza los metodos del primero si tienen metodos con el mismo nombre
    pass

mibici = BicicletaElectrica() # cuando hay herencia multiple se le da preferencia a la primer herencia q indicas. Esto es importante para los argumentos que tiene la clase. Por eso lo dejamos sin argumentos.




#Clase herencia: super() y isistance()
#la funcion super llama al metodo padre (sirve para cuando una propiedad pertenece a dos clases con metodos distintos y queremos aplicar ambos metodos)

class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion_persona(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.lugar_residencia)

class Empleado(Persona): #al ponerle Persona le decimos que hereda de persona
    def __init__(self, salario, antiguedad):
        super().__init__("Antonio", 55, "Espania") #esta llamando al metodo init de la clase padre
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion_empleado(self):
        print("Salario:", self.salario, "\nAntiguedad:", self.antiguedad)

Antonio = Empleado(10000, 10)

Antonio.descripcion_persona()

Antonio.descripcion_empleado()




#Clase herencia: super() y isistance()
#la funcion super llama al metodo padre (sirve para cuando una propiedad pertenece a dos clases con metodos distintos y queremos aplicar ambos metodos)
#principio de susitucion: aplicar los terminos de "es siempre un/a". Un objeto de la subclase sera siempre un objeto de la clase padre. Un empleado sera siempre una persona, no viceversa.
#hay una funcion issitance() para decirte a que clase pertenece

class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.lugar_residencia)

class Empleado(Persona): #al ponerle Persona le decimos que hereda de persona
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #esta llamando al metodo init de la clase padre
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion() #aca con el super llamo a la funcion descripcion del metodo padre
        print("\nSalario:", self.salario, "\nAntiguedad:", self.antiguedad)

Antonio = Empleado (10000, 10, "Antonio", 14, "Roosevelt")

Antonio.descripcion()

print(isinstance(Antonio, Empleado)) #al usar isinstance, poniendo el objeto y la clase, te dice si es cierto que pertenece a esa clase

print(isinstance(Antonio, Persona)) #tambien es verdad

class hola(): #invento clase para probar el falso de un isinstance
    pass

print(isinstance(Antonio, hola)) #al usar isinstance, poniendo el objeto y la clase, te dice si es cierto que pertenece a esa clase. En este caso me tira false porque Antonio no pertenece a la subclase hola


#POLIMORFISMO: un objeto puede cambiar de forma dependiendo del contexto q se lo use.

class Coche():
    def desplazamiento(self):
        print("me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("me desplazo utilizando 6 ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo) # aca llamo polimorfismo pasandole por parametro el objeto creado dentro de la clase camion. Por eso al aplicar esta funcion me llama a su vez la funcion de desplazamiento creado dentro de

#METODOS PARA USAR CADENAS DE CARACTERES: 
# upper() = para convertir a mayusculas
# lower() = pasa a minusculas
# capitalize() = pone la primer letra en mayuscula
# count() = conta cuantas veces aparece una letra o grupo de letras dentro de un texto
# find() = representar el indice o posicion en la cual aparece un caracter o grupo de caracteres
# isdigit() = devuelve booleano true o falos, si es un valor numerico o no
# isalum() = comprobar si es numerico
# isalpha() = comprueba si es alfabetico
# split() = separa por palabras utilizando espacios
# strip() = borra los espacios sobrantes
# replace() = cambia una palabra o letra por otra dentor de un string
# rfind() = representa el indice de un caracter pero contando desde atras del string. R de reverse.
# hay muchos mas metodos. los puedo encontrar en pyspanishdoc.sourceforge.net/lib/string-methods.html

nombreUsuario = input("introduce nombre de Usuario: ")

print("El nombre es: ", nombreUsuario.upper()) # se aplica el metodo poniendo . y la funcion a continuacion

print("El nombre es: ", nombreUsuario.capitalize())

edad = input("introduce la edad")

print(edad.isdigit()) #te dice si se introdujo numero te tira true. 

while (edad.isdigit() == False): #aca compruebo si no es numerico el valor introducie te sigue pidiendo q lo ingreses
    print("introdujiste mal la edad")
    edad = input("introduce la edad")


if int(edad.isdigit()) == True:
    print("tu edad es", edad, "introdujiste bien la edad")

if (int(edad)<18): # RECORDAR que lo que se introduce como input se considera texto, por lo que hay que aclarar que es intergidit (int)
    print("no puede pasar")
else:
    print("puede pasar")




email = input("introduce tu email")

if email.count("@") == 2 or email.endswith("@") or email.startswith("@"):
    print("direccion incorrecta")
    
else:
    email.count("@") < 2
    print("direccion correcta")


# modulo es un archivo con extension .py. Tambien hay con extesion .pyc (python compilado) o archivo escrito en C para CPython.. Posee su propio espacio de nombres y puede contener variables, funciones, clases e incluso otros modulos

#modulariazcion y reutilizacion. Modularizacion es dividir el codigo en modulos, es decir, pequenias partes. La reutilizacion es reutilizar programas usadas en distintos modulos en lugar de volver a crearla


import funciones_matematicas  # el modulo se crea haciendo un arhcivo con .py. Para usar el modulo primero hay que importarlo "import _______"

funciones_matematicas.sumar(7,5) #para usar el modulo lo tenes que llamar poniendolo al principio seguido de punto y con la funcion

funciones_matematicas.restar(7,5)

funciones_matematicas.multiplicar(7,5)

#para no tener q llamar cada vez la funcion se puede hacer con el from

from funciones_matematicas import restar, sumar, multiplicar #con el from llamo el modulo y con el import la funcion del modulo que quiera

restar(4,3) #ahora no tengo la necesidad de invocar cada vez q la uso al modulo

sumar(3,2)

multiplicar (4,2)

from funciones_matematicas import * #con el asterisco llamo todo lo que se encuentra dentro del modulo. A veces no me conviene llamar TODO el modulo por un tema de memoria dentro del programa.

multiplicar (4,3)



from modulo_vehiculos import *

miCoche = Vehiculos("Mazda", "2020")

miCoche.estado() #si muevo el archivo modulo que estoy importando a otra carpeta, y lo intento usar de vuelta tira error. Lo buca en el mismo directoria y si no esta ahi lo busca en syspath.

#hay forma de reutilizar el codigo encuentre donde se encuentre a traves de la funcion paquete. Modulos que esten relacionados o tengan un mismo objetivo lo organizas por paquetes.

#para crear un paquete, guardo un archivo con el nombre de __init__py en una carpeta. Desde ahi puedo guardar distintos codigos de py y quedan en el paquete


from calculos.calculos_generales import dividir # en el primero llamo al paquete, en el segundo al modulo dentro del paquete y en el tercero a la funcion dentro del modulo

dividir(2,2)


from calculos.calculos_generales import dividir, potencia # en el primero llamo al paquete, en el segundo al modulo dentro del paquete y en el tercero a la funcion dentro del modulo

dividir(2,2)

potencia(4,6)

# si hubiera clases puedo importarlas desde la midma forma, sino puedo usar asterisco para utilizar la funcio q queramos

from calculos.calculos_generales import *

restar(4,2)

# se puede crear subpaquetes. Les voy pegando el archivo con __init__.py para hacerlos subpaquetes



#persistencia de datos. Posibilidad de guardar datos en un archivo python para q no se pierdan. Almacena datos q fuimos manejando durante la ejecucion del programa para q no se pierdan.
# guardar esos datos en archivos internos o guardarlo en bases de datos.
#archivos externos de texto plano o sean lo q sean
#primero se crea un archivo externo, luego abrirlo, abierto el archivo hay que manipularlo, y por ultimo luego de trabajado el archivo hay que cerrarlo.

from io import open
#con el metodo open o abre el archivo o lo crea. con el open se abre o crea el archivo, con el write se maninpula, y con el close se cierra
archivo_texto = open("archivo.txt", "w") #la funcion open te pide dos argumentos: nombre del archivo q queremos abrir y el modo en el q lo abrimos (lectura, escritura, append para agregar mas info). La w es para abrirlo en modo escritura

frase = "estupendo dia para estudiar python\n el miercoles"

archivo_texto.write(frase) #la funcion write es para escribir en el doc. Esta es la parte que manipula el archivo

archivo_texto.close() #con el close se cierra el archivo. Cerrar se refiere a cerrar el programa desde python.



from io import open

archivo_texto = open("archivo.txt", "r") # el r es para q lea el archivo

texto = archivo_texto.read() #le decimos q lea el archivo y lo almacene en texto. Tambien esta el metodo real lines. Lee la linea del archivo y la almacena en una lista.

archivo_texto.close() # a pesar de q esta cerrado, podemos imprimr esa info.

print(texto)



from io import open

archivo_texto = open("archivo.txt", "r") 

lineas_texto = archivo_texto.readlines() #el readlines guarda la info dentro de una lista de lineas de texto manipulable

archivo_texto.close()

print(lineas_texto) #ahora te lo imprime como lista. Almancena dentro de esa lista las lineas de texto por lo q te diferencia el \n como si fuera parte del texto.

print(lineas_texto[0]) #aca estoy imprimiendo por numero en la linea. Puedo usar for para recorrer o combinar condicionales para buscar elemento en concreto.

print(lineas_texto[1])




from datetime import datetime

end_date = datetime(2020,8,6)
start_date = datetime(2019, 7, 6)

if end_date.day-start_date.day >= 0:
	num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
else: 
	num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)-1

print("Años: "+str(num_months//12))
print("Meses: "+str(num_months%12))

#----------------------------------------------


if end_date.day-start_date.day >= 0:
	print ("Días: "+str(end_date.day-start_date.day))
elif end_date.month==2:
	print ("Días: "+str(31-start_date.day+end_date.day))
elif end_date.month==3 and (end_date.year%4)!=0:
	print ("Días: "+str(28-start_date.day+end_date.day))
elif end_date.month==3 and (end_date.year%4)==0:
	print ("Días: "+str(29-start_date.day+end_date.day))
elif end_date.month==4:
	print ("Días: "+str(31-start_date.day+end_date.day))
elif end_date.month==5:
	print ("Días: "+str(30-start_date.day+end_date.day))
elif end_date.month==6:
	print ("Días: "+str(31-start_date.day+end_date.day))
elif end_date.month==7:
	print ("Días: "+str(30-start_date.day+end_date.day))
elif end_date.month==8:
	print ("Días: "+str(31-start_date.day+end_date.day))
elif end_date.month==9:
	print ("Días: "+str(31-start_date.day+end_date.day))
elif end_date.month==10:
	print ("Días: "+str(30-start_date.day+end_date.day))
elif end_date.month==11:
	print ("Días: "+str(31-start_date.day+end_date.day))
elif end_date.month==12:
	print ("Días: "+str(30-start_date.day+end_date.day))
elif end_date.month==1:
	print ("Días: "+str(31-start_date.day+end_date.day))





from tkinter import * 

root = Tk() 
root.title("Liquidación por despido sin causa") 
root.resizable(1,1)
root.iconbitmap("32841.ico") 
root.geometry("1024x650") 
root.config(bg="black") 

miFrame = Frame() 
miFrame.config(width="1024", height="650") 
miFrame.config(bg="black") 
miFrame.config(bd="35") 
miFrame.config(cursor="hand2") 
miFrame.pack(fill="both", expand="True") 

miImagen = PhotoImage(file="imagen.liquidacion.gif")
Label(miFrame,image=miImagen).place(x=400, y=0) 

primer_label=Label(miFrame, text="Fecha de ingreso: ", bg="black",fg="white").grid(row=0, column=0, sticky="e", pady=2) #el sticky=e es para q su margen quede a la derecha(east)

cuadrotexto = Entry(miFrame)
cuadrotexto.grid(row=0, column=1, pady=2)
cuadrotexto.config(justify="center")

segundo_label=Label(miFrame, text="Fecha de egreso: ", bg="black",fg="white").grid(row=1, column=0, sticky="e", pady=2) #el padding te permite separar elementos. Agreangole al label lo siguiente:   ,padx/pady = numero. Se agrega igual que el sticky. Ej: ,padx=150

cuadrotexto2 = Entry(miFrame)
cuadrotexto2.grid(row=1, column=1, pady=2)
cuadrotexto2.config(justify="center")

tercer_label=Label(miFrame, text="Salario promedio: ", bg="black",fg="white").grid(row=2, column=0, sticky="e", pady=2)

cuadrotexto3 = Entry(miFrame)
cuadrotexto3.grid(row=2, column=1, pady=2)
cuadrotexto3.config(justify="center")

cuarto_label=Label(miFrame, text="MRMNH: ", bg="black",fg="white").grid(row=3, column=0, sticky="e", pady=2)

cuadrotexto4 = Entry(miFrame)
cuadrotexto4.grid(row=3, column=1, pady=2)
cuadrotexto4.config(justify="center")

quinto_label=Label(miFrame, text="Notas: ", bg="black",fg="white").grid(row=4, column=0, sticky="e", pady=2) #con esto creo un label para agregar notas

texto_nota = Text(miFrame, width="30", height="7")
texto_nota.grid(row=4, column=1, pady=2)

scroll_texto_nota = Scrollbar(miFrame, command=texto_nota.yview) # aca construyo un scroll bar para el label de nota. Le agrego el y para que se pueda scrollear de modo vertical.
scroll_texto_nota.grid(row=4, column=2, sticky = "nsew") # tiene que ser una columna mas para que aparezca al final. El sticky = nsew es para que el scroll tenga el mismo alto que el label de la nota
texto_nota.config(yscrollcommand=scroll_texto_nota.set) # esto es para que el scroll siga a la parte del texto en el label. sino no funciona correctamente.

root.mainloop()



from tkinter import * 

root = Tk() 
root.title("Liquidación por despido sin causa") 
root.resizable(1,1)
root.iconbitmap("32841.ico") 
root.geometry("1024x650") 
root.config(bg="black") 

miFrame = Frame() 
miFrame.config(width="1024", height="650") 
miFrame.config(bg="black") 
miFrame.config(bd="35") 
miFrame.config(cursor="hand2") 
miFrame.pack(fill="both", expand="True") 

mirespuesta=StringVar()#creo la funcion de misalario. Le decimoss que se trata de una cadena de caracteres
def codigo_boton1(): #creo la funcion para darle un programa al boton
    mirespuesta.set("Programa en construcción") #con el set le adjudico un valor a una variable

miImagen = PhotoImage(file="imagen.liquidacion.gif")
Label(miFrame,image=miImagen).place(x=400, y=0) 

primer_label=Label(miFrame, text="Fecha de ingreso: ", bg="black",fg="white").grid(row=0, column=0, sticky="e", pady=2) #el sticky=e es para q su margen quede a la derecha(east)

cuadrotexto = Entry(miFrame, textvariable=mirespuesta) #le agrego el textvariable para asociarla al boton y funcion del boton
cuadrotexto.grid(row=0, column=1, pady=2)
cuadrotexto.config(justify="center")

segundo_label=Label(miFrame, text="Fecha de egreso: ", bg="black",fg="white").grid(row=1, column=0, sticky="e", pady=2) #el padding te permite separar elementos. Agreangole al label lo siguiente:   ,padx/pady = numero. Se agrega igual que el sticky. Ej: ,padx=150

cuadrotexto2 = Entry(miFrame)
cuadrotexto2.grid(row=1, column=1, pady=2)
cuadrotexto2.config(justify="center")

tercer_label=Label(miFrame, text="Salario promedio: ", bg="black",fg="white").grid(row=2, column=0, sticky="e", pady=2)

cuadrotexto3 = Entry(miFrame) #ajuste esta parte para q este cuadro este asociado al valor de la variable q asigna el boton de imprimir liquidacion
cuadrotexto3.grid(row=2, column=1, pady=2)
cuadrotexto3.config(justify="center")

cuarto_label=Label(miFrame, text="MRMNH: ", bg="black",fg="white").grid(row=3, column=0, sticky="e", pady=2)

cuadrotexto4 = Entry(miFrame)
cuadrotexto4.grid(row=3, column=1, pady=2)
cuadrotexto4.config(justify="center")

quinto_label=Label(miFrame, text="Notas: ", bg="black",fg="white").grid(row=4, column=0, sticky="e", pady=2) #con esto creo un label para agregar notas

texto_nota = Text(miFrame, width="30", height="7")
texto_nota.grid(row=4, column=1, pady=2)

scroll_texto_nota = Scrollbar(miFrame, command=texto_nota.yview) # aca construyo un scroll bar para el label de nota. Le agrego el y para que se pueda scrollear de modo vertical.
scroll_texto_nota.grid(row=4, column=2, sticky = "nsew") # tiene que ser una columna mas para que aparezca al final. El sticky = nsew es para que el scroll tenga el mismo alto que el label de la nota
texto_nota.config(yscrollcommand=scroll_texto_nota.set) # esto es para que el scroll siga a la parte del texto en el label. sino no funciona correctamente.

boton1 = Button(miFrame, text="Ejecutar liquidación", command=codigo_boton1) #esto es para crear un boton. El command es para darle una ejecucion al boton.
boton1.pack
boton1.grid(row=6, column=1, pady=2) 

root.mainloop()


#para crear una calculadora

from tkinter import * 

raiz = Tk() 

miFrame = Frame(raiz) 
miFrame.pack() 

# -----------------mi pantalla-------------------------

numeroPantalla=StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #el columnspawn es para que ocupe varias columnass sin desplazarte las columnas de los otros rows
pantalla.config(background = "black", fg="#03f943", justify = "right")

#  -------------------pulsaciones teclado-------------------------

def numeroPulsado():
    numeroPantalla.set(numeroPantalla.get() + "4") #para que se pueda acumular los 4. Se concatena.


# -------------------fila 1-------------------------

boton7=Button(miFrame, text="7", width =3)
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width =3)
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width =3)
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width =3)
botonDiv.grid(row=2, column=4)

# -------------------fila 2-------------------------

boton4=Button(miFrame, text="4", width =3, command=numeroPulsado)
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width =3)
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width =3)
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width =3)
botonMult.grid(row=3, column=4)

# -------------------fila 3-------------------------

boton1=Button(miFrame, text="1", width =3)
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width =3)
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width =3)
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width =3)
botonRest.grid(row=4, column=4)

# -------------------fila 4-------------------------

boton0=Button(miFrame, text="0", width =3)
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width =3)
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width =3)
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width =3)
botonSum.grid(row=5, column=4)

raiz.mainloop()




#para crear una calculadora

from tkinter import * #el Tkinter es el interface estandar para python

raiz = Tk() #Tk se refiere a tkinter

miFrame = Frame(raiz) # con esto creo el frame de la interfaz grafica
miFrame.pack() 

#----------- operacion---------------
# variable operacion que guarda la variable que quiere usar el usuario. Que te permite resetear la pantalla

operacion=""
resultado = 0

# -----------------mi pantalla-------------------------

#todo lo que se considera cuadro de texto, python lo va a tomar como texto, aun cuando sean numeros. Hay que decirle que se trata de un valor numerico. Por eso le agrego int
numeroPantalla=StringVar() #el stringvar es una clase que sirve para los Tk.
#numeroPantalla.set("0")#para que el primer numero que aparezca en la pantalla sea un 0

pantalla = Entry(miFrame, textvariable=numeroPantalla) #el text variable es porque al ser un stringVar, el string o valor de la descripcion va a ir cambiando
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #el columnspawn es para que ocupe varias columnass sin desplazarte las columnas de los otros rows
pantalla.config(background = "black", fg="#03f943", justify = "right")

#  -------------------pulsaciones teclado-------------------------

def numeroPulsado(num):

    global operacion

    if operacion != "": #es decir si se usa la operacion de suma, entonces en lugar de seguir concatenando a los numeros se borra lo anterior
        numeroPantalla.set(num) #el numero de pantalla pasa a ser el numero que insertaste cuando el numero anterior era nada. 
        operacion="" #luego el string vuelve a ser nada, para que se pueda rellenar de vuelta
    
    else: # si habia un numero antes, el numero de pantalla pasa a ser la suma entre el numero anterior y el numero nuevo q insertaste

        numeroPantalla.set(numeroPantalla.get() + num) #le asigna un valor nuevo al numero de pantalla que es la suma

#-------------------funcion suma-------------------
#aca creo el metodo para la variable operacion de suma. Simultaneamente a la operacion (funcion) de numeroPulsado, hay que ir calculando el resultado de las operaciones
def el_resultado():
    global resultado #el global es una funcion de tkinder. Sirve para llamar una variable para una funcion en particular.

    numeroPantalla.set(resultado + float(numeroPantalla.get())) #esto fija el valor del total en el numero de pantalla.

    resultado=0

def suma(num): #aca fijo la funcion para sumar
    global operacion
    global resultado

    resultado += float(num)   #todo lo que se considera cuadro de texto, python lo va a tomar como texto, aun cuando sean numeros. Hay que decirle que se trata de un valor numerico. Por eso le agrego int o float
    
    operacion="suma" # aca agarras la variable operacion y le asignas el valor que es el resultado de la funcion de suma

    numeroPantalla.set(resultado) #esto para que vaya sumando solo sin tener que poner resultado cuando agrego otra suma u operacion


# -------------------fila 1-------------------------

boton7=Button(miFrame, text="7", width =3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width =3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width =3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width =3)
botonDiv.grid(row=2, column=4)

# -------------------fila 2-------------------------

boton4=Button(miFrame, text="4", width =3, command=lambda:numeroPulsado("4")) # el lambda son funciones anonimas. para simplificar la sintaxiss en determinadas circunstancias. Aca sirve para q no se ejecute el comando solo y aparezca un 4 en la calculadora sin usarla/
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width =3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width =3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width =3)
botonMult.grid(row=3, column=4)

# -------------------fila 3-------------------------

boton1=Button(miFrame, text="1", width =3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width =3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width =3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width =3)
botonRest.grid(row=4, column=4)

# -------------------fila 4-------------------------

boton0=Button(miFrame, text="0", width =3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width =3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width =3, command=lambda: el_resultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width =3, command=lambda: suma(numeroPantalla.get())) #le agrego el lambda a este boton para que pueda usar la operacion suma
botonSum.grid(row=5, column=4)

raiz.mainloop()

#-------------- OPERADOR NOT------------------

nota = 3
aprobado = nota


from tkinter import * 
from tkinter import messagebox # llamo la herramienta para ventanas emergentes
from tkinter import filedialog # llamo este tipo de ventana emergente

root = Tk() 
root.title("Liquidación por despido sin causa") 
root.resizable(1,1)
root.iconbitmap("32841.ico") 
root.geometry("1024x650") 
root.config(bg="black") 

miFrame = Frame() 
miFrame.config(width="1024", height="650") 
miFrame.config(bg="black") 
miFrame.config(bd="35") 
miFrame.config(cursor="hand2") 
miFrame.pack(fill="both", expand="True") 

mirespuesta=StringVar()#creo la funcion de misalario. Le decimoss que se trata de una cadena de caracteres
def codigo_boton1(): #creo la funcion para darle un programa al boton
    mirespuesta.set("Programa en construcción") #con el set le adjudico un valor a una variable

# --------------- ventana emergente ------------------

def acerca_del_autor(): # esta es la funcion para la ventana emergente
    messagebox.showinfo("Autor", "Federico Irarrazaval \nAbogado \nCel: 1567887879 \nEmail: fedeirar@gmail.com")

def aviso_licencia(): # esta es la funcion para la ventana emergente
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salir(): # esta es la funcion para la ventana emergente
    #valor = messagebox.askquestion("Salir", "Desea salir de la aplicacion?") #el ask question hace que aparezca voton de si y no. Al apretar el boton se almacena el valor en la variable valor
        #if valor == "yes":
         #   root.destroy() # el destroy es para q se cierre el programa 
        valor = messagebox.askokcancel("Salir", "Desea salir de la aplicacion?") #ac es lo mismo que lo anterior, pero con aceptar y cancelar que guardan valores de True or False
        if valor == True:
            root.destroy() # el destroy es para q se cierre el programa 

def cerrar_documento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor == False: #el reintentar funciona con True y False tambien
        root.destroy()

#-------------- ventanas emergentes 2 ------------------

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*"))) # el primer parametro es el titulo. Esto nos va a devolver la ruta del archivo que queremos abrir. Por defecto busca en la carpeta documentos
    print(fichero) #con el initialdir le digo donde comenzar la busqueda. Podemos tambien especificar que tipo de archivo buscar con filetypes que te pide una tupla

Button (root, text = "Abrir fichero", command=abreFichero).pack() 

#----------------menu-------------------------
barraMenu=Menu(root) #con esto creo una barra de menu
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff = 0) #el tearoff es para sacarle las lineas que aparecen en el menu al principio
barraMenu.add_cascade(label="Archivo", menu=archivoMenu) #le decimos que este elemento que pertecenece a la barramenu debe tener ese texto
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #es para agregar separados entre los submenu
archivoMenu.add_command(label="Cerrar", command = cerrar_documento)
archivoMenu.add_command(label="Salir", command = salir)

archivoEdicion=Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


archivoHerramientas=Menu(barraMenu)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

archivoAyuda=Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia", command = aviso_licencia)
archivoAyuda.add_command(label="Acerca del autor", command = acerca_del_autor) #le agrego el command para poder usar la funcion de la ventana emergente

#----------------imagen--------------------
miImagen = PhotoImage(file="imagen.liquidacion.gif")
Label(miFrame,image=miImagen).place(x=400, y=0) 

# ----------------- labels con cuadros de textos ---------------------
primer_label=Label(miFrame, text="Fecha de ingreso: ", bg="black",fg="white").grid(row=0, column=0, sticky="e", pady=2) #el sticky=e es para q su margen quede a la derecha(east)

cuadrotexto = Entry(miFrame, textvariable=mirespuesta)
cuadrotexto.grid(row=0, column=1, pady=2)
cuadrotexto.config(justify="center")

segundo_label=Label(miFrame, text="Fecha de egreso: ", bg="black",fg="white").grid(row=1, column=0, sticky="e", pady=2) #el padding te permite separar elementos. Agreangole al label lo siguiente:   ,padx/pady = numero. Se agrega igual que el sticky. Ej: ,padx=150

cuadrotexto2 = Entry(miFrame)
cuadrotexto2.grid(row=1, column=1, pady=2)
cuadrotexto2.config(justify="center")

tercer_label=Label(miFrame, text="Salario promedio: ", bg="black",fg="white").grid(row=2, column=0, sticky="e", pady=2)

cuadrotexto3 = Entry(miFrame)
cuadrotexto3.grid(row=2, column=1, pady=2)
cuadrotexto3.config(justify="center")

cuarto_label=Label(miFrame, text="MRMNH: ", bg="black",fg="white").grid(row=3, column=0, sticky="e", pady=2)

cuadrotexto4 = Entry(miFrame)
cuadrotexto4.grid(row=3, column=1, pady=2)
cuadrotexto4.config(justify="center")

quinto_label=Label(miFrame, text="Notas: ", bg="black",fg="white").grid(row=4, column=0, sticky="e", pady=2) #con esto creo un label para agregar notas

texto_nota = Text(miFrame, width="30", height="7")
texto_nota.grid(row=4, column=1, pady=2)

scroll_texto_nota = Scrollbar(miFrame, command=texto_nota.yview) # aca construyo un scroll bar para el label de nota. Le agrego el y para que se pueda scrollear de modo vertical.
scroll_texto_nota.grid(row=4, column=2, sticky = "nsew") # tiene que ser una columna mas para que aparezca al final. El sticky = nsew es para que el scroll tenga el mismo alto que el label de la nota
texto_nota.config(yscrollcommand=scroll_texto_nota.set) # esto es para que el scroll siga a la parte del texto en el label. sino no funciona correctamente.

# ---------- boton -------------
boton1 = Button(miFrame, text="Ejecutar liquidación", command=codigo_boton1) #esto es para crear un boton. El command es para darle una ejecucion al boton.
boton1.pack
boton1.grid(row=8, column=1, pady=2) 

# --------------- otros botones --------------------
indemnizaciones = IntVar() #el IntVar es para darle funcionalidad
proporcionales = IntVar()
multas = IntVar()

# ---------------- label relacionado a los otros botones --------------
textoFinal=Label(miFrame)
textoFinal.grid(row=11, column=1, pady=2)

def opcion_indemnizaciones():
    opcion="" #en principio se inicia esta variable a una cadena vacia
    if (indemnizaciones.get() == 1): #el 1 aca equivale a True
        opcion += "indemnizaciones"
    if (proporcionales.get() == 1): #el 1 aca equivale a True. Basicamente le digo si el boton de proporcionales esta con ok sumarle ...
        opcion += "proporcionales"
    if (multas.get() == 1): #el 1 aca equivale a True
        opcion += "multas"
  
    textoFinal.config(text=opcion) #aca le digo que al label de textofinal le ponga como texto la opcion que podria llegar a 3

# --------------- otros botones --------------------
Checkbutton(root, text = "Indemnizaciones por despido sin causa", variable=indemnizaciones, onvalue=1, offvalue = 0, command=opcion_indemnizaciones).pack() #asocio al boton con la variable de indemnizacion. Le tengo que agregar el onvaluepara indcarle que cuando el check este selccionado el valor en la variable playa va a ser igual a 1

Checkbutton(root, text = "Proporcionales por extincion del contrato de trabajo", variable=proporcionales, onvalue=1, offvalue = 0, command=opcion_indemnizaciones).pack()

Checkbutton(root, text = "Multas e indemnizaciones adicionales", variable=multas, onvalue=1, offvalue = 0, command=opcion_indemnizaciones).pack()

root.mainloop()

"""
escribir un programa q muestre por pantalla el resultado de la siguiente operacion matematica

la suma de a + b 
dividido 
el producto de a por c elevado al cuadrado"""

a = 10
b = 5
c = 2

print("El resultado es: ", (a+b) / (a*c)**2) 

# dado 2 numeros, por ejemplo a = 15 y b=11  determinar con un mensaje de respuesta del programa cual es mayor y en el caso de q sean iguales indicar en un mensaje q son iguales. Evaluar los 3 casos

a=17
b=16

if a>b:
    print ("A es mayor a B")

elif a<b:
    print("B es mayor a A")

elif a == b:
    print("A es igual a B")


#evaluar rangos de variable a. 


a = 32

if a >= 1 and a <= 10:
    print("Esta en el rango de 1 a 10")
elif a >= 11 and a <= 20:
    print("esta entre 11 y 20")
elif a >= 21 and a <= 30:
    print("esta entre 21 y 30")
else:
    print("no esta en ningun rango")


nota_1 = int(input("Ingresa primer nota de 1 a 10: "))
nota_2 = int(input("Ingresa segunda nota de 1 a 10: "))
nota_3 = int(input("Ingresa tercera nota de 1 a 10: "))

nota_final = (nota_1 + nota_2 + nota_3)/3

if nota_final >= 4:
    print("Aprobado")
elif nota_final < 4:
    print("Segui participando")



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

#Matriz: basicamente son listas anidadas donde podemos decir cada lista representa una fila y los elementos dentro una columna

matriz = [[1,2,3],["Hola", "Chau"],[True, False]]

print(type(matriz))

print(matriz [2][0]) #para hacerle print primero eligo numero de lista y despues numero de elemento cada uno entre corchete sin coma

matriz[2].append(5) #para agregar , etc algo a la lista le especifico en el nombre de lista en que numero de lista laburar

print(matriz)


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


import random #LIBRERIAS: una de sus funciones es la de dado. Te tira un numero aleatorio. Libreriass se pueden buscar en documentacion de python https://docs.python.org/3/library/index.html

while True:
    print("Menu")
    print("1 - Tirar dado")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        dado = random.randint(1,6)
        print("El valor del dado es: ", dado)
    elif opcion == 2:
        print("fin del programa")
        break
    else:
        print("Opcion no valida")



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


#ventana
ventana = tk.Tk()
ventana.title("PImprimir numeros")
ventana.config(width="1024", height="650") 

#botones
boton1=tk.Button(text="Imprimir numeros", command = imprimir_numero)
boton1.place(x= 10, y=30)

boton1=tk.Button(text="saludar", command=saludar) #el command es para q el boton use una funcion
boton1.place(x= 50, y=70)

#cuadros de texto

caja1 = tk.Entry()
caja1.place(x= 100, y=140)

#etiqueta
etiqueta_nombre = tk.Label(text= "Ponele")
etiqueta_nombre.place(x= 200, y=140)



ventana.mainloop()