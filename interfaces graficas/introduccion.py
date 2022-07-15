
#para crear una calculadora

from tkinter import * #el Tkinter es el interface estandar para python

raiz = Tk() #Tk se refiere a tkinter

miFrame = Frame(raiz) # con esto creo el frame de la interfaz grafica
miFrame.pack() 

#----------- operacion---------------
# variable operacion que guarda la variable que quiere usar el usuario. Que te permite resetear la pantalla

operacion=""
resultado = 0

# -----------------mi pantalla-------------------------

#todo lo que se considera cuadro de texto, python lo va a tomar como texto, aun cuando sean numeros. Hay que decirle que se trata de un valor numerico. Por eso le agrego int
numeroPantalla=StringVar() #el stringvar es una clase que sirve para los Tk.
#numeroPantalla.set("0")#para que el primer numero que aparezca en la pantalla sea un 0

pantalla = Entry(miFrame, textvariable=numeroPantalla) #el text variable es porque al ser un stringVar, el string o valor de la descripcion va a ir cambiando
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #el columnspawn es para que ocupe varias columnass sin desplazarte las columnas de los otros rows
pantalla.config(background = "black", fg="#03f943", justify = "right")

#  -------------------pulsaciones teclado-------------------------

def numeroPulsado(num):

    global operacion

    if operacion != "": #es decir si se usa la operacion de suma, entonces en lugar de seguir concatenando a los numeros se borra lo anterior
        numeroPantalla.set(num) #el numero de pantalla pasa a ser el numero que insertaste cuando el numero anterior era nada. 
        operacion="" #luego el string vuelve a ser nada, para que se pueda rellenar de vuelta
    
    else: # si habia un numero antes, el numero de pantalla pasa a ser la suma entre el numero anterior y el numero nuevo q insertaste

        numeroPantalla.set(numeroPantalla.get() + num) #le asigna un valor nuevo al numero de pantalla que es la suma

#-------------------funcion suma-------------------
#aca creo el metodo para la variable operacion de suma. Simultaneamente a la operacion (funcion) de numeroPulsado, hay que ir calculando el resultado de las operaciones
def el_resultado():
    global resultado #el global es una funcion de tkinder. Sirve para llamar una variable para una funcion en particular.

    numeroPantalla.set(resultado + float(numeroPantalla.get())) #esto fija el valor del total en el numero de pantalla.

    resultado=0

def suma(num): #aca fijo la funcion para sumar
    global operacion
    global resultado

    resultado += float(num)   #todo lo que se considera cuadro de texto, python lo va a tomar como texto, aun cuando sean numeros. Hay que decirle que se trata de un valor numerico. Por eso le agrego int o float
    
    operacion="suma" # aca agarras la variable operacion y le asignas el valor que es el resultado de la funcion de suma

    numeroPantalla.set(resultado) #esto para que vaya sumando solo sin tener que poner resultado cuando agrego otra suma u operacion


# -------------------fila 1-------------------------

boton7=Button(miFrame, text="7", width =3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width =3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width =3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width =3)
botonDiv.grid(row=2, column=4)

# -------------------fila 2-------------------------

boton4=Button(miFrame, text="4", width =3, command=lambda:numeroPulsado("4")) # el lambda son funciones anonimas. para simplificar la sintaxiss en determinadas circunstancias. Aca sirve para q no se ejecute el comando solo y aparezca un 4 en la calculadora sin usarla/
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width =3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width =3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width =3)
botonMult.grid(row=3, column=4)

# -------------------fila 3-------------------------

boton1=Button(miFrame, text="1", width =3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width =3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width =3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width =3)
botonRest.grid(row=4, column=4)

# -------------------fila 4-------------------------

boton0=Button(miFrame, text="0", width =3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width =3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width =3, command=lambda: el_resultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width =3, command=lambda: suma(numeroPantalla.get())) #le agrego el lambda a este boton para que pueda usar la operacion suma
botonSum.grid(row=5, column=4)

raiz.mainloop()

#-------------- OPERADOR NOT------------------

nota = 3
aprobado = nota


from tkinter import * 
from tkinter import messagebox # llamo la herramienta para ventanas emergentes
from tkinter import filedialog # llamo este tipo de ventana emergente

root = Tk() 
root.title("Liquidación por despido sin causa") 
root.resizable(1,1)
root.iconbitmap("32841.ico") 
root.geometry("1024x650") 
root.config(bg="black") 

miFrame = Frame() 
miFrame.config(width="1024", height="650") 
miFrame.config(bg="black") 
miFrame.config(bd="35") 
miFrame.config(cursor="hand2") 
miFrame.pack(fill="both", expand="True") 

mirespuesta=StringVar()#creo la funcion de misalario. Le decimoss que se trata de una cadena de caracteres
def codigo_boton1(): #creo la funcion para darle un programa al boton
    mirespuesta.set("Programa en construcción") #con el set le adjudico un valor a una variable

# --------------- ventana emergente ------------------

def acerca_del_autor(): # esta es la funcion para la ventana emergente
    messagebox.showinfo("Autor", "Federico Irarrazaval \nAbogado \nCel: 1567887879 \nEmail: fedeirar@gmail.com")

def aviso_licencia(): # esta es la funcion para la ventana emergente
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salir(): # esta es la funcion para la ventana emergente
    #valor = messagebox.askquestion("Salir", "Desea salir de la aplicacion?") #el ask question hace que aparezca voton de si y no. Al apretar el boton se almacena el valor en la variable valor
        #if valor == "yes":
         #   root.destroy() # el destroy es para q se cierre el programa 
        valor = messagebox.askokcancel("Salir", "Desea salir de la aplicacion?") #ac es lo mismo que lo anterior, pero con aceptar y cancelar que guardan valores de True or False
        if valor == True:
            root.destroy() # el destroy es para q se cierre el programa 

def cerrar_documento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor == False: #el reintentar funciona con True y False tambien
        root.destroy()

#-------------- ventanas emergentes 2 ------------------

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*"))) # el primer parametro es el titulo. Esto nos va a devolver la ruta del archivo que queremos abrir. Por defecto busca en la carpeta documentos
    print(fichero) #con el initialdir le digo donde comenzar la busqueda. Podemos tambien especificar que tipo de archivo buscar con filetypes que te pide una tupla

Button (root, text = "Abrir fichero", command=abreFichero).pack() 

#----------------menu-------------------------
barraMenu=Menu(root) #con esto creo una barra de menu
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff = 0) #el tearoff es para sacarle las lineas que aparecen en el menu al principio
barraMenu.add_cascade(label="Archivo", menu=archivoMenu) #le decimos que este elemento que pertecenece a la barramenu debe tener ese texto
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #es para agregar separados entre los submenu
archivoMenu.add_command(label="Cerrar", command = cerrar_documento)
archivoMenu.add_command(label="Salir", command = salir)

archivoEdicion=Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


archivoHerramientas=Menu(barraMenu)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

archivoAyuda=Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia", command = aviso_licencia)
archivoAyuda.add_command(label="Acerca del autor", command = acerca_del_autor) #le agrego el command para poder usar la funcion de la ventana emergente

#----------------imagen--------------------
miImagen = PhotoImage(file="imagen.liquidacion.gif")
Label(miFrame,image=miImagen).place(x=400, y=0) 

# ----------------- labels con cuadros de textos ---------------------
primer_label=Label(miFrame, text="Fecha de ingreso: ", bg="black",fg="white").grid(row=0, column=0, sticky="e", pady=2) #el sticky=e es para q su margen quede a la derecha(east)

cuadrotexto = Entry(miFrame, textvariable=mirespuesta)
cuadrotexto.grid(row=0, column=1, pady=2)
cuadrotexto.config(justify="center")

segundo_label=Label(miFrame, text="Fecha de egreso: ", bg="black",fg="white").grid(row=1, column=0, sticky="e", pady=2) #el padding te permite separar elementos. Agreangole al label lo siguiente:   ,padx/pady = numero. Se agrega igual que el sticky. Ej: ,padx=150

cuadrotexto2 = Entry(miFrame)
cuadrotexto2.grid(row=1, column=1, pady=2)
cuadrotexto2.config(justify="center")

tercer_label=Label(miFrame, text="Salario promedio: ", bg="black",fg="white").grid(row=2, column=0, sticky="e", pady=2)

cuadrotexto3 = Entry(miFrame)
cuadrotexto3.grid(row=2, column=1, pady=2)
cuadrotexto3.config(justify="center")

cuarto_label=Label(miFrame, text="MRMNH: ", bg="black",fg="white").grid(row=3, column=0, sticky="e", pady=2)

cuadrotexto4 = Entry(miFrame)
cuadrotexto4.grid(row=3, column=1, pady=2)
cuadrotexto4.config(justify="center")

quinto_label=Label(miFrame, text="Notas: ", bg="black",fg="white").grid(row=4, column=0, sticky="e", pady=2) #con esto creo un label para agregar notas

texto_nota = Text(miFrame, width="30", height="7")
texto_nota.grid(row=4, column=1, pady=2)

scroll_texto_nota = Scrollbar(miFrame, command=texto_nota.yview) # aca construyo un scroll bar para el label de nota. Le agrego el y para que se pueda scrollear de modo vertical.
scroll_texto_nota.grid(row=4, column=2, sticky = "nsew") # tiene que ser una columna mas para que aparezca al final. El sticky = nsew es para que el scroll tenga el mismo alto que el label de la nota
texto_nota.config(yscrollcommand=scroll_texto_nota.set) # esto es para que el scroll siga a la parte del texto en el label. sino no funciona correctamente.

# ---------- boton -------------
boton1 = Button(miFrame, text="Ejecutar liquidación", command=codigo_boton1) #esto es para crear un boton. El command es para darle una ejecucion al boton.
boton1.pack
boton1.grid(row=8, column=1, pady=2) 

# --------------- otros botones --------------------
indemnizaciones = IntVar() #el IntVar es para darle funcionalidad
proporcionales = IntVar()
multas = IntVar()

# ---------------- label relacionado a los otros botones --------------
textoFinal=Label(miFrame)
textoFinal.grid(row=11, column=1, pady=2)

def opcion_indemnizaciones():
    opcion="" #en principio se inicia esta variable a una cadena vacia
    if (indemnizaciones.get() == 1): #el 1 aca equivale a True
        opcion += "indemnizaciones"
    if (proporcionales.get() == 1): #el 1 aca equivale a True. Basicamente le digo si el boton de proporcionales esta con ok sumarle ...
        opcion += "proporcionales"
    if (multas.get() == 1): #el 1 aca equivale a True
        opcion += "multas"
  
    textoFinal.config(text=opcion) #aca le digo que al label de textofinal le ponga como texto la opcion que podria llegar a 3

# --------------- otros botones --------------------
Checkbutton(root, text = "Indemnizaciones por despido sin causa", variable=indemnizaciones, onvalue=1, offvalue = 0, command=opcion_indemnizaciones).pack() #asocio al boton con la variable de indemnizacion. Le tengo que agregar el onvaluepara indcarle que cuando el check este selccionado el valor en la variable playa va a ser igual a 1

Checkbutton(root, text = "Proporcionales por extincion del contrato de trabajo", variable=proporcionales, onvalue=1, offvalue = 0, command=opcion_indemnizaciones).pack()

Checkbutton(root, text = "Multas e indemnizaciones adicionales", variable=multas, onvalue=1, offvalue = 0, command=opcion_indemnizaciones).pack()

root.mainloop()

"""
escribir un programa q muestre por pantalla el resultado de la siguiente operacion matematica

la suma de a + b 
dividido 
el producto de a por c elevado al cuadrado"""

a = 10
b = 5
c = 2

print("El resultado es: ", (a+b) / (a*c)**2) 

# dado 2 numeros, por ejemplo a = 15 y b=11  determinar con un mensaje de respuesta del programa cual es mayor y en el caso de q sean iguales indicar en un mensaje q son iguales. Evaluar los 3 casos

a=17
b=16

if a>b:
    print ("A es mayor a B")

elif a<b:
    print("B es mayor a A")

elif a == b:
    print("A es igual a B")


#evaluar rangos de variable a. 


a = 32

if a >= 1 and a <= 10:
    print("Esta en el rango de 1 a 10")
elif a >= 11 and a <= 20:
    print("esta entre 11 y 20")
elif a >= 21 and a <= 30:
    print("esta entre 21 y 30")
else:
    print("no esta en ningun rango")


nota_1 = int(input("Ingresa primer nota de 1 a 10: "))
nota_2 = int(input("Ingresa segunda nota de 1 a 10: "))
nota_3 = int(input("Ingresa tercera nota de 1 a 10: "))

nota_final = (nota_1 + nota_2 + nota_3)/3

if nota_final >= 4:
    print("Aprobado")
elif nota_final < 4:
    print("Segui participando")
