def beca (distancia, numero_hermanos, salario_familiar):
    if (distancia>100 and numero_hermanos>5 and salario_familiar<10000):
        print("sale beca")
    else:
        print("no sale nada")

beca (110, 4, 9000)