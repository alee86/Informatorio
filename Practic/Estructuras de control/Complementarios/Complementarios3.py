"""
Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercero numero: "))

if num1<num2 and num1<num3:
	print("-------------------")
	print(f"Número {num1} es el más chico de los 3 ingresados")
	print("-------------------")

else:
	print(f"Número {num1} NO es el más chico de los 3 ingresados")
