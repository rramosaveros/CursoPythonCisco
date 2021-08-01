# ejemplos de prueba aquí
class conClase:
    varia = 2
    def metodo(self):
        print(self.varia, self.var)

obj = conClase()
obj.var = 3
obj.metodo()

class connClase():
    def otro(self):
        print("otro")

    def metodo(self):
        print("método")
        self.otro()

obj = connClase()
obj.metodo()