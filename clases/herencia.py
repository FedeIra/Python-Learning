# HERENCIA 
# #las clases se pueden representar por jerarquias. La primera es clase padre o super clase.
# la clase s2 seria subclase o padre de las siguiente clases
#la utilidad es re utilizar un codigo. A la hora de elaborar un programa llegasa  crear programas similares. Por ejemplo, con el programa de los coches, crear objetos de tipo camion, lanchas, motos, etc.
#para crear herencia tenes q pensar q caracteristcas en comun van a tener los objetos dentro de la clase, tambien los comportamientos

class Vehiculos():
    def __init__(self, marca, modelo):
    
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frene = False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frene = True

    def estado(self):
        marca = "a determinar"
        modelo = "a determinar"
        print("Marca:", self.marca, "\nModelo", self.modelo, "\nEn Marcha", self.enmarcha, "\nAcelerando", self.acelera, "\nFrenando", self.frene) #la /n hace un salto de linea en pantalla

class Moto(Vehiculos): #aca es cuando creamos una nueva clase "moto", que hereda de (Vehiculos)
    pass #es palabra reservada para no construir nada sobre esta clase

miMoto = Moto("Honda" , "CBR")

miMoto.estado()




class Vehiculos():
    def __init__(self, marca, modelo):
    
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frene = False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frene = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo", self.modelo, "\nEn Marcha", self.enmarcha, "\nAcelerando", self.acelera, "\nFrenando", self.frene) 

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"

class Moto(Vehiculos): 
    hcaballito = ""

    def caballito(self): # agrego un nuevo metodo o comportamiento a los otros 5 de la clase padre
        self.hcaballito = "voy haciendo el caballito"

    def estado(self): #aunq estoy usando el mismo comportamiento de la clase padre, el nuevo metodo de la clase hija la reemplaza para esta subclase
        print("Marca:", self.marca, "\nModelo", self.modelo, "\nEn Marcha", self.enmarcha, "\nAcelerando", self.acelera, "\nFrenando", self.frene, "\n", self.hcaballito) 

class VElectricos(): #esto seria una clase independiente
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


miMoto = Moto("Honda" , "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.estado()

class Quad(Moto):
    pass

micuatri = Quad("cuatri", "super")

micuatri.estado()

print(miFurgoneta.carga(True))


class BicicletaElectrica(Vehiculos, VElectricos): #Herencia multiple: hereda de dos clases o mas, separando las clases con una coma. Hereda todos los metodos y propiedades. Utiliza los metodos del primero si tienen metodos con el mismo nombre
    pass

mibici = BicicletaElectrica() # cuando hay herencia multiple se le da preferencia a la primer herencia q indicas. Esto es importante para los argumentos que tiene la clase. Por eso lo dejamos sin argumentos.




#Clase herencia: super() y isistance()
#la funcion super llama al metodo padre (sirve para cuando una propiedad pertenece a dos clases con metodos distintos y queremos aplicar ambos metodos)

class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion_persona(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.lugar_residencia)

class Empleado(Persona): #al ponerle Persona le decimos que hereda de persona
    def __init__(self, salario, antiguedad):
        super().__init__("Antonio", 55, "Espania") #esta llamando al metodo init de la clase padre
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion_empleado(self):
        print("Salario:", self.salario, "\nAntiguedad:", self.antiguedad)

Antonio = Empleado(10000, 10)

Antonio.descripcion_persona()

Antonio.descripcion_empleado()




#Clase herencia: super() y isistance()
#la funcion super llama al metodo padre (sirve para cuando una propiedad pertenece a dos clases con metodos distintos y queremos aplicar ambos metodos)
#principio de susitucion: aplicar los terminos de "es siempre un/a". Un objeto de la subclase sera siempre un objeto de la clase padre. Un empleado sera siempre una persona, no viceversa.
#hay una funcion issitance() para decirte a que clase pertenece

class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.lugar_residencia)

class Empleado(Persona): #al ponerle Persona le decimos que hereda de persona
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #esta llamando al metodo init de la clase padre
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion() #aca con el super llamo a la funcion descripcion del metodo padre
        print("\nSalario:", self.salario, "\nAntiguedad:", self.antiguedad)

Antonio = Empleado (10000, 10, "Antonio", 14, "Roosevelt")

Antonio.descripcion()

print(isinstance(Antonio, Empleado)) #al usar isinstance, poniendo el objeto y la clase, te dice si es cierto que pertenece a esa clase

print(isinstance(Antonio, Persona)) #tambien es verdad

class hola(): #invento clase para probar el falso de un isinstance
    pass

print(isinstance(Antonio, hola)) #al usar isinstance, poniendo el objeto y la clase, te dice si es cierto que pertenece a esa clase. En este caso me tira false porque Antonio no pertenece a la subclase hola


#POLIMORFISMO: un objeto puede cambiar de forma dependiendo del contexto q se lo use.

class Coche():
    def desplazamiento(self):
        print("me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("me desplazo utilizando 6 ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo) # aca llamo polimorfismo pasandole por parametro el objeto creado dentro de la clase camion. Por eso al aplicar esta funcion me llama a su vez la funcion de desplazamiento creado dentro de
