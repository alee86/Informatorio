'''
k. 	Cargue dos listas, y actualice la primer lista con los elementos 
que están en la segunda y no en la primera.
'''

lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = [1, 2, 3, 7, 8, 9, 10, 11, 12]

for i, element in enumerate(lista_2):
	if element in lista_1:
		print(end="")
	else:
		lista_1.append(element)

print(lista_1)
