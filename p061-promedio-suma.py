#p061-promedio-suma.py
continuar = "S"

while continuar == "S":

    print("\033[2J\033[H", end="")

    suma = 0
    contador = 0

    print("Introduce números (0 para terminar):")
    numero = int(input("> "))

    while numero != 0:
        suma = suma + numero
        contador = contador + 1
        numero = int(input("> "))

    print("--------------------")
    print("Se introdujeron", contador, "números.")
    print("La suma es:", suma)

    if contador > 0:
        promedio = suma / contador
        print("El promedio es:", promedio)
    else:
        print("El promedio es: 0")

    print()
    continuar = input("¿Desea continuar (S/N)? ")