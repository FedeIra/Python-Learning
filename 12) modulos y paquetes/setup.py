from setuptools import setup

setup(
    name = "subPaqueteEjemplo",
    version = "1.0",
    description= "Paquete distribuible de operaciones basicas",
    author = "Federico Irarrazaval",
    author_email = "fedeirar@gmail.com",
    url="www.pildorasinformaticas.es",
    packages = ["PaqueteEjemplo","PaqueteEjemplo.subPaqueteEjemplo"]
)