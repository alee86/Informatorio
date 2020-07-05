'''
Leer una frase y luego invierta el orden de las palabras en la frase. 
Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en 
“palabras mil por vale imagen una”.
'''

frase = str(input('Ingrese una frase para verla invrertida: '))
lista = frase.split() 
#el metodo split toma un string y lo divide segun lo que pongas en () creando una lista
lista.reverse()
for i in lista:
	print(i, end=" ")

#print(palabra)

