#p111-comprension-pares-cuadrados.py
print("\033[2J\033[H", end="")
while True:
    try:
        n = int(input("Introduzca el límite n: "))
        if n > 0:
            break
        print("n debe ser mayor que 0.")
    except ValueError:
        print("Debe introducir un número entero.")

rango = list(range(1, n + 1))

# Comprensión de listas: cuadrados solo de los pares
cuadrados = [x ** 2 for x in rango if x % 2 == 0]

print("\n--- Resultados ---")
print(f"Lista original (1 a {n}): {rango}")
print(f"Cuadrados de números pares: {cuadrados}")
print(f"Suma de cuadrados: {sum(cuadrados)}")