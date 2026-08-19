#p005-calculadora-imc.py
#Calcula el índice de masa corporal (IMC)

print("\033[2J\033[H", end="") #Limpia pantalla
print('Calculando el índice de masa corporal (IMC) \n')
peso = float(input('Ingrese su peso en kilogramos: ')) #Lee el peso del usuario
altura = float(input('Ingrese su altura en metros: ')) #Lee la altura del usuario
imc = peso / (altura ** 2) #Calcula el IMC
print(f'Su índice de masa corporal es: {imc:.2f}')