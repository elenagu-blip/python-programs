# p130-conjunto-personas.py
# Operaciones con conjuntos de nombres

print("\033[2J\033[H", end="") #Limpia pantalla

lista1 = ['Juan', 'Maria', 'Pedro', 'Jose', 'Rocio']
lista2 = ['Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther']

# 1. Crear y mostrar los conjuntos
A = set(lista1)
B = set(lista2)
print("--- Conjuntos ---")
print(f"A: {A}")
print(f"B: {B}")

# 2. Operaciones
print("\n--- Operaciones ---")
print(f"Unión (A | B): {A | B}")
print(f"Intersección (A & B): {A & B}")
print(f"Diferencia (A - B): {A - B}")
print(f"Diferencia Simétrica (A ^ B): {A ^ B}")

# 3. Verificaciones (Verdadero/Falso)
sub = {'Pablo', 'Mateo'}
sup = {'Reynaldo', 'Angelica'}

print("\n--- Verificaciones ---")
print(f"¿Es {{Pablo, Mateo}} un subconjunto de B? : {sub <= B}")
print(f"¿Es A un superconjunto de {{Reynaldo, Angelica}}? : {A >= sup}")
print(f"¿Está 'Pedro' en el conjunto A? : {'Pedro' in A}")
print(f"¿No está 'Lilia' en el conjunto B? : {'Lilia' not in B}")