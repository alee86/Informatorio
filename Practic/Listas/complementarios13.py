'''
c. Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. 
El usuario llega y se ubica en la cola de menor cantidad de personas. 
Al finalizar el proceso indique cuántos elementos tiene cada cola.
'''

cola_a = [1, 1]
cola_b = [1, 1, 1, 1]

cantidad = 0

usuario = input('Indicar alguien esta entrando "E" o salienod "S", del local:').lower()

while usuario != "exit":
	
	if usuario == "e":
		cantidad = int(input('Indicar cantidad de personas que llegan: '))
		if len(cola_a) > len(cola_b):
			for i in range(cantidad):
				cola_b.append(1)
		else:
			for i in range(cantidad):
				cola_a.append(1)
			
	elif usuario == "s":
		cantidad = int(input('Indicar cantidad de personas que salieron: '))
		
		if len(cola_a) < len(cola_b):
			for i in range(cantidad):
					cola_b.pop()
		else:
			for i in range(cantidad):
					cola_a.pop()
	elif usuario == "exit":
		break

	else:
		print('Ingrese una de las opciones, entrando "E" o salienod "S": ')

	usuario = input('La persona esta entrando "E" o salienod "S", del local. "Exit" para salir: ').lower()

print(cola_a)
print(cola_b)

'''se puede mejorar marcando que evalua cual fila es mas larga por cada persona que entra al local'''