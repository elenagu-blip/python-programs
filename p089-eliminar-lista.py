#p089-eliminar-lista.py
#Eliminar elementos de una lista

print("\033[2J\033[H", end="")
print("Eliminar elementos de una lista")

nums=[1,3,5,7,9,11,13,15,17,19]

print('Longitud y contenido de la lista:')
print(f'Longitud {len(nums)}')
print(f'Contenido: {nums}')

print('\nEliminar el elemento 11 de la lista')
nums.remove(11)
print(f'Contenido actualizado: {nums}')
print(f'Longitud actualizada: {len(nums)}')

print('\nEliminar el elemento en la posición 4 de la lista')
del nums[4]
print(f'Contenido actualizado: {nums}') 
print(f'Longitud actualizada: {len(nums)}')

print('\n Eliminar el elemento de la posición 5 utilizando pop()')
nums.pop(5)
print(f'Contenido actualizado: {nums}')
print(f'Longitud actualizada: {len(nums)}')
