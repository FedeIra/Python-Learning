def one():
    print("you fool")

one()


def withdraw_money(current_balance, amount, guys):
    if (current_balance >= amount):
        current_balance = (current_balance - amount) / guys
        print("The balance is", current_balance)

withdraw_money(120, 80, 2)


def favorite_city(name):
    print("One of my favirute cities is", name)
    print("One of my favirute cities is", name)
    print("One of my favirute cities i,", name)

favorite_city("Buenos Aires")


def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(100, 80)

if (balance <= 50):
    print("We need to make a deposit")
else:
    print("Nothing to see here!")

def wash_car(amount_paid):
    if (amount_paid == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

wash_car(12)


def beca (distancia, numero_hermanos, salario_familiar):
    if (distancia>100 and numero_hermanos>5 and salario_familiar<10000):
        print("sale beca")
    else:
        print("no sale nada")

beca (110, 6, 9000)

print("Programa becas")

distancia_escuela = int(input("a que distancia estas?"))
print(distancia_escuela)

numeros_hermanos = int(input("cuantos hermanos tenes?"))
print(numeros_hermanos)

salario_familiar = int(input("que salario tiene?"))
print(salario_familiar)

if (distancia_escuela>40 and numeros_hermanos>2 and salario_familiar<=20000):
        print("sale beca")
else:
    print("no sale nada")

print("Programa becas")

distancia_escuela = int(input("a que distancia estas?"))
print(distancia_escuela)

numeros_hermanos = int(input("cuantos hermanos tenes?"))
print(numeros_hermanos)

salario_familiar = int(input("que salario tiene?"))
print(salario_familiar)

if (distancia_escuela>40 and numeros_hermanos>2 and salario_familiar<=20000):
        print("sale beca")
else:
    print("no sale nada")



print("elegi una materia del listao amigo")

print("quimica, biologia o fisica")

lista_optativas = ["quimica", "biologia", "fisica"]

optativa = input("que optativa elegis?")

if optativa in lista_optativas:
    print("perfecto! elegiste",optativa)
else:
    print("flaco elegi bien y no jodas",optativa,"no es una optativa")

print("elegi una materia del listao amigo, podes elegir quimica, biologia o fisica")

optativa = input("escribila")

if optativa in ("quimica", "biologia", "fisica"):
    print("perfecto! elegiste",optativa)
else:
    print("flaco elegi bien y no jodas",optativa,"no es una optativa")

print("elegi una materia del listao amigo, podes elegir quimica, biologia o fisica")

def optar():
    optativa = input("escribila")
    if optativa in ("quimica", "biologia", "fisica"):
        print("perfecto! elegiste",optativa)
    else:
        print("flaco elegi bien y no jodas",optativa,"no es una optativa")

optar()

optar()


def optar():
    opcion = input("escribila")
    optativa = opcion.lower()
    if optativa in ("quimica", "biologia", "fisica"):
        print("perfecto! elegiste",optativa)
    else:
        print("flaco elegi bien y no jodas",optativa,"no es una optativa")

optar()



