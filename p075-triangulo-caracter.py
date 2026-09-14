#p075-triangulo-caracter.py
#Imprime un triangulo rectangulo de caracteres

print("\033[2J\033[H", end="")

#Entrada de datos
n = int(input("¿Cuántos renglones tendrá el triángulo? "))
car = input("¿Qué carácter quieres usar para dibujar? ")

print("\n--- Triángulo Generado ---")

#Bucle exterior: controla cada fila, de 1 a n
for i in range(1, n + 1):
    #Bucle interior: imprime i caracteres en la fila actual
    for j in range(i):
        print(car, end="")
    #Salto de linea para pasar a la siguiente fila
    print()