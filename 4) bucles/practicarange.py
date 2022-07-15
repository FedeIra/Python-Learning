valido = False

email = input("introduce tu email")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("email correcto")
else:
    print("email incorrecto")



for i in "fedeirar@gmail.com":
    print("hola", end="")


email=False

for i in "fedeirar@gmail.com":
    if (i=="@"):
        email=True

if email == True:
    print("email es correcto")
else:
    print("email incorrecto")

email=False

for i in "fedeirar@gmail.com":
    if (i=="@"):
        email=True

if email:
    print("email es correcto")
else:
    print("email incorrecto")

email=False

for i in "fedeirar@gmail.com":
    if (i=="@"):
        email=True

if email:
    print("email es correcto")
else:
    print("email incorrecto")


print("Programa para crear cuenta de gmail:")

contador = 0

miEmail=input("introducie tu email")

for i in miEmail:
    if (i=="@" or i=="."):
        contador = contador + 1

if contador==2:
    print("email introducido")
else:
    print("email incorrecto")

for i in range(5):
    print(i)


for i in range(5):
    print(f"el valor es {i}")

for i in range(5,9):
    print(f"el valor es {i}")

for i in range(5,9,3):
    print(f"el valor es {i}")
