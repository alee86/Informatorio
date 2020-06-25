
COTRA_VALIDA = 'info2020'
INTENTOS = 3

cont = input("ingrese su contrasenia: \t")
i = 1
while i < INTENTOS:
	if cont == COTRA_VALIDA:
		print("ingreso correctamente")
		break
	else:
		cont = input("contrasenia invalida, ingrese nuevamente: \t")
	i += 1

if i == INTENTOS:
	print("SE PASO DE INTENTOS")