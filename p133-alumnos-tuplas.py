# p134-alumnos-tuplas.py
# Registro escolar modelado con tuplas anidadas

alumnos = (
    ("Ana", "ISC", (9, 10, 9, 8)),
    ("Luis", "ISW", (8, 8, 9, 10)),
    ("Mar", "ISC", (10, 9, 10, 10))
)

print(f"Registros de alumnos: {alumnos}")
print(f"Total de alumnos: {len(alumnos)}")

# Desempaquetado y promedio de cada alumno
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Nombre: {nombre}, Carrera: {carrera}, Promedio: {promedio:.2f}")

# Nueva tupla con pares (nombre, promedio)
pares = tuple((a[0], sum(a[2]) / len(a[2])) for a in alumnos)
print(f"Pares (nombre, promedio): {pares}")

mejor = max(pares, key=lambda par: par[1])
print(f"Alumno con mejor promedio: {mejor[0]} con {mejor[1]:.2f}")

# Índices de tuplas anidadas, count() e index()
for alumno in alumnos:
    nombre = alumno[0]
    califs = alumno[2]
    conteo = califs.count(10)
    indice = califs.index(califs[0])  # posición de la primera calificación
    print(f"{nombre} -> Conteo de 10s: {conteo}, Índice de primera calificación: {indice}")

# Ordenar por promedio de menor a mayor
ordenados = tuple(sorted(pares, key=lambda par: par[1]))
print(f"Ordenados por promedio: {ordenados}")

# Nueva tupla con Eva, sin modificar la original
nuevos = alumnos + (("Eva", "ISC", (9, 9, 10)),)
print(f"Tupla original intacta: {alumnos}")
print(f"Nueva tupla con Eva: {nuevos}")