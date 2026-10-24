# p133-coordenadas-tuplas.py
# Coordenadas de ciudades representadas con tuplas

zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

# Mostrar las tuplas y su tipo
print(f"Tupla Zacatecas: {zacatecas}, Tipo: {type(zacatecas)}")
print(f"Tupla Guadalupe: {guadalupe}, Tipo: {type(guadalupe)}")

# Acceso por índices positivos y negativos
print("Acceso por índices (Zacatecas):")
print(f"Positivos -> Nombre: {zacatecas[0]}, Latitud: {zacatecas[1]}, Longitud: {zacatecas[2]}")
print(f"Negativos -> Nombre: {zacatecas[-3]}, Latitud: {zacatecas[-2]}, Longitud: {zacatecas[-1]}")

# Desempaquetar cada tupla
nombre_z, lat_z, lon_z = zacatecas
nombre_g, lat_g, lon_g = guadalupe
print(f"{nombre_z}: ({lat_z}, {lon_z})")
print(f"{nombre_g}: ({lat_g}, {lon_g})")

# Recorrer ambas ubicaciones y obtener las coordenadas con slicing
for ubicacion in (zacatecas, guadalupe):
    print(f"Ubicación: {ubicacion[0]}, Coordenadas: {ubicacion[1:]}")

# Punto medio aproximado
lat_medio = round((lat_z + lat_g) / 2, 2)
lon_medio = round((lon_z + lon_g) / 2, 2)
print(f"Punto medio aproximado: ({lat_medio}, {lon_medio})")

# Nueva tupla con el código (la original no cambia)
zacatecas_codigo = zacatecas + ("ZAC",)
print(f"Nueva tupla Zacatecas: {zacatecas_codigo}")
print(f"Original sin cambios: {zacatecas}")

# Pertenencia
print(f"'Zacatecas' pertenece a la tupla: {'Zacatecas' in zacatecas}")

# Nota: Intentar modificar un elemento directamente, por ejemplo
# zacatecas[1] = 23.0, arroja TypeError porque las tuplas son inmutables.