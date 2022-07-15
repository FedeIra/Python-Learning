class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    def descripcion(self):
        print("Nombre:", self.nombre,
        "\nEdad:", self.edad,
        "\nLugar de residencia:", self.lugar_residencia)

class Empleado(Persona): # de esta forma hereda las propiedades de persona
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) # esta llamando al metodo init de la clase padre. Le estamos pasando los datos de Antonio.
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion() #Se puede usar super para usar la funcion de la superclase tambien
        print("Salario:", self.salario,
        "\nAntiguedad:", self.antiguedad)


Antonio = Persona("Antonio", 55, "Espania")
Antonio.descripcion()

Fede = Empleado(1500, 6, "Fede", 55, "Argentina")
Fede.descripcion()

#Principio de sustitucion: aplicar los terminos es "es siempre un/a. Un objeto de la subclase siempre sera un objeto de la superclase. Al revez no se da"
#En este caso siempre un empleado va a ser una persona. PAra eso esta el isinstance(). Devuelve true si es cierto q pertnece a una clase en concreto y false si no

print(isinstance(Fede, Persona)) #Aca es true pq Fede es una persona ademas de ser un empleado
print(isinstance(Antonio, Empleado))# Aca es false pq Antonio es una persona, pero no un empleado.

#Ambos tienen la superclase, pero no necesariamente la subclase