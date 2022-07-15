from io import open

archivo_texto = open("Cronograma.docx", "w") 

frase = "estupendo dia para estudiar python\n el miercoles"

archivo_texto.write(frase) 

archivo_texto.close()