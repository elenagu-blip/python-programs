#p031-verifica-suma.py
#Verificar si la suma de dos números es igual a un tercero.

print("\033[2J\033[H")

print('--Verificar si la suma de dos números es igual a un tercero. \n')
print('Dame 3 números enteros separador por espacio: \n')

n1,n2,n3 = input().split()

#Asignar y convertir las entradas a enteros
n1,n2,n3 = int(n1), int(n2), int(n3)
#Evaluar las posibles cominaciones con if y elsif
if n1 +n2 == n3:
    print(f' n1 + n2 es igual a n3 \n ({n1} + {n2} = {n3})')
elif n1 + n3 == n2:
    print(f' n1+ n3 es igual a n2 \n ({n1} + {n3} = {n2})')
elif n2 + n3 == n1:
    print(f' n2+ n3 es igual a n1 \n ({n2} + {n3} = {n1})')
    
 #Si ninguna de las condiciones se cumple
else:
    print(f'Ninguna combincación es igual al tercer número')