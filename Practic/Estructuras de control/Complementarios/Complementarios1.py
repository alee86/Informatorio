# 1. Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercero numero: "))

if num1>num2 and num1>num3:
	if  num2>num3:
		num1, num2, num3 = num1, num2, num3
	else:
		num1, num3, num2 = num1, num2, num3

elif num2>num1 and num2>num3:
	if  num1>num3:
		num2, num1, num3 = num1, num2, num3
	else:
		num2, num3, num1 = num1, num2, num3

elif num3>num1 and num3>num2:
	if  num1>num2:
		num3, num1, num2 = num1, num2, num3
	else:
		num3, num2, num1 = num1, num2, num3

print("-------------------")
print(num1, num2, num3)
print("-------------------")
