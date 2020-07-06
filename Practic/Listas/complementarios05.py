'''
f. Cargar k elementos en una cola, y luego copiarlos en una nueva lista.


'''

cola = []
lista = []
respuesta =""

while respuesta != 'n':

	elementos = input('Ingrese un elemento a la cola: ')
	cola.append(elementos)

	respuesta = input("quiere continuar? S/N: ").lower()

print(cola)

#for i in cola:
#	lista.append(i)
#tambien puedo usar el metodo copy()
lista = cola.copy()
print(lista)

