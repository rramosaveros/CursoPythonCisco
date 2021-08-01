def isPrime(num):
    div = num
    cont = 0
    if num > 1: 
        while div >= 1:
            if num % div == 0:
                cont += 1
            div -= 1
    if cont ==  2:
        return True
    else: 
        return False
            
#
# coloca tu código aquí
#

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")

