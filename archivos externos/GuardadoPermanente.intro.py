"""
Guardado permanente en ficheros externos:

Utilizar un fichero para guardar info. incluso desde otros programas. Para guardar info. de modo permanente.

"""

import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de:", self.nombre)
    
    def __str__(self): #la def str convierte en cadena de texto la info de un objeto
        return "{} {} {}".format(self.nombre, self.genero,self.edad) #el format es para aplicarle un formato

class ListaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno","ab+") #el ab+ es para agregar informacion binaria
        listaDePersonas.seek(0) #para que el cursor vuelva al inicio y luego cuando queramos leerlo lo lea todo

        try: #q intente realizar la instruccion. esto es para evitar q te tire error en la primera pq no va a haber nadie
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p) #creo una persona p q sera agregada a la lista de personas. Y asi sucesivamente
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La Informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()

persona = Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(persona)

persona2 = Persona("Antonio", "Masculino", 33)
miLista.agregarPersonas(persona2)

persona3 = Persona("Ana", "Femenino", 19)
miLista.agregarPersonas(persona3)

miLista.mostrarInfoFicheroExterno()
#miLista.mostrarPersonas()