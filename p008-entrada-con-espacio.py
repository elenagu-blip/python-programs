#p008-entrada-con-espacio.py
#Leer datos multiples separados por un espacio u otro caracter y los almacena en variables
print("\033[2J\033[H", end="") #Limpia pantalla
print('Dame tres números separados por un espacio \n')
n1, n2, n3 = input().split('/') #Lee tres números separados por un espacio
n1, n2, n3 = int(n1), int(n2), int(n3) #Convierte los números a enteros
print('Los números ingresados son:', n1, n2, n3)
