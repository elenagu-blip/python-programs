#p108-ciudades.py
print("\033[2J\033[H", end="")
import unicodedata

ciudades = []

while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ").strip()
    if ciudad == "$":
        break
    if ciudad:
        ciudades.append(ciudad)


def inicia_con_consonante(texto):
    """True si la primera letra es una consonante (ignora acentos)."""
    primera = unicodedata.normalize("NFD", texto[0])[0].lower()
    return primera.isalpha() and primera not in "aeiou"


descendente = sorted(ciudades, reverse=True)
con_consonante = [c for c in ciudades if inicia_con_consonante(c)]

print("\n--- Resultados ---")
print(f"Total de ciudades introducidas: {len(ciudades)}")
print(f"Lista original: {ciudades}")
print(f"Lista ordenada descendente: {descendente}")
print(f"Ciudades que inician con consonante: {len(con_consonante)}")
print(f"Lista de ciudades con consonante inicial: {con_consonante}")