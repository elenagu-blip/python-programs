#tercer-angulo.py
#Calcula el tercer ángulo de un triángulo

print("\033[2J\033[H", end="") #Limpia pantalla
print('Calculando el tercer ángulo de un triángulo \n')
angulo1 = float(input('Ingrese el primer ángulo del triangulo: ')) #Lee el primer ángulo
angulo2 = float(input('Ingrese el segundo ángulo del triangulo: ')) #Lee el segundo ángulo

#Calcula el tercer ángulo usando la suma de los ángulos de un triángulo
angulo3 = 180 - (angulo1 + angulo2) #Calcula el tercer ángulo  

#Muestra el resultado
print(f'El tercer ángulo del triángulo con ángulos {angulo1} y {angulo2} es {angulo3:.2f} grados.')
