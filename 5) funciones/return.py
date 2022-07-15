print("CÁLCULO DE INGRESOS PARA DOS LABUROS PART TIME")



#PRIMERO, CREO LA FUNCIÓN QUE ME VA A DETERMINAR CUÁNTA GUITA ME DEJA UN LABURO POR SEMANA

#El return va a ser el ingreso propiamente dicho

def ingreso_por_semana(valor,horas,dias_trabajo):

	ingreso = valor*horas*dias_trabajo

	return ingreso





#SEGUNDO, CREO LA FUNCIÓN QUE ME VA A GENERAR LOS PUESTOS DE LABURO. ESTA FUNCIÓN LLAMA A LA ANTERIOR, PARA VER CUÁNTA GUITA ME VA A DEJAR SEMANALMENTE EL LABURO EN CUESTIÓN

#Los returns van a ser dos: primero, el nombre del laburo; segundo, cuánta guita me deja ese laburo por semana

def trabajo (denom):

	valor=float(input("¿Cuánto paga el laburo por hora? "))

	horas=float(input("¿Cuántas horas al día trabajás de esto? "))

	dias_trabajo=int(input("¿Cuántos días a la semana trabajás de eso? "))

	nombre=denom

	ingreso_semana=ingreso_por_semana(valor,horas,dias_trabajo)

	return nombre,ingreso_semana



#TERCERO, CREO LOS DOS LABUROS LLAMANDO A LA SEGUNDA FUNCIÓN CADA VEZ

#Al separar las variantes en coma, independizo los dos resultados del return de la segunda función

trabajo1, ingreso1 = trabajo(input("Nombre del primer trabajo: "))

trabajo2, ingreso2 = trabajo(input("Nombre del segundo trabajo: "))

print("El trabajo de "+trabajo1+" me deja $"+str(ingreso1)+" por semana y $"+str(ingreso1*4)+" por mes")

print("El trabajo de "+trabajo2+" me deja $"+str(ingreso2)+" por semana y $"+str(ingreso2*4)+" por mes")

print("Por mes junto $"+str((ingreso1+ingreso2)*4))