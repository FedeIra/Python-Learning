class Coche():  #debe ser con mayuscula el nombre de la clase
    largoChasis = 250 #estoy estableciendo propiedades
    anchoChasis = 120
    ruedas = 4
    enmarcha = False 
    color = "rojo"

# para establecer un comportamiento para metodo usas def. Un metodo  es una funcion especial q pertenece a la clase q estas creando mientras que una funcion no pertenece a ninguna clase
    def arrancar(self): #este comportamiento cambia la propiedad enmarcha
        self.enmarcha = True 

    def estado(self): #el self te lo obliga a poner python. Agrego otra funcion para que me confirme el estado del auto. Si esta en marcha o no
        if (self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"
#con lo anterior creamos una clase. A continuacion, creamos un objeto

miCoche = Coche() #le tenes que asignar la clase con Coche(). Es INSTANCIAR (o ejemplejarizar) una clase

print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene:", miCoche.ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes

miCoche.arrancar() #con esto llamo la funcion de arrancar, y el coche para de estar a enmarcha a arrancar

print(miCoche.estado())





class Coche():  #debe ser con mayuscula el nombre de la clase

    def __init__(self): #con esto define que es un contructor. es decir, que las propiedades de abajo van a ser el estado inicial de los objetos que pertenezcan a la clase coche. El constructor tiene siempre el nombre init, que significa estado inicial
        self.largoChasis = 250 #estoy estableciendo propiedades. Estas caracteristicas comunes son el estado inicial de los objetos pertenecientes a esta clase. el self. al principio es para decir que queremos que sean propiedades del estado inicial de los objetos
        self.anchoChasis = 120
        self.__ruedas = 4 #con el doble guion bajo encapsulo esta propiedad para q no pueda accederse y modificarse desde fuera, pero si es posible desde dentro de la propia clase. cada vez q utilices la variable ruedas hay que agregarle el doble guion bajo. solo se puede modificar desde una funcion dentro de la clase como las funciones de estado, cambio de color y arrancar.
        self.enmarcha = False # es decir, en principio, los objetos que pertenecen a esta clase no tienen la propiedad de estar en marcha
        self.color = "rojo"

# para establecer un comportamiento para metodo usas def. Un metodo es una funcion especial q pertenece a la clase q estas creando mientras que una funcion no pertenece a ninguna clase
    def arrancar(self, arrancamos): #Cuando haces una funcion para una clase, le tenes que agregar un parametro self que es el parametro por defecto. este comportamiento cambia la propiedad enmarcha. le agrgamos un parametro "arrancamos"
        self.enmarcha = arrancamos #el self.en marcha le agregamos el self para llamar a la propiedad de la case antes definida

        if(self.enmarcha):
             return "el coche esta en marcha"
        else:
            return "el coche esta parado"
    
    def cambio_de_color(self): #le tengo que agregar un parametro. Aparte recibe el parametro por defecto que es self
        self.color = "azul"
        print("pediste cambio de color a azul")
       
    def estado(self): #el self te lo obliga a poner python. Agrego otra funcion para que me confirme el estado del auto. Si esta en marcha o no
        print("el coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis, "y es de color", self.color)

#con lo anterior creamos una clase. A continuacion, creamos un objeto

miCoche = Coche() #para incorporar el objeto a la clase le tenes que asignar antes la clase con Coche(). Es INSTANCIAR (o ejemplejarizar) una clase

print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene:", miCoche.__ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes
print("el color del coche es:", miCoche.color)

print(miCoche.arrancar(True)) #con esto llamo la funcion de arrancar, y el coche para de estar a enmarcha a arrancar al ponerle True. Ademas al agarrar la funcion me dice si esta en marcha o parado

miCoche.cambio_de_color() # aca no le tengo q poner imprimir porque en la funcion en lugar de return tiene print

miCoche.estado() #aca llamo la segunda funcion de def estado(self) y por lo tanto me imprime las propiedad del coche

print("----- a continuacion creamos el segundo objeto ----------")

miCoche2 = Coche() #aca creo un segundo objeto q lo asigno a la clase coche. El objeto es una instancia de la clase (objeto = instancia)
print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene:", miCoche.__ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes
print(miCoche.arrancar(False)) # aca llamo la funcion de arrancar, pero al ponerle False no arranca y me retorna que esta parado

miCoche2.estado() #aca llamo a la funcion estado y me dice las propiedades del objeto. Como tiene print la funcion no necesita que le ponga print al invocar la funcion

print("----- a continuacion creamos el tercer objeto ----------")

cocheFede = Coche() #creo una nuevo objeto para la clase de coche
cocheFede.cambio_de_color()
cocheFede.arrancar(True)
cocheFede.estado()


print("----- a continuacion creamos el cuarto objeto ----------")

cochedelpueblo = Coche()
cochedelpueblo.__ruedas = 2 #esto es para cambiar propiedades mas facilmente. 
print(cochedelpueblo.estado(), "aguante el auto del pueblo!")

#ahora bien, esta mal que tenga 2 ruedas. Para evitar que se modifieque una propiedad desde fuera como este caso puedo encapsular esta propiedad. 




class Coche():  #debe ser con mayuscula el nombre de la clase

    def __init__(self): #con esto define que es un contructor. es decir, que las propiedades de abajo van a ser el estado inicial de los objetos que pertenezcan a la clase coche. El constructor tiene siempre el nombre init, que significa estado inicial
        self.largoChasis = 250 #estoy estableciendo propiedades. Estas caracteristicas comunes son el estado inicial de los objetos pertenecientes a esta clase. el self. al principio es para decir que queremos que sean propiedades del estado inicial de los objetos
        self.anchoChasis = 120
        self.__ruedas = 4 #con el doble guion bajo encapsulo esta propiedad para q no pueda accederse y modificarse desde fuera, pero si es posible desde dentro de la propia clase. cada vez q utilices la variable ruedas hay que agregarle el doble guion bajo. solo se puede modificar desde una funcion dentro de la clase como las funciones de estado, cambio de color y arrancar.
        self.enmarcha = False # es decir, en principio, los objetos que pertenecen a esta clase no tienen la propiedad de estar en marcha
        self.color = "rojo"

# para establecer un comportamiento para metodo usas def. Un metodo es una funcion especial q pertenece a la clase q estas creando mientras que una funcion no pertenece a ninguna clase
    def arrancar(self, arrancamos): #Cuando haces una funcion para una clase, le tenes que agregar un parametro self que es el parametro por defecto. este comportamiento cambia la propiedad enmarcha. le agrgamos un parametro "arrancamos"
        self.enmarcha = arrancamos #el self.en marcha le agregamos el self para llamar a la propiedad de la case antes definida

        if(self.enmarcha):
             return "el coche esta en marcha"
        else:
            return "el coche esta parado"
    
    def cambio_de_color(self): #le tengo que agregar un parametro. Aparte recibe el parametro por defecto que es self
        self.color = "azul"
        print("pediste cambio de color a azul")
       
    def estado(self): #el self te lo obliga a poner python. Agrego otra funcion para que me confirme el estado del auto. Si esta en marcha o no
        print("el coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis, "y es de color", self.color)

#con lo anterior creamos una clase. A continuacion, creamos un objeto

miCoche = Coche() #para incorporar el objeto a la clase le tenes que asignar antes la clase con Coche(). Es INSTANCIAR (o ejemplejarizar) una clase

print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene:", miCoche.__ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes
print("el color del coche es:", miCoche.color)

print(miCoche.arrancar(True)) #con esto llamo la funcion de arrancar, y el coche para de estar a enmarcha a arrancar al ponerle True. Ademas al agarrar la funcion me dice si esta en marcha o parado

miCoche.cambio_de_color() # aca no le tengo q poner imprimir porque en la funcion en lugar de return tiene print

miCoche.estado() #aca llamo la segunda funcion de def estado(self) y por lo tanto me imprime las propiedad del coche

print("----- a continuacion creamos el segundo objeto ----------")

miCoche2 = Coche() #aca creo un segundo objeto q lo asigno a la clase coche. El objeto es una instancia de la clase (objeto = instancia)
print("el largo del coche es: ", miCoche2.largoChasis)
print("el coche tiene:", miCoche2.__ruedas, "ruedas") #llamo a las propiedades del objeto dentro de la clase definida antes
print(miCoche.arrancar(False)) # aca llamo la funcion de arrancar, pero al ponerle False no arranca y me retorna que esta parado

miCoche2.estado() #aca llamo a la funcion estado y me dice las propiedades del objeto. Como tiene print la funcion no necesita que le ponga print al invocar la funcion

print("----- a continuacion creamos el tercer objeto ----------")

cocheFede = Coche() #creo una nuevo objeto para la clase de coche
cocheFede.cambio_de_color()
cocheFede.arrancar(True)
cocheFede.estado()


print("----- a continuacion creamos el cuarto objeto ----------")

cochedelpueblo = Coche()
cochedelpueblo.__ruedas = 2 #esto es para cambiar propiedades mas facilmente. 
print(cochedelpueblo.estado(), "aguante el auto del pueblo!")

#ahora bien, esta mal que tenga 2 ruedas. Para evitar que se modifieque una propiedad desde fuera como este caso puedo encapsular esta propiedad. 


class Coche():  

    def __init__(self): 
        self.largoChasis = 250 
        self.anchoChasis = 120
        self.ruedas = 4 
        self.__enmarcha = False
      
    def arrancar(self, arrancamos): 
        self.__enmarcha = arrancamos 

        if(self.__enmarcha): 
            chequeo = self.__chequeo_interno() # Aca le pongo chequeo es igual chequeo interno para el proximo if

        if(self.__enmarcha and chequeo): # aca la agregams el and chequeo para que arranque solo si la funcion de chequeo interno es True.
             return "el coche esta en marcha"
        
        elif(self.__enmarcha and chequeo == False):
            return "algo ha ido mal en el chequeo. no podemos arrancar"

        else:
            return "el coche esta parado"
       
    def estado(self):
        print("el coche tiene ", self.ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

    def __chequeo_interno(self): # le agrego otro comportamiento que es un cheque general. Pero lo quiero q se haga antes de arrancar. Al ponerle el __ encapsulamos el metodo. Esto para que no lo puedas llamar desde afuero sino desde una funcion de la clase. La llamamos desde afuera cuando decimos: print(miCoche.__chequeo_interno())
        print("realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False 

miCoche = Coche() 

print(miCoche.arrancar(True)) 

miCoche.estado() 

print("----- a continuacion creamos el segundo objeto ----------")

miCoche2 = Coche()

print(miCoche.arrancar(False)) 

miCoche2.estado() 
