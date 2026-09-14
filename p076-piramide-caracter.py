#p076-piramide-caracter.py
#Imprime una piramide de caracteres, centrada con espacios

print("\033[2J\033[H", end="")
print("Imprime una pirámide de caracteres")

#Entrada de datos
altura = int(input("Introduce la altura de la pirámide: "))
car = input("Introduce el carácter para la pirámide: ")

print("\n--- Pirámide Generada ---")

#Bucle exterior: controla cada nivel de la piramide, de 1 a altura
for i in range(1, altura + 1):
    #Calculamos cuantos espacios y cuantos caracteres lleva este nivel
    espacios = altura - i
    caracteres = 2 * i - 1
    
    #Primer bucle interior: imprime los espacios en blanco a la izquierda
    for j in range(espacios):
        print(" ", end="")
    
    #Segundo bucle interior: imprime los caracteres del nivel
    for k in range(caracteres):
        print(car, end="")
    
    #Salto de linea para pasar al siguiente nivel
    print()