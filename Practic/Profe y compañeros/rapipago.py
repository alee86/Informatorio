'''
c. Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. El usuario llega y se ubica en la 
cola de menor cantidad de personas. Al finalizar el proceso indique cuántos elementos tiene cada cola.
'''

cola1 = list()
cola2 = list()
n=''

print ('Para ingresar a la cola de espera, escriba su nombre, 0 para finalizar')

while True:
	n=input('Ingrese su nombre: ')
	print ('')
	if  n != "0":
		 c1 = len(cola1)
		 c2 = len(cola2)
		 if c1 < c2:
		 	cola1.append(n)
		 else:	
		 	cola2.append(n)


	else:
		break


print ('En la fila 1 hay: ',len(cola1))
print ('En la fila 2 hay: ',len(cola2))