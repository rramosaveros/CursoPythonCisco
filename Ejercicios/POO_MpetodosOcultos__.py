class conClase:
    def __init__(self, valor = None):
        self.var = valor

obj1 = conClase("objeto")
obj2 = conClase()

print(obj1.var)
print(obj2.var)

class connClase:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")

obj = connClase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")

obj._connClase__oculto()