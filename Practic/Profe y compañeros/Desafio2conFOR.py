 
Personas = int(input("INGRESE CUANTAS PERSONAS SON: \t")) 
Grupo_menos_100 = 0 
Grupo_entre = 0 
Grupo_mas_200 = 0 


for persona in range(1,Personas+1):
	Colillas_recolectadas = int(input("Ingrese cantidad de colillas recolectadas de la persona numero: " 
									  + str(persona) +"\t"))
	if Colillas_recolectadas < 100:   
		Grupo_menos_100 = Grupo_menos_100 + 1 
	elif Colillas_recolectadas < 200:
		Grupo_entre = Grupo_entre + 1
	else:  
		Grupo_mas_200 = Grupo_mas_200 + 1 
	 

Porcentaje_100 = (Grupo_menos_100 * 100) / Personas
Porcentaje_entre = (Grupo_entre * 100) / Personas
Porcentaje_200 = (Grupo_mas_200 * 100) / Personas
print("La cantidad de personas que recolectaron colillas fueron:", Personas)  
print("Las personas que recolectaron menos de 100 colillas fueron:", Porcentaje_100, "% sobre el total")  
print("Las personas que recolectaron entre 100 y 200 colillas fueron:", Porcentaje_entre, "% sobre el total")
print("Las personas que recolectaron mas de 200 colillas fueron:", Porcentaje_200, "% sobre el total") 
		
		
	



 
