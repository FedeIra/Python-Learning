salario_presidente = int(input("introduce salario presidente"))
print("salario_presidente",str(salario_presidente))

salario_director = int(input("introduce salario director"))
print("salario_director",str(salario_director))

salario_jefe_area = int(input("introduce salario jefe_area"))
print("salario_jefe_area",str(salario_jefe_area))

salario_administrativo = int(input("introduce salario administrativo"))
print("salario_administrativo",str(salario_administrativo))

if salario_presidente>salario_director>salario_jefe_area>salario_administrativo:
    print("todo ok")
else:
    print("todo mal")