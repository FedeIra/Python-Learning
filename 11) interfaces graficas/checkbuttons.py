from tkinter import*

root = Tk()
root.title("Ejemplo")

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa").pack() #con esto creo los botones
Checkbutton(frame, text="Hola").pack()
Checkbutton(frame, text="Chau").pack()

miImagen = PhotoImage(file="imagen.liquidacion.gif")
Label(root,image=miImagen).pack()



root.mainloop()