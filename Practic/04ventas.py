vta_dia1 = float(input("Ingrese ventas del día 1: "))
vta_dia2 = float(input("Ingrese ventas del día 2: "))

if vta_dia1 > vta_dia2 :
	print("Se vendio más en el día 1")

elif vta_dia1 == vta_dia2:
	print("Se vendio lo mismo en ambos días")

else:
	print("Se vendio más e el día 2")