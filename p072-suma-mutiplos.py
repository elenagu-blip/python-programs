#p072-suma-mutiplos.py
#Imprime los multiplos de m entre 1 y n, los cuenta y suma

while True:
    print("\033[2J\033[H", end="")
    print("Imprime múltiplos de m entre 1 y n")
    
    n = int(input("Hasta dónde? "))
    m = int(input("¿Qué múltiplos quieres? "))
    
    #Contador y acumulador de la suma de los multiplos encontrados
    contador_multiplos = 0
    suma_multiplos = 0
    
    #Ciclo for que recorre cada numero de 1 a n
    for i in range(1, n + 1):
        if i % m == 0:  #es multiplo de m
            print(i, end=" ")
            suma_multiplos = suma_multiplos + i
            contador_multiplos = contador_multiplos + 1
    
    print(f"\nFueron {contador_multiplos} múltiplos, los cuales suman {suma_multiplos}")
    
    if input("\n\n¿Deseas continuar (S/N)? ").upper() == "N":
        break

print("\nHemos llegado al final....")