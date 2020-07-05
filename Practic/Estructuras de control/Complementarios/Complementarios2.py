'''
Desarrolle un programa que permita determinar si un número X ingresado es par o impar.
'''
num = int(input("Ingrese un numero para ser evaluado: \n"))

if num%2 == 0:
	print(f"El número {num} es PAR")
else:
		print(f"El número {num} es IMPAR")