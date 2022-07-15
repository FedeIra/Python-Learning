personas = ["Rosa 55 ingeniera", "Juan 25 Programador", "Tomas 30 Profesor"]

resultados = []

for persona in personas:
    lista_nombre = persona.split(" ")

    diccionario = {}
  
    diccionario["nombre"] = lista_nombre[0]
    diccionario["edad"] = lista_nombre[1]
    diccionario["profesion"] = lista_nombre[2]

    resultados.append(diccionario)

print(resultados)


# Liquidación = open(r"C:\Users\fedei\OneDrive\Escritorio\Programacion\Python\Liquidación.txt", "r+")

diccionario = {"Javier" : 21, "Pablo" : 17, "Raul" : 24}

alumnos_menores = []

for name in diccionario:
    if diccionario[name] <= 18:
        alumnos_menores.append(f"{name} {diccionario[name]}")
  

with open(r"C:\Users\fedei\OneDrive\Escritorio\Programacion\Python\Liquidación.txt", "w") as names_alumnos: 
    for alumno in alumnos_menores:
        names_alumnos.write(f"{alumno}\n")




#Con base al siguiente diccionario, filtrar a los alumnos que no sean mayores de edad y almacenarlos en un archivo de texto llamado, alumnos.txt.

diccionario = {“Javier”: 21, “Pablo”: 17, “Raul”: 17, “Esteban”: 16, “Milagros”: 19, “Santiago”: 20}


 



#Con base al archivo que acabamos de crear se nos pide que lo leamos y almacenemos el contenido en un diccionario con el mismo formato que utilizamos para crear “alumnos.txt”.


 

#Pablo

   

    diccionario = {"Javier": 21, "Pablo": 17, "Raul": 17, "Esteban": 16, "Milagros": 19, "Santiago": 20}

listado=[]

for key in diccionario:

    if diccionario[key] < 18:

        listado.append([key,diccionario[key]])

 

with open("alumnos.txt","a") as archivo:

    for elemento in listado:

        archivo.write(f"\n Alumno: {elemento[0]} -- Edad: {elemento[1]}")

 

# claudio

     

diccionario =  {“Javier”: 21, “Pablo”: 17, “Raul”: 17, “Esteban”: 16, “Milagros”: 19, “Santiago”: 20}

mayor = 18

menores=open("archivo.txt" , "w")

while (diccionario<mayor):

 

#leandro

 

diccionario = {"Javier": 21, "Pablo": 17, "Raul": 17, "Esteban": 16, "Milagros": 19, "Santiago": 20}

 

alumnos_menores = []

 

for name in diccionario:

    if diccionario[name] <= 18:

        alumnos_menores.append(name)

 

with open("archivo.txt","w") as Names_alumnos:

    for n in alumnos_menores:

        Names_alumnos.write(f"{n}" + "\n")

       

        

        

# Claudio

     

diccionario =  {"Javier": 21, "Pablo": 17, "Raul": 17, "Esteban": 16, "Milagros": 19, "Santiago": 20}

alumnos_menores=[]

 

 

for clave in diccionario:

    if diccionario[clave] < 18:

        alumnos_menores.append(diccionario[clave])

 

with open() as object:

    pass

 

#Pablo segunda parte

diccionario = {"Javier": 21, "Pablo": 17, "Raul": 17, "Esteban": 16, "Milagros": 19, "Santiago": 20}

listado=[]

for key in diccionario:

    if diccionario[key] < 18:

        listado.append([key,diccionario[key]])

 

with open("alumnos.txt","a") as archivo:

   for elemento in listado:

        archivo.write(f"\n Alumno: {elemento[0]} -- Edad: {elemento[1]}")

 

with open("alumnos.txt","r") as lectura:

    contenido=lectura.read()

 

listado2=contenido.split()

 

dicc={}

 

for n in range(0,len(listado2)+1,5):

    try:

        dicc[listado2[n+1]]=listado2[n+4]

    except:

        pass

 

print(dicc)

 

 

# Resolución 1

diccionario = {"Javier": 21, "Pablo": 17, "Raul": 17, "Esteban": 16, "Milagros": 19, "Santiago": 20}

 

alumnos_menores = []

 

for name in diccionario:

    if diccionario[name] <= 18:

        alumnos_menores.append(f"{name} {diccionario[name]}")

 

with open("archivo.txt","w") as names_alumnos:

    for alumno in alumnos_menores:

        names_alumnos.write(f"{alumno}\n")

 

 

# Resolución 2

variable = open("archivo.txt", "r")

resultado = variable.readlines()

diccionario = {}

 

for persona in resultado:

    nombre, edad = persona.split(" ")

    edad = int(edad.strip())

    diccionario[nombre] = edad


print(diccionario)