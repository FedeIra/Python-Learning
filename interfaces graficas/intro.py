#ventana
ventana = tk.Tk()
ventana.title("PImprimir numeros")
ventana.config(width="1024", height="650") 

#botones
boton1=tk.Button(text="Imprimir numeros", command = imprimir_numero)
boton1.place(x= 10, y=30)

boton1=tk.Button(text="saludar", command=saludar) #el command es para q el boton use una funcion
boton1.place(x= 50, y=70)

#cuadros de texto

caja1 = tk.Entry()
caja1.place(x= 100, y=140)

#etiqueta
etiqueta_nombre = tk.Label(text= "Ponele")
etiqueta_nombre.place(x= 200, y=140)


ventana.mainloop()

import tkinter as tk

def saludar():
    nombre= caja1.get()  # el metodo get es leer el contenido del control
    print("Hola mundo para", nombre)
    
def imprimir_numero():
    for i in range(1,11):
        print(i)

#ventana
ventana = tk.Tk()
ventana.title("PImprimir numeros")
ventana.config(width="1024", height="650") 

#botones
boton1=tk.Button(text="Imprimir numeros", command = imprimir_numero)
boton1.place(x= 10, y=30)

boton1=tk.Button(text="saludar", command=saludar) #el command es para q el boton use una funcion
boton1.place(x= 50, y=70)

#cuadros de texto

caja1 = tk.Entry()
caja1.place(x= 100, y=140)

#etiqueta
etiqueta_nombre = tk.Label(text= "Ponele")
etiqueta_nombre.place(x= 200, y=140)


ventana.mainloop()
