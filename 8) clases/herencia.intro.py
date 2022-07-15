"""
HERENCIA

Se trata de trasladar el comportamiento a codigo de programacion. Hay una cadena o jerarquia de herencia. 
La primer clase es la clase padre o superclase.
La segunda clase es la clase dos> clase padre o subclase. A su vez es superclase de la clase 3, 4 y 5.. etc.

La principal utildiad es la reutilizacion de codigo. Al hacer programas complejos haces clases similares. 

Primero tenes q tener idea de q caracteristicas en comun van a tener los objetos. 
Tambien q comportamientos van a tener.

Se trata de construir una clase para varios objetos.

"""

#primero creo la superclase

from re import S


class Soldados():

    def __init__(self, ataque, defensa):
        self.ataque=ataque
        self.defensa=defensa
        self.agressive_stance=False
        self.defensive_stance=False
        self.march_stance=False 

    def marchar(self):
        self.march_stance = True

    def atacar(self):
        self.agressive_stance=True

    def defender(self):
        self.defensive_stance=True
    
    def estado(self):
        print ("Ataque:", self.ataque, 
        "\nDefensa:", self.defensa, 
        "\nEn Marcha:",self.march_stance, 
        "\nPosicion Defensiva:", self.defensive_stance,
        "\nPosicion de Ataque:", self.agressive_stance) #el /n es para salto de linea

#Creamos una segunda clase
class Legionario(Soldados):
    def arrojar_jabalinas(self, arrojar):
        self.jabalinas = arrojar
        if(self.jabalinas):
            return "Volley"
        else:
            return "Wait"

#Creamos una nueva superclase
class arqueros(Soldados):
    def __init__(self, ataque, defensa):

        super().__init__(ataque, defensa)
        self.ataque = 3
        self.defensa = 0
    
    def lluvia_de_flechas(self, lluvia):
        self.lluvia = lluvia
        if(self.lluvia):
            return "LLuvia de flechas"
        else:
            return "Aguarden"
    
    def estado(self):
        super().estado() 
        
class catafracta(arqueros, Soldados): #aca creo una subclase que hereda de dos clases distintas, soldados y arqueros pq tiene comport. y propiedades de las dos
    #cuando hay herencia multiple se la de preferencia a la primer clase q le pongas. Usa el metodo init de la primer clase (arqueros)
    pass

#Ahora creamos una clase que hereda la clase Soldados. La nueva clase hereda las propiedades (el constructor) y comportamiento de la super clase
class Hoplitas(Soldados):
    muro_escudos = ""

    def shieldwall(self):   #este es un metodo propio de la sublcase. Ademas tiene los comportamientos o metodos de la superclase
        self.muro_escudos = "Shieldwall!"

    def estado(self): #esto es una sobreescritura de metodos.
        print ("Ataque:", self.ataque, 
        "\nDefensa:", self.defensa, 
        "\nEn Marcha:",self.march_stance, 
        "\nPosicion Defensiva:", self.defensive_stance,
        "\nPosicion de Ataque:", self.agressive_stance,
        "\n", self.muro_escudos) #hago copy/paste del estado de la superclase y le agrego. Siempre tiene prioridad el nuevo estado o comportamiento si son los mismos

# Creo un objeto de la subclase hoplita
Hoplita_normal = Hoplitas(1,3)
Hoplita_normal.shieldwall()
Hoplita_normal.estado()

# Creo un objeto de la subclase Legionario
Legionario_normal = Legionario(2,2)
Legionario_normal.atacar()
Legionario_normal.defender()
Legionario_normal.estado()
print(Legionario_normal.arrojar_jabalinas(True))

#Creo un objeto para la subclase de catafracta q hereda de dos superclases

Catafracta_normal = catafracta(3,5) #Por usar el metodo init de arqueros, no le puedo agregar aca en el parentesis.
print(Catafracta_normal.lluvia_de_flechas(True))
Catafracta_normal.estado()
#Funcion super. Llama al metodo de la clase padre o la @superclase.