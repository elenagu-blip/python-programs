#p032-2da-ley-de-newton.py
# Calcular fuerza, masa o aceleración según la elección del usuario.

print("\033[2J\033[H")

print('--Calculando la 2da Ley de Newton--')
print('[1] Calcular la Fuerza      (f = m * a) \n')
print('[2] Calcular la Masa        (m = f / a) \n')
print('[3] Calcular la aceleración (a = f / m) \n')
opcion = int(input('Elige la opción correspondiente (1, 2 o 3): \n'))

#Estructura if/elif/else ejecutando el calculo correcto
if opcion == 1:
    print('Dame los Valores siguientes:  \n')
    m = float (input('Masa (kg): '))
    a = float (input('Aceleración (m/s²):'))
    f = m * a
    print('Calculando la Fuerza... \n')
    print(f'La Fuerza es: {f} N')
elif opcion == 2:
    print('Dame los Valores siguientes:  \n')
    f = float(input('Fuerza (N): '))
    a = float (input('Aceleración (m/s²):'))
    m = f / a
    print('Calculando la Masa... \n')
    print(f'La Masa es: {m} Kg ')
elif opcion == 3:
    print('Dame los Valores siguientes:  \n')
    f = float(input('Fuerza (N): '))
    m = float (input('Masa (kg):'))
    a = f / m
    print('Calculando la Masa... \n')
    print(f'La Aceleración es: {m} m/s² ')
    

    