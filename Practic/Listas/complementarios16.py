'''
f. Se tiene una lista con los datos de los clientes de una compañía de telefonía celular, 
los cuales pueden aparecer repetidos en la lista, si tienen registrado más de un número 
telefónico. La compañía para su próximo aniversario desea enviar un regalo a sus clientes, 
sin repetir regalos a un mismo cliente. En una lista se almacenan los regalos disponibles en 
orden. Se desea un programa que cree una nueva lista con los clientes, sin repetir y ordenada. 
 que al final muestre el regalo que le corresponde a cada cliente.
'''

lista = ['Ale', 'Edu', 'Ari', 'Car', 'Guada', 'Mauri', 'Dami', 'Fer', 'Guada', 'Mauri', 'Dami', 
'Fer', 'Guada', 'Mauri', 'Dami', 'Fer', 'Ari', 'Car', 'Guada', 'Mauri', 'Dami', 'Fer', 'Guada',
'Mauri', 'Ari', 'Car', 'Guada', 'Mauri', 'Dami', 'Fer', 'Guada', 'Mauri']

usuarios = []
delivery = []

regalos = ['birra', '$200', '4gb','abrazo', '$500', '2gb','Siga participando', '$200']

for i, element in enumerate(lista):
	
	if element not in usuarios:
		usuarios.append(element)

usuarios.sort()

for i in usuarios:
	aux = usuarios[usuarios.index(i)] , regalos[usuarios.index(i)]
	delivery.append(aux)
print(delivery)