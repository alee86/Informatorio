'''
d. 	Realice una función que dada una lista de enteros L, y un número entero n. 
Elimine de la lista original los elementos que sean iguales a ese número dado.
'''

lista = [1, 2, 3, 5, 8, 9, 1, 2, 3, 5, 8, 9, 1, 2, 3, 5, 8, 9, 1, 2, 3, 5, 8, 9]

print('La lista es:', lista)
print("\n")
eliminar = int(input('Indique el numero que quiere eliminar: '))

for i, element in enumerate(lista):
	if element == eliminar:
		lista.remove(eliminar)

print(lista)
