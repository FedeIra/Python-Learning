from tkinter import*

root = Tk()

VarOpcion=IntVar() #aca le digo q la variable va a ser un numero intVar en lugar de script q seria ScriptVar.

Label(root, text = "Genero: ").pack()

def imprimir():
    #print(VarOpcion.get()) #resctaamos el valor del radiobuton pulsada
    if VarOpcion.get()==1:
        etiqueta.config(text="has elegido masculino")
    else:
        etiqueta.config(text="has elegido femenino")

Radiobutton(root, text="Masculino", variable=VarOpcion, value=1, command=imprimir).pack() #el radiobuttom es redonde y te permite seleccionar uno solo
Radiobutton(root, text="Femenino", variable=VarOpcion, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()