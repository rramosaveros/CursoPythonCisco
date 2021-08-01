miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
miListaAuxiliar = []
#
# coloca tu código aquí
for numero in miLista: 
    if (numero in miListaAuxiliar) == False: 
        miListaAuxiliar.append(numero)
#
print("La lista solo con elementos únicos:")
print(miListaAuxiliar)