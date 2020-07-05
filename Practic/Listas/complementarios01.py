'''
Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada, 
controle y sustituya cualquier elemento negativo por 0.
'''
numero = 0
lista = []
respuesta =""


while respuesta != 'n':

	numeros = int(input('Ingrese un número: '))
	lista.append(numeros)

	respuesta = input("quiere continuar? S/N: ").lower()

for i, element in enumerate(lista):
	if element < 0:
		lista[i] = 0
print(lista)