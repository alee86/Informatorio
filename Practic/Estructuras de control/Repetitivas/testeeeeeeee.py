

inicio = True
personas = 0
menos100 = 0
menos200 = 0
mas200 = 0

while inicio:
	print('Cantidad de Colillas')
	colillas = int(input('Colillas'))
	if colillas < 100:
		menos100 += colillas
	elif colillas <200:
		menos200 += colillas
	else:
		mas200 += colillas


	personas += 1

	seguimos = int(input("Seguimios 1 si 0 no"))
	if seguimos == 0:
		inicio = False

print('Cantidad de personas', personas)
print('% de menos de 100', menos100*100/personas)
print('FIN')
