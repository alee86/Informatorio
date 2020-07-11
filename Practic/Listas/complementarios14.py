
'''
d. En un almacén se guarda mercadería en contenedores. No es posible colocar más de n 
contenedores uno encima del otro y, no hay área para más de 5 pilas de contenedores. 
Elabore un programa que permita gestionar el ingreso y salida de contenedores. 
Note que para retirar un contenedor es necesario retirar los contenedores que están encima 
de él y colocarlos en otra pila.
puedo tener muchos contenedores en una misma pila. Pero no puedo tener mas de 5 pilas
Los contenedores se reitran desde el que esta mas abajo (el primero que entro, sale primero)
'''

pila_aux = []
pila_1 = ['0','1','2','3','4','5']
pila_2 = ['a','b','c','d']
pila_3 = ['a1','a2','a3','a4','a5','a6']
pila_4 = ['2f','2f','2f','2f']

usuario = input('Indicar entrada "E", salida "S" o "EXIT" para salir:').lower()

while usuario != "exit":
	if usuario == "e":
		ingreso = int(input('en que pila quiere agregar el contenedor?: Pila 1, 2, 3 o 4 (ingresar numero)?: '))
		contenedor = input('Indicar nombre del contenedor: ')

		if ingreso == 1:
			pila_1.append(contenedor)
		elif ingreso == 2:
			pila_2.append(contenedor)
		elif ingreso == 3:
			pila_3.append(contenedor)
		elif ingreso == 4:
			pila_4.append(contenedor)
		else:
			print('No hay una pila con ese numero')

	elif usuario == 's':
		print(f'''
	Estado actual del deposito.
		Pila 1 {pila_1} contenedores.
		Pila 2 {pila_2} contenedores.
		Pila 3 {pila_3} contenedores.
		Pila 4 {pila_4} contenedores.

		Pila 5 (auxiliar) {pila_aux} contenedores 
		''')

		ingreso = int(input('en que pila esta el contenedor para sacar?: Pila 1, 2, 3 o 4 (ingresar numero)?: '))
		contenedor = input('Indicar nombre del contenedor: ')

		if ingreso == 1:
			pila_1.reverse()
			indice = pila_1.index(contenedor)
					
			for i in range(indice):
				pila_aux.append(pila_1[i])
			pila_1.reverse()
			del pila_1[indice-1:]

		if ingreso == 2:
			pila_2.reverse()
			indice = pila_2.index(contenedor)
					
			for i in range(indice):
				pila_aux.append(pila_2[i])
			pila_2.reverse()
			del pila_2[indice-1:]

		if ingreso == 3:
			pila_3.reverse()
			indice = pila_3.index(contenedor)
					
			for i in range(indice):
				pila_aux.append(pila_3[i])
			pila_3.reverse()
			del pila_3[indice-1:]

		if ingreso == 4:
			pila_4.reverse()
			indice = pila_4.index(contenedor)
					
			for i in range(indice):
				pila_aux.append(pila_4[i])
			pila_4.reverse()
			del pila_4[indice-1:]

	elif usuario == 'exit':
		break
	else:
		print('No es una opcion valida') 

	usuario = input('Indicar entrada "E", salida "S" o "EXIT" para salir:').lower()



print(f'''
Estado actual del deposito

Pila 1 {pila_1} contenedores.
Pila 2 {pila_2} contenedores.
Pila 3 {pila_3} contenedores.
Pila 4 {pila_4} contenedores.

Pila 5 (auxiliar) {pila_aux} contenedores 
	''')