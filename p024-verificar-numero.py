#p024-verificar-numero.py
#Verificar si un número entero es positivo, negativo o cero.

print("\033[2J\033[H", end="") #Limpia la pantalla
print('Verificar si un número es positivo, negativo o cero')
número = int(input('Dame un número: \n'))
if número > 0:
    print('El número es positivo😉')
else:
    if número < 0:
        print('El número es negativo 🤨')
    elif número == 0:
        print('El número es cero 🫨')