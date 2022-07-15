# calcular el area de un triangulo (base por altura)/2. interactuando y previendo error al escribir palabra en lugar de numero

base = None # se usa None con asignacion de variable cuando aun no le queremos dar un valor
altura = None

while True: # el while es para que si escribis mal, vuelva a preguntarte
    try:
        base = float(input("escriba la base del traingulo: "))
        break #se rompe el while al escribir un numero
    except: # si escribis una palabra no se rompe
        print("debe escribir un numero.")

while True:
    try:
        altura = float(input("escriba la altura del traingulo: "))
        break
    except:
        print("debe escribir un numero.")

area = base*altura/2
