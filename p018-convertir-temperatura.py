#p018-convertir-temperatura.py
#Convierte la temperatura de grados Celsius a grados Fahrenheit

print("\033[2J\033[H", end="") #Limpia pantalla

print('Convertir temperatura de grados Celsius a grados Fahrenheit \n')
celsius = float(input('Ingrese la temperatura en grados Celsius: ')) #Lee la temperatura

print(f'La temperatura en grados Celsius es: {celsius:.2f} °C') #Muestra la temperatura en grados Celsius
#Convierte la temperatura a grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32 #Calcula la temperatura en grados Fahrenheit
print(f'La temperatura en grados Fahrenheit es: {fahrenheit:.2f} °F') #Muestra la temperatura en grados Fahrenheit

