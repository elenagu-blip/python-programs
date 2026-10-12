#p105-listas-multiplica.py
print("\033[2J\033[H", end="")
def leer_lista(nombre):
    """Lee exactamente 5 números separados por espacios."""
    while True:
        texto = input(f"Introduzca 5 números para la Lista {nombre}: ").split()
        if len(texto) != 5:
            print("Debe introducir exactamente 5 números.")
            continue
        try:
            return [int(x) if x.lstrip("-").isdigit() else float(x) for x in texto]
        except ValueError:
            print("Todos los elementos deben ser numéricos.")


lista_a = leer_lista("A")
lista_b = leer_lista("B")

lista_c = [lista_a[i] * lista_b[i] for i in range(5)]

print("\n--- Resultados ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C (A * B): {lista_c}")