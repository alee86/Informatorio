'''
DESAFÍO 4
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de
acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado 
de un tamaño: 8x6
'''

import os
os.system('color')



columna = int(input("ingrese columnas: "))
fila = int(input("ingrese filas: "))


for fila in range(fila):
	for i in range(columna):
		if i%2 != 0:
			print("I", end=" ")
		else:
			print("P", end=" ")
	print()
