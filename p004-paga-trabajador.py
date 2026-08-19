#p004-paga-trabajador.py
#Calcula el pago de un trabajador
print("\033[2J\033[H", end="") #Limpia pantalla
print('Calculando el pago de un trabajador \n')

#Entrada de datos
nombre = input('Ingrese el nombre del trabajador: ')
horas = int(input('Ingrese el número de horas trabajadas: '))
pago_por_hora = float(input('Ingrese el pago por hora: '))
#Procesamiento de datos
tasa_impuestos = 0.03 #Tasa de impuestos del 15%
pagabruta = horas * pago_por_hora #Calcula el pago bruto
impuestos = pagabruta * tasa_impuestos #Calcula los impuestos
pagoneto = pagabruta - impuestos #Calcula el pago neto
#Salida de datos
print('Resumen del pago del trabajador \n')
print(f'El trabajador {nombre} trabajó {horas} horas a un pago de {pago_por_hora:.2f} pesos por hora.')
print(f'El pago bruto es de ${pagabruta:>5,.2f}.')
print(f'Los impuestos son de ${impuestos:>5,.2f}.')
print(f'El pago neto es de ${pagoneto:>5,.2f}.')