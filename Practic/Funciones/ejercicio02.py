'''
Ejercicio 2: Tarifa del taxi
En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de 
$40.00, más $15.00 por cada 140 metros recorridos. Escriba una función que tome la distancia 
recorrida (en kilómetros) como su único parámetro y devuelva la tarifa total como su único 
resultado. Escriba un programa principal que use la función.
'''

import funciones

distancia = float(input('Ingrese la distancia en kilomentros: '))

pagar = funciones.tarifa(distancia)

print(f'El importe por el recorrido es ${round(pagar,2)}')
