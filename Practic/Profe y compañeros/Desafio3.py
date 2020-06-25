'''Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad 
de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la 
utilización de fertilizantes.'''


print("Iniciando programa para calculo de utilización de fertilizantes.")

hectarea = bool(int(input("¿Usted ya midio el suelo?\n\t 1- Verdadero \n\t 0- Falso\n")))



if hectarea:
	compuesto = bool(int(input("¿El compuesto existe en al menos de 10% por hectarea?\n\t 1- Verdadero \n\t 0- Falso\n")))
	vegetacion = bool(int(input("¿Existe vegetacion del tipo Matorral?\n\t 1- Verdadero \n\t 0- Falso\n ")))
	if compuesto and vegetacion:
			print("El uso de del fertilizante es factible.")
	elif compuesto and vegetacion:
			print("Debe exterminar la vegetacion del tipo Matorral para que el fertilizante sea factible. ")
	elif compuesto and vegetacion:
			print("Procure que almenos usar el fertilizante cubra un 10", "% " ,"de la hectarea para que sea factible usarlo. ")
	else:
		print("Procure que almenos usar el fertilizante cubra un 10", "% " ,"de la hectarea para que sea factible usarlo." ,"\n\t y ", "\n Debe exterminar la vegetacion del tipo Matorral para que el fertilizante sea factible. ")
else:
	print("Mida el suelo primero y luego vuelva a iniciar el programa. ")
	



