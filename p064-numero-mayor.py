continuar = "S"

while continuar == "S":

    print("\033[2J\033[H", end="")

    print("Introduce números (0 para terminar):")

    numero = int(input("> "))

    if numero != 0:
        mayor = numero

        while numero != 0:

            if numero > mayor:
                mayor = numero

            numero = int(input("> "))

        print("--------------------")
        print("El número mayor fue:", mayor)

    else:
        print("--------------------")
        print("No se introdujeron números.")

    print()
    continuar = input("¿Desea continuar (S/N)? ").upper()