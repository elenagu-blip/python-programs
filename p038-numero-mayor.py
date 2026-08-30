#p038-numero-mayor.py
#reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.

print("\033[2J\033[H", end = "")

numeros = input("Dame tres números: ")
a, b, c = map(int, numeros.split())

if a >= b and a >= c:
    print(f'El mayor es {a}.')
elif b >= a and b >= c:
    print(f'El mayor es {b}.')
else:
    print(f'El mayor es {c}')
    