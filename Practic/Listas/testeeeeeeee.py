pila_aux = []
pila_1 = ['a','b','c','d']

pila_1.reverse()
print(pila_1)

indice = pila_1.index('b')
print(indice)

for i in range(indice):
	pila_aux.append(pila_1[i])

pila_1.remove('c')
print(pila_aux)
pila_1.reverse()
print(pila_1)