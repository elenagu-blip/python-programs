#p077-factorial-numeros.py
#Calcula e imprime el factorial de los numeros desde 1 hasta n

print("\033[2J\033[H", end="")
print("--- Cálculo Sucesivo de Factoriales ---\n")

#Entrada de datos
n = int(input("¿Hasta qué número deseas calcular el factorial? "))

#Bucle exterior: recorre cada numero al que le calcularemos el factorial
for i in range(1, n + 1):
    factorial = 1  #Reiniciamos el factorial para cada numero nuevo
    
    #Bucle interior: multiplica 1 * 2 * 3 * ... * i
    for j in range(1, i + 1):
        factorial = factorial * j
    
    print(f"El factorial de {i}! es = {factorial}")