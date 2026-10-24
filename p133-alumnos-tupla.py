# p131-alumnos-tuplas.py
# Registro escolar con tuplas
alumnos = (
    ("Ana", "ISC", (9, 10, 9)),
    ("Luis", "ISW", (8, 8, 9)),
    ("Mar", "ISC", (10, 9, 10)),
)

print("--- Registro escolar ---")
print("Total:", len(alumnos))

for nombre, carrera, notas in alumnos:
    promedio = sum(notas) / len(notas)
    print(f"{nombre} ({carrera}): {promedio:.2f}")

# Consultas y cálculo de promedio
print("Primera persona:", alumnos[0][0])
print("Notas de Mar:", alumnos[-1][2])

promedios = tuple(
    (nombre, sum(notas) / len(notas))
    for nombre, _, notas in alumnos
)
print("Promedios:", promedios)

mejor = max(promedios, key=lambda x: x[1])
print("Mayor promedio:", mejor)

nombres = tuple(a[0] for a in alumnos)
print("Nombres:", nombres)