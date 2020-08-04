'''
Ejercicio 1: Triángulos
Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo
 rectángulo como sus parámetros y devuelva la hipotenusa del triángulo, calculada usando 
 el teorema de Pitágoras, como resultado de la función. Incluya un programa principal que 
 lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, use su 
 función para calcular la longitud de la hipotenusa y muestre el resultado.
'''
import funciones

a = int(input('ingrese el valor de a: '))
b = int(input('ingrese el valor de b: '))

diagonal = funciones.pitagoras(a, b)

print(f'La hipotenusa es {round(diagonal,2)}')