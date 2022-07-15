from tkinter import * 

raiz = Tk() 

miFrame = Frame(raiz) 
miFrame.pack() 

# -----------------mi pantalla-------------------------

pantalla = Entry(miFrame)
pantalla.grid(row=1, column=1, padx=10, pady=10)
pantalla.config(background = "black", fg="#03f943", justify = "right")

# -------------------boton-------------------------

boton7=Button(miFrame, text="7", width =3)
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width =3)
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width =3)
boton9.grid(row=2, column=3)
botonMult=Button(miFrame, text="x", width =3)
botonMult.grid(row=2, column=4)


root.mainloop()