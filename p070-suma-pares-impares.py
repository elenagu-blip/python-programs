#p070-suma-pares-impares.py
#Imprime los numeros pares e impares en un rango de 1 a n, y su suma

while True:
    print("\033[2J\033[H", end="")
    print("Imprimir la suma de pares e impares en un rango de 1 a n")
    
    n = int(input("Dame el valor final? "))
    
    #Variables acumuladoras: suma de pares, suma de impares
    suma_pares = 0
    suma_impares = 0
    #Variables tipo texto que van juntando los numeros encontrados, para mostrarlos al final
    cadena_pares = ""
    cadena_impares = ""
    
    #Ciclo for que recorre cada numero de 1 a n
    for i in range(1, n + 1):
        if i % 2 == 0:  #es par
            cadena_pares = cadena_pares + " " + str(i)
            suma_pares = suma_pares + i
        else:  #es impar
            cadena_impares = cadena_impares + " " + str(i)
            suma_impares = suma_impares + i
    
    print(f"\nLos pares:{cadena_pares}")
    print(f"Suma de pares: {suma_pares}")
    print(f"\nLos impares:{cadena_impares}")
    print(f"Suma de impares: {suma_impares}")