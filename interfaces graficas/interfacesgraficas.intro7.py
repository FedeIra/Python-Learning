#CHECK BUTTOM. el check buttom es cuadrado y te permite seleccionar varios. PAra preguntas con respuestas multiples

from tkinter import*

root = Tk()
root.title("Ejemplo")

hechicero = IntVar()
mago = IntVar()
brujo = IntVar()

foto=PhotoImage(file="small.png")
Label(root,image=foto, height=600, width=600).pack()

def opcionesclase():
    opcionEscogida=""

    if(hechicero.get()==1): # el 1 es por True. De lo contrario es false, es decir 0
        opcionEscogida+=" Hechicero"
    
    if(mago.get()==1):
        opcionEscogida+=" Mago"

    if(brujo.get()==1):
        opcionEscogida+=" Brujo"
    
    textoFinal.config(text=opcionEscogida)

frame=Frame(root).pack()
Label(frame, text="Elige clase:", width=50).pack()

Checkbutton(frame, text="Hechicero", variable=hechicero, onvalue=1, offvalue=0, command=opcionesclase).pack() #con onvalue le decimos que cuando el check este seleccionado el valor de la variable va a ser igual a uno
Checkbutton(frame, text="Mago", variable=mago, onvalue=1, offvalue=0, command=opcionesclase).pack()
Checkbutton(frame, text="Brujo", variable=brujo, onvalue=1, offvalue=0, command=opcionesclase).pack()

textoFinal=Label(frame)
textoFinal.pack()
 
root.mainloop()