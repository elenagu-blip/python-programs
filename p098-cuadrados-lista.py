#p098-cuadrados-lista.py
#Genera los cuadrados de una lista de numeros usando una comprension

print("\033[2J\033[H", end="")
print("Cuadrados de números\n")

n = int(input("¿Hasta qué número? "))

numeros = list(range(1, n + 1))
cuadrados = [numero ** 2 for numero in numeros]

print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")