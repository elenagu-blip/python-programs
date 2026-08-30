#p041-calculo-notas.py
#Este código calcula el promedio de 5 calificaciones y muestra un mensaje según el rango

print("\033[2J\033[H", end="")

#Entrada de datos
nota1 = float(input("Dame la calificación 1: "))
nota2 = float(input("Dame la calificación 2: "))
nota3 = float(input("Dame la calificación 3: "))
nota4 = float(input("Dame la calificación 4: "))
nota5 = float(input("Dame la calificación 5: "))

#Proceso
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

#Salida
if promedio < 6:
    print(f"Promedio: {promedio}. Quedas reprobado")
elif promedio < 7:
    print(f"Promedio: {promedio}. Pasas de panzazo")
elif promedio < 8:
    print(f"Promedio: {promedio}. Muy bien, puedes mejorar")
elif promedio < 9:
    print(f"Promedio: {promedio}. Excelente, sigue así")
else:
    print(f"Promedio: {promedio}. Perfecto, tu esfuerzo valió la pena")