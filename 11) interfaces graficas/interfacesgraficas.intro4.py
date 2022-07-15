from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame) #entry por entrada para escribir
cuadroNombre.grid(row=0, column=1) #con el grid puedo agregar row y column. Arranca a contar desde 0
#cuadroTexto.place(x=100, y=100)
#cuadroTexto.pack() el pack se saca cuando le indico un lugar (place)
cuadroNombre.config(fg="red", justify="center")#el justify es para q se escriba en el centro del frame. Se puede poner right o left tambien

nombreLabel=Label(miFrame, text="Nombre") 
#nombreLabel.place(x=100, y=100) #te lo pone pegada al x y y del cuadro texto. Uno empuja al otro. Pero no es lo recomendable.
#nombreLabel.place(x=100, y=100)
nombreLabel.grid(row=0, column=0, sticky="e", padx=150, pady=30) #automaticamente tiene una alineacion central. Con sitcky lo puedo alinear segun puntos cardinales
#el pady (vertical) y padx (horizontal) te permite separar los elementos, ej> cuadro de textos. El padding es la distancia entre elementos por los 4 lados

cuadroPass = Entry(miFrame) #entry por entrada para escribir
cuadroPass.grid(row=3, column=0) #con el grid puedo agregar row y column. Arranca a contar desde 0
cuadroPass.config(show="*")#con esto cambiamos el caracter de las letras con lo q queramos. cuanod vaya a base de datos va con lo q se escribio, no asterizcos

raiz.mainloop()