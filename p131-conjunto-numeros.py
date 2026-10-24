# p131-conjunto-numeros.py
# Operaciones con conjuntos de números
print("\033[2J\033[H", end="") #Limpia pantalla

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

# 1. Crear y mostrar los conjuntos
A = set(lista1)
B = set(lista2)
C = set(lista3)
print("--- Conjuntos ---")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")

# 2. Operaciones
print("\n--- Operaciones ---")
print(f"Unión (A | B): {A | B}")
print(f"Unión (B | C): {B | C}")
print(f"Diferencia (A - C): {A - C}")
print(f"Diferencia Simétrica (B ^ C): {B ^ C}")
print(f"Intersección (B & C): {B & C}")

# 3. Verificaciones (Verdadero/Falso)
print("\n--- Verificaciones ---")
print(f"¿Es A subconjunto de B? : {A <= B}")
print(f"¿Es C subconjunto de A? : {C <= A}")
print(f"¿Está el número 100 en A? : {100 in A}")
print(f"¿Está el número 60 en A, B y C? : {60 in A and 60 in B and 60 in C}")
print(f"¿No está el número 900 en C? : {900 not in C}")