"""
Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. 
"""


total = 0
descuento = 0

while True:
	importe = int(input("Ingrese el importe de la compra: $"))
	total += importe
if total>1000:
	descuento = 0.15

print(f"""
	Total de compras ${total}
	Descuento {descuento*100}%
	---------------------------
	Total a abonar {total - total*descuento}
	""")
