#p033-aceptar-estudiante.py
#Aceptar un estudiante en base a la edad y las calificaciones
print("\033[2J\033[H")
print('--Admisión de la Universidad Autonoma Internacional')

nombre = input('Ingresa tu nombre: \n')
edad = int(input('Ingresa tu edad: \n'))

#Verificador de edad
if edad < 18:
    print(f'Lo sentimos, {nombre}. Solo aceptamos a mayores de 18 años.')
else:
    #Si la edad es aceptable se pasa al segundo nivel.
    print('Ingresa 2 calificaciones para continuar:')
    calificacion1 = float(input())
    calificacion2 = float(input())
    if calificacion1 < 8 or calificacion2 < 8:
        print('Lo sentimos, se requiere una calificación mínima de 8 en ambos exámenes.')
    else:
        # Si ambas condiciones (edad y calificaciones) se cumplen
        print(f'¡Bienvenido, {nombre}! Tu edad de {edad} y tus calificaciones te permiten ingresar.')
   