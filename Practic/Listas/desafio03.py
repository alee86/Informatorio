'''

Desafío 3		
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email 
(no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que 
no quiere insertar mas. No se podrán insertar nombres repetidos.

'''

biologos = { 'Alejandro': 'ale@gmail.com', 'Ernesto': 'ernes_to@gmail.com'}

while True:
	#ingresar nombre del biologo
	carga = input('Quiere agregar datos de un profecional? S/N: ').lower()
	if carga == 's':
		name = input('Ingrese el nombre de el biologo: ').capitalize()
		mail = input('Ingresar correo electronico: ')

		if name not in biologos:
			biologos.setdefault(name, mail)
		else:
			print('El nombre ya esta cargado. Ingrese otro')

	elif carga == 'n':
		print(biologos)
		break

	else:
		print('El valor ingresado no es correcto.')