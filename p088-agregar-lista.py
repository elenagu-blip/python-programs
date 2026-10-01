#p088-agregar-lista.py
#Agregar elementos a una lista

print("\033[2J\033[H", end="")
print("Agregar elementos a una lista")

nums=[10,20,30,40,50,70,99]

print('Longitud y contenido de la lista:')
print(f'Longitud {len(nums)}')
print(f'Contenido: {nums}')

print('\nAgregar 90 y 100 al final de la lista')
nums.append(90)
nums.append(100)
print(f'Contenido actualizado: {nums}')
print(f'Longitud actualizada: {len(nums)}')

print('\nAgregar 80 en la posición 4 de la lista')
nums.insert(4, 80)
print(f'Contenido actualizado: {nums}')
print(f'Longitud actualizada: {len(nums)}')

print(f'\n Extender la lista con [110,120,130]')
nums.extend([110,120,130])
print(f'Contenido actualizado: {nums}')
print(f'Longitud actualizada: {len(nums)}')
