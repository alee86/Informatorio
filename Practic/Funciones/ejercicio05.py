'''
Ejercicio 5: De número entero a número ordinal
Las palabras como primero, segundo y tercero se refieren a números ordinales. En este ejercicio, 
escribirá una función que toma un número entero como su único parámetro y devuelve una cadena que 
contiene el número ordinal apropiado como único resultado. Su función debe manejar los enteros 
entre 1 y 12 (inclusive). Debería devolver una cadena vacía si se proporciona un valor fuera de este 
rango como parámetro. Incluya un programa principal que utilice su función mostrando cada número entero 
del 1 al 12 y su número ordinal.
'''
import funciones

numero = int(input('Ingrese un valor numerico del 1 al 12 para ver su ordinal: '))

ordi = funciones.ordinales(numero)