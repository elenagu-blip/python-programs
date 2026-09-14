#p069-arriba-abajo.py
#Imprime numeros de 1 a n o de n a 1, segun elija el usuario

while True:
    print("\033[2J\033[H", end="")
    print("Imprimir números usando ciclo for - Arriba o Abajo")
    print("[ 1 ] Imprimir números de 1 a n")
    print("[ 2 ] Imprimir números de n a 1")
    
    op = int(input("¿Qué eliges? "))
    
    if op == 1:
        print("\nImprimir números de 1 a n")
        n = int(input("Hasta dónde? "))
        #Ciclo for que sube de 1 hasta n
        for x in range(1, n + 1):
            print(x, end=" ")
    elif op == 2:
        print("\nImprimir números de n a 1")
        n = int(input("Desde dónde? "))
        #Ciclo for que baja de n hasta 1
        for x in range(n, 0, -1):
            print(x, end=" ")
    else:
        print("\nOpción no válida")
    
    if input("\n\n¿Deseas continuar (S/N)? ").upper() == "N":
        break

print("\nHemos llegado al final....")