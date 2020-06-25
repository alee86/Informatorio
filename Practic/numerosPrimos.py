num = int(input("Numero para evaluar: "))
contador = 0

for x in range(num-2):
	if (num%(x+2)) != 0:
		contador += 1
if contador != 0:
	print(f"El numero {num} NO es primo")
else:
	print(f"El numero {num} es primo")