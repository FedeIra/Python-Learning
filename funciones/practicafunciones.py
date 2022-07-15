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
