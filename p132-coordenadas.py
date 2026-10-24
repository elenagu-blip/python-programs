# p130-coordenadas.py
# Registro de coordenadas
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

print("--- Coordenadas ---")
print("Tipo:", type(zacatecas))
print("Ciudad:", zacatecas[0])
print("Latitud:", zacatecas[1])
print("Longitud:", zacatecas[-1])

nombre, lat, lon = zacatecas
print(f"{nombre}: ({lat}, {lon})")

for lugar in (zacatecas, guadalupe):
    print(lugar[0], "->", lugar[1:])

# Desempaquetar coordenadas
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe

# Punto medio aproximado
centro = (round((lat1 + lat2) / 2, 2),
          round((lon1 + lon2) / 2, 2))
print("Punto medio:", centro)

# Verificar pertenencia
print("Zacatecas" in zacatecas)

# Crear otra tupla con datos extra
ampliada = zacatecas + ("ZAC",)
print("Ampliada:", ampliada)
print("Original:", zacatecas)