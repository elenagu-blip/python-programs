#p044-calculadora-anio-bisiesto.py
#Este código determina si un año ingresado por el usuario es bisiesto

print("\033[2J\033[H", end="")

#Entrada de datos
año = int(input("Dame un año: "))

#Proceso y salida
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")