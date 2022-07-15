"""
Se trabaja con tkinder
interfaz grafica es una intermediacion entre el prograa y el usuario. Es una ventana q en su interior tiene diferentes elementos.


"""

#RAIZ

from tkinter import *

raiz = Tk() 

raiz.title("Ventana de pruebas") #le pongo titulo a la venta

raiz.resizable(1,0) #le cambio el fram ancho (with) y alto (heigh). Son booleanos, true (1) y false (0)

raiz.iconbitmap("EjemploDeIcono.ico")

raiz.geometry("650x350") #para alargar la ventana

#para cambiarle el icono tenes q tener una imagen .ico

raiz.config(bg="blue") #bg por background

#si quiero q se me abra el archivo sin la consola detras, tengo que cambiarle el nombre al archivo de .py a .pyw

raiz.mainloop() #esto siempre tiene q estar al final 