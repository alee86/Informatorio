'''
a. Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.

palíndromo: se lee de adelante para atras y es la misma palabra: Anana, Arañara, Solos
'''

palabra = input('Ingrese una palabra: ')
pali = []

for i,element in enumerate(palabra):
	pali.append(element)

rever_pali = pali.copy()
rever_pali.reverse()
print(pali)
print(rever_pali )

if pali == rever_pali:
	print('Es un palíndromo.')
else:
	print('NO es un palíndromo.')
