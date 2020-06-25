num = int(input("Numero para evaluar: "))
contador = 0

for x in range(num):
	if num%(x+1) == 0:
		contador += 1
if contador > 2:
	print(f"El número {num} NO es primo")
else:
	print(f"El número {num} SI es primo")
