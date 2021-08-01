c0 = int(input("Ingrese un número: "))

cont = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else: 
        c0 =  3 * c0 + 1
    print(str(int(c0)))
    cont += 1
print("pasos = " + str(cont))