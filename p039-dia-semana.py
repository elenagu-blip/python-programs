#p039-dia-semana.py
#Este codigo funciona mostrando el dia de la semana

print("\033[2J\033[H", end ="")

#Entrada de datos
numero = int(input('Dame un número'))

if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Lunes')
elif numero == 3:
    print("Martes")
elif numero == 4:
    print("Miércoles")
elif numero == 5:
    print("Jueves")
elif numero == 6:
    print("Viernes")
elif numero == 7:
    print("Sábado")
else:
    print("Error: el número debe estar entre 1 y 7.")