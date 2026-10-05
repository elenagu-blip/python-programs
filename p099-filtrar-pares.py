#p099-filtrar-pares.py
#Filtra numeros pares con una comprension

print("\033[2J\033[H", end="")
print("Filtro de números pares\n")

cantidad = int(input("¿Cuántos números capturarás? "))

numeros = []
for i in range(cantidad):
    numeros.append(int(input(f"Número {i + 1}: ")))

pares = [numero for numero in numeros if numero % 2 == 0]

print(f"Lista original: {numeros}")
print(f"Números pares: {pares}")
print(f"Cantidad de pares: {len(pares)}")