#p079-suma-potencias.py
#Suma las potencias de x, desde x^1 hasta x^n

print("\033[2J\033[H", end="")
print("--- Suma de Potencias ---\n")

#Entrada de datos
x = float(input("Introduce el valor de x: "))
n = int(input("Introduce el número de términos (n): "))

#Acumulador de la suma total de la serie
suma_total = 0

print(f"\nCalculando la serie S = x^1 + ... + x^{n}")

#Bucle exterior: recorre cada termino de la serie, de 1 a n
for i in range(1, n + 1):
    termino_actual = 1
    
    #Bucle interior: multiplica x por si mismo i veces, para calcular x^i
    for j in range(i):
        termino_actual = termino_actual * x
    
    print(f"Término {i}: {x}^{i} = {termino_actual}")
    suma_total = suma_total + termino_actual

print(f"\nEl resultado de la serie es: {suma_total}")