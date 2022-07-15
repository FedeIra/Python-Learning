from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar() #con esto le decimos que esta variable se trata de una cadena de caracteres

cuadroNombre = Entry(miFrame, textvariable=minombre) # con el textvariable hacemos que este cuadro este asociado a la variable minombre
cuadroNombre.grid(row=0, column=1) 
cuadroNombre.config(fg="red", justify="center")

nombreLabel=Label(miFrame, text="Nombre") 
nombreLabel.grid(row=0, column=0, sticky="e", padx=150, pady=30) 

cuadroPass = Entry(miFrame) 
cuadroPass.grid(row=3, column=0) 
cuadroPass.config(show="*")

comentariosLabel=Label(miFrame, text="Comentarios") 
comentariosLabel.grid(row=3, column=3, sticky="e")

textocomentario = Text(miFrame, width=16,height=5) #con esto creo un cuadro donde se puede escribir
textocomentario.grid(row=3, column=4, sticky="e")

scrollVert=Scrollbar(miFrame,command=textocomentario.yview) #con esto le decimos q va a ser un scroll bar del textocomentario
scrollVert.grid(row=3,column=5, sticky="nsw") #tiene que ir al costado de la columna del textocomentario. Con el nsw hace q se ajuste al tamanio del cuadro de comentarios

textocomentario.config(yscrollcommand=scrollVert.set) #esto es para q el scroll siga por donde estas escribiendo y no se quede en el medio o al principio

def codigoBoton():
    minombre.set("Juan")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton) #el command es para q funciona una funcion q vamos a construir

#para obtener la info de un cuadro de texto usamos la funcion get

botonEnvio.pack()

raiz.mainloop()