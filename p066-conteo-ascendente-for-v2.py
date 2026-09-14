#p066-conteo-ascendente-for-v2.py
#Imprime los numeros de 1 a n, en incrementos de m, usando un ciclo for

print("\033[2J\033[H", end="")

print("Iniciando secuencia de conteo ascendente...")

#Entrada de datos
n = int(input("Hasta dónde? "))
m = int(input("De cuánto en cuánto? "))

#Ciclo for que recorre de 1 a n, avanzando de m en m
for i in range(1, n + 1, m):
    print(i, end=" ")

print()