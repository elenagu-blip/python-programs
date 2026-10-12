#p106-mes-día-nombre.py
print("\033[2J\033[H", end="")
nombres = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
           "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        mes = int(input("Introduzca un número de mes (1-12): "))
    except ValueError:
        print("Debe introducir un número entero.")
        continue
    if 1 <= mes <= 12:
        break
    print("El mes debe estar entre 1 y 12.")

print("\n--- Resultados ---")
print(f"Mes: {nombres[mes - 1]}")
print(f"Días: {dias[mes - 1]}")