from cgitb import text
from tkinter import*
from tkinter import filedialog

root = Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="abrir", initialdir="C:/Users/fedei/OneDrive/Escritorio/Programacion/Python/", 
                                                      filetypes=(("Fotos", "*.png"), ("Ficheros de texto", "*.txt"), ("todos los ficheros", "*.*")))
    #te devuelve la ruta de lo que queres abrir. Por defecto, te busca en la carpeta de documentos
    print(fichero)                                             #le puedo indicar donde busque por defecto con initialdir

Button(root, text="Abrir Fichero", command=abreFichero).pack()

root.mainloop()