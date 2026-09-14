#p078-combina-colores.py
#Genera todas las combinaciones posibles de dos colores, sin repetir un color consigo mismo

print("\033[2J\033[H", end="")
print("--- Generador de Combinaciones de Colores ---\n")

#Entrada de datos: el usuario escribe los colores separados por comas
colores = input("Ingresa los colores separados por comas: ").strip().split(',')

print(f"\nColores base: {colores}")
print("--- Combinaciones Posibles ---")

#Bucle exterior: toma el primer color de la combinacion
for color1 in colores:
    #Bucle interior: toma el segundo color de la combinacion
    for color2 in colores:
        #Evitamos combinar un color consigo mismo
        if color1 != color2:
            print(f"- {color1} y {color2}")