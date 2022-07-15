
import pickle

fichero = open("lista_nombres", "rb") # 

lista = pickle.load(fichero) #load para cargar la informacion que esta en fichero

print(lista) #te imprime la lista q estaba en codigo binario y ahora la rescatamos en codigo normal