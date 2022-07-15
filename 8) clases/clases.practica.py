class Desarrollador(): # los nombres de las clases van em mayuscula
    def __init__(self, nombre, apellido, rol, salario_neto): # constructor. El init son metodos especiales. Permite crear los atributos. Es parecido a una funcion
        #el self va a llamar a la clase misma.
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.salario_neto = salario_neto #estas son las caracteristicas

    def __estimar_horas_proyecto(self): #agregamos un metodo
        pass #el dos guiones bajo corresponde a un metodo privado por eso no te lo imprime

    def presupuestar_proyecto(self, proyecto, costo_hora):
        horas_estimadas = self.__estimar_horas_proyectos(proyecto)
        return horas_estimadas * costo_hora

    def conocer_posicion(self):
        print(f"mi posicion es: {self.rol}")

desarrollador = Desarrollador("Ezequiel", "Ustar", "Programador", "10") #creamos una instancia

desarrollador.nombre = "Hola" #para modificar una de las propiedades

print(desarrollador)

class Analista():
    pass

class Junior(Desarrollador, Analista): #heredan el comportamiento de la clase desarrollador. se puede heredar de muchas clases
    def __init__(self, nombre, apellido, rol, salario_neto):
        #opcion 1
        Desarrollador.__init__(nombre, apellido, rol, salario_neto) # aca no necesitas el constructor self porque a los metodos no se les pasa
        #opcion 2
        super().__init__(nombre, apellido, rol, salario_neto) #es super class. te dice de la clase heredada, llevaba estos atributos. Hereda solo los atributos de la clase desarrollar con super class
        Analista.__init__()
        self.responsable_a_cargo = "Claudio" #le agrego funcionalidad extra

    def programar():
        pass

class SemiSenior(Desarrollador):
    def __init__(self, nombre, apellido, rol, salario_neto):
        Desarrollador.__init__(nombre, apellido, rol, salario_neto) # aca no necesitas el constructor self porque a los metodos no se les pasa
        self.junior_a_cargo = "Ezequiel"

    def programar():
        pass

class Senior(Desarrollador):
    def __init__(self, nombre, apellido, rol, salario_neto):
        Desarrollador.__init__(nombre, apellido, rol, salario_neto) # aca no necesitas el constructor self porque a los metodos no se les pasa
        self.junior_a_cargo = "Antonio"

    def programar():
        pass

ezequiel = Junior()
guido = SemiSenior() 
natalia = Senior()

#polimorfismo

ezequiel.programar()
guido.programar()
natalia.programar()

def programador_programa(programador):
    programador.programar()

#############################################################

class Persona(): 
    def __init__(self, nombre, apellido): 
        self.nombre = nombre
        self.apellido = apellido
    
    def nombre_completo(self):
        print(self.nombre, self.apellido)

class Estudiante(Persona):
        def __init__(self, nombre, apellido, edad, carrera):
            super().__init(nombre, apellido)
            self.edad = edad
            self.carrera = carrera
        
        def mostrar_carrera(self):
            print(self.carrera)

#######################################################################

class Persona2():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleanios(self):
        self.edad += 1

p = Persona()