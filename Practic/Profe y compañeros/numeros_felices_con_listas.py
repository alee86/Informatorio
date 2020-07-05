numero = int(input("numero feliz:"))
primernumero = numero
lista = []
counter = True

while counter:
    total = 0
    if numero != 1:
        for i in str(numero):
            parcial = int(i)**2
            total = total + parcial
        numero = total
        for j in lista:
            if (total == j):
                flag = "No es feliz"
                counter = False
        lista.append(numero)
    else:
        flag = "Es Feliz"
        break
    print(numero)

print(primernumero,flag)
