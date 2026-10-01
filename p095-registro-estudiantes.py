#p095-registro-estudiantes.py
#Registro y analisis de asistentes a un evento

print("\033[2J\033[H", end="")
print("Sistema de Registro para Evento\n")
print("Introduce los nombres y edades de los asistentes (* en nombre para terminar)\n")
#Listas paralelas para almacenar los datos
nombres = []
edades = []

#Ciclo para la captura de datos
while True:
    nombre = input("Nombre del asistente: ")
    if nombre == "*":
        break  #Termina el ciclo si el nombre es *
    try:
        edad = int(input(f"Edad de {nombre}: "))
        nombres.append(nombre)  #Agrega el nombre a la lista
        edades.append(edad)     #Agrega la edad en la misma posicion
    except ValueError:
        print("Por favor, introduce una edad válida (número entero).")

# --- Generación de Reportes ---
if not nombres:
    print("\nNo se registraron asistentes.")
else:
    print("\n--- Asistentes mayores de edad (18 años o más) ---")
    hay_mayores = False
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(f"{nombres[i]} ({edades[i]} años)")
            hay_mayores = True