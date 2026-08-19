#p009-entrada-multiple2.py
#Entrada multiple de valores en una sola linea con map
# 1. Leer 10 números en la misma linea (separados por espacios)
print("\033[2J\033[H", end="") #Limpia pantalla
print('Dame 10 números separados por un espacio \n')
v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = map( float, input().split()) #Lee 10 números separados por un espacio y los convierte a enteros
#2. Sumar las 10 variables
suma = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10
#3. Mostrar el resultado
print('La suma de los 10 números ingresados es:', suma)
