#Barrios

nombre = input("Introduzca el nombre del barrio: ")

nombre = nombre.capitalize()

print("Ingrese 1 si el barrio es CÉNTRICO o 2 si es NO CÉNTRICO")
ubicacion = int(input("Ingrese la opción 1 o 2: "))
	
if (nombre [0] < "M") and (ubicacion ==1):
	print("El barrio pertenece a la sección A")
elif (nombre [0] > "M") and (ubicacion ==2):
	print("El barrio pertenece a la sección A")
else:
	print("El barrio pertenece a la sección B")