﻿palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
userWord = input("Ingresa una palabra: ")
# y asignarlo a la variable userWord.
userWord = userWord.upper() 

for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra == "A":
        continue 
    elif letra == "E":
        continue 
    elif letra == "I": 
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else: 
        palabraSinVocal += letra
    pass
print(palabraSinVocal)
    
