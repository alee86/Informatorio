'''

#Listas

personas = [
			['nico',24],
			['pedro',27],
			['maria',30],
			['clara',22],
			['franco',24],
			['lucia',28]
			]

contador = 1
for i in personas:
	print(contador, end=" - ")
	print("Nombre:",i[0].capitalize(), end=" ")
	print("Edad:",i[1])
	contador +=1
'''



'''

	x = list()

while True:
	nombre = input("ingrese nombre del alumno: ")
	edad = int(input("ingrese su edad: "))
	persona = [nombre,edad]
	x.append(persona)
	continuar = input("quiere continuar? Si o No: ")
	if continuar.lower() == "no":
		break


print(x)

'''



'''
Nicolás Tortosa16:48
cargar una lista con el nonbre, sexo y edad de todo el curso

a) mostrar la lista de asistencia ordenada por nombre
b) mostrar el nombre del alumno de mayor y menor edad
c) mostrar el promedio de edad del curso
d) mostrar el promediode edad del sexo femenino y masculino

'''


personas = list()

while True:
	nombre = input("Ingrese el nombre del alumno: ")
	sexo = int("Indique sexo del a (M o F): ").upper()
	#if sexo != "M" or sexo != "F":
	#	print("ingrese M o F")

	edad = int(input("Indique la edad del alumno:"))
	alumno = [nombre, sexo, edad]
	personas.append(alumno)
	seguir = input("Desea ingresar otro alumno? (S)i o (N)o")

