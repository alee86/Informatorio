'''
h. 	Construya un algoritmo que sume todos los elementos en posición par de una lista.
'''

numeros = input('Ingrese la lista de numeros separados por espacio: ')
lista = numeros.split()

print('La lista ingresada es:',lista)
suma = 0
for i,element in enumerate(lista):
	if i%2 == 0:
		suma += int(element)
print('La suma de los elmentos en posicion par es:',suma)



