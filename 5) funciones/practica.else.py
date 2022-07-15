print("hola, este es el primer ejercicio. Te vamos a pedir que introduzcas lo siguiente")

num1 = (int(input("introduce tu primer numero:")))
num2 = (int(input("introduce tu segundo numero:")))

def DevuelveMax(n1,n2):
    if (n1>n2):
        print(n1)
    elif (n2>n1):
        print(n2)
    else:
        print("son iguales")

print("el numero mas alto es:")

DevuelveMax(num1, num2)