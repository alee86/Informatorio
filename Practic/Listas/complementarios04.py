'''
e. 	Cargar m elementos en una pila, y luego copiarlos en una nueva lista.

La principal diferencia entre una Pila y una Cola en java consiste en su modelo de 
entrada y salida, es decir, una Pila tiene un modelo LIFO (last-in / first-out), 
el cual quiere decir que el último elemento en entrar a la Pila será el primero en salir

'''
pila = []
lista = []
respuesta =""

while respuesta != 'n':

	elementos = input('Ingrese un elemento a la pila: ')
	pila.append(elementos)

	respuesta = input("quiere continuar? S/N: ").lower()
pila.reverse()
for i in pila:
	lista.append(i)
	
print(pila)
