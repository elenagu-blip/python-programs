#p083-rombo-caracter.py
#Dibuja un rombo usando el caracter elegido por el usuario

print("\033[2J\033[H", end="")

#Entrada de datos
n = int(input("Dame un número impar para la altura: "))
caracter = input("¿Qué carácter quieres usar? ")

#La fila de en medio es la mas ancha (todo el rombo es simetrico respecto a ella)
mitad = n // 2

#Ciclo for que recorre cada fila del rombo, de 0 a n-1
for fila in range(n):
    #En la mitad de arriba (incluyendo el centro), el ancho va creciendo
    if fila <= mitad:
        num_caracteres = 2 * fila + 1
    else:
        #En la mitad de abajo, el ancho va disminuyendo
        num_caracteres = 2 * (n - 1 - fila) + 1
    
    #Los espacios a la izquierda son los que centran la fila
    num_espacios = (n - num_caracteres) // 2
    
    #Imprimimos primero los espacios de relleno
    for i in range(num_espacios):
        print(" ", end="")
    
    #Despues imprimimos el caracter la cantidad de veces que toque en esta fila
    for i in range(num_caracteres):
        print(caracter, end="")
    
    #Saltamos a la siguiente linea para dibujar la fila que sigue
    print()