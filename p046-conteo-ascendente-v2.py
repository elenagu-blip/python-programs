print("\033[2J\033[H", end="")

print('Iniciando secuencia de conteo ascendente')

n = int(input('¿Hasta dónde queremos llegar? '))
m = int(input('¿De en cuánto en cuánto? '))
c = 1

while c <= n:

    print(f'{c}', end="")
    c += m

print('\nSecuencia completa!!')