'''
Desafío 2	
Crea una tupla con los factores que más afectan a los mares. 
Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea 
un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, 
muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.

'''

factores_mares = ('bolsas', 'mercurio', 'desechos toxicos', 'derrames', 'desechos industriales', 'aumento de la temperatura')


while True:
	pregunta = input('queres jugar? responde "si" o "no": ').lower()
	
	if pregunta == 'si':
		numero = int(input('Elegi un numero: '))

		if numero >= 0 and numero <= len(factores_mares):
			print(f'Sabias que {factores_mares[numero]} es un contaminante de los mares')
		else:
			print('Elegi otro numero! Ese no esta en la lista. Intenalo de nuevo')	
		

	elif pregunta == 'no':
		print('Gracias por jugar con nosotros!')
		break

	else:
		print('No es una respuesta valida. Intenalo de nuevo')
