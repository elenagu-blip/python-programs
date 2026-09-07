#p065-verificar-palindromo.py
continuar = "S"

while continuar == "S":

    print("\033[2J\033[H", end="")

    numero = int(
        input("Introduce un número para verificar si es palíndromo: ")
    )

    numero_original = numero
    numero_auxiliar = numero
    numero_invertido = 0

    while numero_auxiliar > 0:
        digito = numero_auxiliar % 10

        numero_invertido = numero_invertido * 10 + digito

        numero_auxiliar = numero_auxiliar // 10

    if numero_original == numero_invertido:
        print("El número", numero_original, "es un palíndromo.")
    else:
        print("El número", numero_original, "no es un palíndromo.")

    print()
    continuar = input("¿Desea continuar (S/N)? ").upper()