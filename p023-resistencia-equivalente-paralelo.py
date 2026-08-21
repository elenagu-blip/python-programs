#p023-resistencia-equivalente-paralelo.py
#Calcula la resistencia total o equivalente de un circuito de cuatro resistencias en paralelo.

print("\033[2J\033[H", end="") #Limpia pantalla
print('Ingrese los datos necesarios: \n')
r1 = float(input('Ingrese el valor de la R1: '))
r2 = float(input('Ingrese el valor de la R2: '))
r3 = float(input('Ingrese el valor de la R3: '))
r4 = float(input('Ingrese el valor de la R4: '))

rt = (1 / (1/r1 + 1/r2 + 1/r3 + 1/r4))

#Mostrar el resultado
print(f'La resistencia equivalente es: {rt:.2f} ohms')