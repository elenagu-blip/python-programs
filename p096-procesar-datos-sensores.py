#p096-procesar-datos-sensores.py
#Simulacion de recoleccion y procesamiento de datos de sensores

print("\033[2J\033[H", end="")

import random

print("Simulando la recolección de datos de dos sensores...")

sensor_a_datos = []
sensor_b_datos = []

for i in range(10):
    sensor_a_datos.append(random.randint(1, 100))  #Llena la lista del sensor A
    sensor_b_datos.append(random.randint(1, 100))  #Llena la lista del sensor B

print("\n--- Datos Originales de los Sensores ---")
print(f"Sensor A: {sensor_a_datos}")
print(f"Sensor B: {sensor_b_datos}")

datos_combinados = []

for i in range(10):
    #Elevamos al cuadrado la medicion de cada sensor en esta posicion
    sensor_a_datos[i] = sensor_a_datos[i] ** 2
    sensor_b_datos[i] = sensor_b_datos[i] ** 2
    #Sumamos ambas mediciones ya transformadas, y la guardamos en la tercera lista
    suma = sensor_a_datos[i] + sensor_b_datos[i]
    datos_combinados.append(suma)

print("\n--- Datos Transformados (elevados al cuadrado) ---")
print(f"Sensor A: {sensor_a_datos}")
print(f"Sensor B: {sensor_b_datos}")
print(f"\nDatos Combinados: {datos_combinados}")