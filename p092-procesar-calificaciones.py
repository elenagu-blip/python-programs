#p092-procesar-calificaciones.py
#Procesa calificaciones en una lista

print("\033[2J\033[H", end="")
print("Procesador de calificaciones de un curso\n")
print("Introduce calificaciones entre 0 y 10 (usa 99 para terminar):\n")

calificaciones = []
suma = 0.0

while True:
    try:
        n = float(input("Calificación > "))
        if n == 99:
            break
        if 0 <= n <= 10:
            calificaciones.append(n)
            suma += n
        else:
            print("Error: la calificación debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

if not calificaciones:
    print("\nNo se ingresaron calificaciones.")
else:
    promedio = suma / len(calificaciones)
    maxima = max(calificaciones)
    minima = min(calificaciones)
    
    #Contamos cuantas calificaciones superaron el promedio
    arriba_del_promedio = 0
    for c in calificaciones:
        if c > promedio:
            arriba_del_promedio += 1
    
    print("\n--- Resumen Estadístico ---")
    print(f"Calificaciones: {calificaciones}")
    print(f"Suma: {suma:.2f}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Calificación más alta: {maxima}")
    print(f"Calificación más baja: {minima}")
    print(f"Alumnos que superaron el promedio: {arriba_del_promedio}")