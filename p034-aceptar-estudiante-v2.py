#p034-aceptar-estudiante-v2.py
print("\033[2J\033[H")
print('--- Admisiones de la Universidad ---')
nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

# Primer nivel: verificar la edad
if edad >= 18:
    # Si la edad es aceptable, pasar al siguiente nivel de verificación
    print('Ingresa 2 calificaciones para continuar:')
    calificacion1 = float(input())
    calificacion2 = float(input())

    # Segundo nivel: verificar las calificaciones
    if calificacion1 >= 8 and calificacion2 >= 8:
        # Si ambas condiciones (edad y calificaciones) se cumplen
        print(f' ¡Bienvenid@, {nombre}! Tu edad de {edad} y tus calificaciones te permiten ingresar.')
    else:
        print(' Lo sentimos, se requiere una calificación mínima de 8 en ambos exámenes.')
else:
    print(f' Lo sentimos, {nombre}. Solo aceptamos a mayores de 18 años.')