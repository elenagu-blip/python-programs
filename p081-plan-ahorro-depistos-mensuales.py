#p081-plan-ahorro-depositos-mensuales.py
#Simula un plan de ahorro con depositos mensuales fijos e interes mensual

print("\033[2J\033[H", end="")

#Entrada de datos
monto_inicial = float(input("Monto inicial de ahorro: "))
deposito_mensual = float(input("Depósito mensual: "))
tasa_mensual = float(input("Tasa de interés mensual (%): "))
meses = int(input("Número de meses a simular: "))

print()
print("--- Plan de Ahorro Detallado ---")

#Variable que va llevando el saldo actual, mes tras mes
saldo = monto_inicial

#Ciclo for que recorre cada mes, del 1 hasta el total de meses a simular
for mes in range(1, meses + 1):
    #El saldo inicial de este mes es el saldo que traiamos del mes anterior
    saldo_inicial = saldo
    
    #El interes se calcula sobre el saldo inicial, ANTES de sumar el deposito
    interes = saldo_inicial * (tasa_mensual / 100)
    
    #El saldo final suma el saldo inicial, el interes ganado y el nuevo deposito
    saldo = saldo_inicial + interes + deposito_mensual
    
    print(f"Mes {mes}: Saldo Inicial: ${saldo_inicial:.2f} | Interés: ${interes:.2f} | Saldo Final: ${saldo:.2f}")

print()
print(f"Al final de {meses} meses, tendrás ${saldo:.2f}")