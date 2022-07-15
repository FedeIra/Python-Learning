numero1 = int(input("introduce tu numero"))
numero2 = int(input("introduce un numero mayor que" + str(numero1)+ ": "))

while numero2 > numero1:
    numero1 = numero2
    numero2 = int(input("introduce un numero mayor que " + str(numero1)+ ": "))

print() 
print(numero2,"no es mayor que", str(numero1))


for i in range(5):
	a+=1
	print(a)	

    
