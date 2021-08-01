numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input("Adivina el número secreto: "))

while numero != numeroSecreto: 
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numero = int(input("Intenta adivinar nuevamente"))
print("¡Bien hecho, muggle! Eres libre ahora")