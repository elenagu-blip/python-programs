#p104-procesar-notas.py
#Transforma y filtra notas con comprensiones
print("\033[2J\033[H", end="")
notas = []
 
while True:
    try:
        nota = float(input("Introduzca nota (0 para detener): "))
    except ValueError:
        print("Entrada inválida, debe ser un número entre 0 y 100.")
        continue
 
    if nota == 0:
        break
    if nota < 0 or nota > 100:
        print("Entrada inválida, debe ser 0-100.")
        continue
 
    # Guardar como entero si no tiene decimales
    notas.append(int(nota) if nota == int(nota) else nota)
 
print("\n--- Resultados ---")
print(f"Total de notas introducidas: {len(notas)}")
print(f"Lista de notas: {notas}")
 
if notas:
    suma = sum(notas)
    promedio = suma / len(notas)
    menores = [n for n in notas if n < promedio]
 
    print(f"Suma de notas: {suma}")
    print(f"Promedio de notas: {promedio}")
    print(f"Nota máxima: {max(notas)}")
    print(f"Nota mínima: {min(notas)}")
    print(f"Notas menores al promedio ({promedio}): {len(menores)}")
    print(f"Lista de notas menores al promedio: {menores}")
else:
    print("No se introdujeron notas, no hay nada que calcular.")