#p016-hipotenusa-triangulo.py
#Calcular la hipotenusa de un triángulo rectángulo

print("\033[2J\033[H", end="") #Limpia pantalla

import math as mt
print('Calculando la hipotenusa de un triángulo rectángulo \n')
cateto1 = float(input('Ingrese la longitud del primer cateto: ')) #Lee el primer cateto
cateto2 = float(input('Ingrese la longitud del segundo cateto: ')) #Lee el segundo cateto

#Calcula la hipotenusa usando el teorema de Pitágoras
hipotenusa = mt.sqrt(cateto1 ** 2 + cateto2 ** 2) #Calcula la hipotenusa

#Muestra el resultado 

print(f'La hipotenusa del triángulo rectángulo con catetos {cateto1} y {cateto2} es {hipotenusa:.2f} unidades de longitud.')   
