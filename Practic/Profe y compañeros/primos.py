



N = int(input("INGRESE EL NUMERO: \t"))
primo = True
c = 2

while primo and (c < N):
    if N % c == 0:
        primo = False
    c+=1


if primo:
    print("EL NUMERO ES PRIMO")
else:
    print("EL NUMERO NO ES PRIMO")
