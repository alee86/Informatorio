'''
DESAFÍO 4
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de
acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado 
de un tamaño: 8x6


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


'''
import os
os.system('color')

columna = int(input("Ingrese numero de columnas: "))
filas = int(input("Ingrese numero de filas : "))

for f in range(filas):
	if f%2 == 0: #Evaluo que las filas pares inicien con P
		for c in range(columna):
			if c%2 == 0: 
				print("\033[1;32;40m[V]", end ="")
			else:
				print("\033[93m[B]",end ="")
	else: #Evaluo que las filas impares inicien con I
		for c in range(columna):
			if c%2 == 0:
				print("\033[1;37;44m[V]", end ="")
			else:
				print("\033[91m[B]",end ="")
	print()