'''
Lista de funciones que vamos a usar
'''
def pitagoras(cateto_a, cateto_b):
	return (cateto_a*cateto_a + cateto_b*cateto_b)**0.5


def tarifa(distancia):
	return 40+15*(distancia*100)/140


def envio(elem):
	return 10.95 + (elem-1)*2.95


def mediana(lista):
	for i in range(0, len(lista)): 
		lista[i] = int(lista[i]) 
	
	print(lista)


def ordinales():
	numero = int(input('Ingrese un valor numerico del 1 al 12 para ver su ordinal: '))
	ordinales = ['','1º - primero', '2º - segundo', '3º - tercero', '4º - cuarto', '5º - quinto',
	'6º - sexto', '7º - séptimo', '8º - octavo', '9º - noveno', '10º - décimo', 
	'11º - decimoprimero / undécimo', '12º - decimosegundo / duodécimo']

	if numero <= 12 and numero >=1:
		print('El numero ordinal es:', ordinales[numero])
	else:
		print('El numero ordinal es:', ordinales[0])
		print('Podes acceder a los siguientes ordinales: ', ordinales)
	#podemos mejorar la presentacion, imprimiendo con un for los str en lugar d emostrar la lista


def capitalizando(msj):
	msj_new = msj.split()
	capitalizo = ''
	msj_new[0] = msj_new[0].capitalize()
	
	for i, element in enumerate(msj_new):
		
		if capitalizo == True:
			msj_new[i] = element.capitalize()
		
		if ("." in element or '?' in element or '!' in element):
			capitalizo = True
		else:
			capitalizo = False

	for i in msj_new:
		print(i, end= " ")


def primo(num):
	for i in range(2, num):
		if num%i == 0:
			evalua = False
			break
		else:
			evalua = True		
	print(evalua)


def proximo_primo(num):
	
	num +=1 #aumento en 1 el numero ingresado
	mitad = num//2
	
	evalua = False
	
	while evalua == False:
		for i in range(2, mitad):
			if num%i == 0:
				evalua = False
				break			
			else:
				evalua = True #Es un numero primo		
		num +=1
		mitad = num//2
	print(num-1)		
