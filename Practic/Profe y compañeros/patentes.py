x = True
autos = 0
basura = 0
multa = 0

while x:
	monitoreo = str(input("Ingrese valor de monitoreo\t"))
	autos = autos + 1
	
	if (monitoreo[6] == "1"):
		basura = basura + 1
		
		if(monitoreo[7] == "1"): 
			multa = multa + 1
		
	y = int(input("Desea Continuar Si. 1 No 2\t"))
	if y == 2:
		x = False
print("El total de vehículos observados es:\t",  autos)
print("El total de vehículos que tiraron basura es:\t", basura)
print("El porcentaje de vehículos que tenían multa es:\t", (multa * 100) / autos)
print ("Fin.")




 

