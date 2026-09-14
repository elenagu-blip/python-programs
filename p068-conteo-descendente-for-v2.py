#p068-conteo-descendente-for-v2.py
#Imprime los numeros de n a 1, en decrementos de m, usando un ciclo for

print("\033[2J\033[H", end="")

print("Iniciando cuenta regresiva...")

#Entrada de datos
n = int(input("Desde dónde? "))
m = int(input("De cuánto en cuánto? "))

#Ciclo for que recorre desde n hasta 1, bajando de m en m
for x in range(n, 0, -m):
    print(x, end=" ")

print()