"""
Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
"""

m = int(input("Ingrese el valor para el numerador "))
n = int(input("Ingrese el valor para el denominador "))

if m%n == 0:
	print(f"{n} es DIVISOR de {m}")
else:
	print(f"{n} es NO es DIVISOR de {m}")
	