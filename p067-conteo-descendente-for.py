#p067-conteo-descendente-for.py
#Imprime los numeros de 100 a 1 usando un ciclo for

print("\033[2J\033[H", end="")

print("Iniciando cuenta regresiva...")

#Ciclo for que recorre los numeros de 100 hasta 1, bajando de 1 en 1
for x in range(100, 0, -1):
    print(x, end=" ")

print()