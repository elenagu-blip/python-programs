#p040-numero-romano.py
#Este código convierte un número del 1 al 10 a su equivalente en números romanos

print("\033[2J\033[H", end="")

#Entrada de datos
número = int(input("Dame un número (1-10): "))
válido = True

#Proceso
if número == 1:
    romano = "I"
elif número == 2:
    romano = "II"
elif número == 3:
    romano = "III"
elif número == 4:
    romano = "IV"
elif número == 5:
    romano = "V"
elif número == 6:
    romano = "VI"
elif número == 7:
    romano = "VII"
elif número == 8:
    romano = "VIII"
elif número == 9:
    romano = "IX"
elif número == 10:
    romano = "X"
else:
    válido = False

#Salida
if válido == True:
    print(romano)
else:
    print("Error: el número debe estar entre 1 y 10.")