#va a describir la configuracion del paquete

from setuptools import setup

setup(       #se utiliza la funcion setup y se ponen los atributos del paquete obligatorios si o si

    name ="paquetecalculos",
    version = "1.0",
    description = "Paquete de redondeo y potencia",
    author = "Fede",
    author_email = "fedeirar@gmail.com", #este y los siguientes son datos que no son obligatorios
    url = "wwww.pildorasinformaticas.es", #tampoco es obligatorio
    packages = ["calculos", "calculos.redondeo_potencia"] #este es el atributo mas importante. escribo la ruta completa del paquete

)