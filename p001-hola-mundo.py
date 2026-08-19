#p001-hola-mundo.py
#Lee datos y envia saludo

print('Leyendo datos y envia un saludo')

#Leer datos del usuario
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
peso = float(input('Ingrese su peso: '))
print(f'Hola {nombre}, tienes {edad} años y pesas {peso} kg.')
print (nombre + ' tiene ' + edad + ' años y pesa ' + str(peso) + ' kg.')
print("\033[2J\033[H", end="") #Limpia pantalla]