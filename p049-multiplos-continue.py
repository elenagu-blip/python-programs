#p049-multiplos-continue.py

print("\033[2J\033[H", end="")
print("Buscando múltiplos de 10 entre 1 y 200...")

c = 0
while c < 200:
    c += 1
    if c % 10 != 0:
        continue
    print(f'{c}', end = " ")
    
print('Busqueda realizada')