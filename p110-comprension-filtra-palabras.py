#p110-comprension-filtra-palabras.py
print("\033[2J\033[H", end="")
palabras = input("Introduzca palabras separadas por espacios: ").split()

# Comprensión de listas: más de 4 caracteres, en mayúsculas
filtradas = [p.upper() for p in palabras if len(p) > 4]

print("\n--- Resultados ---")
print(f"Lista original: {palabras}")
print(f"Lista filtrada (>4 caracteres en mayúsculas): {filtradas}")