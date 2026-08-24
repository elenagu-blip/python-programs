#p025-verificar-numero-v2.py
#Verificar si un número es positivo
print('Verificar si un número es positivo, negativo o cero')
numero = int(input('Dame un numero entero: '))

if numero > 0:
    print('El numero es POSITIVO ')
else:
    if numero < 0:
        print('El numero es NEGATIVO ')
    else:
        print('El numero es CERO ')

print('\nAqui ya terminamos de tomar decisiones')