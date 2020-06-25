name = ""
while name != "quite":

	name = input("Ingresa tu nombre completo: ").upper()
	turn = input("ingresa si sos del TT (Turno Tarde) o del TN (Turno Noche): ").upper()

	letters = "ABCDEFGHIJKLMNÑOPQRSTUVWYZ"
	ft_letra = name[0]
	 
	if (letters[0:13].find(ft_letra) >= 0 and turn == "TT") or (letters[13:25].find(ft_letra) >= 0 and turn == "TN"):
		print(f"El estudiante",name,"pertenece al grupo A")

	else :
		print(f"El estudiante",name,"pertenece al grupo B")