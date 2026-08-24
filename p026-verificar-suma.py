#p026-verificar-suma.py
# Pide dos números, los suma y verifica si el resultado es igual a un tercer número.

print("\033[2J\033[H", end="")
#Entrada de datos
print('Ingrese tres números enteros:\n')    
n1 = int(input('Dame el primer número : '))
n2 = int(input('Dame el segundo número: '))
n3 = int(input('Dame el tercer número : '))

#Proceso y Salida
suma = n1 + n2 
if suma == n3:
	print(f"\n ¡Correcto! La suma de {n1} + {n2} es igual a {n3}.")
else:
	print(f"\n No coincide. La suma de {n1} + {n2} es {suma}, lo cual es distinto de {n3}.")
print('-' * 60)
print('Fin del programa.')