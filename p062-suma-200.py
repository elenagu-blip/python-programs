#p062-suma-200.py
continuar = "S"

while continuar == "S":

    print("\033[2J\033[H", end="")

    suma = 0
    contador = 0

    while suma < 200:
        print("Suma actual:", suma, end="")
        numero = int(input(". Introduce un número: "))

        suma = suma + numero
        contador = contador + 1

    print("--------------------")
    print("Meta de 200 alcanzada.")
    print("Suma final:", suma)
    print("Total de números introducidos:", contador)
    print()

    continuar = input("¿Desea continuar (S/N)? ").upper()