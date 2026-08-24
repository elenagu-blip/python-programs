#p028-calcular-paga-extra.py
#Cálcula la paga de un trabajador considerando las horas extras

print("\033[2J\033[H", end="")
print('Calculando la paga del colaborador:\n')

#Entrada de datos
print('Datos del trabajador: \n')
nombre = input('Nombre del trabajador: ')
horas = int(input('Horas trabajadas: \n'))
paga_hora = float(input('Paga por hora: \n'))
#Calculo de la paga
horas_normales = 40
paga_normal = horas_normales * paga_hora
horas_extra = paga_extra = 0
if horas > 40:
    horas_extras = horas-40
    paga_extra = horas_extra * (paga_hora*2)
    total = paga_normal + paga_extra

else:
    total = paga_normal
    print("\n Cálculo completado.")
print(f'\nEl trabajador {nombre} tiene {horas_normales} horas normales + {horas_extra} horas extra.')
print(f'Paga normal = ${paga_normal:13,.2f}')
print(f'Paga extra = ${paga_extra:13,.2f}')
print(f'El pago total = ${total:13,.2f}')
print('\n* ¡Programa finalizado! *')

    
