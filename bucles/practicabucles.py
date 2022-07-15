for i in ["primavera", "verano", "otono", "invierno"]:
    print(i)


i = 1

while i<=10:
    print("ejecucion" + str(i))
    i=i+1

print("Termino la ejecucion")



edad = int(input("introduci tu edad"))

while edad<30:
    print("edad equivocada")
    edad = int(input("introduci tu edad de vuelta"))

print("edad correcta")



edad = int(input("introduci tu edad"))

while edad<30:
    print("edad equivocada")
    edad = int(input("introduci tu edad de vuelta"))

print("edad correcta")
print("edad correcta", str(edad))



edad = int(input("introduci tu edad"))

while edad>30 or edad>100:
    print("edad equivocada")
    edad = int(input("introduci tu edad de vuelta"))

print("edad correcta")
print("edad correcta", str(edad))
