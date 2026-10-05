#p100-normalizar-nombres.py
#Limpia nombres mediante una comprension

print("\033[2J\033[H", end="")

nombres = [' ana', 'LUIS ', '', ' maría josé ', 'Pedro']
normalizados = [nombre.strip().title() for nombre in nombres if nombre.strip()]

print(f"Datos originales: {nombres}")
print(f"Nombres normalizados: {normalizados}")