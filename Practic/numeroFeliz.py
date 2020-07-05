'''
Número feliz. Los números felices se definen por el siguiente procedimiento: 
empezando con cualquier número entero positivo, se reemplaza el número por la suma de 
los cuadrados de sus dígitos, y se repite el proceso hasta que el número es igual a 1 o 
hasta que se entra en un bucle que no incluye el 1.

'''

num = input("Ingrese un numero para saber si es feliz: ")
z = 0
control = 0

while num != "1":
	for x in range(len(num)): 	#Saco el indice

		y = int(num[x])
		y = y**2 		#Calculo el cuadrado de cada indice
		z += y		#saco la suma de los cuadrados

	if z == 1:
		print(f"El numero SI es feliz")
		break

	elif control == z:
		print("El numero NO es feliz")
		break
	
	else:
		control = z
		num = str(z)
		z = int(0)

	# El bucle no termina nunca cuando no es feliz... falta poner eso en el codigo.
