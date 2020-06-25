'''
Para seguir colaborando en esta misión de salvar al planeta, necesitamos que 
elabores un programa en Python que dado el tamaño de un pez indique si su organismo 
está contaminado. Para ello tendremos 4 opciones:

*Tamaño Normal: Mensaje "Pez en buenas condiciones"
*Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
*Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
*Tamaño sobredimensionado: Mensaje "Pez contaminado"
'''

size = ""
msj ="""Indique el tamaño del pez segun la escala:
1- Nomal
2- Debajo del normal
3- Superior al normal
4- Sobredimensionado
0 - para salir"""

while size != 0:
	print(msj)
	size = int(input(">>>> "))

	if size == 1:
		print("Pez en buenas condiciones")

	elif size == 2:
		print("Pez con problemas de nutrición")

	elif size == 3:
		print("Pez con síntomas de organismo contaminado")

	elif size == 4: 
		print("Pez contaminado")

	else:

		print("El valor ingresado no corresponde a la escala")
		print(msj)
