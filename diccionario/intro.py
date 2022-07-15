# DICCIONARIOS

diccionario = {'nombre' : 'Carlos', 'edad' : '22', 'cursos' : ['Python', 'Java', 'CJ']}

print(diccionario)

for key in diccionario:
    print(key, ":", diccionario[key])

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


# diccionario
diccionarios = {
    'valor': 1,
    'valor_2' : 2,

}

elemento = diccionarios["valor"]

diccionarios = {
0 : {
"nombre" : "ezequiel",
"curso"  : "Python programming"
}
}

curso = diccionarios ["Ezequiel"]["curso"]

longitud_de_alumnos = len(diccionarios)

del diccionarios[1]
del elemento # el del puede eliminar incluso variables

roles = {

"admin" : 1111,  #le asigno a admin el valor de 1111
"profesor"  : 2222,
"alumno"  : 3333
}

roles["admin"] # con esto invoco el valor de admin almacenado en el diccionario
rol = input("Que rol desempenia?")

if rol != "admin" and "profesor" and "alumno":
    print("ingresaste un roll equivocado")

password = int(input("Ingresa contrasenia: "))

if roles == roles[rol]:
    print("rol y contrasenia correcta")
else:
    ("Contrasenia incorrecta")


curso_1 = input("Ingrese un curso: ")
curso_2 = input("Ingrese un curso: ")
curso_3 = input("Ingrese un curso: ")
curso_4 = input("Ingrese un curso: ")
curso_5 = input("Ingrese un curso: ")

lista = [curso_1, curso_2, curso_3, curso_4, curso_5]
