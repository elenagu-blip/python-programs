#p060-pares-descendente.py
continuar = "S"

while continuar == "S":

    print("\033[2J\033[H", end="")

    limite = int(input("Introduce un número límite (menor a 100): "))

    numero = 100
    suma = 0

    print("Números pares: ", end="")

    while numero >= limite:
        print(numero, end="")
        suma = suma + numero
        numero = numero - 2

        if numero >= limite:
            print(", ", end="")

    print()
    print("La suma de los pares es:", suma)
    print()

    continuar = input("¿Desea continuar (S/N)? ")