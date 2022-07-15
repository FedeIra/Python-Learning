contrasenia = input("introduce tu contrasenia")

contador = 0

for i in range(len(contrasenia)):
    if contrasenia[i] == " ":
        contador = contador + 1

if len(contrasenia)>8 or contador == 1:
    print("contrasenia incorrecta")
else:
    print("contrasenia correcta")