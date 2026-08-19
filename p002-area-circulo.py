# p002-area-circulo.py
# Calcula el área de un círculo

import math #importa la libreria de constantes matemáticas
print('Calculando el área de un círculo')
radio = float(input('Ingrese el radio del círculo: \n')) #Lee el radio del círculo
#area = math.pi * radio ** 2 #Calcula el área del círculo
area = math.pi * math.pow (radio, 2) #Calcula el área del círculo
print(f'El circulo de radio {radio} tiene un área de {area:.2f} unidades cuadradas.')








