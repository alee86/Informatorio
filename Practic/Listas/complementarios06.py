'''
g. 	Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas, 
cargándolas ordenadas en otra lista.
'''
elementos_1 = input('Ingrese 5 elementos separados por "espacio": ')
elementos_2 = input('Ingrese otros 5 elementos separados por "espacio": ')

lista_1 = elementos_1.split()
lista_2 = elementos_2.split()

del lista_1 [5:]
del lista_2 [5:]

lista = lista_1 + lista_2 #
lista.sort() #ordenando la lista

print(lista)