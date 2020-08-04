def mediana(lista):
	for i in range(0, len(lista)): 
		lista[i] = int(lista[i]) 
	
	print(lista)


num = input('Inserte 3 numeros separados por espacio: ')

lista = num.split()

valor_medio = mediana(lista)

print(valor_medio[1])