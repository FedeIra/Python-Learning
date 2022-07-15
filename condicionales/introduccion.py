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
