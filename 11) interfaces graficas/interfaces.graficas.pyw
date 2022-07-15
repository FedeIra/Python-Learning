#hay que trabajar con la librearia tkinter. Hay otras como WxPython, PyQT y PyGTK. Tkinter viene instalado por defecto y es un punte entre Python y la libreria TCL/Tk.
# son ventanas con las que interactuamos los usuarios. Nos permite interactuar con el programa. Son los intermediarios entre los programas y los usuarios.open(
# se lo denomina GUI 
# si no esta instalado entonces hay q instalarlo con la siguiente instruccion: $sudo apt-getinstall python3-tk. Esto en la consola del sistema
# primero hay que construir la raiz o la ventana, luego un frama dentro de la ventana como organizador o aglutinador de elementos. Dentro del frame hay botones o menus desplegables o widgets. Un fram es considerado por python tambien como widgets

#ahora aprendemos a construir la raiz
#para buscar distintos tkinders y raices, etc, en google lo buscas con standard library tkinder python segundo enlace

from tkinter import * #asi importamos todas las clases de la libreria tkinder

raiz = Tk() #aca creo una raiz

raiz.title("Liquidación por despido") #con esto le pongo titulo

raiz.resizable(1,1) #este metodo admite ancho y alto. El primer es ancho y el segundo el alto. con esto hago que no se pueda redimensionar ademas. El 0 equivale a false, es decir no se puede redimensionar. El 1 equivale a true, se puede redimensionar

raiz.iconbitmap("imagen.liquidacion.ico.ico") #con esto aplico la imagen

raiz.geometry("650x350") #con esto puedo aumentar el tamanio de la ventana

raiz.config(bg="blue") #para cambiar cosas de la ventana, ejemplo color de fondo (bg que es background)

raiz.mainloop() #esto es para que la ventana este activa mientras el usuario usa el programa. Debe estar en un bucle infinito o continua ejecucion. Es lo que hace el mainloop
#la instruccion de mainloop debe estar siempre al final

#para cambiar el icono tenes q tener en tu ordenador localizado en el directorio donde esta la aplicacion un archivo con extension .ico. El tamanio no debe ser muy grande. se puedo convertir imagenes a .ico

#para abrir aplicacion grafica sin consola detras, hay que cambiar la extension del archivo de .py a .pyw  . Aca solo abre la aplicacion grafica