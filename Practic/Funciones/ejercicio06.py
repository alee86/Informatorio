'''
Ejercicio 6: Centrar una cadena en la terminal
Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de la terminal 
en caracteres como segundo parámetro. Su función debe devolver una nueva cadena que consta de la cadena 
original y el número correcto de espacios iniciales para que la cadena original aparezca centrada dentro 
el ancho proporcionado cuando se imprima. No agregue ningún carácter al final de la cadena. Incluya 
un programa principal que use su función.
'''

def centrando(cadena, largo):
		
		espacio_blanco = "*"*((largo - len(cadena))//2) #el * es colo para ver como toma los espacios
		return espacio_blanco+cadena+espacio_blanco
	

cadena = input('Ingresa una palabra: ')
largo = int(input('Ingresa el largo parder centrarla: '))


print(centrando(cadena, largo))
