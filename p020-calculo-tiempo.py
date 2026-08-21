#p020-calculo-tiempo.py
#Convierte una cantidad de tiempo de horas a dias, minutos y segundos

print("\033[2J\033[H", end="") #Limpia pantalla
print('Convertir tiempo de horas a días, minutos y segundos \n')   
Horas = int(input('Ingrese la cantidad de horas: ')) #Lee la cantidad de horas
Dias = Horas // 24 #Calcula el número de días
Minutos = Horas * 60 #Calcula el número de minutos
Segundos = Horas * 3600 #Calcula el número de segundos

#Muestra el resultado
print(f'La cantidad de horas ingresada es: {Horas} horas') #Muestra la cantidad de horas ingresada
print(f'Equivale a: {Dias} días, {Minutos} minutos y {Segundos} segundos') #Muestra la cantidad de días, minutos y segundos equivalentes  