"""
CLASES

Clase: modelo donde se redactan las caracteristicas comunes de un grupo de objetos

Instancia: objeto o ejemplar pertenciente a una clase

Modularizacion: es normal q una aplicacion este formada por varias clases. Cada uno de los modulos funcionan de forma independiente. 
Permite reutilizar trozos de codigos de un prorgrama en otro.

Encapsulacion: el funcionamiento interno de un objeto esta protegido del exterior. el funcionamiento de una clase concreta de tu programa nada sabe sobre las otras clases. 
Sin embargo, las clases estan conectadas para funcionar en equipo. Se usa para proteger una propiedad desde fuera para q no la cambien. Tambien se puede encapsular metodos o comportamientos.

Metodos de acceso: se puede acceder a ciertos metodos de una clases q estan encapsuladas.

Nomenclatura del punto: los objetos tienen un nombre, pero para acceder a su propiedad hay q ponerle punto y luego la propiedad. Ejemplo> miCoche.color = "rojo"
Para acceder al comportamiento es lo mismo. Ejemplo: miCoche.arranca()

El comportamiento viene determinado por los metodo

"""
import random

class Hoplita():
    #Estas caracteristicas son las de fabrica o estado inicial, lo que se llama el constructor. Luego tal vez quiero cambiarlas. 
    def __init__(self): #este es el contractor de tu clase. El constructor tiene el nombre "init" por estado inicial. Luego a las propiedad agregarles self.
    #aca van las propiedades. Son 4
        self.__arma="lanza" 
        self.__escudo="hoplon" #la encapsulamos pq no queremos q la cambien de afuera a traves de los dos guiones bajo. Es solo accesible desde dentro de la propia clase
        self.fuerza=2
        self.__shieldwall=False

    #ahora creamos el metodo. Un metodo es una funcion q pertenece a la clase. No es lo mismo que una funcion perse.
    #Tenemos dos comportamientos (funciones)
    def posicion(self, modo): # El parametro self hace referencia al propio objeto perteneciente a la clase.
        self.__shieldwall = modo

        if(self.__shieldwall):
            chequeo=self.__chequeo_companions()

        if(self.__shieldwall and chequeo): # esto es igual a poner if ___ : True, no hace falta ponerlo. el chequeo es para q vea si es true la funcion de chequeo companions
            return "El hoplita esta en shieldwall"
        elif(self.__shieldwall and chequeo==False):
            return "No es posible hacer shieldwall! No hay brother in arms"
        else:
            return "El hoplita no esta en posicion defensiva"

    def estado(self): #se pone self porque se refiere al propio objeto, es decir es una funcion para si mismo, self. Se le puede agregar parametros como cualquier funcion
       print("El hoplita tiene lo siguiente: arma: ", self.__arma, ", escudo:", self.__escudo, " y un nivel de fuerza:", self.fuerza) #con el self me refiere al objeto al que aplique la funcion. 

    def __chequeo_companions(self): #lo encapsulo para q no se pueda acceder a este metodo desde afuera de la clase. Queda restringido a un uso interno
        print("chequeando brother in arms")
        self.escudo = "ok"
        self.companieros = "ok"

        if(self.escudo == "ok" and self.companieros == "ok"):
            return True
        else:
            return False

#Hay un solo objeto
miHoplita = Hoplita() #aca creo mi primer objeto (hoplita). Es instanciar una clase. Crear un ejemplar.
#miHoplita.__escudo="tower shield" #esto no funciona pq encapsulamos a la propiedad escudo

miHoplita.estado()
print(miHoplita.posicion(True)) #con esta funcion lo ponemos en shieldwall al objeto perteneciente a la clase

print("--------- A continuacion, creamos el segundo objeto -----------------")

miHoplita2=Hoplita() #creo un segundo objeto
miHoplita2.fuerza = random.randint(1,3) #aca cambio la fuerza pidiendo un numero random para eso lo importe al inicio
miHoplita2.estado() #no hay q ponerle print pq la funcion ya imprime
print(miHoplita2.posicion(False)) #hay q ponerle print pq la funcion no imprime


