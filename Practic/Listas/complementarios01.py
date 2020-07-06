'''
Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada, 
controle y sustituya cualquier elemento negativo por 0.
'''
cola = []
lista = []
respuesta =""

while respuesta != 'n':

	elementos = input('Ingrese un elemento a la cola: ')
	cola.append(elementos)

	respuesta = input("quiere continuar? S/N: ").lower()

print(cola)

for i in cola:
	lista.append(i)
#tambien puedo usar el metodo copy()

lista = cola.copy()
print(lista)
