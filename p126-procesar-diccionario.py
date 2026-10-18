# p126-procesar-diccionario.py
# Crear un diccionario a partir de dos listas y procesarlo

print('\033[H\033[J')

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))

print("Diccionario de nómina:")
print(nomina)

print("\n--- Iterando Llaves (keys) ---")
for llave in nomina.keys():
    print(llave)

print("\n--- Iterando Valores (values) ---")
for valor in nomina.values():
    print(valor)

print("\n--- Iterando Llave y Valor (accediendo por llave) ---")
for llave in nomina:
    print(f"{llave} -> {nomina[llave]}")

print("\n--- Iterando Llave y Valor (items) ---")
for par in nomina.items():
    print(par)

suma = sum(nomina.values())
promedio = suma / len(nomina)

print("\n--- Cálculos ---")
print(f"Suma total de sueldos: {suma:.2f}")
print(f"Promedio de sueldos: {promedio:.2f}")