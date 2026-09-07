#p063-conversion-temperaturas.py
continuar = "S"

while continuar == "S":

    print("\033[2J\033[H", end="")

    temperatura_inicial = int(
        input("Introduce la temperatura inicial en °C: ")
    )

    temperatura_final = int(
        input("Introduce la temperatura final en °C: ")
    )

    print("--------------------")

    celsius = temperatura_inicial

    while celsius <= temperatura_final:
        fahrenheit = (celsius * 9 / 5) + 32

        print(celsius, "°C = ", fahrenheit, "°F", sep="")

        celsius = celsius + 1

    print()
    continuar = input("¿Desea continuar (S/N)? ").upper()