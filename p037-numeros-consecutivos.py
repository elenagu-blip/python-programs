#p037-numeros-consecutivos.py
# Tres números y saber si son consecutivos.

print("\033[2J\033[H", end="")
numeros = input('Dame tres números separados por espacio: \n')
a, b, c = map(int, numeros.split())
#Ordenar los números para verificar consecutividad sin importar.

lista = sorted([a, b, c])

if lista[1] == lista[0] + 1 and lista[2] == lista [1] + 1:
    print(f"Los números {a}, {b}, {c} son consecutivos")
elif lista[0] == lista[1] or lista[1] == lista[2]:
    print(f"Los números {a}, {b}, {c} no son consecutivos")
else:
    print(f"Los números {a}, {b}, {c} no son consecutivos")
