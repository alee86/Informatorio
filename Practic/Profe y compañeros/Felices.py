numero = input("ingrese un numero pa saber: ")
inicio = True

while inicio:

    print(numero)
    suma = 0

    for n in numero:
        potencia = int(n)** 2
        suma = suma + potencia

    numero = str(suma)

    if (numero == "1"):
        print(numero)
        print("ES FELIZ!!")
        inicio = False
    elif (numero == "4"):
        print(numero)
        print("F!!")
        inicio = False