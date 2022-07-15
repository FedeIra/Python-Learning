from io import open

archivo_texto = open("ejemplo_archivo_externo","r") 

print(archivo_texto.read()) #reproduce exactmente lo escrito en el archivo texto. El tema es q cuando lo lee el puntero vuelve al inicio.
#si esccribimos entonces se escribe al principio. Esto se puede modificar.



archivo_texto.close()