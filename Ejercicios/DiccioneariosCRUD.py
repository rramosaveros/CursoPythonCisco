dict = {"gato" : "perro", "dog" : "chien", "caballo" : "cheval"}

dict['gato'] = 'minou'
print(dict)

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['cisne'] = 'cygne'
print(dict)

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict.update({"pato" : "canard"})
print(dict)

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dict['perro']
print(dict)