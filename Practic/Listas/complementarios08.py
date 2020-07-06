'''
i. Elabore un programa que dada una lista de 15 elementos, copie en otra 
lista los elementos pares multiplicados por 2.

'''

numeros = input('Ingrese la lista de  15 numeros separados por espacio: ')
lista = numeros.split()
lista_par = []
del lista[15:]

print('La lista ingresada es:',lista)

for i,element in enumerate(lista):
	if i%2 == 0:
		lista_par.append(int(element)*2)
print('El doble de los elementos en posiciones pares es:',lista_par)
