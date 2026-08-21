#p019-area-volumen-cilindro.py
#Calcula el área y el volumen de un cilindro

print("\033[2J\033[H", end="") #Limpia pantalla
print('Ingrese los datos del cilindro \n')
radio = float(input('Ingrese el radio del cilindro: ')) #Lee el radio del cilindro
altura = float(input('Ingrese la altura del cilindro: ')) #Lee la altura del cilindro

#Calcula el área y el volumen del cilindro
import math as mt
area = 2 * mt.pi * radio * (radio + altura) #Calcula el área del cilindro
volumen = mt.pi * radio ** 2 * altura # Calcula el volumen del cilindro
print(f'El área del cilindro es: {area:.2f} unidades cuadradas') #Muestra el área del cilindro
print(f'El volumen del cilindro es: {volumen:.2f} unidades cúbicas') #Muestra el volumen del cilindro   
