# p050-conteo-numeros.py
# Lee números hasta ingresar 999, luego, muestra un resumen estadístico

print("\033[2J\033[H", end="")

cuenta = 0
suma = 0
cuenta_positivos = 0
cuenta_negativos = 0
cuenta_ceros = 0

print("Analizador de Números (escribe 999 para finalizar)")

while True:
    num = int(input('Introduce un número entero: '))
    
    if num == 999:  # Condición de salida
        print("Detectado código de salida (999)")
        break  # Rompe el ciclo infinito.
    
    # Proceso
    cuenta += 1
    suma += num
    if num > 0:
        cuenta_positivos += 1
    elif num < 0:
        cuenta_negativos += 1
    else:
        cuenta_ceros += 1

# Resumen estadístico
print("\n--- Resumen Estadístico ---")
print(f"Cantidad de números ingresados: {cuenta}")
if cuenta > 0:
    print(f"Suma total: {suma}")
    print(f"Promedio: {suma / cuenta:.2f}")
else:
    print("No se ingresaron números.")
print(f"Números positivos: {cuenta_positivos}")
print(f"Números negativos: {cuenta_negativos}")
print(f"Números en cero: {cuenta_ceros}")