'''
La ciudad esta dividida en 2 secciones de recolección sección A y B 
de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a 
M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.




centrico = True
barrio = ""
letters = "ABCDEFGHIJKLMNÑOPQRSTUVWYZ"

consulta = input("Es tu barri centrico? S/N: ").upper()

while consulta != ("S" or "N"):
	print("Ingrese S para SÍ o N para NO")
	consulta = input("Es tu barri centrico? S/N: ").upper()		
if consulta == "S":
		centrico = True
elif consulta == "N":
	centrico = False

barrio = input("Ingresa el nombre de tu barrio: ").upper()

#Seccion A (Barrios centros de A-M y Barriso No centricos de N-Z)
if letters[0:13].find(barrio[0]) >= 0 and centrico == True:
	print(f'El barrio {barrio} pertenece a la seccion A')
elif letters[13:26].find(barrio[0]) >= 0 and centrico == False:
	print(f'El barrio {barrio} pertenece a la seccion A')
else:
	print(f'El barrio {barrio} pertenece a la seccion B')


'''



centrico = True
barrio = ""
letters = "ABCDEFGHIJKLMNÑOPQRSTUVWYZ"

consulta = input("Es tu barri centrico? S/N: ").upper()

while consulta != ("S" or "N"):
	print("Ingrese S para SÍ o N para NO")
	consulta = input("Es tu barri centrico? S/N: ").upper()		
if consulta == "S":
		centrico = True
elif consulta == "N":
	centrico = False

barrio = input("Ingresa el nombre de tu barrio: ").upper()

#Seccion A (Barrios centros de A-M y Barriso No centricos de N-Z)
if letters[0:13].find(barrio[0]) >= 0 and centrico == True:
	print(f'El barrio {barrio} pertenece a la seccion A')
elif letters[13:26].find(barrio[0]) >= 0 and centrico == False:
	print(f'El barrio {barrio} pertenece a la seccion A')
else:
	print(f'El barrio {barrio} pertenece a la seccion B')