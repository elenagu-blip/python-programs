#p015-funciones-trigonometricas.py
#Demostrar el uso de funciones trigonométricas básicas

print("\033[2J\033[H", end="") #Limpia pantalla
import math as mt

#Definir un ángulo en grados y convertirlo a radianes
angulo_grados = float(input("Dame un ángulo en grados: "))
angulo_radianes = mt.radians(angulo_grados)

#Calcular las funciones trigonométricas
seno = mt.sin(angulo_radianes)
coseno = mt.cos(angulo_radianes)
tangente = mt.tan(angulo_radianes)

#Convertir de vuelta a grados para demostración
angulo_degrees = mt.degrees(angulo_radianes)

#Formatear y mostrar los resultados para mejor presentaciión
salida = (f"Resumen de funciones\n"
          f"El seno es: {seno:.4f}\n"
          f"El coseno es: {coseno:.4f}\n"
          f"La tangente es: {tangente:.4f}\n"
          f"El ángulo en grados es: {angulo_degrees:.2f}\n"
          f"El ángulo en radianes es: {angulo_radianes:.4f}")

print(salida)