#p010-promedio-de-calificaciones.py 
#Calcular el promedio de calificaciones de un estudiante

print("\033[2J\033[H", end="") #Limpia pantalla
print ('Calculando el promedio de calificaciones \n')
#Solicitar las calificaciones en una sola línea separadas por espacio
print('Dame 3 calificaciones separadas por espacio: ')
cal1, cal2, cal3 = map(float, input().split()) #Lee las calificaciones y las convierte a float
cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3) #Convierte las calificaciones a enteros

#Calcula el promedio de las calificaciones
promedio = (cal1 + cal2 + cal3) / 3
#Mostrar el resultado del promedio de calificaciones
print(f'Las calificaciones son: {cal1}, {cal2}, {cal3}')
print(f'El promedio es: {promedio}')
