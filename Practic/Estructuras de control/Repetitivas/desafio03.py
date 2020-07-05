'''
DESAFÍO 3
En una tienda de descuento por reciclado las personas que van a pagar el importe de 
su compra llegan a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad 
que lleven en la caja le entregan un código de descuento que se aplicará sobre el total 
de su compra. Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta 
que cierra. 

Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es 
amarilla un 25% y si es blanca no obtendrá descuento.
'''

tapitas = int(input("Indique la cantidad de tapitas recicladas: "))
cuenta = int(input("De cuanto es su compraadas: "))
tapitas_total = 0
q_ventas = 0
ventas_total = 0
vta = True
respuesta =""

while vta == True:

	if tapitas >= 40:
		descuento = 0.4
	elif tapitas < 40 and tapitas > 25:
		descuento = 0.25
	else:
		descuento = 0

	tapitas_total += tapitas
	q_ventas += 1
	ventas_total += cuenta*(1-descuento)

	print(f"""
		Su descuento es de {descuento*100}%
		Total a pagar es {cuenta*(1-descuento)}
		------------------------------------------------
		Total de tapitas recolectas: 	{tapitas_total}
		Cantidad de ventas realizadas: 	{q_ventas}
		Dinero recaudado: 				$ {ventas_total}
		------------------------------------------------
		""")
	respuesa = input("Quiere registrar otra venta? S/N")
	if respuesa == "S":
		vta = True
	elif respuesa == "NO":
		vta = False
	

