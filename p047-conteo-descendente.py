#p047-conteo-descendente.py
#Imprime una cuenta regresiva desde n hasta 1 (o menos), con paso personalizable, usando un ciclo while.

print("\033[2J\033[H", end="")
print('Iniciando cuenta regresiva')

n = int(input('¿Desde qué número quieres empezar? '))
paso = int(input('¿De cuánto en cuánto quieres bajar? '))

if paso <= 0:
    print("Error: el paso debe ser un número mayor a 0.")
else:
    c = n
    while c > 0:
        print(f'{c:4}', end="")
        c -= paso
    print('\n¡Cuenta regresiva completada!')