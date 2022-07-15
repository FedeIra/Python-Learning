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

from funciones_matematicas import * #con el asterisco llamo todo lo que se encuentra dentro del modulo

multiplicar (4,3)
