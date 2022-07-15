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

# EJERCICIO

email = input("introduce tu email")

if email.count("@") == 2 or email.endswith("@") or email.startswith("@"):
    print("direccion incorrecta")
    
else:
    email.count("@") < 2
    print("direccion correcta")