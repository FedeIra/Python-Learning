#para crear una calculadora

from tkinter import * #el Tkinter es el interface estandar para python

raiz = Tk() #Tk se refiere a tkinter

miFrame = Frame(raiz) # con esto creo el frame de la interfaz grafica
miFrame.pack() 

#----------- operacion---------------
# variable operacion que guarda la variable que quiere usar el usuario. Que te permite resetear la pantalla

operacion="" #le asigno un valor a operacion igual a nada
resultado = 0 #le asigno un valor a resultado igual a 0

# -----------------mi pantalla-------------------------

#todo lo que se considera cuadro de texto, python lo va a tomar como texto, aun cuando sean numeros. Hay que decirle que se trata de un valor numerico. Por eso le agrego int
numeroPantalla=StringVar() #el stringvar es una clase que sirve para los Tk. Este va a ser el valor que aparece en la frame de pantalla
#numeroPantalla.set("0")#para que el primer numero que aparezca en la pantalla sea un 0

pantalla = Entry(miFrame, textvariable=numeroPantalla) #el text variable es porque al ser un stringVar, el string o valor de la descripcion va a ir cambiando
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #el columnspawn es para que ocupe varias columnass sin desplazarte las columnas de los otros rows
pantalla.config(background = "black", fg="#03f943", justify = "right")

#  -------------------pulsaciones teclado-------------------------

def numeroPulsado(num): #esta funcion es llamada luego al asignarle el command a cada boton. Cada boton tiene asignado un valor que es igual al num de esta funcion

    global operacion

    if operacion != "": #es decir si se usa la operacion de suma, entonces en lugar de seguir concatenando a los numeros se borra lo anterior
        numeroPantalla.set(num) #el numero de pantalla pasa a ser el numero que insertaste cuando el numero anterior era nada. 
        operacion="" #luego el string vuelve a ser nada, para que se pueda rellenar de vuelta
    
    else: # si habia un numero antes, el numero de pantalla pasa a ser la suma entre el numero anterior y el numero nuevo q insertaste

        numeroPantalla.set(numeroPantalla.get() + num) #si habia un valor anterior en la pantalla, le suma el nuevo numero y hace que en la pantalla aparezca la suma.

#-------------------funcion suma-------------------
#aca creo el metodo para la variable operacion de suma. Simultaneamente a la operacion (funcion) de numeroPulsado, hay que ir calculando el resultado de las operaciones
def el_resultado():
    global resultado #el global es una funcion de tkinder. Sirve para llamar una variable para una funcion en particular.

    numeroPantalla.set(resultado + float(numeroPantalla.get())) #esto fija el valor del total en el numero de pantalla.

    resultado=0 #entiendo que lo vuelve a 0 para que se pueda hacer una nueva operacion.

def suma(num): #aca fijo la funcion para sumar
    global operacion #para eso tengo que llamar a la variable operacion y variable resultado luego de que pasaron por las funciones de numeroPulsado y el_resultado
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