#p014-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas para redondeo y manejo de precios

import math


print("\033[2J\033[H", end="") # Limpia pantalla
import math as mt
precio= float(input("Dame el precio del producto: "))
print(f'El precio original es: {precio:,.2f}')
print(f'El precio redondeado es: {mt.ceil(precio):,.2f}')
print(f'El precio redondeado hacia abajo es: {mt.floor(precio):,.2f}')
print(f'Truncando el precio es: {mt.trunc(precio):,.2f}')
print(f'Redondeando en automático el precio es: {round(precio):,.2f}')
