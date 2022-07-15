
from tkinter import *

root = Tk() 

miFrame=Frame(root, width=500, height=400) 
miFrame.pack()

#miImagen=PhotoImage(file="mouse.gif")
#Image(miFrame, text="Hola Alumnos de Python", fg="red", font=("Calibri", 18)).place(x=100, y=200) 
#miLabel=Label(miFrame, text="Hola Alumnos de Python")
#miLabel.place(x=100, y=200) #si queremos q respete el tamanio de la raiz debemos sustituir el pack por place. Nos deja decir donde va a estar. Le indicamos donde
#lo anterior puedo reemplazarlo por la linea de abajo
Label(miFrame, text="Hola Alumnos de Python", fg="red", font=("Calibri", 18)).place(x=100, y=200) #fg es para color de letra. El font es para tipo de letra

#tkinter trabajab con imagenes png y gif. Hay que tener en la carpeta una imagen

root.mainloop() 