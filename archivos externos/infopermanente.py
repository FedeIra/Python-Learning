import pickle

#importamos pickle y creamos una clase

class Persona:
    def __init__(self, nombre,genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("se ha creado una persona nueva con el nobre de ", self.nombre)
    
    def __str__(self): #la funcion str convierte en cadena de texto la info. de un objeto
        return "{} {} {}".format(self.nombre, self.genero, self.edad) #con format le aplico un formato

#estas personas se van generando y guardando en un fichero externo

class ListaPersonas: #creo una clase para guardar las listas de personas
    personas = [] #aca creo la lista

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+") #ahora quiero grabar en un fichero externo esta lista de personas. Hay varias formas.aca creo un fichero externo. Este es el fichero que se va a almancenar en nuestro sistema de archivos y que ira guardando info.
        listaDePersonas.seek(0) #aca desplazo el cursos al inicio, es decir 0 segun lo q explico abajo

        try:
            self.personas=pickle.load(listaDePersonas) #ahora tengo q hacer el volcado de info para leerla. Tengo que almacenarla. Tengo que utiklizar la libreria pickle con el metodo load y que nos cargue lista de personas
            print("Se cargaron {} personas del fichero externo".format(len(self.personas))) #para que nos diga cuantas personas se cargaron.
        except:
            print("el fichero esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

#ahora tengo que hacer que el cursos vuelva al comienzo del archivo, de lo contrario cuando quiera leer la info. lo hara desde el cursor en adelante y entonces va a estar al final del archivo y no nos lee nada

#el fichero se puede abrir de diversoso modos. Le pongo ab+ para poder agregar info. y hacer otras funciones en modo binario

    def agregarPersonas (self,p): #aca creo el primer metodo de esta lista
        self.personas.append(p) #el metodo append es para agregar la persona a la lista
        self.guardarPersonasEnFicheroExterno() #guarda la persona en el fichero externo
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb") #en wb para que pueda escribir info
        pickle.dump(self.personas, listaDePersonas) #el dump es para que pueda hacer volcado de informacion
        listaDePersonas.close()
        del (listaDePersonas)

    def mostrarInfoFichero(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()

persona = Persona("Antonio", "Masculino", "49")
miLista.agregarPersonas(persona)
miLista.mostrarInfoFichero()



from io import open 

archivo_texto = open("archivo.txt", "r")

print(archivo_texto.read()) 

archivo_texto.seek(0) #esto te trae el cursor a 0

print(archivo_texto.read()) 

# te lo lee desde el principio, donde esta el cursor o puntero. Se puede desplazar el cursor o puntero por defecto.
#se puede mover el punto con seek(5)



from io import open 

archivo_texto = open("archivo.txt", "r")

archivo_texto.seek(11) 

print(archivo_texto.read(11)) #en read puedo pedir hasta que punto del cursor leer

print(archivo_texto.read()) #en este lee a partir de donde esta el puntero, es decir, 11

archivo_texto.seek(len(archivo_texto.read())/2) #esto te lee la mitad del archivo al dividir el len en dos

archivo_texto.seek(len(archivo_texto.readline())) #con esto lees las lineas que pidas

print(archivo_texto.read())



from io import open 

archivo_texto = open("archivo.txt", "r+") #la r+ es para lectura y escritura

#archivo_texto.write("comienzo del texto")

#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines();

lista_texto[1] = "Esta linea ha sido incluida desde el exterio \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()



#la serializacion es guardar en un archivo externo un diccionario, objeto, etcs
#para eso necesitas la bibioletca pickle. para hacer un fichado de datos binario externo

import pickle

lista_nombres = ["Pedro" , "Ana", "Maria", "Isabel"]

fichero_binario = open("lista_nombres", "wb") #el w es por write y el b por binaria

pickle.dump(lista_nombres, fichero_binario) #crea un archivo con nuestra lista en codigo binario

fichero_binario.close()

del(fichero_binario)


import pickle

fichero = open("lista_nombres", "rb") #la r es para leer, y la b para leer binaria

lista = pickle.load(fichero)

print(lista) # con esto llame la lista en codigo binario


#hay que trabajar con la librearia tkinter. Hay otras como WxPython, PyQT y PyGTK. Tkinter viene instalado por defecto y es un punte entre Python y la libreria TCL/Tk.
# son ventanas con las que interactuamos los usuarios. Nos permite interactuar con el programa. Son los intermediarios entre los programas y los usuarios.open(
# se lo denomina GUI 
# si no esta instalado entonces hay q instalarlo con la siguiente instruccion: $sudo apt-getinstall python3-tk. Esto en la consola del sistema
# primero hay que construir la raiz o la ventana, luego un frama dentro de la ventana como organizador o aglutinador de elementos. Dentro del frame hay botones o menus desplegables o widgets. Un fram es considerado por python tambien como widgets

#ahora aprendemos a construir la raiz


from tkinter import * #asi importamos todas las clases de la libreria tkinder

raiz = Tk() #aca creo una raiz

raiz.title("Liquidación por despido sin causa") #con esto le pongo titulo

raiz.resizable(1,1) #este metodo admite ancho y alto. El primer es ancho y el segundo el alto. con esto hago que no se pueda redimensionar ademas. El 0 equivale a false, es decir no se puede redimensionar. El 1 equivale a true, se puede redimensionar

raiz.iconbitmap("32841.ico") #con esto aplico la imagen

#raiz.geometry("650x350") #con esto puedo aumentar el tamanio de la ventana. Se puede sacar ya que su tamanio se adapta solo al tamanio del frame.

raiz.config(bg="black") #para cambiar cosas de la ventana, ejemplo color de fondo (bg que es background)

#ahora vemos como crear un frame

miFrame = Frame() #creo un frame.

miFrame.config(width="650", height="350") #El tamanio del frame es algo fijo y anclado que no se adapta, salvo que lo cambie

miFrame.config(bg="red") #para poder usar esto hay que darle tamanio antes al frame. 

miFrame.pack(side="right") #para empaquetar al frame a la raiz

raiz.mainloop() #esto es para que la ventana este activa mientras el usuario usa el programa. Debe estar en un bucle infinito o continua ejecucion. Es lo que hace el mainloop
#la instruccion de mainloop debe estar siempre al final

#para cambiar el icono tenes q tener en tu ordenador localizado en el directorio donde esta la aplicacion un archivo con extension .ico. El tamanio no debe ser muy grande. se puedo convertir imagenes a .ico

#para abrir aplicacion grafica sin consola detras, hay que cambiar la extension del archivo de .py a .pyw  . Aca solo abre la aplicacion grafica


#ahora vemos como crear un frame

miFrame = Frame() #creo un frame.

miFrame.config(width="650", height="350") #El tamanio del frame es algo fijo y anclado que no se adapta, salvo que lo cambie

miFrame.config(bg="black") #para poder usar esto hay que darle tamanio antes al frame. 

miFrame.config(relief="groove") #con esto cambio el tipo de frame

miFrame.config(bd="35") #con esto aumento el tamanio del borde

miFrame.config(cursor="hand2") #con esto puedo cambiar el tipo de cursor

miFrame.pack(fill="both", expand="True") #para empaquetar al frame a la raiz. El anchor maneja puntos cadinales, North, sout... etc pero solo con la primer letra... n, s, e, w. Tambien se le puede poner fill y both para que se expanda junto a la raiz. hay que agregarle el true al final

raiz.mainloop() #esto es para que la ventana este activa mientras el usuario usa el programa. Debe estar en un bucle infinito o continua ejecucion. Es lo que hace el mainloop
#la instruccion de mainloop debe estar siempre al final

#para cambiar el icono tenes q tener en tu ordenador localizado en el directorio donde esta la aplicacion un archivo con extension .ico. El tamanio no debe ser muy grande. se puedo convertir imagenes a .ico

#para abrir aplicacion grafica sin consola detras, hay que cambiar la extension del archivo de .py a .pyw  . Aca solo abre la aplicacion grafica
