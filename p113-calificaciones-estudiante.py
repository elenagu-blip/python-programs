# p113-calificaciones-estudiante.py
# Gestión de calificaciones de un estudiante usando diccionarios

print('\033[H\033[J')
print('Gestión de calificaciones de un estudiante usando diccionarios')

# Datos iniciales: dos listas
materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
califs = [10, 9, 8, 7.5, 6]
print(f'Lista de materias : \n{materias}\n')
print(f'Lista de calificaciones: \n{califs}\n')

# Crear diccionario combinando ambas listas
notas = dict(zip(materias, califs))
print(f'\nDiccionario nuevo juntando las listas: \n {len(notas)} - {notas} ')

# Agregar elementos
notas.update({'Ingles': 10})
notas.update({'Programacion': 7})
print(f'\nSe agregaron elementos : \n{len(notas)} - {notas}')

# Eliminar elementos
notas.pop('Fisica')
notas.popitem()  # remueve el último insertado (Programacion)
print(f'\nSe removieron elementos : \n {len(notas)} - {notas}')

# Actualizar elementos
notas.update({'Quimica': 10})
notas.update({'Matematicas': 10})
print(f'\nSe modificaron elementos : \n{notas}')

# Calcular suma y promedio
s = 0
print('\nMaterias y calificaciones finales')
for m, c in notas.items():
    print(f'{m:<12} - {c:5}')
    s += c

p = s / len(notas)
print(f'\nLa suma: {s} y el promedio: {p:.2f}')

# Limpiar el diccionario
notas.clear()
print(f'\nSe borró todo : {notas}')