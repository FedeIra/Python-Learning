from tkinter import*

raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()

operacion = "" #al iniciar programa operacion es igual a nada

resultado = 0 #aca es donde se ira almacenando la suma de los valores introducidos

# ------------PANTALLA--------------------
numeroPantalla = StringVar()

pantalla=Entry(miFrame, textvariable = numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #colspan. Si queres que la pantalla ocupe muchas columnas
pantalla.config(bg="black", fg="#03f943", justify="right")

# ------------ pusaciones teclado -------------------

def numeroPulsado(num):
    global operacion

    if operacion != "": #le digo que si la variable operacion es igual a nada q haga tal cosa. Esto se aplica entonces cuando no se pulso ninguna operacion de suma, resta, etc
        numeroPantalla.set(num) # q en la pantalla ponga el valor q le pase a la funcion por parametro. Es decir, q no concatene sino q escriba el nuevo numero
        operacion= "" #esto es para q la operacion pase a ser de vuelta la nada y que pueda aplicarse luego el else q le sigue si pongo otro numero
    else:
        numeroPantalla.set(numeroPantalla.get()+num) #el set pone tal info en la pantalla el get obtiene la info q esta. Entocnes si pongo get me da el valor de lo que tiene, y si le pongo
    #despues set entonces le suma el string nuevo de 4. Asi acumulo cuatros. Con esto se concatena

# ------------ funcion suma -------------------
def suma(num):
    global operacion #con el global le digo q va a operar con la variable global de operacion. Es la forma de llamar a la variable operacion
    global resultado

    resultado += int(num) #de este modo le pasa valor de int al string compuesto por nnumeros
    operacion = "suma"
    numeroPantalla.set(resultado) #le dice q en la pantalla aparezca lo que sumamos

# -----------------funcio el_resultado-----------------

def el_resultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))

    resultado = 0 #hay q volver a resetear el resultado luego

# ------------BOTONES--------------------
# ------------fila 1--------------------

boton7=Button(miFrame, text="7", width=3, command= lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command= lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command= lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

# ------------fila 2--------------------

boton4=Button(miFrame, text="4", width=3, command= lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command= lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command= lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="*", width=3)
botonMult.grid(row=3, column=4)

# ------------fila 3--------------------

boton1=Button(miFrame, text="1", width=3, command= lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command= lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command= lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)

# ------------fila 4--------------------

boton0=Button(miFrame, text="0", width=3, command= lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3, command= lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command= lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)


raiz.mainloop()