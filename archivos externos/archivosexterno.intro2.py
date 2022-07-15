from io import open

archivo_texto = open("ejemplo_archivo_externo","r") #le pongo en modo read

#texto = archivo_texto.read() #creo una variable para luego darle print. Tambien esta el metodo readlines q lee la info linea a linea y la almacena en una lista.
#la lista es mejor para manipular la informacion

lineas_texto = archivo_texto.readlines()

archivo_texto.close()

#print(texto)

print(lineas_texto)
print(lineas_texto[0]) #a partir de aca puedo jugar con listas for
