numerador = int(input("inresar el numerador: "))
denominador = int(input("Ingresar el denominador: "))
resultado = 0

while  numerador >= denominador:
	numerador = numerador - denominador
	resultado = resultado + 1
	
print(f"El cociente es: "{resultado})
print(f"El resto es: "{numerador})



'''
a = int(input("Tirate un número wachín: "))
b = int(input("Dividilo por: "))

control = b
resultado = 0

while control <= a:
  control = control + b
  resultado = resultado + 1

print("¡El resultado es ", resultado, " pibe! aprende a dividir gil.")
'''