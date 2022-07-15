print("elegi una materia del listao amigo, podes elegir quimica, biologia o fisica")

def optar():
    opcion = input("escribila")
    optativa = opcion.lower()
    if optativa in ("quimica", "biologia", "fisica"):
        print("perfecto! elegiste",optativa)
    else:
        print("flaco elegi bien y no jodas",optativa,"no es una optativa")

optar()

optar()