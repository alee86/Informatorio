

total = 0
importe=(int(input("ingrese importe: ")))
while  importe!=0: 
	print("ingrese la opcion que corresponde con el codigo de descuento")
	print("1: Codigo Rojo")
	print("2: Codigo Amarillo")
	print("3: Codigo Blanco")
	codigo=(int(input("")))
	if codigo==1:
		descuento=(importe*25)/100
		print("el total a pagar es:", importe-descuento)
		total = total + importe - descuento
	elif codigo==2:
		descuento=(importe*40)/100
		print("el total a pagar es:", importe-descuento)
		total = total + importe - descuento
	else:
		print("el total a pagar es:", importe)
		total =  total + importe

	importe=int(input("ingrese importe: (si desea salir ingrese 0)"))

print("LA VENTA TOTAL DEL DIA ES: \t" + str(total))