contador = 0

edad = int(input("escribi tu edad:"))

while edad<18:
    contador = contador + 1
    edad = int(input("escribi de vuelta tu edad:"))
    if contador == 2:
        print("se acabaron tus chances")  
        break;
     