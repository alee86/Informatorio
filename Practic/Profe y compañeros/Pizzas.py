
pregunta_usuario = input("Desea pizza vegetariana? si/no \t") 

if pregunta_usuario == "si":
	
	while True:
		print("Puede escoger entre uno de los siguientes ingredientes: \n 1-pimiento \n 2-rucula. ")
		Ingrediente_elegido = input("Ingrese el ingrediente que desea:\t\n") 
		if Ingrediente_elegido == "1":
			print("Usted eligio pizza vegetariana") 
			print("Los ingredientes son pimiento, mozzarela y tomate")
			break
		elif Ingrediente_elegido == "2": 
			print("Usted eligio pizza vegetariana") 
			print("Los ingredientes son rucula, mozzarela y tomate")
			break
		print("ingrese un ingrediente valido")

elif pregunta_usuario == "no": 
	while True:
		print("Puede escoger entre uno de los siguientes ingredientes: \n 1-jamon \n 2-panceta")
		Ingrediente_elegido = input("Ingrese el ingrediente que desea:\t\n") 
		if Ingrediente_elegido == "1": 
			print("Usted eligio pizza no vegetariana") 
			print("Los ingredientes son jamon, mozzarela y tomate") 
		elif Ingrediente_elegido == "2": 
			print("Usted eligio pizza no vegetariana") 
			print("Los ingredientes son panceta, mozzarela y tomate")
		print("ingrese un ingrediente valido")