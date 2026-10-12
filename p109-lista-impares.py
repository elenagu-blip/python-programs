#p109-lista-impares.py
print("\033[2J\033[H", end="")
while True:
    try:
        n = int(input("Introduzca la cantidad de números impares (n): "))
        if n > 0:
            break
        print("n debe ser mayor que 0.")
    except ValueError:
        print("Debe introducir un número entero.")

impares = [2 * i + 1 for i in range(n)]

print("\n--- Generación de Lista ---")
print(f"Lista de los primeros {n} números impares: {impares}")

suma = sum(impares)
promedio = suma / n
print("\n--- Cálculos ---")
print(f"Suma de los números: {suma}")
print(f"Promedio de los números: {promedio}")

div3 = [x for x in impares if x % 3 == 0]
print("\n--- Divisibles entre 3 ---")
print(f"Números divisibles entre 3: {div3}")
print(f"Suma de los números divisibles entre 3: {sum(div3)}")

print("\n--- Búsqueda ---")
try:
    buscar = int(input("Introduzca elemento a buscar: "))
    if buscar in impares:
        print(f"Result: El elemento {buscar} está en la lista en la posición (índice) {impares.index(buscar)}.")
    else:
        print(f"Result: El elemento {buscar} no está en la lista.")
except ValueError:
    print("Result: Debe introducir un número entero.")