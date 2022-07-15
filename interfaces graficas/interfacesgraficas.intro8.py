#MENUS

from tkinter import*
from tkinter import messagebox # esto es para poder usar ventanas emergentes

root = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Juan", "Procesar de textos version 2018")

def avisoLicencia():
    messagebox.showwarning("Licnecia", "Licencia producto de Fede")


def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "Deseas salir de la aplicacion_") #los bottones de askquestions devuelve valores
    valor=messagebox.askokcancel("Cancelar", "Deseas cancelar_")

    #if valor == "yes":
    if valor == True:    
        root.destroy() #para salir del programa

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reiintentar", "No es posible cerrar. documento bloqueado")
    
    if valor==False:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0) #especificamos a q menu pertenece. Con el tearoff saco la barra inicial q aparece en el submenu
archivoMenu.add_command(label="Nuevo") #con esto creo submenus
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #le agrego una barra que separa los submenu
archivoMenu.add_command(label="cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="copiar")
archivoEdicion.add_command(label="cortar")
archivoEdicion.add_command(label="pegar")

archivoHerramientas=Menu(barraMenu)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command = infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()