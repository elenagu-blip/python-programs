#p084-triangulo-invertido-numeros.py
#Imprime un triangulo numerico invertido, de n renglones

print("\033[2J\033[H", end="")

#Entrada de datos
n = int(input("Dame un número: "))

#Ciclo for externo: recorre cada renglon, empezando en n y bajando hasta 1
for limite in range(n, 0, -1):
    #Ciclo for interno: imprime los numeros del 1 hasta el limite de este renglon
    for numero in range(1, limite + 1):
        print(numero, end=" ")
    #Al terminar de imprimir los numeros de un renglon, saltamos a la siguiente linea
    print()