#p029-retira-cuenta.py
# Simula un retiro de dinero de una cuenta con validaciones anidadas

print("\033[2J\033[H", end="")
print("Bienvenido a tu Cajero de Confianza: \n")
Saldo_actual = 16489.00
print(f"Tu saldo actual es: ${Saldo_actual:,.2f}")

cantidad_retiro = float(input('Ingresa la cantidad a retirar: '))
#Verificación de saldo
if cantidad_retiro <= Saldo_actual:
    nuevo_saldo = Saldo_actual-cantidad_retiro
    print('\n Retiro exitoso. ')
    print(f"Tu nuevo saldo es : ${nuevo_saldo:,.2f}")
    
    #Si la cantidad es válida pero excede el saldo
else:
    print("\n La cantidad a retirar debe ser un número positivo.")
    
print("\n Gracias por usar nuestro servicio")



      