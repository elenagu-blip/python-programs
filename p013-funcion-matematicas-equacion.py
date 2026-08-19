#p013-funcion-matematicas-equacion.py
#Ejemplifica el uso de funciones matemáticas dentro de math
#Evaluar la funcion f(x) = 3x^2 + raiz(x al cuadrado + y al cuadrado) + e^(ln(x)

import math as mt
print("\033[2J\033[H", end="") #Limpia pantalla
x= int(input("Dame el valor de x: "))
y= int(input("Dame el valor de y: "))
fxy= 3* mt.pow(x,2) + mt.sqrt(mt.pow(x,2)+mt.pow(y,2)) + mt.exp(mt.log(x))
fxy2= 3 * x **2 + mt.sqrt(x ** 2 + y ** 2) + mt.exp(mt.log(x))
print(f'El resultado es : {fxy:,.2f}')
print(f'El resultado es : {fxy2:,.2f}')