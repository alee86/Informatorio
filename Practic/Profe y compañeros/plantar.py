def separar(lista):
	aux=list()
	l1=list()
	l2=list()
	

	for i in lista:
		if i[1]>100:
			l1.append(i[0])
		

		else:
			l2.append(i[0])
			
	l1.sort()
	l2.sort()
	print("Ciudades que plantaron mas de 100 arboles: ")
	print(l1)
	print("Ciudades que plantaron menos de 100 arboles: ")
	print(l2)
	



lista1=[["Resistencia",200],["Barranqueras",30],["Basail",125],["Reconquista",15],["Villa Ocampo", 23], ["Fontana",140],["San Cosme",12]]

separar(lista1)