#para crear una calculadora

from tkinter import * 

raiz = Tk() 

miFrame = Frame(raiz) 
miFrame.pack() 

#----------- operacion---------------
# variable operacion que guarda la variable que quiere usar el usuario. Que te permite resetear la pantalla

operacion=""
resultado = 0


# -----------------mi pantalla-------------------------

#todo lo que se considera cuadro de texto, python lo va a tomar como texto, aun cuando sean numeros. Hay que decirle que se trata de un valor numerico. Por eso le agrego int
numeroPantalla=StringVar()
#numeroPantalla.set("0")#para que el primer numero que aparezca en la pantalla sea un 0

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #el columnspawn es para que ocupe varias columnass sin desplazarte las columnas de los otros rows
pantalla.config(background = "black", fg="#03f943", justify = "right")

#  -------------------pulsaciones teclado-------------------------

def numeroPulsado(num):

    global operacion

    if operacion != "": #es decir si se usa la operacion de suma, entonces en lugar de seguir concatenando a los numeros se borra lo anterior
        numeroPantalla.set(num)
        operacion=""
    
    else:

        numeroPantalla.set(numeroPantalla.get() + num) #para que se pueda acumular los 4. Se concatena.

#-------------------funcion suma-------------------
#aca creo el metodo para la variable operacion de suma
def el_resultado():
    global resultado

    numeroPantalla.set(resultado + int(numeroPantalla.get()))

    resultado=0

def suma(num):
    global operacion
    global resultado

    resultado += int(num)   #todo lo que se considera cuadro de texto, python lo va a tomar como texto, aun cuando sean numeros. Hay que decirle que se trata de un valor numerico. Por eso le agrego int
    
    operacion="suma"

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

boton4=Button(miFrame, text="4", width =3, command=lambda:numeroPulsado("4")) #son funciones anonimas. para simplificar la sintaxiss en determinadas circunstancias. Aca sirve para q no se ejecute el comando solo y aparezca un 4 en la calculadora sin usarla/
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

# --------------- check button --------------------

