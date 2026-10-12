# p116-conversion-divisas.py
# Conversor de divisas a pesos mexicanos usando diccionarios

# Tasas de cambio a MXN
conversiones = {
    'USD': 20.50,
    'EUR': 22.30,
    'GBP': 25.80,
    'JPY': 0.19,
    'CAD': 16.20
}

print('\033[H\033[J')
print("Conversor de monedas a pesos mexicanos (MXN)")

# Mostrar opciones
print("\nOpciones de monedas: ")
for moneda in conversiones:
    print(f"- {moneda} ")

# Entrada y validación de la moneda
while True:
    moneda = input("\nIngrese la moneda a convertir: ").strip().upper()
    if moneda in conversiones:
        break
    else:
        print("Moneda no válida. Intente de nuevo.")

# Entrada y validación de la cantidad
while True:
    try:
        cantidad = float(input(f"Ingrese la cantidad en {moneda}: "))
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser un número positivo. Intente de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número (ej. 150.50).")

# Cálculo y salida
resultado = cantidad * conversiones[moneda]

print(f"{cantidad:,.2f} {moneda} son {resultado:,.2f} MXN")