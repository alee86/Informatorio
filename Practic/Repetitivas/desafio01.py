'''
DESAFÍO 1
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar 
al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 
'''

enter_pass ="1"
true_pass = "123"
user_name = ""
intento = 1

enter_user_name = input("Ingresa tu usuario: ")
enter_pass = str(input("Ingresa tu pass: "))


if enter_pass == true_pass:
		print("""
	#########################################
	 Pass correcto... Ingresando a tu cuenta
	#########################################""")

else:
	print(f"El pass ingresado no es correcto. Tenes 2 intentos más")
	enter_pass = str(input("Ingresa tu pass: "))

	if enter_pass == true_pass:
		print("""
	#########################################
	 Pass correcto... Ingresando a tu cuenta
	#########################################""")

	else:
		print(f"El pass ingresado no es correcto. Tenes 1 intentos más")
		enter_pass = str(input("Ingresa tu pass: "))
		
		if enter_pass == true_pass:
			print("""
		#########################################
		 Pass correcto... Ingresando a tu cuenta
		#########################################""")

		else:
			print("""
		#########################
		 No tenes mas intentos.
		 Tu cuenta esa bloqueada.
		#########################""")