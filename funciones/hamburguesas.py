class Hamburguesas_Nacho():
    def __init__(self):
    
        self.calidad = "una poronga"
        self.tamanio = "mas chica q la de nacho, si es q eso es posible"

    def estado(self):
        print("Calidad:", self.calidad, "\nTamanio:", self.tamanio) 

hamburguesa_de_nacho = Hamburguesas_Nacho()

class hamburguesas_Fede(): 
    def __init__(self):

        self.calidad = "mil veces mejores que las de nacho"
        self.tamanio = "mas grande q la de fede, si es q es posible"

    def estado(self):
        print("Calidad:", self.calidad, "\nTamanio", self.tamanio) 

hamburguesa_de_fede = hamburguesas_Fede()
    
print("que onda las hamburguesas de nacho??")
hamburguesa_de_nacho.estado()

print("y las de fede?")
hamburguesa_de_fede.estado()
