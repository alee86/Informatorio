"""
Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario
para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:

Sueldo Actual (en $)    Aumento
0 – 6000		15%
6000 – 7900		10%
7900 – 12000	6%
Más de 12000	0%

Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, 
el sueldo actual y el sueldo aumentado.
"""

salario_actual = int(input("Ingrese salario: "))
aumento = 0

if salario_actual <= 6000:
	aumento = 0.15

elif salario_actual <= 7900:
	aumento = 0.1

elif salario_actual <= 12000:
	aumento = 0.06
else:
	aumento = 0

print(f"""
Salario actual = ${salario_actual}
Aumento = {aumento*100}%
------------------------------
Salario nuevo = ${salario_actual*(1+aumento)}
 """)