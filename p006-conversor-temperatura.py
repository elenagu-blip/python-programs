#p006-conversor-temperatura.py
#Calcular una temperatura da en grados celsius y la convierte a grados fahrenheit
print("\033[2J\033[H", end="") #Limpia pantalla
print('Calculando la conversión de temperatura \n')

celsius = float(input("Grados celsius: "))
fahrenheit = (celsius * 9/5) + 32 #Lee la temperatura en grados celsius y la convierte a grados fahrenheit
print(f'La temperatura en grados fahrenheit es: {fahrenheit:.2f}') 