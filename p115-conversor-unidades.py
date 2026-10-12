# p115-conversor-unidades.py
# Conversor de unidades de longitud usando diccionarios

print('\033[H\033[J')
print('Conversor de unidades de longitud usando diccionarios\n')

# Factores para convertir a metros
conversiones = {
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}

# Entrada: longitud (número)
while True:
    try:
        longitud = float(input("Dame la longitud ? "))
        break
    except ValueError:
        print("Debe ingresar un número. Intente de nuevo.")

# Validación: la unidad debe ser una llave válida
while True:
    unidad = input("Unidad (km, m, cm ,mm) ? ").strip().lower()
    if unidad in conversiones:
        break
    else:
        print("Unidad no válida. Intente de nuevo.")

# Cálculo y salida
resultado = longitud * conversiones[unidad]

print(f"{longitud:,.2f} {unidad} son {resultado:,.2f} metros")