#p086-acceder-lista.py
#Acceder a los elementos de una lista

print("\033[2J\033[H", end="")
nums = [10,20,30,40,50,70,99]
print("Acceder a los elementos de una lista")

print('Longitud y contenido de la lista:')
print(f'Cuantas medidas hay en la lista: {len(nums)}')
print(f'Todas las medidas: {nums}')

print('\nPor indice positivo : ')
print(f'Primera y última : {nums[0]}, {nums[-1]}')
print('\nPor indice negativo : ')
print(f'Primera y última : {nums[-len(nums)]}, {nums[-1]}')
print('\nPor rango : ')
print(f'De la 2 a la 6 (6 no incluida): {nums[2:6]}')
print('\nPor saltos :')
print(f'Las primeras 3 desde el principio : {nums[:3]}')
print(f'Las últimas 3 desde el índice 6 hasta el final : {nums[6:]}')