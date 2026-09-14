#p074-tablas-todas.py
#Imprime las tablas de multiplicar de la 1 hasta la n, cada una hasta el multiplo m

print("\033[2J\033[H", end="")

n = int(input("¿Hasta qué tabla de multiplicar deseas generar? "))
m = int(input("¿Hasta qué número deseas multiplicar cada tabla? "))

print("\n--- Generando Tablas de Multiplicar ---")

for i in range(1, n + 1):
    print(f"\n--- Tabla del {i} ---")
    for j in range(1, m + 1):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")