# p121-area-figuras.py
# Diccionario de diccionarios para representar figuras geométricas

import math

# Cada figura guarda sus parámetros y la fórmula del área como string
figuras = {
    "Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
    "Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
    "Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}

# Letra que usa la fórmula para cada parámetro
variables = {
    "radio": "r",
    "base": "b",
    "altura": "a",
    "largo": "l",
    "ancho": "a"
}

print('\033[H\033[J')
print('Área de Figuras Geométricas\n')

print("Calculadora de áreas de figuras geométricas")
print("Figuras disponibles:")
for k, v in figuras.items():
    print(f'{k:<10} - Fórmula: {v["formula"]}')

# Elegir figura (validada)
while True:
    fig = input('\nElige una Figura: ').strip().title()
    if fig in figuras:
        break
    print("Error: Figura no válida. Intenta de nuevo.")

# Pedir los parámetros de la figura elegida
valores = {}
for parametro in figuras[fig]:
    if parametro == "formula":
        continue
    while True:
        try:
            dato = float(input(f'{parametro.capitalize()} : '))
            if dato > 0:
                break
            print("El valor debe ser mayor que 0.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")
    valores[variables[parametro]] = dato

# Interpretar la fórmula almacenada (sin funciones integradas, solo math y los valores)
area = eval(figuras[fig]["formula"], {"__builtins__": {}, "math": math}, valores)

print(f'\nEl Área del {fig} es : {area:.4f}')