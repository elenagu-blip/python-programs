#p045-conteo-ascendente.py
#Imprime los números del 1 al 100 usando un ciclo while
print("\033[2J\033[H", end ="")

print('Iniciando secuencia de conteo ascendente')

c= 1

while c <= 100:
    print(f'{c:4}', end = "")
    if c % 10 == 0:
        print()
    c += 1
    
print('\n ¡Secuencia completada!')
