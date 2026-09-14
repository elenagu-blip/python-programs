#p080-compara-rendimiento-inversion.py
#Compara el crecimiento de dos fondos de inversion a lo largo de varios anios

print("\033[2J\033[H", end="")

#Entrada de datos del Fondo A
print("--- Fondo de Inversión A ---")
monto_inicial_a = float(input("Monto inicial: "))
tasa_a = float(input("Tasa de interés anual (%): "))

print()

#Entrada de datos del Fondo B
print("--- Fondo de Inversión B ---")
monto_inicial_b = float(input("Monto inicial: "))
tasa_b = float(input("Tasa de interés anual (%): "))

print()

#Numero de anios a proyectar
anios = int(input("Años a proyectar: "))

print()
print("--- Comparación de Rendimientos Anuales ---")
print("Año | Fondo A       | Fondo B")
print("-" * 43)

#Variables que van acumulando el crecimiento de cada fondo, anio tras anio
capital_a = monto_inicial_a
capital_b = monto_inicial_b

#Ciclo for que recorre cada anio, del 1 hasta el total de anios a proyectar
for anio in range(1, anios + 1):
    #Se le suma a cada capital el interes ganado ese anio (interes compuesto)
    capital_a = capital_a + capital_a * (tasa_a / 100)
    capital_b = capital_b + capital_b * (tasa_b / 100)
    print(f"{anio:2} | $ {capital_a:9.2f} | $ {capital_b:9.2f}")

print()

#Comparacion final: se revisa cual capital termino siendo mayor
if capital_a > capital_b:
    print(f"Resultado final: El Fondo A (${capital_a:.2f}) superó al Fondo B (${capital_b:.2f}).")
elif capital_b > capital_a:
    print(f"Resultado final: El Fondo B (${capital_b:.2f}) superó al Fondo A (${capital_a:.2f}).")
else:
    print(f"Resultado final: Ambos fondos quedaron empatados con (${capital_a:.2f}).")