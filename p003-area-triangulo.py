#p003-area-triangulo.py
#Calcula el área de un triángulo 
print('Calculando el área de un triángulo')
print('Dame la base y la altura del triangulo separadas por <Enter>')
base, altura = int(input()), int(input()) #Lee la base y la altura del triángulo
area = base * altura / 2 #Calcula el área del triángulo
print(f'El triángulo de base {base} y altura {altura} tiene un área de {area:.2f} unidades cuadradas.')


