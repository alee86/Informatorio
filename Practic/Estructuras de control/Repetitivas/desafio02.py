'''
DESAFÍO 2
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado 
de personas. Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado 
menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas.

'''

encuestados = 0
colillas = 0
recolectadas = 0

bajo = 1 #menos de 100
medio = 1 #entre 100 y 200
alto = 1 #mas de 200

while True:
	colillas = int(input("Cantidad de colillas recolectadas: "))
	encuestados += 1
	recolectadas = recolectadas + colillas

	if colillas < 100:
		bajo += 1

	elif colillas < 200:
		medio += 1
	
	elif colillas >= 200:
		alto += 1

	else:
		print("Ingrese el valor con numeros.")

	print(f"""
	##################################################################
	Encuestados: {encuestados}
	Colillas: {recolectadas}
	Menos de 100: {bajo} prepresenta {bajo/(bajo + medio + alto)}
	Entre 100 y 200 {medio} prepresenta {medio/(bajo + medio + alto)}
	Más de 200: {alto} prepresenta {alto/(bajo + medio + alto)}
	##################################################################
		""")