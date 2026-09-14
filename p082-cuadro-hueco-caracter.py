#p082-cuadro-hueco-caracter.py
#Dibuja un cuadrado hueco: el caracter solo forma el contorno

print("\033[2J\033[H", end="")

#Entrada de datos
lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
caracter = input("¿Qué carácter quieres usar? ")

#Ciclo for externo: recorre cada fila del cuadrado, de 0 a lado-1
for fila in range(lado):
    #Ciclo for interno: recorre cada columna de esa fila, de 0 a lado-1
    for columna in range(lado):
        #Es borde si estamos en la primera/ultima fila O en la primera/ultima columna
        if fila == 0 or fila == lado - 1 or columna == 0 or columna == lado - 1:
            print(caracter, end=" ")
        else:
            #Si no es borde, es hueco: se imprime un espacio en vez del caracter
            print(" ", end=" ")
    #Al terminar de recorrer las columnas de una fila, saltamos a la siguiente linea
    print()