'''
Para el uso de fertilizantes es necesario medir cuánto abarca un determinado 
compuesto en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea, 
y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es
factible la utilización de fertilizantes.
'''

cantidad = int(input("Indique la cantidad del compuestoX: "))
if cantidad >= 10:
	compuestoX = True
else:
	compuestoX = False

matorral = input("Indique si hay matorrales (si o no): ").lower()
if matorral == "si":
	matorral = True
else:
	matorral = False


if not matorral and compuestoX:
	print("Es factuble utilizar el fertilizante.")
else:
	print("No usar el fertilizante.")