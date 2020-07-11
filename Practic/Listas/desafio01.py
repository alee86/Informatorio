'''
Desafío 1
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación 
del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de 
menor a mayor. 

'''
encuesta = []

consulta = input('Encuesta? S/N: ').lower()

while consulta != "n":

	if consulta == 's':
		persona = int(input('Del 1 al 10, cuanto sabes de contaminación?: '))
		encuesta.append(persona)
	elif consulta == 'n':
		break
	else:
		print('Ingrese una opcion valida')

	consulta = input('Encuesta? S/N: ').lower()



encuesta.sort()

print(encuesta)