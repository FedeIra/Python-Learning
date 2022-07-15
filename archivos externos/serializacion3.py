import pickle

class Hoplita():
     
    def __init__(self, fuerza, defensa): 

        self.__arma="lanza" 
        self.__escudo="hoplon" 
        self.__defensa = defensa
        self.__fuerza= fuerza
        #self.__shieldwall=False

    """def posicion(self, modo): 
        self.__shieldwall = modo

        if(self.__shieldwall):
            chequeo=self.__chequeo_companions()

        if(self.__shieldwall and chequeo): 
            return "El hoplita esta en shieldwall"
        elif(self.__shieldwall and chequeo==False):
            return "No es posible hacer shieldwall! No hay brother in arms"
        else:
            return "El hoplita no esta en posicion defensiva"
"""
    def estado(self): 
       print("El hoplita tiene lo siguiente: arma: ", self.__arma, ", escudo:", self.__escudo, "  un nivel de fuerza:", self.__fuerza, "y un nivel de defensa: ", self.__defensa) 
"""
    def __chequeo_companions(self):
        print("chequeando brother in arms")
        self.escudo = "ok"
        self.companieros = "ok"

        if(self.escudo == "ok" and self.companieros == "ok"):
            return True
        else:
            return False
"""
Aquiles = Hoplita(3,3)

Hector = Hoplita(2,2)

Alcibiades = Hoplita(1,2)

hoplitas = [Aquiles, Hector, Alcibiades]

fichero = open("Los Hoplitas", "wb")

pickle.dump(hoplitas, fichero) #en el primer agregamos lo q queremos escribir, en el segundo donde. El dump se refiere a tirar info.

fichero.close()
del (fichero) # esto es para borrar la info. del fichero de la memoria

ficheroApertura = open("Los Hoplitas","rb")

misHoplitas = pickle.load(ficheroApertura)

ficheroApertura.close()

for i in misHoplitas:
    print(i.estado())