
'''
g. Se tiene una lista que almacena pedidos en orden de llegada, por ende puede haber más 
de un pedido para el mismo artículo. Crear una lista donde se almacene la cantidad de 
pedidos por artículo.
'''

articulo_1 = [1, 2]
articulo_2 = [3, 2, 1, 4]
articulo_3 = [3, 2]

cantidad = 0
usuario = input('Indicar el articulo: 1, 2, 3 o "quit" para salir: ').lower()

while usuario != "quit":
	if usuario == "1":
		cantidad = int(input('Indicar cantidad de pedidos: '))
		articulo_1.append(cantidad)
	elif usuario == "2":
		cantidad = int(input('Indicar cantidad de pedidos: '))
		articulo_2.append(cantidad)
	elif usuario == "3":
		cantidad = int(input('Indicar cantidad de pedidos: '))
		articulo_3.append(cantidad)
	elif usuario == "quit":
		break
	else:
		print('El articulo no esta disponible.')
	
	usuario = input('Indicar el articulo: 1, 2, 3 o "quit" para salir: ').lower()

print(f'''
-----------------------------------
PEDIDOS:
Articulo 1: {articulo_1}
Articulo 2: {articulo_2}
Articulo 3: {articulo_3}
-----------------------------------
''')
