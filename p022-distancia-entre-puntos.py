#p022-distancia-entre-puntos.py
#Calcular distancia entre dos puntos en un plano cartesiano

print("\033[2J\033[H", end="") #Limpia pantalla
import math as mt
print('Calculando la distancia entre dos puntos en un plano cartesiano \n')

x1 = float(input('Ingrese la coordenada x del primer punto: ')) #Lee la coordenada x del primer punto
y1 = float(input('Ingrese la coordenada y del primer punto: ')) #Lee la coordenada y del primer punto
x2 = float(input('Ingrese la coordenada x del segundo punto: ')) #Lee la coordenada x del segundo punto
y2 = float(input('Ingrese la coordenada y del segundo punto: ')) #Lee la coordenada y del segundo punto 

#Calcula la distancia entre los dos puntos usando la fórmula de distancia  
d = mt.sqrt((x2-x1)**2 + (y2-y1)**2) #Calcula la distancia entre los dos puntos

#Muestra el resultado
print(f'La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {d:.2f} unidades de longitud.') #Muestra la distancia entre los dos puntos    
