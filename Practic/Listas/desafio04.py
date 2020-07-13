'''
Desafío 4
Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de 
especie imprima el mensaje Hola soy ......, cuidame.

Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el 
mensaje anterior para los n nombres que se encuentran a partir de la posición i.

'''

tupla = ('Perro', 'Gato', 'Pajaro', 'Tortuga', 'Mosca', 'Mosquito', 'Rana', 'Hipopotamo')
posicion = int(input('Ingrese desde que posicion (1, 2, 3, 4...) '))

#los elementos se enumeran desde el 0.
for i, element in enumerate(tupla):
	if i >= posicion:
		print(f'Hola soy {element}, cuidame.')
		print(i)