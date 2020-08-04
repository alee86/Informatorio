'''
Ejercicio 12: Próximo Siguiente
En este ejercicio creará una función llamada proximo_primo que encuentra y devuelve el primer número 
primo mayor que algún número entero, n. El valor de n se pasará a la función como su único parámetro. 
Incluya un programa principal que lea un número entero del usuario y muestre el primer número primo mayor 
que el valor ingresado.

lista de num primos (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
79, 83, 89 y 97)
'''
from funciones import proximo_primo	


num = int(input('Ingresa un numero: '))
proximo_primo(num)
