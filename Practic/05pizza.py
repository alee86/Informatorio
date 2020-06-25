'''

pizza = input("¿Quiere una pizza vegetariana? ")
ingrediente = ""

if pizza == "si":
	ingrediente = input("Indique un ingrediente: Pimiento o Rúcula: ")
	
	if ingrediente == "pimenton":
		print("Pedido confirmado de una pizza con: muzzarella, tomate y  Pimenton")
	elif ingrediente == "rucula":
		print("Pedido confirmado de una pizza con: muzzarella, tomate y  Rúcula")

elif pizza == "no":
	ingrediente = input("Indique un ingrediente: 1 para Jamón o 2 Panceta: ")
	
	if ingrediente == "jamon":
		print("Pedido confirmado de una pizza con: muzzarella, tomate y  Jamón")
	elif ingrediente == "panceta":
		print("Pedido confirmado de una pizza con: muzzarella, tomate y  Panceta")


else:
	print('Ingese como opcion "si" o "no"')

'''

pizza = input("¿Quiere una pizza vegetariana? ")
ingrediente = ""

if pizza == "si":
	pizza = "VEGETARIANA"
	ingrediente = input("Que ingrediente prefiere? 1 para Pimiento o 2 para Rúcula: ")
	
	if ingrediente == "1":
		ingrediente = "Pimiento"
	elif ingrediente == "2":
		ingrediente = "Rúcula"
		
elif pizza == "no":
	pizza = "TRADICIONAL"
	ingrediente = input("Que ingrediente prefiere? 1 para Jamón o 2 para Panceta: ")

	if ingrediente == "1":
		ingrediente = "Jamón"
	elif ingrediente == "2":
		ingrediente = "Panceta"
		

print("Pedido confirmado de una pizza",pizza,"con los siguientes ingrediente: Muzzarella, Tomate y",ingrediente)