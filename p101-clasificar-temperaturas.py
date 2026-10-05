#p101-clasificar-temperaturas.py
#Clasifica datos con una expresion condicional

print("\033[2J\033[H", end="")

temperaturas = [8, 14, 18, 22, 27, 35]
clasificacion = [
    'Fría' if t < 15 else
    'Templada' if t <= 25 else
    'Caliente'
    for t in temperaturas
]

print(f"Temperaturas: {temperaturas}")
print(f"Clasificación: {clasificacion}")