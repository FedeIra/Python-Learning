
from tkinter import *

raiz = Tk() 
raiz.title("Ventana de pruebas") 
#raiz.resizable(1,0) 
raiz.iconbitmap("EjemploDeIcono.ico")
raiz.geometry("650x350") 
raiz.config(bg="blue") 

miFrame=Frame() #creo el frame pero hay que empaquetarlo. Es decir, meterlo dentro de la raiz
#miFrame.pack(side="right", anchor="n")#con esto lo empaqueto. El side right es para que se quede anclado a la derecha cuando lo redimensiono. solo lo puedo hacer de un lado
#para anclarlo de otro lado adicional puedo usar el anchor q usa los puntos cardinales
miFrame.pack(fill="x") #con fil hago q al redimensionarlo quede anclado horizontalmente. 
#miFrame.pack(fill="y", expand="True") # Verticalmente seria y, pero tengo que agregarle el expand true. En fill puedo poner tambien both para q llene todo
miFrame.config(bg="red", width=650, height=250)
miFrame.config(relief="groove", bd=35)#puedo cambiaar el borde con el relief. Le agrego el bd por borde
miFrame.config(cursor="pirate") #puedo cambiar el cursor o mouse

#todo lo q aplicamos al frame puedo aplicarlo a la raiz

raiz.mainloop() 