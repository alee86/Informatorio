"""
Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo
de triángulo es, de acuerdo a los siguientes casos. 
Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:

Si A>=B + C  No se trata de un triángulo
Si A2 = B2 + C2  Es un triángulo rectángulo
Si A2 > B2 + C2  Es un triángulo obtusángulo
Si A2 < B2 + C2  Es un triángulo acutángulo

"""

A = int(input("Ingrese el valor del primer (el mayor) lado: "))
B = int(input("Ingrese el valor del segundo lado: "))
C = int(input("Ingrese el valor del tercero lado: "))

if A>= (B + C):
	print("No se trata de un triángulo")

elif A**2 == (B**2 + C**2):
	print ("Es un triángulo rectángulo")

elif A**2 > (B**2 + C**2):
	print("Es un triángulo obtusángulo")

elif A**2 < (B**2 + C**2):
	print("Es un triángulo acutángulo")