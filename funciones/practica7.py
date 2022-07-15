email = input("introduce tu email")

contador = 0

for i in range(len(email)):
    if email[i] == "@":
        contador = contador + 1
       
if email[i] == "." and contador == 1:
    print("contrasenia correcta")
else:
     print("contrasenia incorrecta")