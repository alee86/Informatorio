'''
b. 	Haz un programa que almacene 5 elementos en una variable del tipo lista, 
la modiﬁque para que cada componente sea igual al cuadrado del componente original. 
El programa mostrara la lista resultante por pantalla.
'''

lista_str = input('Ingrese 5 elmentos se parados por espacio:  ')
lista = lista_str.split()

print("Lista inicial es: ", lista)
# Calculando el cuadrado de cada elemento
del lista [5:]
for i, element in enumerate(lista):
	lista[i] = int(element)**2
print('El cuadrado de los 5 primeros elementos es: ', lista)

