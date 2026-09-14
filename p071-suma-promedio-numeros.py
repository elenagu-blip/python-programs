#p071-suma-promedio-numeros.py
#Suma y promedio de n numeros introducidos por el usuario, usando ciclo for

while True:
    print("\033[2J\033[H", end="")
    print("Suma y promedio de números")
    
    cuantos = int(input("¿Cuántos números deseas procesar? "))
    
    #Variable acumuladora de la suma
    suma = 0
    #Variable de texto que va juntando los numeros capturados, para mostrarlos al final
    cadena_numeros = ""
    
    #Ciclo for que pide 'cuantos' numeros, uno por uno
    for i in range(1, cuantos + 1):
        numero = int(input(f"Número[{i}] = "))
        suma = suma + numero
        cadena_numeros = cadena_numeros + " " + str(numero)
    
    promedio = suma / cuantos
    
    print(f"\nLos números que introdujiste fueron:{cadena_numeros}")
    print(f"La suma es {suma}, el promedio es {promedio:.2f}")
    
    if input("\n\n¿Deseas continuar (S/N)? ").upper() == "N":
        break

print("\nHemos llegado al final....")