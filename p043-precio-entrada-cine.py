#p043-precio-entrada-cine.py
#Este código determina el precio de una entrada al cine según la edad del cliente

print("\033[2J\033[H", end="")

#Entrada de datos
edad = int(input("Dame la edad del cliente: "))

#Proceso y salida
if edad < 5:
    print("Entra gratis.")
elif edad <= 12:
    print("Precio: $5")
elif edad <= 64:
    print("Precio: $10")
else:
    print("Precio: $7")