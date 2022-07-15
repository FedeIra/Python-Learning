"""
POLIMORFISMO: cuando un objeto cambia de forma dependiendo del contexto en q se lo utiliza
Un mismo objeto puede cambiar de forma y por lo tanto cambia de comportamiento.

"""

class Heroe():

    def grito_guerra(self):
        print("Por el honor y por la gloria!")

class Rey():
    
    def grito_guerra(self):
        print("Por el oro!")

class Villano():

    def grito_guerra(self):
        print("Muerte y Sangre!")



def categoria_personaje(categoria): #Aca pasa el polimorfismo. Se transforma en un objeto de cierto tipo y llama al comportamiento de esa clase
    categoria.grito_guerra()

#AlejandroMagno = Rey()
#AlejandroMagno = Villano()
AlejandroMagno = Heroe()

categoria_personaje(AlejandroMagno)