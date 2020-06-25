'''
Codigo para ver numeros primos. Mejora la verificacion para poder probar numeros con muchas
cifras
'''

while True:

	num = int(input("Numero para evaluar: "))
	i = 2
	primo = True

	while primo and ((num/2) > i):
		if num%i == 0:
			primo = False
		i += 1

	if primo:
		print(f"El número {num} SI es primo")
	else:
		print(f"El número {num} NO es primo")