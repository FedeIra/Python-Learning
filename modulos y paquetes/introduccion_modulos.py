
# modulo es un archivo con extension .py. Tambien hay con extesion .pyc (python compilado) o archivo escrito en C para CPython.. Posee su propio espacio de nombres y puede contener variables, funciones, clases e incluso otros modulos

#modulariazcion y reutilizacion. Modularizacion es dividir el codigo en modulos, es decir, pequenias partes. La reutilizacion es reutilizar programas usadas en distintos modulos en lugar de volver a crearla


import funciones_matematicas  # el modulo se crea haciendo un arhcivo con .py. Para usar el modulo primero hay que importarlo "import _______"

funciones_matematicas.sumar(7,5) #para usar el modulo lo tenes que llamar poniendolo al principio seguido de punto y con la funcion

funciones_matematicas.restar(7,5)

funciones_matematicas.multiplicar(7,5)

#para no tener q llamar cada vez la funcion se puede hacer con el from

from funciones_matematicas import restar, sumar, multiplicar #con el from llamo el modulo y con el import la funcion del modulo que quiera

restar(4,3) #ahora no tengo la necesidad de invocar cada vez q la uso al modulo

sumar(3,2)

multiplicar (4,2)

from funciones_matematicas import * #con el asterisco llamo todo lo que se encuentra dentro del modulo. A veces no me conviene llamar TODO el modulo por un tema de memoria dentro del programa.

multiplicar (4,3)



from modulo_vehiculos import *

miCoche = Vehiculos("Mazda", "2020")

miCoche.estado() #si muevo el archivo modulo que estoy importando a otra carpeta, y lo intento usar de vuelta tira error. Lo buca en el mismo directoria y si no esta ahi lo busca en syspath.

#hay forma de reutilizar el codigo encuentre donde se encuentre a traves de la funcion paquete. Modulos que esten relacionados o tengan un mismo objetivo lo organizas por paquetes.

#para crear un paquete, guardo un archivo con el nombre de __init__py en una carpeta. Desde ahi puedo guardar distintos codigos de py y quedan en el paquete


from calculos.calculos_generales import dividir # en el primero llamo al paquete, en el segundo al modulo dentro del paquete y en el tercero a la funcion dentro del modulo

dividir(2,2)


from calculos.calculos_generales import dividir, potencia # en el primero llamo al paquete, en el segundo al modulo dentro del paquete y en el tercero a la funcion dentro del modulo

dividir(2,2)

potencia(4,6)

# si hubiera clases puedo importarlas desde la midma forma, sino puedo usar asterisco para utilizar la funcio q queramos

from calculos.calculos_generales import *

restar(4,2)

# se puede crear subpaquetes. Les voy pegando el archivo con __init__.py para hacerlos subpaquetes


