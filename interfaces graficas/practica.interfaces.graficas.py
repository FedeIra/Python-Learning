from tkinter import * 

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
    mirespuesta.set("Programa en construcción")

miImagen = PhotoImage(file="imagen.liquidacion.gif")
Label(miFrame,image=miImagen).place(x=400, y=0) 

primer_label=Label(miFrame, text="Fecha de ingreso: ", bg="black",fg="white").grid(row=0, column=0, sticky="e", pady=2) #el sticky=e es para q su margen quede a la derecha(east)

cuadrotexto = Entry(miFrame, textvariable=mirespuesta) #le agrego el textvariable para asociarla al boton y funcion del boton
cuadrotexto.grid(row=0, column=1, pady=2)
cuadrotexto.config(justify="center")

segundo_label=Label(miFrame, text="Fecha de egreso: ", bg="black",fg="white").grid(row=1, column=0, sticky="e", pady=2) #el padding te permite separar elementos. Agreangole al label lo siguiente:   ,padx/pady = numero. Se agrega igual que el sticky. Ej: ,padx=150

cuadrotexto2 = Entry(miFrame)
cuadrotexto2.grid(row=1, column=1, pady=2)
cuadrotexto2.config(justify="center")

tercer_label=Label(miFrame, text="Salario promedio: ", bg="black",fg="white").grid(row=2, column=0, sticky="e", pady=2)

cuadrotexto3 = Entry(miFrame) #ajuste esta parte para q este cuadro este asociado al valor de la variable q asigna el boton de imprimir liquidacion
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

boton1 = Button(miFrame, text="Ejecutar liquidación", command=codigo_boton1) #esto es para crear un boton. El command es para darle una ejecucion al boton.
boton1.pack
boton1.grid(row=6, column=1, pady=2) 

root.mainloop()