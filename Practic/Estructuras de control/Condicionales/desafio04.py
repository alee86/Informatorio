'''
Tenemos que decidir entre 2 recetas ecológicas. 
Los ingredientes para cada tipo de receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.
Ingredientes Receta 1: Lentejas y apio.
Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, 
y en función de su respuesta le muestre un menú con los ingredientes 
disponibles para que elija. Solo se puede eligir 3 ingrediente 
(entre la receta elegida y los comunes.) y el tipo de receta. 
Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.

'''

ingredientes_receta1 = "Lenjetas y Apio"
ingredientes_receta2 = "Morrón y Cebolla"

print ("""
*******************************
Menu:
Receta 1: Lentejas y Apio.
Receta 2: Morrón y Cebolla.
*******************************
""")

receta = int(input("Indique si quiere la receta (1) o (2): "))
comun = int(input("Queres agregar Verduras (1) o Berenjenas (2)?"))


if comun == 1:
	comun = "Verduras"

else:
	comun = "Berenjenas"

if receta == 1:
	receta = ingredientes_receta1

else:
	receta = ingredientes_receta2


print(f"Su plato tiene los siguientes ingredientes: {comun}, {receta}.")