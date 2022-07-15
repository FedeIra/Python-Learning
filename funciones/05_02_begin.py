def one():
    print("you fool")

def two():
    print("saaaay whaaat?")

def three():
    print("neeeeeee")

one()
two()
three()




# FUNCION DE MINIMO Y MAXIMO SIN USAR MIN() Y MAX()
def max(lista):
    lista_1.sort()
    numero = lista_1[-1]
    return numero
   

def min(lista):
    lista_1.sort()
    numero = lista_1[0]
    return numero

def operador(funcion, lista):
    return funcion(lista_1)
    
lista_1 = [1,2,4,2,1,-5,888,6,3]

print("max: ", operador(max, lista_1))
print("min: ", operador(min, lista_1))

####### otra formula#########

def max(lista):
    maximo = lista[0]
    for numero in lista:
        if maximo < numero:
            maximo = numero
    return maximo
        
def min(lista):
    minimo = lista[0]
    for numero in lista:
        if minimo > numero:
            minimo = numero
    return minimo

def operador(funcion, lista):
    return funcion(lista_1)
    
lista_1 = [1,2,4,2,1,-5,888,6,3]

print("max: ", operador(max, lista_1))
print("min: ", operador(min, lista_1))

paises = { 
    "ar": "Argentina", 
    "br": "Brazil", 
    "cl": "Chile", 
    "us":"Estados Unidos" 
    }

codigo = input("Ingresa codigo de tu pais: ")   

try: 
    print(paises[codigo])
    if codigo == "salir":
        print("Se termino el programa")
        
except KeyError:
    print("Ingresaste pais q no esta en el diccionario")
    codigo = input("Ingresa codigo de tu pais: ")
